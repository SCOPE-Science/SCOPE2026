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

The included `check_4x4_perfect_matching.py` is a complete standard-library checker for the specific finite graph, with no external files or network access required.

It recursively enumerates all 36 perfect matchings and the complete 5,407-face augmented simplicial poset. It checks the 2,702 disjoint toggle pairs, exhaustively verifies acyclicity by topological sorting 24,812 directed Hasse incidences, and identifies precisely two two-dimensional and one three-dimensional critical faces. An independent simplicial reduction checks 2,628 elementary free-face collapses to 14 vertices, 49 edges, 62 triangles and 25 tetrahedra. Exact signed integer boundaries verify a nonzero 25-term top cycle, and exact binary elimination computes boundary ranks 13, 36 and 24. Those calculations certify the vanishing of the sole integral three-cell Morse attaching column through rational homology, completing the wedge proof.

The coefficient vector refers to tetrahedra of the deterministically reduced complex sorted by integer face bitmask, not to the original 36 maximal simplices. The script asserts all claimed values and prints `MORSE_AND_EXACT_TOP_CYCLE_GRID_4X4_OK` only upon complete success. Finite verification proves this exact finite case only; it does not establish the conjectured wedge property for arbitrary grids. Independent audit has not been performed.
