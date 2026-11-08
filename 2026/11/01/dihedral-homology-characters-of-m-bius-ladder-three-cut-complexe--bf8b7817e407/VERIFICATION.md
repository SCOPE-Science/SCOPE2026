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

For the ordinary (not total) three-cut of the 2n-vertex Möbius ladder, n≥5, Alexander dual K has full 1-skeleton, exactly 6n connected induced triples and n square tetrahedra; 5-vertex dual faces are impossible by 5·4=3e contradiction. In d2, 2n unique distance-two chord rows isolate all cycle-path triangles and 3 signed edge rows per square have determinant ±1, giving a 5n×5n unimodular minor. Since n primitive disjoint tetrahedron boundaries lie in ker d2, rank d2=5n and ker d2=im d3 integrally. H1(K)=Z^{2n²−8n+1}; duality and connectivity upgrade Δ≃∨^{2n²−8n+1}S^{2n−4}. Equivariant Alexander duality adds ambient permutation sign to signed K-chain Lefschetz: all nonidentity rotations (−1)^a; reflection cases n even even/odd a: n−3,3−n; n odd:4−n,n−2. Invariant dimension floor((n−3)/2). Independently built ladder edges, all connected triples, square faces, and signed simplicial traces for n=5…10; all match; finite checks do not establish integral saturation, which relies on the uniform integer minor.

## originality

PASS

Read the full Agarwal–Basak 19-page 2026 manuscript: it treats independence and perfect-matching complexes, explicitly lists cut and total-cut complexes as future problems. Compared published untwisted circular-ladder ordinary cut wedge result and graph-wide edge-disjoint-square theorem; neither provides twisted Möbius D_{2n} character. Exact rank may coincide but equivalence/implication does not.

## value

PASS

The family is a canonical symmetric cubic graph and cut-complex topology is explicitly proposed as a future direction by Agarwal–Basak. The all-n rational dihedral character differentiates reflection axes and computes invariant rank despite quadratic nonequivariant Betti rank. The exact topology of the twisted graph is mathematically motivated and not merely a repeated untwisted result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
