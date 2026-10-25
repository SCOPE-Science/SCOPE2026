---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The graph is the explicitly listed 18-vertex, 27-edge, cubic Pappus graph, and Ind2(P) consists of vertex sets whose induced components each have ≤2 vertices, equivalently max induced degree ≤1. My independent 2^18-subset face enumeration yields exactly 20651 nonempty faces and the listed ten-coordinate f-vector (18,153,762,2394,4806,6027,4428,1728,308,27), with high-dimensional nonpurity. The fixed pivot sequence gives 10319 nonempty-face matching pairs and precisely one critical vertex, ten critical 5-cells and two 6-cells. Orienting all 120222 nonempty face-poset cover edges and exhausting a topological order checks the matching has no gradient cycle. Integer unit-incidence elimination yields Morse ∂6 with rows [-1,0,0,-1,-1,0,0,0,0,0] and the exact negative, rank1 and unit invariant factor. Therefore integral reduced H5=Z^9,H6=Z, other reduced homology zero. With no Morse cells of degrees1–4, its 5-skeleton is wedge10 S5; pi5 equals H5 by Hurewicz, so the one primitive attaching degree cancels a 5/6-cell pair and the remaining 6-cell attaches trivially. Hence integral homotopy ≃ wedge9 S5 ∨ S6 for precisely this graph.

## originality

PASS

The graph and parameter Ind2 must both match. Known Pappus ordinary independence is wedge10 S4, not Ind2. The literature on higher independence complexes gives major graph-family classifications (trees, multipartite, paths etc), but the canonical cyclic cubic incidence graph does not fall into them. Targeted Resultary search found no same object/parameter mixed wedge; this remains a best-of-knowledge verdict with an unindexed-census risk.

## value

PASS

The Pappus graph is a canonical 18-vertex cubic Levi/incidence graph; the natural induced-degree-one/higher independence complex is a standard invariant. Its exact mixed-dimensional integral homotopy with a nonzero critical 6-cell, verified nonpurity and torsion-free result is neither mechanically inferred from its ordinary independence calculation nor a textbook exercise. The explicit finite natural invariant is a useful benchmark for higher independence and Morse topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
