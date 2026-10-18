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

# Verification of the paired-cluster covariance formula

The proof covers every integer \(m\ge2\) and real \(0<t\le1\). Its nonstandard steps are the minimum-coordinate dissection and explicit band moments, both derived in `RESULT.md`. Exact symbolic factorization of the two formulas gives the positive gap and the boundary-layer limit.

The enclosed `enumerate_lattice.cpp` implements an independent integer enumeration of the anchored Lipschitz potential polytope. For each rational parameter \(t=a/b\), the program enumerates dilations indexed by \(k=0,\ldots,2m+1\), recording the count and squared differences. `verify.py` uses rational finite differences of the weighted Ehrhart polynomials to recover the exact continuous covariance eigenvalues. No floating-point arithmetic or random sampling is used.

Command: `python3 verify.py` from the directory containing both files, with Python 3 and a C++17 `g++` compiler installed.

The five cases \((2,1/2),(2,1),(2,2/3),(3,1/2),(3,1)\) returned exact matches. The endpoints \(t=1\) check the isotropic case. Weighted Ehrhart leading-coefficient extraction is justified because the dilated integer difference-bound polytope has integral vertices.

These finite checks do not establish the infinite-family theorem or any assertion about an empirical covariance estimator. No separate external mathematical audit has been performed.
