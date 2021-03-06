#!/usr/bin/env python

import argparse
import os
import sys

from .downloader import MyFilesDownloader
from .links_finder.finder import FileFinder
from .links_finder.finder import NewFileFinder
from .links_finder.filter import *
from .executor import *

PDF = ["pdf"]
ADOBE = PDF + [".ps"]
OFFICE = ["ppt", "pptx", "doc", "docx"]
MEDIA = ["mp4", "bittorrent", "mp3"]
DOCS = PDF + OFFICE





def main():
    """
    The entry point
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store_true",
                        help="Enable Downloading files")
    parser.add_argument("-o", "--output", type=str, help="Output directory")
    parser.add_argument("-f", "--filter", type=str, help="File type filter")
    parser.add_argument("url", type=str, help="The Webpage")
    args = parser.parse_args(sys.argv)

    filetypes = PDF
    # print args.filter, args.d, args.url

    if args.url is None:
        print "url not found"

    if args.filter is None:
        filetypes = PDF
    else:
        if args.filter == "all":
            filetypes = DOCS + MEDIA
        elif args.filter == "office":
            filetypes = OFFICE
        elif args.filter == "document":
            filetypes = DOCS
        elif args.filter == "media":
            filetypes = MEDIA
        elif args.filter == "open":
            download_opentrain_from_json("/home/huang/Desktop/opentrain/result.json")
            return

        ffinder = FileFinder(filetypes, args.url)
        links = list(ffinder.find())
    if args.d:
        if args.output is not None:
            dirname = args.output
        else:
            dirname = os.path.abspath('.')
        downer = MyFilesDownloader(links, dirname)
        downer.startDownloadingFiles()
    else:
        print "Found Links:\n", links

    '''
	url = "http://csiflabs.cs.ucdavis.edu/~ssdavis/60/"
	filetypes = [".pdf"]
	dirname = "/Volumes/Transcend/DAVISWork/Classes/ecs60/materials"

	ffinder = FileFinder(filetypes,url)
	links = list(ffinder.find())

	downer = MyFilesDownloader(links,dirname)
	downer.startDownloadingFiles()
    '''


if __name__ == '__main__':
    main()
