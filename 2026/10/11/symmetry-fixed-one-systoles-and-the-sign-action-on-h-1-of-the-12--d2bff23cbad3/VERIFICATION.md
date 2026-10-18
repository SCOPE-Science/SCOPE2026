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

Using the exact 54 tetrahedra from the inspected verify.py, independently reconstructed 12 vertices, all 66 edges and 108 distinct triangles. The fundamental cycle lattice relative to the vertex-1 star has 55 edges. An independent SymPy exact integer determinant of the source specified 55-column triangular boundary minor is -3. Independent modulo-three elimination of the full 55x108 boundary matrix has rank 54, so integral H1 is Z/3, not merely a mod-three lower bound. Its nonzero dual cocycle evaluates the 112 missing triangles nontrivially, with class counts 56 and 56; complete one-skeleton makes these exactly all length-three nonzero simple 1-cycles and minimizes length. Independently generated all six published S3 automorphisms, checked preservation of the 54 tetrahedra and obtained 15 size-six, six size-three, one size-two and two singleton orbits. Exactly (7,8,9),(10,11,12) are globally invariant triples, and the two generator actions on mod-three homology are -1 and +1. These are exhaustive checks of this finite complex, not a claim about other lens-space triangulations.

## originality

PASS

Lutz gives the 12-vertex facet table, face vector, lens-space identity and full S3 generators; these data do not themselves state that all 112 missing triangles are essential nor enumerate orbit-size distributions and induced H1 sign action. Another published same-complex result concerns **dual degree-one cohomology cosystole support 28 and 18 minima**, not primal shortest homology cycles and the 112 triangle supports. The 14-vertex cyclic L(3,1) spectrum has a distinct facet set, automorphism group and orbit spectrum. No earlier statement with the same 112-carrier census and character was found in the materially inspected public texts.

## value

PASS

The exact labeled 12-vertex Lutz lens-space triangulation is a canonical minimal-vertex model, and shortest nonzero integral H1 carriers with their S3 orbit spectrum are natural invariants of its triangulation. Identifying the only globally invariant cycles and nontrivial sign action is a specific topological–combinatorial symmetry fact, not an arbitrary slice or mere recomputation of the known face vector.

The dated certificate retains the supplied scientific assessment, sources and limitations.
