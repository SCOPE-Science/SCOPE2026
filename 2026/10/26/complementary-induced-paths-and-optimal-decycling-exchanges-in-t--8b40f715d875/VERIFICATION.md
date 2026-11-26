---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently enumerated all deletion sets of sizes 0 through 6 in the specified ring graph using disjoint-set cycle detection, not the supplied traversal. Exactly sixty are optimal. Both sides of each have an acyclic induced graph with degree sequence (1,1,2,2,2,2), which forces one path on six vertices. Formed every unordered single-exchange edge by set difference, verified that the exchanged host vertices are adjacent and all sixty exchange degrees are four, and used Floyd–Warshall to reproduce all 3,600 ordered overlap–distance entries, complement distance six, eccentricity six throughout, the distance-parity bipartition and 840 ordered detours. The argument and computation are exhaustive for this finite graph. Replay: python3 /workspace/review-checks/icosahedron.py. The frozen DFS/BFS implementations and recorded outputs were inspected, not executed.

## originality

PASS

Pass is for the complementary induced-path structure and optimum exchange geometry, not the known scalar decycling number or the already tabulated count of sixty. A distinct later record reproduces the core claim in an equivalent convention and is substantive matching coverage, but not evidence that this claim was already covered at the frozen record's date. No earlier inspected source or stronger theorem established the complementary-path and exchange assertions.

## value

PASS

For a canonical small graph, the complete optimal solution space exposes a rigidity not conveyed by the previously known count: two induced paths on every optimum cut and no jump that is not a host-edge slide. The distance census quantifies exactly when the natural overlap lower bound is attained and when an intermediate detour is necessary, giving reproducible benchmark data for optimal feedback-set reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
