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

The complete proof is analytical. A separate executable `check_surface.py` reproduces geometric computations with Python 3, NumPy and SciPy (`requirements.txt`). Running `python check_surface.py` from the directory containing both files produced the terminal marker `ALL_TWO_DISC_ANGULAR_AREA_CHECKS_PASSED`.

The checker compares the exact one-dimensional elliptic integral with a directly parameterized two-angle mixed cross-product integral, tests surface-area ordering, checks the small-angle quotient, and constructs three-dimensional convex hulls of the Minkowski sums of regular inscribed disk polygons. It checks areas and volumes at several nonzero angles, two radius pairs and two polygon resolutions, and confirms convergence against the exact predictions.

Finite-precision quadrature, finitely many polygon vertices and numerical tolerances only corroborate the formulas; they cannot verify every angle or prove the singular expansion. The rigorous steps are the segment representation, intrinsic-volume identities, monotonicity of the elliptic integral, uniform complementary-modulus remainder and exact beta-integral evaluations in `RESULT.md`. Independent mathematical audit has not been performed.
