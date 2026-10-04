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

The symbolic proof reduces the graph to a support-disjointness graph on a finite product of fields. The critical checks are:

1. A nonzero element is a zero-divisor exactly when its support is a nonempty proper subset of the factor index set.
2. Two vertices multiply to zero exactly when their supports are disjoint.
3. For each coordinate, any dominating set must meet the singleton-support fiber or the complementary-support fiber. For at least three factors these requirements are pairwise disjoint.
4. Paired dominating sets have even cardinality.
5. The singleton-support vertices form a dominating clique. For odd factor count, adding one two-coordinate vertex gives an explicit perfect matching of the required size.

The standalone verifier independently constructs actual products of prime fields and searches minimum paired dominating sets exactly. Its output is:

```text
VERIFY_OK
F2xF2 vertices=2 paired=2
F2xF3 vertices=3 paired=2
F3xF3 vertices=4 paired=2
F2xF2xF2 vertices=6 paired=4
F2xF2xF3 vertices=9 paired=4
F2xF3xF3 vertices=13 paired=4
F3xF3xF3 vertices=18 paired=4
F2xF2xF2xF2 vertices=14 paired=4
F2xF2xF2xF2xF2 vertices=30 paired=6
```

The finite calculations are corroborative only. The general theorem is proved by the support argument above.
