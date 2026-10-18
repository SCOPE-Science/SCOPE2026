# Deterministic reproduction

This directory contains `make_tables.py`, `tables.hpp`, `census.cpp`, `orbits.csv`, `results.txt`, `independent_groebner.py`, and `verify_independent.py`. Requires ISO C++17, Python 3, and SymPy for the independent checks. Run in a writable directory containing these files:

```sh
python make_tables.py
g++ -std=c++17 -O3 census.cpp -o census
./census > results-new.txt
cmp results.txt results-new.txt
python independent_groebner.py
python verify_independent.py
```

The program writes `orbits.csv` and standard output containing the joint distribution. It is deterministic and generates all input tables. The 15 coefficient digits are ordered by descending powers of the first variable, then descending powers of the second. The set of smooth orbit reps is obtained by geometric rank, not an experimental finite-extension search.

Expected SHA-256 outputs after replay (not part of the proof):

- `orbits.csv`: `2ba8f97c12f999bac20c09abfd186cdd93924ab0c274c7e34e22e59c29150f75`
- `results.txt`: `a05b3e2aff4cba985a7240d932fa0fc9db7f867b0b553feb6c39961052f05e32`

The external mathematical assumptions and proof are explained in `RESULT.md`; all calculations are finite.
