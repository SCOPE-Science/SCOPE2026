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

The direct numerical Gram construction and independent formula comparison passed 65 dimension/degree tests, with maximum absolute eigenvalue error 4.546e-14. Exact SymPy simplifications verified the stated degree-five and degree-six determinant identities for symbolic dimension. To reproduce, execute `python checks/check_bn.py` with Python, NumPy and SymPy installed. The tested range is finite; completeness in all dimensions and degrees follows from the character-block proof. Independent validation has not been performed.
