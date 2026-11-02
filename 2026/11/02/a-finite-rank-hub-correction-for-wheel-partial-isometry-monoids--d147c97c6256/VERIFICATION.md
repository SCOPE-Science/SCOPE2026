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

Run `python3 verify.py` with Python 3 and only the standard library. On the included file, the actual output was:

```text
RUN_INVENTORY_OK n=5..11
EXHAUSTIVE_OK 5 rank_counts 1,36,250,400,200,60,10 exceptional 10,125,200,50
EXHAUSTIVE_OK 6 rank_counts 1,49,450,978,672,288,84,12 exceptional 12,180,360,72
EXHAUSTIVE_OK 7 rank_counts 1,64,784,2352,2450,1470,490,112,14 exceptional 14,245,588,98
POLYNOMIAL_INTERNAL_OK n=8..13
VERIFY_OK
```

The verifier independently enumerates every injective partial map on the rim cycle and wheel for \(n=5,6,7\), checks all pairwise adjacency relations, and categorizes whether a valid wheel map avoids the hub, fixes it, or belongs to the exceptional class. Its separate subset inventory check reconstructs run profiles directly by graph connectivity on all vertex subsets for \(5\le n\le11\). The final larger-parameter arithmetic checks verify consistency of the displayed polynomial identity but are not exhaustive partial-map checks. Only the mathematical argument in `RESULT.md` establishes all \(n\ge5\); finite verification alone cannot do so.
