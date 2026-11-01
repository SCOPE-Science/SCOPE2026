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
# Reproducibility and limits

Run `python verification.py` with a Python installation containing `sympy`. The exact-rational tests and symbolic assertions in this standalone program were executed successfully. It checks normalized stationary masses, affine branch-image alignment, characteristic polynomial, full rational covariance resolvent, first fifteen covariances for each integer from 3 through 50 (720 exact comparisons), the Poisson equation, and the Green–Kubo/martingale variance identity. It also confirms primitivity via a positive sixth matrix power in each finite case.

The proof covers all integer parameters \(k\ge3\), not just the tested finite set. The CLT uses a bounded martingale-coboundary decomposition and stationarity, as proved in `RESULT.md`. Tests do not establish novelty or independent mathematical certification. The original 2021 article could only be inspected through its abstract and publisher preview; whole-document priority remains unverified.
