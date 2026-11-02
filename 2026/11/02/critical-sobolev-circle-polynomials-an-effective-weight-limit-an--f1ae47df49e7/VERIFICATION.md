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

# Verification of the explicit critical model

Run `python3 verify.py` with Python 3 standard library only. It creates the monomial Gram matrix exactly with rational entries for \(\lambda=1,c=5/13,\rho=1/5\) and \(\lambda=2,c=6/17,\rho=1/4\), solves complete finite monic orthogonality systems for every degree from 2 through 12, and checks the exact discrete coefficient recurrence and first-order approximation residual. A separate tridiagonal algorithm checks the first correction at degree 300. The run produced `FINITE_CHECKS_OK`.

The all-degree theorem is verified by the analytic argument in RESULT.md: an explicit positive diagonal surplus supplies a uniform maximum-norm inverse bound, and the exact polynomial cancellation bounds the comparison residual for all coefficient indices. Finite examples alone do not establish the theorem and are not described as doing so.

No independent audit has been performed.
