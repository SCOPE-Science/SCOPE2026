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

Independently reconstructed all 48 tetrahedra from the frozen 48-facet list, obtaining f=(12,60,96,48), missing graph-edge pairs {(1,7),...,(6,12)}, 160 three-cliques and exactly 64 nonfacial triangular loops. Exact mod-two boundary rank 48 inside 49-dimensional graph cycle space gives H1(F2) dimension 1; direct reduction finds each of 64 nonfacial boundaries nonzero. Published topology RP3 implies integral H1=Z2, and H0 torsion-free means mod-two reduction of its unique torsion generator is nonzero, so these are exactly the simple integral 3-edge systoles. Exhausted all 6!·2^6=46080 permutations of six opposite pairs, precisely 24 facet-preserving automorphisms, and computed orbit sizes 4/12/24/24, representatives (1,5,9),(1,2,12),(1,2,4),(1,2,6); four smallest orbit triangles cover all 12 vertices disjointly. No geometric/Riemannian-length conclusion.

## originality

PASS

Best-of-knowledge statement/implication assessment: The classification and underlying 48 facets allow reproduction but neither the published topology nor the 24-cell quotient fact logically states or forces the four shortest-carrier orbits without additional computation. Relevant primary exact-object sources and indexed findings were checked by object, invariant and quantifiers; inaccessible plausible material is retained explicitly as risk, not treated as automatic scientific rejection.

## value

PASS

The antipodal regular 24-cell quotient is a canonical vertex-transitive RP3 triangulation. Its complete simple shortest nonzero integral homology layer is a natural combinatorial systolic invariant. The 64-carrier count, four symmetry orbits and disjoint parallel class refine the known RP3 topology and group order, not arbitrary cherry-picked enumerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
