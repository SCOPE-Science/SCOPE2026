---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of exact cubic-surface Gauss-fiber counts

The included source files reproduce the numerical claim using finite-field arithmetic and algebraically exact Gröbner bases. On a system with a C++17 compiler and Python with `sympy`, execute:

```sh
g++ -O3 -std=c++17 orbit.cpp -o orbit
./orbit > orbit_representatives.csv
python classify.py
python independent_gauss.py
python line_comparison.py
```

`orbit.cpp` applies three adjacent variable swaps and one elementary shear to each nonzero 20-bit cubic coefficient vector and exhaustively determines group orbits. `classify.py` uses the orbit sizes, formal gradient evaluations at every rational point, and four-chart unit-ideal Gröbner tests to construct `cubic_orbit_certificate.csv` and `gauss_profile.csv`. `independent_gauss.py` independently recomputes all 36 smooth representative Gauss profiles by direct monomial differentiation, cross-checking the weighted table. `line_comparison.py` verifies a pair of distinct profiles at fixed known rational point/line/Eckardt incidence invariants.

The run-specific scientific outputs included here are `primary_output.txt`, `secondary_output.txt`, and `comparison_output.txt`; the two CSV certificates are the actual machine-readable computed data. The expected overall domain size is 1,048,575 nonzero forms, with 141 projective orbits, 36 geometrically smooth orbits, 322,560 smooth equations, and 14 Gauss-fiber partitions.

The checker's orbit construction and smoothness tests are not independently repeated by the derivative cross-check. In particular, the algebraic smoothness condition cannot be replaced by checking only \(\mathbf F_2\)-rational points. No assertion is made about arithmetic over extensions or the geometric degree of the Gauss morphism.
