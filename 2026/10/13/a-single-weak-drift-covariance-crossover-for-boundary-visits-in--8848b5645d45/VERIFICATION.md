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

# Reproducibility of the boundary-visit covariance identity

Run `python verify_walk_cov.py` using Python 3.10 or later; no third-party packages are required.

The script constructs the transient transition matrix of the absorbing walk, solves the moment recurrences with exact rational arithmetic, and independently compares the mixed-moment covariance with the Green-function identity. It checks every initial state for barriers from \(3\) through \(10\) and four rational jump probabilities. It also compares the finite covariance divided by the barrier size against the proposed analytic limit for multiple fixed starts and scaled drifts, and brackets the uniquely defined positive sign-reversal parameter.

A successful run prints exactly:

`VERIFY_OK exact_finite_independent_conditions=600 asymptotic_sign_root=1.49888421886734`

Only the finite recurrences and numerical approximations are programmatically checked. Infinite asymptotic convergence, global uniqueness of the crossover, and signs across all admissible parameters are established by the analytic proof in the companion result. No independent external assessment has been performed.
