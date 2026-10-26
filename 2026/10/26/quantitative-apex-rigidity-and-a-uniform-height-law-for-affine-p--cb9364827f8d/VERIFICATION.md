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

The normalized uniform-cone moments, apex Beta integral, reproducing-kernel interpolation, and finite-dimensional strict base gap were proved symbolically in RESULT.md. The proof covers all integers \(d\ge2\) and all evaluation points, without using numerical extrapolation.

`CHECK.py` verifies 795 exact rational identities/inequalities (160 strict-gap instances and 635 covariance/kernel checks), 72 two-dimensional Gauss--Jacobi kernel-row quadrature inequalities, and six independent apex integrals. The tolerance of the floating-point quadrature comparisons is 0.004 for apex rows and 0.003 for the row-envelope inequalities. Numerical checks do not independently certify universal inequalities or originality.

Full-source scientific comparison includes Xu's conical kernel and convolution formulas and the published exact single-simplex affine projector; the matching scalar expression is not claimed as an independent novelty. No independent audit or external certification is represented by this file.
