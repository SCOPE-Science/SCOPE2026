---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Read full RESULT.md and actual standard-library verify_mk_ind2.py at frozen blob. The graph has 16 vertices, 24 edges and exactly 48 forbidden length-two path triples. Independent enumeration from the graph (not imported face list) found 6812 nonempty faces with f-vector (16,120,512,1324,2064,1840,816,120). Independent prescribed ordered matching has 3400 pairs, 35104 oriented Hasse covers, visited all 6812 nodes in a directed topological sort, and leaves one 0-cell, one 4-cell, four 5-cells and six 6-cells. Signed elimination gives D5=(-1,0,-1,-1), D6 rows (-1,0,0,0,1,-1),(-1,0,-1,-1,1,0),(0,1,0,0,0,1),(1,-1,0,0,-1,0). D5*D6=0; degree -1 cancellation and determinant ±1 of 3×3 minor of quotient 3×6 D6 give a 5-connected homotopy equivalent CW wedge of three 6-spheres by Hurewicz and cellular Whitehead theory. Finite computation is exhaustive for this fixed graph; mod2 ranks alone would not certify homotopy.

## originality

PASS

The 16-vertex graph is not a tree. Sawant proves vertex decomposability of higher independence complexes of trees, not Ind_2(GP(8,3)). Previously published Möbius–Kantor ordinary vertex independence and ordinary edge-matching complex have different face predicates and different homotopy dimensions. A mathematically identical Ind_2(GP(8,3)) result was not found in the actual semantic searches. Knill (2026) full text unavailable, retained as named priority risk.

## value

PASS

The exact integral homotopy classification of the natural three-path-free subset complex of a canonical symmetric cubic graph is a motivated discrete-topology invariant; a complete acyclic matching with verified degree-one cancellations yields information genuinely stronger than Euler characteristic or field ranks. It does not purport to cover all cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
