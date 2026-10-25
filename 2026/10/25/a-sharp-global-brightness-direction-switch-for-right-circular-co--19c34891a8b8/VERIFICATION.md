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

The accompanying `verify.py` was executed on the extracted research files. It returned:

```text
CRITICAL_HEIGHT_AND_SADDLE_INTERVALS_OK
GLOBAL_MAXIMUM_COMPETITION_ALL_REGIMES_OK
INDEPENDENT_1200_PROJECTED_CONVEX_HULLS_OK
ALL_CIRCULAR_CONE_GLOBAL_BRIGHTNESS_CHECKS_OK
```

The checker performs numerical root isolation, directional global comparisons at aspects on both sides of the global switch, and 1,200 independent projected convex hulls of refined polygonal cone approximations. These checks support but do not prove the continuum theorem, which follows from the exact derivative and monotone crossing argument. Numerical decimal digits are informational, not formally interval-certified. The 1989 projected-area paper's complete text remains uninspected; only its published abstract was available.
