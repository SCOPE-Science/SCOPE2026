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

# Reproduction

Extract `verify.py` next to this file and execute `python3 verify.py` with Python 3.9+; only standard-library modules are used. The checker reconstructs the graph, independently enumerates the entire independence complex, verifies cardinality-based counts and exact Euler characteristic, generates the canonical lexicographic matching, and performs a Kahn topological sort on the **entire** reversed-matching Hasse diagram. It fails with an AssertionError on any mismatched count, invalid simplex, incorrect pair, or detected directed cycle. Successful execution ends in the line `IND_K3_K3_K4_WEDGE_96_S3_VERIFIED`.

Successful package preparation verified outputs: `VERTICES 36 GRAPH_EDGES 216`, `FACES_INCLUDING_EMPTY 30992`, `HASSE_COVERS 178704`, `MATCHED_PAIRS_AUGMENTED 15448`, `ACYCLIC_DAG_VERTICES 30992`, `ORDINARY_CRITICAL_DIMENSIONS {0: 1, 3: 96}`.

The scale-one and scale-three parts use explicit coordinate and diameter arguments in `RESULT.md`. The independence-complex certificate supports this one finite parameter only; no independent scientific assessment has been performed.
