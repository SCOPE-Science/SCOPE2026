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

# Reproducible finite mathematical checks

Execute `python3 verify.py`. This single standard-library Python program constructs the eleven-vertex eighteen-edge Herschel graph, enumerates every subset of its edge set and retains precisely the disjoint-edge faces. It checks the complete nonempty face vector `(18, 111, 280, 270, 72)` and verifies all `752` faces including the empty face.

It constructs the explicit discrete-Morse matching using the ordered toggles in `RESULT.md`, verifies `369` matched pairs and thirteen critical simplices (one 0-simplex, twelve 3-simplices), orients all `2502` Hasse incidences, and verifies that the resulting directed graph on all `751` nonempty simplices is acyclic via a complete topological traversal. This is a finite, exhaustive acyclic discrete-Morse certificate for the given graph. The standard discrete-Morse theorem gives the asserted integral homotopy wedge.

The same program constructs every one of the twelve elements of \(S_3\times C_2\), checks their edge actions, evaluates the signed reduced Lefschetz trace for each one and tests class constancy. The traces, arranged by \(S_3\) identity/transposition/three-cycle with flip off then on, are `(12, 0, -3, -2, 2, 1)`. Exact character inner products yield multiplicities `(1, 0)`, `(0, 1)` and `(2, 3)` for trivial, sign and standard \(S_3\) types, respectively.

The successful terminal output begins with `VERIFY_OK_HERSCHEL_MATCHING_COMPLEX_DIHEDRAL_HOMOLOGY`. These calculations verify one finite complex exhaustively and use exact integer counts and character sums. They do not certify novelty, represent an independent audit, or imply analogous results for other graphs.
