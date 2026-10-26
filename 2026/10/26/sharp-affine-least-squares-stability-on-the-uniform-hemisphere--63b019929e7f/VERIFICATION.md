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

# Reproducible verification

Use Python 3 standard library and run `python3 check.py` in the same directory as this file. The code checks exact rational moment and normalization identities, a rational separation certificate for the strict Cauchy--Schwarz gap, algebraic equivalence of the two norm formulas, and the sharp negative-cap mass. It also integrates the kernel by two separately implemented numerical methods: a direct two-coordinate grid quadrature and a conditional-azimuth one-coordinate integration.

Observed replay output:

```
CHECKS_PASSED=96
HEMISPHERE_NORM=2.093343108499145
AZIMUTH_QUADRATURE=2.093343108639714
DIRECT_SURFACE_QUADRATURE=2.093341942229042
SHARP_NEGATIVE_OVERSHOOT=0.546671554249572
```

The nonnumerical parts of the proof are reproduced in RESULT.md. In particular, monotonicity under increasing horizontal coefficient, convex interpolation, Cauchy--Schwarz at all heights, and spherical-cap integration establish the exact infinite-domain conclusion. The checker is corroboration, not an exhaustive finite certificate of the continuum or an independent audit. External mathematical priority has not been exhaustively verified.
