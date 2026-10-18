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

# Reproducible checks

Run `python3 check_trees.py` with Python 3 and no third-party packages. Expected final lines:

```
DP_VS_EMBED_OK 5016
BRUTE_VS_DP_OK 196
```

The first comparison is over all pairs of unlabeled rooted-tree shapes with 1–7 source vertices and no more target vertices; it compares a direct predicate based on recursive matching with an independently encoded LCA-preserving embedding search. The second enumerates all functions with the source root mapped to the target root and verifies for every source vertex that the image of its entire descendant cone equals the corresponding target cone. Both are finite checks, and neither establishes the universal assertion outside the tested bounds. The mathematical proof is in RESULT.md, Steps 1–3, with separate necessity and sufficiency arguments. The source files and their encoded byte hashes are embedded in the accompanying record.
