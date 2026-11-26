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

For a flag complex with nonzero reduced H_d on a minimal induced support, removing a vertex forces nonzero H_{d-1} in its link by the deletion–star exact sequence. A universal vertex would make it a cone. Induction from two nonadjacent vertices in degree zero gives at least 2d+2 vertices, and at equality each vertex has exactly one nonneighbor. Nonzero ambient image implies nonzero intrinsic homology, so this bound applies to the claim. The five opposite pairs at equality must come from five disjoint centered two-edge paths; every such packing gives a candidate and its inclusion class must still be checked. A vertex-deletion matching enumeration and path recursion on the least uncovered graph vertex (one omitted vertex allowed) recovered 912 distinct supports. I verified the Hasse DAG with 5,525 pairs and 53,256 covers, then subtracted signed coface boundaries in topological order. Surviving matched-upper coordinates cannot support a cycle by themselves, since their boundary has a unit triangular block. The six critical boundary columns were (u,0,0,v,u,0) with u,v as stated; their unit minor on rows 1,5 and agreement with the image of all 2,444 original degree-five boundaries give an injective quotient coordinate map to Z^8. The named eight cycles have determinant +1 in exactly the stated q chart, so the map is onto. All 912 signed chains are cycles and all have gcd-one integral coordinates. Metric-preserving automorphism enumeration gave 96 group elements, the stated ten orbits, and exact Smith forms with all nonzero invariants one and precisely the stated ranks. In particular orbits 0,6,7,9 each integrally generate H_4.

## originality

PASS

The properly credited ambient homotopy type and Morse matching were already in the October 4 same-object record. The distinct contribution is the cardinality and inclusion geometry of minimum supports and the integral structure of their symmetry-orbit spans. Neither that result nor the other inspected statements establish these claims.

## value

PASS

The minimal-support invariant asks which induced subcomplexes of a standard symmetric cubic graph can actually realize a nonzero ambient integral class. It refines the known rank by giving explicit smallest generators, and by separating rank-four, rank-seven and rank-eight orbit spans while showing each is saturated. In particular, four individual orbits provide alternative integral generating sets, useful for symmetry-sensitive constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
