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

I reconstructed the LCF edges (36 edges, all degrees three) and computed girth by finding the shortest alternate path for each edge (girth seven). Inclusion-maximal independence is equivalent to independence plus domination: an undominated vertex is exactly a vertex that can be added. An independent exact calculation (/tmp/opencode/scope-review-mcgee.py) enumerated maximal cliques of the complement with pivoted Bron–Kerbosch (all maximal cliques, no duplicates), then used intersection size seven to form all exchanges at the minimum and Floyd–Warshall for the distance matrix. It yielded maximal-set counts 146, 352 and 8 at sizes 8, 9 and 10 only; 216 edges, no triangles, degrees 2:64, 3:48, 4:16, 5:16, 8:2; radius 11, diameter 12, eccentricities 11:144 and 12:2. The only distance-12 pair had sorted zero-based indices (77,104) and masks (4793490,9586980), the two stated residue classes. Any admissible jump removes the old neighbor of the added vertex, since the old set dominates it and the new set is independent; thus all jumps are slides. Exhaustive adjacency/nonadjacency-preserving partial bijections generated the full 32-element automorphism group, with exactly seven orbits of the stated sizes and the pair the sole two-element orbit. All labelled minima, edges, eccentricities, permutations and orbit representatives matched mcgee_certificate.json; deletion–contraction independently gave the claimed face vector. The frozen Python checker validates listed permutations, not their completeness by itself; the primary enumeration and my independent bijection search establish completeness. Frozen scripts were inspected, not executed. No C++ rerun or external attestation is asserted.

## originality

PASS

Credit the already-defined i-graph, known cage and known independent-face vector. The retained contribution is the exact labelled minimum-independent-domination exchange classification of this cage, in particular the unique diameter pair and its exceptional symmetry orbit. The closest inspected same-object and same-graph statements do not establish this classification.

## value

PASS

The smallest cubic girth-seven graph is a canonical sparse benchmark, and the natural i-graph asks whether exact independent domination optima can move locally while keeping feasibility and optimality. Its sole farthest pair, exactly coincident with an exceptional original-graph orbit, and 11/12 eccentricity separation are structural information beyond a routine face count and useful for checking exact reconfiguration computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
