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

# Reproducible finite verification

The graph is defined explicitly in `RESULT.md`. The complete standalone standard-library Python programs `verify_dfs.py` and `verify_edges.py` each rebuild that graph from an independently expressed adjacency rule. Execute:

```sh
python verify_dfs.py
python verify_edges.py
```

The depth-first program enumerates all unoriented spanning paths and their endpoint backbites, then runs breadth-first searches from every state. It asserts the entire distance histogram and checks an explicit pair at distance nine with distance-sphere sizes \((1,4,12,28,45,55,49,21,6,1)\).

The edge-subset program checks all \(43758\) ten-edge subsets for a connected spanning path, reconstructs legal exchanges via edge differences, repeats all-pairs shortest distances, and verifies endpoint counts using a separate dynamic-programming recurrence.

Expected success messages include `DFS_222_UNDIRECTED_HAMILTONIAN_PATHS_PASS`, `EDGE_SUBSETS_43758_EXHAUSTIVE_222_PATHS_PASS`, and `ALTERNATE_DISTANCE_HISTOGRAM_RADIUS8_DIAMETER9_PASS`. Every reported numerical assertion is checked in executable code; a computation failure invalidates the affected evidence rather than providing a negative mathematical result.

The proof is exact for the stated finite eleven-vertex graph only. No independent human audit or external validation is represented by this document.
