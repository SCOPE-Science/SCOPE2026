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

# Verification

Run `python3 verify_ind2.py` with Python 3 and its standard library. The accompanying `verification_output.txt` is the actual output from executing that exact source on the two graph models.

The verifier enumerates all \(65,536\) possible vertex subsets twice per graph, once by an incremental face recurrence and again by induced-graph connectivity. It independently verifies graph parameters; derives each face dimension; constructs each element-matching pair by the fully stated vertex order; orients every Hasse cover upward exactly for matched pairs; and proves no directed cycle exists by Kahn's exhaustive topological sort. The code asserts the precise one-plus-three-dimensional critical-cell lists. Separate mod-two boundary-matrix elimination reproduces the indicated Betti numbers.

Results: rook graph — 1192 nonempty faces, 543 matched pairs, 4224 Hasse relations, one critical vertex and 105 critical three-cells; Shrikhande graph — 1336 faces, 639 matched pairs, 4960 relations, one critical vertex and 57 critical three-cells. The last line is `VERIFY_OK`. These are exhaustive finite checks for the exact models specified, and the cited discrete-Morse theorem supplies the integral homotopy conclusion. Independent external scientific audit has not been performed.
