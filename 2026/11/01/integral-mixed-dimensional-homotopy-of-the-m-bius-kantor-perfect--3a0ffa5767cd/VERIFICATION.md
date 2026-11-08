---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

PASS: The GP(8,3) graph is explicitly rebuilt on 16 vertices and 24 edges. Exhaustive smallest-unused-vertex recursion and a second bipartite permutation enumeration both give exactly 33 perfect matchings, and their downward closure has 6,051 nonempty faces with face vector (24,228,984,1842,1752,924,264,33). A distinct enumeration of all 11,068 graph matchings with residual perfect-matching feasibility matches the extendible face set. Independently reconstructed the 3,014 staged toggle matching pairs and entire oriented Hasse graph (27,192 covers); topological sorting visits every one of 6,051 faces with critical cells 1 in dimension 0, 9 in dimension 2, 13 in dimension 3. Reconstructed the signed gradient-path Morse matrix from actual face lists; its rational rank is exactly 5 and the asserted 5×5 minor on rows (1,2,3,4,5), columns (0,1,4,5,7) has determinant -1. Hence all five Smith factors are units. The Morse 2-skeleton is a simply connected wedge of nine 2-spheres; π2=H2 identifies all 3-cell attaching maps by integer degrees, and unimodular cancellation gives exactly wedge^4 S² ∨ wedge^8 S³. The finite enumeration is exhaustive for the stated single graph; no infinite graph-family theorem is inferred.

## originality

PASS

PASS best-of-knowledge: exact same graph ordinary matching complex is known but has a strictly larger face set and different homotopy type; known perfect-matching-complex theorems are for planar honeycomb or polygonal-line graph families. No inspected prior theorem implies the integral wedge of the 6,051-face extendible subcomplex. Residual unindexed graph-alias priority risk recorded.

## value

PASS

PASS: The perfect-matching subcomplex is a canonical but substantially different object from the ordinary matching complex of the famous Möbius–Kantor graph. The exact integral mixed-dimensional homotopy, with a primitive nonzero 3→2 attaching matrix, resolves its natural complete invariant and can inform future perfect-matching-complex families and comparisons. It is not an arbitrary numerical slice or reproduction of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
