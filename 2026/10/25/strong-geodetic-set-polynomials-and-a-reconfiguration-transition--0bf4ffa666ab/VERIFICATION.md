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

# Reproducibility and scope

Run `python3 verify.py` with an ordinary Python 3 interpreter and no third-party packages. It constructs the simple undirected Cartesian graph from edges, computes distances by breadth-first search, and for every vertex subset builds a bipartite incidence graph from omitted vertices to distinct selected-pair geodesics. Because these prisms have diameter two, each selected endpoint pair can cover at most one omitted internal vertex; an augmenting-path matching determines whether all omissions can be covered simultaneously. This procedure does not import or call the structural classifier.

Tested orders are \(n=2,3,4,5,6,7\), covering 21,840 vertex subsets. The script compares every predicate value, every coefficient of the all-set and inclusion-minimal polynomials, and the minimum-set token-jumping distances for \(n=4,5,6,7\). It outputs `ALL_CHECKS_PASS` on successful completion. The mathematical proof in RESULT.md establishes the theorem for every integer \(n\ge2\); exhaustive finite testing does not imply the infinite case. Independent external mathematical audit has not been performed.
