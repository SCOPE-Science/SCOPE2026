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
# Verification

The universal covariance identity is proved symbolically from Gaussian radial-angular independence and chi moments.

`checker.py` numerically verifies the bivariate absolute-Gaussian moment identity by high-precision quadrature for several correlations, checks the chi-moment covariance relation for several homogeneity degrees, and evaluates the MAD variance and correlation formulas for \(2\le n\le5000\).

These computations are supplementary consistency checks. They are not used as proof of the all-\(n\) theorem.
