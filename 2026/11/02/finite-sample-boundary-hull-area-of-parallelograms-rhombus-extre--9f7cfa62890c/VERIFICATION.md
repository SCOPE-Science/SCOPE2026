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

Execute the standalone checker with `python3 CHECKER.py` (Python standard library only). It evaluates the stated closed form by exact integer/fraction arithmetic and by a separately expanded two-uniform integral for 28 cases, independently constructs sampled convex hulls with varying shear angles, and checks the limiting formulas at finite large sample sizes.

Observed checks: `EXACT_TWO_INDEPENDENT_INTEGRATIONS_AND_SHARP_BOUNDS_PASSED 28`; `AFFINE_SHEAR_ANGLE_BLINDNESS_DIAGNOSTICS_PASSED`; `FIXED_SHAPE_AND_THIN_BOUNDARY_LAYER_LIMITS_PASSED`; `ALL_CHECKS_PASSED`.

The proof for every integer sample size is the cap-integral identity and strict-convexity argument in `RESULT.md`; neither floating-point simulations nor finite enumerations constitute a universal proof. Independent mathematical review is not claimed or recorded.
