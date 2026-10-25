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

# Reproducibility

Run `python3 verify.py` with the standard Python library. The checker independently builds both regular polygons and clips each against the other's edges, without invoking the analytic tangent-line area expression as its reference. It checks 868 separate overlap-area identities (all side counts 3 through 30), tests the cross-order coupling on 199 values of the uniform parameter for side counts 3 through 149, samples the exact CDF and mean at six side counts, and measures the order-\(n^{-4}\) remainder after the displayed second-order quantile expansion at four large side counts. This execution printed:

```
DIRECT_HALFPLANE_POLYGON_CLIPPING_IDENTITY_OK 868
STRICT_ORDER_BY_POLYGON_SIDES_AND_BETA_BOUND_OK
EXACT_CDF_AND_EXACT_MEAN_MONTE_CARLO_OK
UNIFORM_SECOND_ORDER_EXPANSION_NUMERICS_OK
ALL_ROTATED_POLYGON_OVERLAP_CHECKS_OK
```

These are finite consistency checks, not exhaustive verification of the infinite integer range, the uniform remainder, or historical originality. Analytical details and boundary cases are provided in `RESULT.md`. Independent review has not been performed.
