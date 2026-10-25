---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and checked limits

Execute `python3 verify.py` in a directory containing the attached standalone checker. It requires only Python's standard library.

The checker constructs the Cartesian grid graph, independently enumerates all connected three-vertex subsets and all four-vertex subsets whose triples are connected, checks absence of triangles, and exhaustively excludes five-vertex dual simplices when the grid has at most 30 vertices. It then executes all stated elementary collapses with exact free-face tests against the currently surviving faces, verifies the remaining triangulated torus and isolated long chords, checks that every original edge belongs to exactly two square boundaries, and checks that the sum of consistently oriented torus triangles has zero boundary. It does not infer the infinite theorem from samples.

The four checked grids are \((5,5),(5,6),(6,6),(5,7)\). Their dual face vectors are respectively \((25,300,150,25)\), \((30,435,180,30)\), \((36,630,216,36)\), and \((35,595,210,35)\), with \(100,120,144,140\) verified collapse pairs. The exact long-chord counts are \(150,255,414,385\), and the corresponding predicted lower/top cut-homology ranks are \((1,152),(1,257),(1,416),(1,387)\). The checker terminates with `VERIFY_OK` when all assertions pass.

The proof for all \(m,n\ge5\) is combinatorial: uniqueness of paths and squares, explicit free-face collapses, the standard torus cellulation, and integral combinatorial Alexander duality. The checker does not directly construct the large original cut complex or provide an external independent mathematical assessment. No cases with a shorter cycle or a different cut convention were checked or claimed.
