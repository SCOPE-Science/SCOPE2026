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

The mathematical recurrence is proved in `RESULT.md`. To reproduce the finite independent checks, install dependencies from `requirements.txt` and execute `python verify.py`.

The verifier compares the incidence-forest maximum against an unrelated brute-force closure implementation, testing all subsets on 103 connected cactus isomorphism types from the graph atlas with at most seven vertices. Four larger branching examples are also tested. A separately assembled optimal seed set is checked against deletion of every seed.

Expected terminal output:

```
ALL_CONNECTED_CACTI_GRAPH_ATLAS_THROUGH_7_OK 103
BRANCHED_CACTUS_OK (3, 3, 3, 3) 9 4
BRANCHED_CACTUS_OK (3, 4, 5) 10 7
BRANCHED_CACTUS_OK (4, 4, 4) 10 7
BRANCHED_CACTUS_OK (3, 3, 3, 3, 3) 11 5
VERIFY_OK
```

These exhaustive finite checks do not themselves verify the infinite theorem; the proof's factor-forest and essential-branch arguments supply that step. The main historical-priority uncertainty is that an unindexed general closure-algebra theorem might imply the max–sum recurrence. No independent audit has been performed.
