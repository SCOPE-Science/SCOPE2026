# Reproduction of the finite classification

Run from the root of this package on a system with an ISO C++17 compiler and Python 3. All arithmetic in the C++ programs is exact integer arithmetic modulo three; no external mathematical libraries are needed.

```sh
mkdir -p replay
cd replay
g++ -std=c++17 -O3 -o orbit_census ../verify/quartic_flex.cpp
./orbit_census > flex_counts.txt
g++ -std=c++17 -O3 -o direct_census ../verify/quartic_flex_direct.cpp
./direct_census > direct_counts.txt
g++ -std=c++17 -O3 -DORBIT_RECHECK -o orbit_crosscheck ../verify/quartic_flex_crosscheck.cpp
./orbit_crosscheck > crosscheck_counts.txt
python3 ../verify/inspect_example.py > example_inspection.txt
cmp flex_counts.txt ../data/flex_counts.txt
cmp direct_counts.txt ../data/direct_counts.txt
cmp crosscheck_counts.txt ../data/crosscheck_counts.txt
cmp example_inspection.txt ../data/example_inspection.txt
cmp flex_orbits.tsv ../data/flex_orbits.tsv
cmp direct_candidates.tsv ../data/direct_candidates.tsv
```

The orbit census generates 1,557 complete projective orbits and evaluates smoothness and flex contacts on their representatives. The direct census bypasses orbit grouping, enumerates 7,174,453 normalized coefficient vectors, and performs exact geometric smoothness tests on all 6,097 candidate seven-flex equations. The third program independently recomputes each orbit representative's smoothness and contact invariants using precomputed linear and Hasse derivative coefficient forms.

The complete projective representative census is `data/flex_orbits.tsv`; the full list of high-contact candidates, including singular ones, is `data/direct_candidates.tsv`. The output of the example checker exhibits all rational points, their tangent lines, and precise intersection multiplicities.

The source code is intended to be replayed rather than treated as a formal proof assistant certificate. All projective-smoothness decisions are exact and apply over an algebraic closure via the rank-36 criterion described in `RESULT.md`.
