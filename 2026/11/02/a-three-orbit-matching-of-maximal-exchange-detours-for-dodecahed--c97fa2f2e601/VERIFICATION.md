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

The complete certificate is finite and deterministic. Run `python3 verify_direct.py` and `python3 verify_independent.py` using Python 3.10 or later. Neither program downloads data or depends on external packages.

The direct implementation constructs `GP(10,2)` using modular edges, enumerates all 38,760 six-subsets, checks acyclicity by disjoint-set union, constructs the full one-vertex exchange graph, and computes breadth-first distances from all 2520 accepted masks. It verifies the degree distribution, overlap-distance census, the 180 maximal-excess pairs, per-edge counts, group closure from checked automorphisms, and the three explicit orbit representatives.

The independent implementation constructs a differently labeled dodecahedral graph, checks an explicit isomorphism, detects cycles by residual leaf stripping, constructs adjacency using intersection size five, and recomputes every pairwise distance. It independently checks the table, all eccentricities, unique exceptional partners, and unique common original edges.

Successful executions print `DIRECT_DODECAHEDRAL_FVS_ALL_PAIRS_AND_ORBITS_PASS` and `INDEPENDENT_PLANAR_PEELING_METRIC_PASS`. The finite exhaustiveness is justified by the complete six-subset generation and exhaustive all-pairs BFS, not by approximate experiment. The outputs do not constitute independent external auditing or proof of priority.
