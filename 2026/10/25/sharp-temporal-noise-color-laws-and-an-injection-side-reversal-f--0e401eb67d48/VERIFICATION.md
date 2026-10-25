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

# Verification details

The exact covariance identity follows by summing the absolutely convergent double series of the AR(1)-correlated filtered perturbations. The spectral curvature and two derivative polynomials are proved by differentiation and exact algebra in RESULT.md. The standard-library Python `verify.py` checks the stationary moment recurrence against that closed form, exact rational derivative identities, the two rational independent-noise values, the two symbolic-root risk values, finite-convolution consistency, and rational-grid lower bounds. It passed **1,080 assertions**.

The exact root and strict convexity proof, rather than any finite test, establish the global statements. The tests do not assert independence, publication priority, nonlinear generality, or uniform convergence near ±1 correlation. No independent audit has been performed.
