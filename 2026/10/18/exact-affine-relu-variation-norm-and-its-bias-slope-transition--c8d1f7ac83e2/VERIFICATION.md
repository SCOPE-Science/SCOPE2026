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

The claimed equality follows analytically from signed distributional second-derivative cancellation, a Euclidean moment lower bound, exact minimization of \(|c|+2\sqrt{s^2+(b-c)^2}\), and an explicit three-support-or-less measure. For the slope-zero case, the evaluation functional at the origin proves the cost exactly. For nonzero slopes, projection from the real Hilbert space to the one-dimensional slope line preserves the unit-ball constraint and does not increase total variation.

The independent supplementary checker `affine_variation_check.py` evaluates finite parameter examples and the explicit ReLU representation; its successful output provides numerical diagnostics only. It does not verify all signed measures, prove the infinite-dimensional implication, or constitute an independent scientific audit. Reproduce with `python affine_variation_check.py` on Python 3 with SciPy installed.
