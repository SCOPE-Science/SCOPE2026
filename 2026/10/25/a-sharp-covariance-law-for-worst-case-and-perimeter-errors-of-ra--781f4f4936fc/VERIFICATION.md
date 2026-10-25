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

Deterministic reproduction: run `python verify.py` from the directory containing this file. The script verifies the exponential influence polynomial's exact mean and variance by factorial identities, and one-dimensional quadrature for the conditional covariance involving the largest exponential observation. Finite values converge slowly because their leading correction is logarithmic; no finite grid or finite numerical sequence proves the asymptotic statement.

The infinite result is proved analytically in `RESULT.md` using Dirichlet spacings, exact conditional truncation, exponential moment estimates, and a bivariate triangular-array central limit theorem. The full circle-to-polygon Hausdorff identity is exact and applies to arbitrary circular gaps. Independent mathematical review has not been performed.
