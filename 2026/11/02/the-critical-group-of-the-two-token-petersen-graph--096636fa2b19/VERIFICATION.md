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

The invariant factors are reconstructed by exact Smith diagonalization modulo five prime powers for a fully specified integer Laplacian. The prime-power computation is complete because the order of the finite group is independently fixed by the exact characteristic polynomial and Kirchhoff's theorem.

Run `python verify_primary.py` (dependencies: `networkx`, `sympy`). This constructs all 45 states and all 120 exchanges from the standard Petersen graph, checks the exact characteristic polynomial, computes Smith valuations at each of \(2,3,5,7,19\), and verifies the invariant-factor product. The resulting last-line statements include `PRIMARY_EXACT_PASS` and `PRIMARY_SMITH {1: 28, 2: 8, 4: 2, 28: 1, 1596: 1, 38304: 1, 191520: 3}`.

Independently compile and execute `g++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent`. This creates a different Petersen labeling from all two-element subsets of five points, performs separate prime-power reductions, checks every elementary-operation cancellation, and prints `INDEPENDENT_KNESER_AND_SMITH_PASS order=45 edges=120 nontrivial=16`.

The modular elimination algorithm selects a least-valuation pivot and uses only invertible row/column additions, swaps and unit inversions over \(\mathbb Z/p^{e+1}\mathbb Z\). For every possible prime divisor of the determinant, the exact output profiles are given in `certificate.json`. The order constraint and aligned valuations determine the entire integer Smith normal form. The displayed factorization is computed with symbolic integer coefficients, not with floating point. This procedure is a finite, exhaustive proof of this one graph's invariant; it does not certify other parameter values or exclude unseen prior publications.
