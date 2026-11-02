#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify_extension.py
python3 verify_pebble.py
