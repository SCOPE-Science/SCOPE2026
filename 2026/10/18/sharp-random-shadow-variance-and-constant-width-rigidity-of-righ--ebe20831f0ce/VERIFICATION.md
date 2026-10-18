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

A reproducible standalone check is included as `verify.py`. Run `python3 verify.py` with the Python standard library. It prints `VERIFY_OK`, checks the positivity and decimal values of the sharp constants, re-evaluates the unit square's raw second moment by an independent orthotope facet calculation, and uses independent two-dimensional midpoint integration to approximate the actual square-prism brightness's first and second moments. The checker separately tests a circular constant-width base and the exact rational-profile algebra for several values of its normalized width variance.

For the infinite-dimensional statement, the proof in `RESULT.md` establishes the pointwise Minkowski projection formula and all five exact independent Haar moments. Strict convex quadratic minimization, the nonnegative angular width variance and its equality condition, and an exact quadratic equation for the common equality-law CDF complete the noncomputational certificate. Finite sampling and quadrature do not verify unrestricted convex bodies; the analytic argument does.

Independent mathematical audit has not been performed.
