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

# Verification record

The exact analytic proof is in RESULT.md. Running `python verify.py` with Python 3, numpy, scipy and mpmath compares the closed bubble integral with direct numerical cell integration, the closed weights with independently integrated kernel Gram-system weights, and the explicit cardinal spline with a direct kernel interpolant. The checks passed for grid sizes 2 through 14 with 13 bubble integral, 65 kernel solve, 140 interpolant, and 65 sign-classification comparisons. Six high-precision large-grid checks support the asymptotic constant. Finite checks do not certify the continuum/all-size theorem.

No independent mathematical audit has been performed.
