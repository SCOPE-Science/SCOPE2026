---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Any two compatible placements specify two distinct input-output assignments of a permutation of three letters, so they belong to just one full permutation block, which also contains any third compatible placement extending them. Each vertex alone occurs in two blocks; two distinct permutations meet in n vertices iff they differ by a transposition. The nine intersecting pairs form K_{3,3}, with n distinct identifications per pair. All blocks are connected: given two rook positions in Δ_{3,n}, choose a row and column avoiding the row and column of both. To check the gluing, replace identifications by intervals in the disjoint union of the blocks. The intervals are disjoint because each block-slot vertex is used once, so each can be collapsed as a contractible CW subcomplex; the quotient recovers X_n up to homotopy. Instead one can move the endpoint attaching maps to chosen block basepoints by paths (homotopy invariance of the graph-of-spaces attachment), then contract a spanning tree. The resulting wedge has six blocks and 9n−5 circles; the decomposition is not a canonical choice of based wedge maps. At n=3 every edge belongs to a unique triangle, so one distinct free edge can be removed per triangle; the graph has 9 vertices and 12 edges, giving 4 circles per block. At n=4 vertex links are K_{3,3} minus a matching (six-cycles), and adjacent triangles swap the appended unused column with one row column, giving opposite orientations along their shared edge. The connected orientable surface has Euler characteristic 0, hence is a torus. For n≥5, BLVZ Theorem 1.1 makes each ordinary block simply connected. The rank of its free H₂ is χ−1=3n−3n(n−1)+n(n−1)(n−2)−1; Hurewicz and homological Whitehead give the claimed two-sphere wedge. These checks yield 46 circles at n=3, six tori and 31 extra circles at n=4, the sphere/circle formulas thereafter, and the fundamental groups and torsion-free integral homology. Read the bundled finite checker, not run; no inference from finite-field ranks to integer homology is needed.

## originality

PASS

The supported distinct statement is the gluing and full homotopy type of the three-coordinate (3,3,n) matching complex, not the connectivity or types of the ordinary two-coordinate blocks. The directly checked general multidimensional results give connectedness and an ordinary-board homology summand, not the six factors and additional fundamental group. Related indexed ordinary graph matching/avoidance results are different functors on different objects.

## value

PASS

This natural small-side infinite family has an exact, integral homotopy classification, not merely a connectivity bound or table of ranks. The block graph explains why the fundamental group is nontrivial at arbitrarily large n even though each ordinary block is simply connected, and why there are genuine torus summands at n=4. That gives structural information of independent use when testing broader multidimensional chessboard claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
