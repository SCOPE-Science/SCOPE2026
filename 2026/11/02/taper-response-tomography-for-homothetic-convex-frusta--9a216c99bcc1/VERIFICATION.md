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

The accompanying `verify.py` is standalone Python 3 source; run `python3 verify.py` with no external packages. It independently evaluates exposed-face support maxima for a triangle and a square, compares these with the positive-part width representation, and checks numerical midpoint integration against the closed arctangent transform for three taper levels. Further checks cover the quadratic limiting coefficient, a deterministic directional coupling for the symmetric square, and a separate dense one-dimensional disk integral. Executing the packaged file produced `ALL_CHECKS_PASSED`.

The mathematical proof is the support-max reduction and elementary definite integral, plus analytic power-series uniqueness for compactly supported measures and the convexity/reflection argument. Deterministic quadrature does not certify an infinite family of convex bases, and no independent audit or empirical-sample statistical analysis was performed. The parameter continuum and homothety center must be known for the stated inverse characterization.
