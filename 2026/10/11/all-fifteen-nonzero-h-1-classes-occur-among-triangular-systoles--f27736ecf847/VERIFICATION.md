---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The pinned verify.py embeds the exact 107-tetrahedron Lutz G6 facet list, which has now been compared with the public flat_3manifolds.txt G6 block; vertices 17, edges 124, faces 214, tetrahedra 107. A spanning tree contracts 16 edges, yielding Z^108 graph-cycle generators and 214 oriented face relations. An independent implementation computes the integer Smith form as 106 unit invariants and 4,4; mod-4 elimination independently derives two quotient coordinates annihilating face relations. Exhaustive enumeration of all C(17,3) possible triples finds 519 complete graph triples; 214 are facial, so 305 are nonfacial triangles. All 305 give nonzero class, and their classes cover all 15 nonzero elements of (Z/4)^2. Unoriented order-four inverse-pair counts are (52,51,51,48,45,38) and three order-two counts (13,5,2). No simple edge-cycle has fewer than three edges; each missing triangle is thus a length-3 integral homology systole. Orientations reverse classes and do not change the unoriented counts.

## originality

PASS

Lutz’s exact geometric manifold table already gives the triangulation, f-vector and H1; it does not supply the **class of each nonface triangle**. The nontrivial complete 305-carrier, all-15-class systolic census therefore extends established base data by a new natural combinatorial invariant.

## value

PASS

A complete class-by-class shortest homology-cycle spectrum of the canonical small Hantzsche–Wendt triangulation is a motivated exact topological/combinatorial invariant. It distinguishes the torsion classes by shortest carriers and multiplicity even though abstract H1 is known. Exhaustiveness over a natural finite fixed complex and the all-15-class coverage are independently useful, and not a textbook corollary of the homology group alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
