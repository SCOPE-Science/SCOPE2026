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

Execute `python verify.py` using standard Python 3 (no external dependencies). It prints `VERIFY_OK` if all checks pass. The program forms exact rational square-root and inverse-sine enclosures for the explicitly algebraic optimal angle, then proves the sharp area belongs to the rational interval \((0.79457850,0.79457852)\). The arcsine tail is bounded using positive decreasing coefficients and a geometric upper tail; hence its numerical enclosure is not a floating-point assertion.

As a separate finite consistency check, the program constructs paired boundary curves at seven selected angles, compares polygonal area to the analytic closed area formula, verifies endpoint closure moments, and compares direct numerical convolution against the first-variation obstacle. These examples are not an exhaustive proof for all profiles or all angles.

The actual universal correctness argument is in RESULT.md: exact area functional, strict conditional negativity of its quadratic form using Dirichlet Poincaré, signed first-variation complementarity and algebraic one-variable derivative. In particular, the rational checks alone do not establish the global maximum, and historical uniqueness or independent audit has not been asserted.
