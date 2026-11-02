#!/bin/sh
set -eu
python3 verify_reductions.py
python3 verify_orbits.py
python3 verify_direct.py
