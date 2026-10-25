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
# Finite verification and analytic limits

The standalone standard-library `verify.py` was executed successfully: 230 exact-rational checks for every integer \(m=2,\ldots,24\). It uses a **second representation** of the uniform Dirichlet spacings: conditional on their ordering, weighted successive ranked gaps form another uniform Dirichlet vector. This approach directly computes all joint moments, independently of the two-coordinate splitting method used in the proof. It checks the full finite covariance, both variances, exact correlation, the ranked discrepancy mean/variance, and deterministic decomposition.

The infinite claims are proved with Dirichlet beta moments and the Hoeffding decomposition/delta method. Computing the exponential influence moments yields \(1/12\), \(1/2\), and \(4\); hence the ranked discrepancy's asymptotic variance is \(37/12\). Finite checks do not establish those infinite assertions by themselves. This work does not compute a full finite-sample distribution, calibration quantiles, or power. No independent mathematical audit has been performed.

Reproduce with `python3 verify.py` in an ordinary Python 3 environment; no third-party dependencies are required.
