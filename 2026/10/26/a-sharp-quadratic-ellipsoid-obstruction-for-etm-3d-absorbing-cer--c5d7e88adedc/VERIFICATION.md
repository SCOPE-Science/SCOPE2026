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

# Direct verification and limits

`python check.py` executed successfully against the actual packaged source. Its exact symbolic output was:

```
SYMMETRIC_CUBIC_CANCELLATION_AND_COEFFICIENTS_PASS
UNIVERSAL_TRANSVERSE_FORCING_COEFFICIENT_PASS 3
EXACT_AXIS_NORMAL_DERIVATIVE_PASS
EXPLICIT_SOURCE_RADIUS_SHARP_ASYMPTOTIC_PASS 3/2
GLOBAL_SEMIDEFINITE_AND_INVARIANCE_IMPLICATIONS_REQUIRE_ANALYTICAL_PROOF
```

The checker uses SymPy for exact symbolic expansion and exact limits; it has no stochastic tests. The infinite-parameter quantifier and the invariant-boundary implications are justified by the written proof in `RESULT.md`, not by finite sampling. The mathematical conclusion is restricted to fixed, energy-compatible quadratic metrics and certified forward-invariant ellipsoids. Independent validation is not performed.
