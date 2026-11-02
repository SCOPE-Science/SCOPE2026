#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify_rank4.py
python3 verify_geometry.py
