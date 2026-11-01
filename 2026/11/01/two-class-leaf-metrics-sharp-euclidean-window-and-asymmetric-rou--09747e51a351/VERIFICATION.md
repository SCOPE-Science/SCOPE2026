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
# Reproducibility and verification
The accompanying Python checker independently constructs the two-class leaf metric from arm lengths and compares its powered distance quadratic form to the exact fluctuation/radial identity using rational arithmetic. Its 480 exact examples cover class sizes \((2,2)\), \((2,3)\), \((3,4)\), \((4,5)\), three rational length profiles, five integer exponents and eight distinct zero-sum coefficient samples each. The checker also uses NumPy eigenvalue calculations and SciPy's Brent solver on 20 nondegenerate examples to inspect the exact critical Gram nullity, strictly smaller powers and strictly larger powers. Additional checks target monotonicity, the asymmetric singular asymptotic constants and Euclidean feasibility boundaries.

Execute `python verify_two_class_leaf_roundness.py` with Python 3, NumPy and SciPy installed. The code does not prove the all-parameter theorem; the proof is the exact identity, convexity and limiting-root analysis in RESULT.md. Floating-point tests near equal arm lengths may be ill-conditioned and are deliberately separated from the asymptotic argument. Independent scientific audit has not been performed.
