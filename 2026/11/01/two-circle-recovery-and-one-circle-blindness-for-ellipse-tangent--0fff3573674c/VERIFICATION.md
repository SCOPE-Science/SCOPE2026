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

# Reproducibility and proof boundaries

Run `python verify.py` with Python 3 and SciPy installed. The checker computes direct quadratic-intersection endpoints and compares their unsigned product against the closed formula for 96 angles in each of five test ellipses. It verifies recovery on either side of the equipotential radius, checks a family of exact-resonance ellipses and their separation at a second radius, and integrates the stated density after a trigonometric change of variable for four nonconstant examples. On the authored package it printed:

```
EXACT_QUADRATIC_AND_ENDPOINT_INVERSION_PASSED
RESONANT_FIBER_AND_TWO_RADIUS_SEPARATION_PASSED
DENSITY_NORMALIZATION_AND_EXACT_SENSITIVITY_PASSED
ALL_CHECKS_PASSED
```

The finite tests do not certify statements quantified over all real ellipses. The proof of the universal theorem is the intersection polynomial, Rayleigh-quotient range, endpoint algebra, arcsine change of variables, and incompatibility of the two resonance equations, all written in RESULT.md. No externally performed independent mathematical audit is asserted.
