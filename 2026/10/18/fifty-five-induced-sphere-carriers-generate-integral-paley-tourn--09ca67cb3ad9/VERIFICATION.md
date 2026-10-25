---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Construct transitive-face simplices with canonical source-to-sink order, f=(11,55,110,55), chain matrices satisfying d1*d2=d2*d3=0. Independent Python/SymPy enumeration of all C(11,5)=462 supports finds precisely 55 with beta_2(F2)=1 and affine orbit of W0={0,1,2,3,7}; W0 six triangles form triangular-bipyramid sphere plus extra edge, with no tetrahedra. d1 rank10, d2 rank45, d3 rank55; exact Smith d3 factors 1^54 and 2 => H2 free rank 65-55=10 with Z/2. Construct orientation cycles of 55 spheres, augment d3: exact Smith has precisely 65 nonzero factors all units, establishing saturation of rank65 primitive ker d2. Tetrahedral sum d3 has 110 coefficients ±2 (55 each); half is integral cycle with 2z boundary, and d3 rationally injective forces z not boundary. Affine action permutes source-to-sink tetrahedra, so z fixed. All claims independently replayed with exact integer operations, not inferred from logs.

## originality

PASS

Govc 2020 Proposition 3.4 explicitly already computes the abstract homotopy type of the unique order-11 doubly regular tournament, including Moore-space 2-torsion; that fact is prior and not counted as new. Its published result does not provide induced five-vertex carrier orbit, unimodular integral cycle generation by these carriers, nor the explicit group-invariant full-support torsion representative. Relevant related Resultary records concern other complexes and larger Paley tournaments.

## value

PASS

A complete minimal-support classification and integral spanning certificate for a natural small tournament are substantive geometric-homological invariants; Smith data distinguish integral generation from weaker rational spanning, while invariant torsion chain makes abstract torsion concretely accessible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
