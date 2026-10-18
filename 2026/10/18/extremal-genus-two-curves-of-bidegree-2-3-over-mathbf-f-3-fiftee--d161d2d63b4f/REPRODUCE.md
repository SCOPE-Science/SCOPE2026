# Reproducing the finite-field classification

Run all commands from the directory containing the files. Dependencies are C++17, Python 3, NumPy and SymPy. The programs perform exhaustive calculations over finite coefficient sets and prime-power extensions; no randomized sampling is involved.

```sh
g++ -O3 -std=c++17 census.cpp -o census
./census > census_results.txt
python orbits.py > orbit_results.txt
python interpolation_check.py > interpolation_results.txt
python extremal_checks.py > extremal_results.txt
python symbolic_orbit_check.py > symbolic_orbit_results.txt
```

`census.cpp` recreates `smooth_models.csv` from all 265720 coefficient classes, testing a binary-sextic squarefreeness criterion and rational fibers. `orbits.py` consumes the CSV, constructs the full order-576 ruling-preserving group, and regenerates `orbit_reps.csv`, whose 286 records give a complete set of orbit representatives. `symbolic_orbit_check.py` independently uses symbolic polynomial gcd on every orbit representative.

`interpolation_check.py` instead starts from four split rational quadratic fibers. Its 10368 candidates contain exactly 6096 smooth curves, with branch-type multiplicities 3888, 1872, and 336. This is independent of the coefficient-space sieve and of the group orbit algorithm. `extremal_checks.py` computes the branch splitting and point count over the quadratic extension for each of the fifteen maximal-orbit representatives.

The text output files in the package are exact expected results. The transcript of a successful rerun may be compared by bytes; SymPy may issue version-specific warnings on standard error. The plain CSV files are generated scientific data and are not imported from any external database.
