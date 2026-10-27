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

# Verification record

A standalone reproducible checker is included as `check_weak_ideals.py`, runnable using `python3 check_weak_ideals.py` with no external dependencies.

The checker directly evaluates union-closure and convexity for **every** collection of teams over universes of \(0,1,2,3,4\) valuations, and compares that predicate with an independently implemented unique-maximum/upset criterion. It also directly counts globally upward-closed collections and verifies the combinatorial decomposition by maximum-team cardinality.

Actual output:

```
DIRECT_FAMILY_CLASSIFICATION_OK n=0 weak=2 global_upset=2 by_top=[1]
DIRECT_FAMILY_CLASSIFICATION_OK n=1 weak=4 global_upset=3 by_top=[1, 2]
DIRECT_FAMILY_CLASSIFICATION_OK n=2 weak=11 global_upset=6 by_top=[1, 4, 5]
DIRECT_FAMILY_CLASSIFICATION_OK n=3 weak=42 global_upset=20 by_top=[1, 6, 15, 19]
DIRECT_FAMILY_CLASSIFICATION_OK n=4 weak=283 global_upset=168 by_top=[1, 8, 30, 76, 167]
BSL_SUPPORT_SPECTRUM_OK q=1 N=2 total=11 upward=6 exceptional=5
BSL_SUPPORT_SPECTRUM_OK q=2 N=4 total=283 upward=168 exceptional=115
BSL_SUPPORT_SPECTRUM_OK q=3 N=8 total=56130437248005233867039 upward=56130437228687557907788 exceptional=19317675959251
WEAK_IDEAL_SPECTRUM_AND_CONCENTRATION_CHECK_OK
```

The last three lines use published exact Dedekind numbers; the \(N=8\) number is **not** obtained from an exhaustive enumeration of all weak ideals. The limitless asymptotic follows from the proof and the externally established logarithmic Dedekind estimate, not from these finite computations. A review of source assumptions and of the distinction between support-only and full bilateral equivalence was conducted; no independent audit was performed.
