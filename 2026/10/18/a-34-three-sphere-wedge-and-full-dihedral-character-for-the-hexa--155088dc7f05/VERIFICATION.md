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

The two standalone standard-library Python checks and the full 243-pair finite matching certificate are included with this result. `verify_morse.py` independently reconstructs all 521 nonempty faces and 1800 face-cover relations, verifies complete disjoint pairing, visits the entire directed face poset in an acyclicity topological sort, and leaves one critical vertex and 34 critical 3-faces. This finite exhaustive certificate proves the integral wedge homotopy type via the discrete-Morse theorem; there is no extrapolation from limited sampling.

`verify_equivariant.py` uses a separate, three-vertex-path forbidden-support enumeration and exact binary boundary elimination, reproducing the mod-two homology ranks. It evaluates the fixed-face orientation-sign Lefschetz formula for each of 24 graph symmetries and reproduces the complete character. See the exact recorded outputs `morse_output.txt` and `equivariant_output.txt`.

The homotopy equivalence is a consequence of the certified Morse matching, not an assertion of an explicit simplicial collapse onto an embedded sphere wedge. No classification is claimed for larger antiprisms. External independent mathematical assessment remains outstanding.
