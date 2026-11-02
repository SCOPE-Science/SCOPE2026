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

The reproducible standalone `verify.py` enumerates dimensions \(2\) through \(8\) and exponents \(2,3,4\), computes exact rational monomial moments under \(\operatorname{Dirichlet}(1,\ldots,1)\), and compares direct mixed covariances with the weighted derivative representation. All 63 exact rational checks and the one elementary entropy-sign check pass. It requires only the Python standard library and can be executed with `python verify.py`.

This finite program does not certify the complete continuous functional class. The mathematical proof of that class is the ranked-gap bijection, the divergence-based covariance identity, the gradient-order argument and the strict-equality step given in RESULT.md. The singular Shannon entropy extension uses regularization plus integrable monotone convergence. Neither a full historical priority audit nor independent verification is included.
