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

Execute `python3 verify_rankone_graph.py` with Python 3.10 or later; it uses only the Python standard library. The file is embedded beside this document in the same research package. It performs exhaustive *finite* tests over prime fields and \(\mathbb F_4\), enumerating the nonzero rank-one square-zero matrices, constructing adjacency from matrix products, listing maximal cliques, and comparing their sizes, numbers, recovered subspaces, intersections and extremal sizes with the proposed closed formulas.

Expected terminal marker: `RANK_ONE_NILPOTENT_CLIQUE_GEOMETRY_OK 8`.

Successful testing verifies only the listed finite instances, not all \(n\) or all prime powers. Universal correctness rests on the proof in `RESULT.md`. No independent audit or external certification was conducted.
