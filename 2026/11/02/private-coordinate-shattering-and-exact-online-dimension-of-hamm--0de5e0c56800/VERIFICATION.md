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

The standalone script `check_hamming_boxes.py` uses only Python standard-library modules. Run `python3 check_hamming_boxes.py` in the same directory.

The program constructs Cartesian-box concepts directly for each finite tuple of alphabet sizes. Independently, for shapes `(1,1)`, `(1,3)`, `(2,2)`, `(2,3)`, `(2,4)`, `(3,3)`, `(2,2,2)`, and `(2,2,3)` it enumerates every vertex subset, checks closure under all graph geodesics by Hamming distance, and confirms equality with the box list. It then exhaustively enumerates all candidate supports, all induced Boolean traces, and the independent private-coordinate predicate; it checks the precise VC maxima and two-factor extremal counts.

For all those shapes and additionally `(2,2,4)`, `(2,3,3)`, `(2,2,2,2)`, `(3,3,3)`, and `(2,2,2,2,2)`, it computes exact online dimension by memoized version-space recursion, without inserting the predicted dimension as a recursive shortcut. Finite cases include the five-dimensional binary cube (244 concepts). The output ends with `ALL_HAMMING_BOX_CHECKS_PASS`.

These exhaustions cover only the listed small graphs; they do not prove the all-parameter theorem. The universal assertions follow from the written proof, especially the exact two-query adversarial construction and its induction with one factor reduced. No independent audit, formal proof assistant or external certification is asserted.
