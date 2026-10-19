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
# Computational verification and limitations

The two code representations use integer arithmetic without floating-point approximations. With a C++17 compiler and Python 3.8+:

```sh
g++ -O2 -std=c++17 -Wall -Wextra -pedantic check_polynomial.cpp -o polynomial_check
./polynomial_check > polynomial.out
python3 check_roots.py > roots.out
diff -u polynomial.out roots.out
```

The C++ program exhausts all 65,536 generator multiples and computes cyclic sliding-window masks. The Python program constructs \(\mathbb F_{32}\), checks the polynomial factorization and BCH root equations, row-reduces all parity-check equations to rank 15, and exhaustively enumerates the 16 free coordinates. It computes the weights by cyclic zero gaps. Both output all 31 complete histograms with identical byte serialization. The Python program also checks the fourteen claimed rank-13 complementary-support submatrices.

Expected success markers on standard error: `POLYNOMIAL_CENSUS_OK`, `BCH_GENERATOR_OK`, `TWO_DISJOINT_NINE_ZERO_RUNS_IMPOSSIBLE`, and `ROOT_SYNDROME_CENSUS_OK`. The counts are reproducible and exact for this finite code; nothing in these checks establishes a theorem for all BCH lengths. The two implementations are not an external independent audit.
