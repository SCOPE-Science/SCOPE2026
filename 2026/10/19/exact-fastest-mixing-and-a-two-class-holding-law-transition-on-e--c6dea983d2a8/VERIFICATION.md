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

# Verification procedure

Run `python verify.py` after installing `requirements.txt`. It independently solves the cyclic Fourier minmax LP for each even size from 8 to 120 and checks all explicit formulas and full matrix eigenvalues. The exact global lower bound rests on the positive three-contact dual identity in RESULT.md; these finite floating-point checks are not a proof for all orders. The three relevant spectral-contact modes are the first, antipodal and nearest-negative-quadrature frequencies.
