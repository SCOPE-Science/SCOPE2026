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

# Reproducibility

Run `python checks/verify.py` in an environment with NumPy, SciPy, and mpmath installed. The checks cover the complex exponential full-flight increment, its zero mean and isotropic second moment, the finite-curvature renewal coefficient, an exact Lomax characteristic integral, the zero-curvature mean-square integral, and the asymptotic coefficients at representative tail indices. The test uses a fixed pseudorandom seed for finite Monte Carlo comparisons.

The functional central limit theorem uses the iid invariance principle, the renewal strong law and deterministic time change; the finite test suite is not a proof of those theorems. The joint long-time/weak-curvature crossover is not proved. Source comparisons are evidence of an originality review rather than a certificate of global publication priority.
