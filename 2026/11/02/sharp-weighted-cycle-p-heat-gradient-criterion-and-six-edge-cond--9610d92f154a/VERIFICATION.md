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

# Reproducibility and verification limits

The research result is proved analytically from the edge equation, cyclic closure and sharp scalar maximizations. The supporting checker is pure Python 3 and is included alongside the manuscript: run `python3 verify_weighted_cycle_pheat.py`.

Its actual execution returned:

```
NUMERIC_SHARP_WITNESSES_AND_DINI_BOUNDS_OK 3600
EXACT_RATIONAL_CUBIC_WITNESSES_OK 630
EXACT_RATIONAL_GRID_UPPER_BOUNDS_OK 1712
PENTAGON_EXPONENT_PHASE_TRANSITION_OK 1.336485730165
SIX_VERTEX_CONDUCTANCE_RIGIDITY_CHECKS_OK
ALL_WEIGHTED_CYCLE_P_HEAT_CHECKS_OK
```

The rational checks use exact fractions for the cubic flux; the random real-power comparisons and the pentagon root use ordinary floating-point arithmetic. These finite tests do not establish the all-parameter theorem, optimality for all real exponents, or literature uniqueness. No independent mathematical audit has been performed.
