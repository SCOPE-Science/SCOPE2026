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

The analytic proof in `RESULT.md` establishes the minimum diameter, the positive gap for edges in non-longest directions, the dominant-edge formula, and the weighted cross-polytope volume that determines the asymptotic constant. The standalone `verify.py` was executed from the packaged path using exact rational arithmetic for representative dimension-three edge configurations. It checks four dominant-edge cases, one non-dominant gap case, and the dimension-three coefficient simplification. These are consistency checks; the infinite-dimensional claim for every fixed \(n\ge3\) is proved by the analytic argument, not by finite enumeration. Independent audit and independent validation have not been performed.

Actual checker output:

```text
ORTHOTOPE_TAIL_CHECK_OK
dominant_edge_cases=4 exact_fraction_checks=passed
non_dominant_gap_check=passed
dimension_3_coefficient_reduction=passed
```
