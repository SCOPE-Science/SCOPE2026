# Reproduction instructions

Requirements: C++17 compiler, Python 3.9+, and SymPy.

Run from the directory containing the supplied source files:

```
g++ -O3 -std=c++17 quadric_p4.cpp -o quadric_p4
./quadric_p4
g++ -O3 -std=c++17 orbits.cpp -o orbits
./orbits
python hyperplanes.py
python independent_geometry.py
```

Compare outputs to `EXPECTED.txt`. The binary quadratic encoding is specified in `RESULT.md`. Both C++ programs perform complete finite enumeration; the second includes the first source for the same quadratic functions but has its own main function. The Python hyperplane test is exact over \(\mathbf F_2\) with four affine charts per rational hyperplane and Gröbner unit-ideal tests. The geometry script independently verifies the three canonical representative surfaces. No network, private files or external datasets are required.
