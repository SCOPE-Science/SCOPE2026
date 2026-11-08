---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The vertex set V={2A+B:A,B among four regular tetrahedron corners, A!=B} has 12 vertices of squared norm 11 and exactly 18 truncated-tetrahedron edges of squared length 8, with adjacent inner product 7. A generic central section has one polygon corner per edge with opposite-signed normal projections. Tetrahedral and coordinate-sign symmetries reduce normal directions to 0<=z<=y<=1, partitioned by exactly four internal vertex-normal lines into six rational planar cells. Exhaustively classifying the cell interior sign patterns gives only 4,5,6 sides, two cells each. Hexagonal cell solid angles follow the exact 3-ray determinant identity, yielding q=24/pi(atan(2/S1)+atan(1/S2)); independent edge-sign separation gives mean mu=18/pi arccos(7/11), so p4=5-mu+q, p5=mu-4-2q, p6=q. Independent rational cell counts, determinant checks, high-precision evaluation give (0.21593608531264,0.52024746523894,0.26381644944842); source supplies a separate exact rational >0.518 pentagon certificate. Six cells partition the chamber, so no appeal to Monte Carlo for universality.

## originality

PASS

Random central section type is a natural stereological object. Inspecting classical truncated tetrahedron geometry and nearby exact random-section laws revealed different solids or different observables; the particular full three-atom law was not implied.

## value

PASS

The full distribution of polygon complexity of a Haar-random central section is a basic stereological invariant of a canonical regular Archimedean solid. The noncentrally symmetric truncated tetrahedron has a new six-cell normal arrangement with three possible polygon types, unlike classical cube/icosahedron cases; exact p4,p5,p6 and rigorous pentagonal majority are independently useful facts not implied by a standard face-count table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
