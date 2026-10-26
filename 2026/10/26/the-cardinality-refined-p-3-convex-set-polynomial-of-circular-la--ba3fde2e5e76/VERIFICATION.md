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

# Reproduction of the exact circular-ladder polynomial

Run `python verify.py` with Python 3.10+ and SymPy; no Internet connection or input files are needed. The script constructs 16 ordered-pair states directly from the local three-neighbor rule, including all 33 locally allowable transitions, and computes the exact symbolic polynomial determinant of the transfer matrix over integer polynomials. It separately checks the determinant on the ten recurrent states and tests the product formula in RESULT.md exactly, then compares the Newton-identity generating-function coefficients with separately accumulated cyclic transfer walks through circumference twenty. For circumferences three through nine, it also enumerates all vertex subsets of each actual simple graph and tests the \(P_3\)-convex definition directly on adjacency lists, without using any transfer constraints. The output is `verify_output.txt` and must end with `VERIFY_OK`.

The determinant calculation is a finite exact certificate for the only lengthy algebraic step, not a numerical approximation. A separate paper-and-pencil check is possible from the ten-row table in RESULT.md. Neither the finite enumeration nor a successful script execution alone establishes the theorem for arbitrary circumference: the infinite quantifier is covered by the local-word bijection, formal determinant identity, and minimum-degree proof. Independent mathematical validation remains unperformed.
