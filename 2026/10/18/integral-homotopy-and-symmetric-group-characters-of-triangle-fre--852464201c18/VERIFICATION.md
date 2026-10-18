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

# Reproduction and limits
The executable `verify.py` requires Python 3 and no third-party modules. Execute `python3 verify.py` and compare its eight output lines exactly to the contents of `verification_output.txt`.

The checker constructs all \(14{,}430\) faces and all \(175\) missing triangles of the line graph, checks simplex closure, constructs \(7{,}018\) Morse pairs, and verifies directed acyclicity by topologically sorting the entire \(14{,}430\)-vertex, \(69{,}762\)-cover Hasse diagram. It checks the signed integral Morse boundary by explicitly summing gradient-path normal forms, then performs \(123\) integral unit-pivot eliminations, checking that the remaining row is zero. It separately recomputes original mod-two boundary ranks \((20,190,965,2605,3001,360)\). All \(15\) permutation cycle types are handled with signed fixed-face enumeration, and the Specht character table is independently computed by rim-hook recursion with its full orthogonality checks. The verifier's output includes a SHA-256 checksum for the signed Morse matrix.

This is an exhaustive calculation for the specified finite complex, and together with the topological cell-attachment argument in `RESULT.md` supports its integral homotopy type. It makes no claim about arbitrary numbers of labels, integral representation-lattice uniqueness, independent audit, or proof of bibliographic priority.
