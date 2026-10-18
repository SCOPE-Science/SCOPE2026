# Reproduction guide

The entire coefficient space is the nonzero binary masks for the fifteen degree-four monomials in three variables, ordered by decreasing first and then second exponent. There are exactly \(2^{15}-1\) masks. Only geometrically smooth curves are included in the result.

Require Python 3, SymPy, an available C++17 compiler, and no external network access. In the directory with these files, execute:

```
python enumerate_quartics.py
g++ -O2 -std=c++17 bitangent_spectrum.cpp -o primary
./primary
g++ -O2 -std=c++17 independent_spectrum.cpp -o independent
./independent
python analyze_splitting.py
```

The enumerator writes `quartic_orbits.json` (monomial order, nonzero projective orbits, and geometrically smooth orbit representatives) and `smooth_orbits.txt` (one mask and orbit size per line). The first C++ checker writes `splittings.tsv`: mask, orbit size, the seven fixed-line counts for extensions of degree one through seven, the seven numbers of Frobenius orbits of each corresponding degree, and their total. The second C++ checker independently writes `independent_fixed_counts.txt` with the mask, orbit size, and seven fixed-line counts. The final Python checker verifies agreement of every field count, recomputes Jacobian \(2\)-ranks from Cartier--Manin stable ranks, checks geometric counts and complete orbit totals, then writes `splitting_orbits.csv` and `splitting_distribution.csv`.

Field polynomial models in both C++ files are monic irreducibles, encoded as binary integers for degrees one through seven. The two independent programs use different polynomials for degrees three through seven, which tests representation independence. Geometric smoothness is tested using exact Gröbner bases on all three affine plane charts, not merely checking rational points.

The exact result concerns these finite objects and no infinite-field extrapolation is intended. The independent implementations are independent calculations within this reproduction bundle, not third-party independent validation.
