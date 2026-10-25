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

# Finite exact verification

Compile `truncated_cube_verifier.cpp` using `g++ -O3 -std=c++17 truncated_cube_verifier.cpp -o check` and run `./check`. No downloaded graph data, graph-library API or previously recorded program output is used in the computation.

The executable reconstructs the 24-vertex graph from the cube-truncation definition, independently verifies the cubic vertex degrees and eight triangles, enumerates all 1,019,739 nonempty matching faces, checks the exhaustive matching face vector, constructs 509,667 face-coface pairs, and topologically sorts all 1,019,739 vertices of the fully directed Hasse diagram with 7,220,436 covering relations. The complete sort certifies acyclicity.

The remaining Morse complex contains exactly one zero-cell, 368 seven-cells and 36 eight-cells. The signed 368-by-36 cellular boundary is computed by recursive gradient-path reduction and recomputed by a separate topologically ordered coefficient-flow algorithm. Both calculations agree on all entries. Exactly 698 entries are nonzero, all equal to \(\pm1\). The exact integral elimination finds 36 unit pivots with intermediate absolute values at most two. These give an injective, primitively embedded image of rank 36 and the asserted wedge homotopy type.

The checker reports `VERIFY_OK` only after the tests pass. All results concern this one graph; neither infinite families nor independence from other verification are claimed. Self-review does not constitute an independent audit.
