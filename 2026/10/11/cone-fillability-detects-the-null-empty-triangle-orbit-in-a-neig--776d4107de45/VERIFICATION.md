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

Independently reconstructed all 35 tetrahedra from four cyclic representatives, with f-vector (10,45,70,35), a complete graph as 1-skeleton, and exactly 70 facial/50 missing triangles. Spanning-tree collapse reduces ∂2 to 70x36 integral cycle relation matrix R with rank 35. Source verifier supplies a 35x35 unimodular minor of determinant -1 and primitive annihilating cocycle, proving H1=Z with no torsion, not merely rational rank one. Independently recomputed the primitive annihilator and evaluated all 50 missing triangles: value distribution +1:30,-1:10,0:10, with 5 cyclic orbits of size 10. Independent apex enumeration yields (0,3) for exactly 10 null triangles and (±1,0) for the other 40; representative (1,2,8) has apices 3,6,7. These finite exhaustive checks cover all faces/triangles/apices of the specified complex; no infinite extrapolation.

## originality

PASS

The primary historical classifications list this exact neighborly type and its facet orbits, but inspected original 1985 full text and the 2005 atlas do not count empty triangles by integral H1 class or characterize local cone-fillability. A highly ranked related Resultary ten-vertex S2×S1 record concerns a *different* f-vector (10,40,60,30) and induced H2 supports, so cannot cover this empty-triangle H1 result. Bounded novelty risk remains for older unindexed finite tables.

## value

PASS

On a canonical neighborly S2×S1 triangulation, the exact integral homology classes of all shortest nonfacial 3-cycles and their local conical fillability classify a natural minimum-support invariant, giving a concrete local criterion for null-homologous shortest cycles. This is object-specific but complete, reproducible and mathematically motivated beyond restating a facet table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
