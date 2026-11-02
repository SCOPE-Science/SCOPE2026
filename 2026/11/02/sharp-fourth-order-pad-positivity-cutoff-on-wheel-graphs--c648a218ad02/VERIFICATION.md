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

The companion `verify.py` recomputes the four finite-wheel rational identities over exact rational functions, verifies a finite collection of wheel pseudoinverse identities, checks the sign-variation/root bracket for the first failing wheel, and checks asymptotic negativity numerically on several larger wheels.

The infinite-family part is proved in RESULT.md using an explicit inverse-circulant Green kernel and a dimension-uniform strict inequality. Finite checks and test logs do not independently certify that infinite argument. SymPy is the only nonstandard software dependency; run `python verify.py` alongside this document.
