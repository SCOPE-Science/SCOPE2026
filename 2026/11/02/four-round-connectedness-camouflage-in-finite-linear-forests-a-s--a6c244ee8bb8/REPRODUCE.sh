#!/bin/sh
set -eu
c++ -std=c++17 -O3 -o verify_exhaustive verify_exhaustive.cpp
./verify_exhaustive 29 > exhaustive_output_replay.txt 2> exhaustive_diagnostics_replay.txt
python3 verify_boundary.py > boundary_output_replay.txt
printf '%s\n' 'Reproduction finished; compare the outputs to the packaged records.'
