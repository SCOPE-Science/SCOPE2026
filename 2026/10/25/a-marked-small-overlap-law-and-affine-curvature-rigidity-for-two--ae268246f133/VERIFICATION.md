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

# Verification and limitations

Run `python verify.py` using NumPy and SciPy. The program computes genuine numerical quadratures of two-ellipse near-tangency areas and unequal-disk small-overlap probabilities, rather than relying on previously recorded output. It also checks the pointwise unordered curvature-radius inversion and the affine-normal-angle diagnostic.

Observed output from the complete packaged checker:

```
INDEPENDENT_ELLIPTIC_TANGENCY_LENS_COEFFICIENT_OK 3
UNIFORM_RANDOM_TRANSLATION_TAIL_AND_BETA_DEPTH_OK 2
UNORDERED_CONTACT_CURVATURE_RADII_RECOVERY_OK 41
AFFINE_ARCLENGTH_SPECIALIZATION_OK 2
AFFINE_NORMAL_ANGLE_RIGIDITY_GEOMETRIC_DIAGNOSTIC_OK 2
ALL_SHORT_OVERLAP_CONTACT_LAW_CHECKS_OK
```

These finite checks are corroboration, not a computer proof of the general theorem or independent external certification. Analytic quantifiers, assumptions, and proof are in `RESULT.md`. The joint beta law follows analytically from the threshold Jacobian; numerical tests cover representative ellipses and disks, not all smooth convex bodies. A potentially relevant 1992 scalar-distribution source was not accessible in full; the risk is disclosed in `REVIEW.md`.
