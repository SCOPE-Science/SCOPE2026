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

Exact computations are reproducible with `python verify.py` and `sympy` (Python 3). The script checks all four Gröbner bases, geometric ordinary nodes, all rational lines, line/node incidence, the explicit 21-class minor, point counts over both finite fields, and the Frobenius dimension argument. The actual successful execution is preserved in `VERIFY_OUTPUT.txt`. The arithmetic Picard upper bound rests on the K3 Weil theorem and the first-Chern-class bound, not finite extrapolation. The statement does not verify integral saturation or classify geometrically non-rational lines.
