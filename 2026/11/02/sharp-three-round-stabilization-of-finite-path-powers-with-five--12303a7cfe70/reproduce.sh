#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 verify_pathpowers_rank3.py > verification.replayed.stdout
python3 check_pathpair_formula.py > arithmetic.replayed.stdout
cmp verification.replayed.stdout verify_pathpowers_rank3.stdout
cmp arithmetic.replayed.stdout check_pathpair_formula.stdout
printf '%s\n' 'REPRODUCE_OK'
