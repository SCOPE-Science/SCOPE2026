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

# Verification summary

Run `python3 verify.py` with Python 3 and its standard library. Actual test output:

```
TRANSITIVE_FRAME_COUNTS 1:2,2:13,3:171,4:3994
REFLEXIVE_TRANSITIVE_COUNTS 1:1,2:4,3:29,4:355
VALUATION_TESTS 65328
SHARP_STRICT_ORDERS_TESTED 3..60
SHARP_TWO_WORLD_WITNESS (3, 3) 0 3
VERIFY_OK
```

The checker enumerates all directed relations satisfying transitivity on one through four labeled worlds, every propositional valuation on each such frame, and all strict-order witnesses from three through sixty worlds. The explicit two-world witness uses the universal accessibility relation and a split valuation. This is finite validation, not a proof of the arbitrary-size assertion. The general proof depends on forward closure, cardinality growth and a terminal strongly connected component of a nonempty finite successor subgraph. Independent audit has not been performed.
