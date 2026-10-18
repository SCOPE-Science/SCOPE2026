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

# Reproducible verification

Run `python3 verify_morse.py` and `python3 verify_homology_symmetry.py` in a directory containing just these scripts (Python 3 standard library). Their recorded deterministic outputs are provided separately. Both programs are standalone and construct the graph from separate explicit data encodings; no downloads, packages, external data or commands are needed.

The first certificate counts 424 nonempty faces, 211 discrete-Morse pairs, and all 1,428 covering relations, and topologically sorts the entire oriented Hasse graph. Exactly one critical vertex and one critical three-dimensional simplex remain. Representatives of the deletion and link computations have face/pair counts `(302,150)`, `(121,60)`, `(305,152)`, `(118,58)` for `D0,L0,D2,L2`, respectively. The script checks acyclicity for all four and separately exhibits complete legal simplicial collapses of `L0` (60 pairs) and `D2` (152 pairs). It also tests all adjacency-preserving bijections and finds exactly 8 automorphisms in the stated vertex orbits.

The second program uses combinations and a separately encoded adjacency table, reconstructs the complete mod-two simplicial boundary matrices, and obtains reduced Betti supports `{3:1}` for `K,D0`, `{2:1}` for `L2`, and none for `L0,D2`. It checks all eight dihedral automorphisms and the signed fixed-face Lefschetz traces, with character values `r:-1`, `s:+1`; it checks multiplicativity for every ordered pair of group elements and finds zero invariant dimension.

The integral homotopy proof uses the complete acyclic Morse matching, not the mod-two Betti calculation alone. The homology character follows from integral homology rank one and exact signed trace. The finite certificate concerns the specified graph only, and this verification is not an external scientific audit.
