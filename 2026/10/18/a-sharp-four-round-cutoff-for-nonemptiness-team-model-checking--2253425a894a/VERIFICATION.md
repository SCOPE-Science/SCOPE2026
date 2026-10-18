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
The executable `verify_ne_obligations.py` uses only Python's standard library. It cross-checks direct lax-split semantics against flat-obligation and top-down methods on 14,400 finite formula/team combinations. It reproduces the alternating update algorithm on 21,600 additional instances and checks equality of stage-four, stage-five and stage-six labels. It separately checks the singleton-team sharpness example.

Run `python3 verify_ne_obligations.py`; expected output:

```
CONVEX_NE_FLAT_OBLIGATIONS_OK 14400
FOUR_ROUND_FIXED_POINT_BOUND_OK 21600
FOUR_ROUND_SHARPNESS_OK
```

These bounded checks validate the implementation and selected examples, not all infinite formula sizes. The inductive proof in RESULT.md supplies the unbounded justification. Independent external validation has not been performed.
