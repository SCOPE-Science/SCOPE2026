# Standalone reproducibility

The files `RESULT.md` and `verify.py` together provide a proof and a finite exact-arithmetic cross-check for the circular consecutive-approval PAV winning-committee theorem.

Run `python3 verify.py` with Python 3.9 or later; no additional packages or inputs are required. The script enumerates committee subsets for n from 3 through 18 (all d through 12, d=3 through 18), checks exact PAV scores and all equality predicates, and reports the exact tie counts.

The code does not prove claims outside its finite search bounds; the proof in RESULT.md does.
