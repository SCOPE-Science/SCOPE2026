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

# Reproducibility and verification

Run the accompanying program with Python 3:

```bash
python verify_graph_stability.py
```

The script builds each graph context from the edge-vertex incidence relation, enumerates every subset of the edge objects, directly calculates its common incident vertices, derives the associated formal concept, and counts the subsets giving each intent. The resulting rational multiset is compared to the proposed exact expression. It additionally checks that coatom-star intersections recover adjacency, and tests the nonisomorphic cubic witness graphs by triangle existence and by direct stability calculation.

Observed run:

```text
VERIFY_OK graphs=266 enumerated_object_subsets=37624 witness=K33_vs_triangular_prism spectrum=1:1,1/2:15,239/256:1
```

All labelled simple graphs with minimum degree at least two on three, four, and five vertices are checked exhaustively, along with the two six-vertex cubic witnesses. This bounded enumeration independently exercises the formulas; it is not an infinite mathematical proof. The written proof supplies the unrestricted argument. No independent external review was performed.
