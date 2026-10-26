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

Run `python3 verify.py` with Python 3 standard library. It checks the determinant and trace identities with exact fractions and solves the two-group endemic equilibrium for five minority fractions using high precision. The script also reconstructs infectious and quarantined compartments and tests stationary residuals against the source equations, and checks convergence of the rescaled prevalence coefficients.

The uniform-in-parameter existence and singular limit follow from the analytical fixed-point and implicit-function arguments in `RESULT.md`; finite numerical checks alone cannot prove them. The published infection-invasion threshold is attributed to the original authors. This package contains no experimental finite-population persistence verification or independent scientific review.
