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

# Reproduction

Run `python3 verify.py` using Python 3 (standard library only). Successful output ends in `NOTTINGHAM_QEVEN_CONJUGACY_OK`. Finite-field multiplication is implemented from irreducible binary polynomials for q=2,4,8,16. Each entire quotient is enumerated by its four coefficients, and every predicted conjugacy class is compared with its explicit conjugation orbit. Composition/commutation are tested exhaustively at q=2,4 and in deterministic samples at q=8,16.

# Limits

The symbolic argument in `RESULT.md` establishes the arbitrary-even-field conclusion; finite verification cannot establish infinitely many cases. This report does not constitute an independent audit or proof of historical priority.
