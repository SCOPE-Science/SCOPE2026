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

Reproduced the full labeled census from an independent even-parity representative model of the folded five-cube. Two distinct even representatives are adjacent exactly when they differ in four bits. The maximum independent set size is five, ruling out three colors. Each proper coloring gives an exact cover by four nonempty independent sets. Choosing the block of the least uncovered vertex at each stage counts each cover once; 1,190 covers times 24 palette permutations gives 28,560 states. Transfers of one vertex between color blocks, retaining only valid states, reproduce all edges, the full degree distribution and the component census: 1,680 singletons and 960 components each with 28 vertices, 60 edges, diameter 6. The BFS tests include all source vertices. Independent component orbit enumeration gives 960, 1,440 and 240. For completeness of the symmetry group, translations are transitive and the stabilizer at zero acts faithfully on the five neighbors: each other nonzero vertex is determined by its distinct pair of neighbors among them. Coordinate permutations realize the entire symmetric group on these five neighbors, and palette transpositions generate S4. Thus the full product action yields exactly those orbits; in particular transitivity on non-singletons implies isomorphism, not just common numerical invariants.

## originality

PASS

The total coloring count is already recorded and the broad edge-count formula applies, but the checked work does not cover the complete component, distance and orbit census of this graph. The strongest relevant indexed comparisons address different kinds of colorings or configurations, not the stated reconfiguration graph.

## value

PASS

Recoloring at the chromatic number is a natural reachability problem on a canonical graph. The classification exposes two genuinely different frozen-state orbits and one common connected component type; it answers both reachability-structure and distance questions that the known coloring count cannot answer. It supplies a reproducible exact benchmark for minimum-palette recoloring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
