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
# Reproducible checks and scope
Run `python3 verify_ladder.py` with a standard CPython interpreter; no third-party packages are needed. The program enumerates the actual graph adjacencies, all-pairs shortest paths, maximal shortest paths and vertex subsets for each \(n\in\{2,3,4,5,6,7,8\}\). Observed output:

```
ALL_LADDER_CHECKS_PASS orders=2..8 graphs= 7 successful_sets= 85577 maximal_geodesics=2n
```

The script compares the graph-definition answer to the claimed subset characterization, all-set coefficient polynomial and inclusion-minimal coefficient polynomial. Finite verification does not replace the proof for every \(n\ge2\). No independent scientific audit is represented by the script.
