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

The included `verification.py` independently constructs the adjacency of each \(K_{a,b}-M_t\) for \(3\le a,b\le6\), and all \(0\le t\le\min(a,b)\). For each vertex subset it directly evaluates whether every vertex selected has at most one selected neighbor, and tests whether adding any unselected vertex preserves that property. It compares *all coefficients* of the resulting two polynomial counters to the exact closed-form coefficients.

The standalone program ran with no failed assertions:

```
VERIFICATION_OK profiles=78 vertex_subsets=83456
```

The scripts use the standard Python library only. Run `python verification.py` to reproduce the record. The infinite-family proof is given in `RESULT.md`; finite exhaustive verification alone cannot establish the infinite theorem or bibliographic novelty. Independent external validation is not performed.
