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

# Reproducibility and limits

Run `python3 diagonal_segre_char2_checker.py` in the directory containing this file. The checker uses only the Python standard library and exact field operations. Successful output is:

`VERIFY_OK: polynomial Jacobian, A^2=I and Frobenius dual; 85 ambient F4 points, 45 cubic points, 27 lines, 15 F2 planes (15 partition specializations), 6 Frobenius pairs`

The checker establishes by exhaustive explicit finite arithmetic the \(\mathbb F_4\)-rational line count, Frobenius orbits, and distinct pairing specializations. It also verifies the characteristic-two Jacobian polynomials and linear change of variables symbolically. It **does not** independently prove the classical 27-line theorem over an algebraic closure, the normal-sheaf syzygy theorem, or the flatness implication: those are mathematical arguments in RESULT.md. No independent audit or external certification has been performed.
