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

# Reproducible mathematical checks

Run the accompanying `verify.py` with Python 3; it requires only the standard library. The executable independently evaluates the two Patankar linear solves in rational arithmetic, compares the next-state value with the rational multiplier, checks conservation and strict positivity on its complete deterministic test grid, and verifies rational endpoint/derivative identities, a strict contraction bound, root isolation and the exact cubic recursion.

Every rational computation in this verifier is exact. The finite grid cannot establish a statement for all states and step sizes; those universal parts rely on the explicit denominator, derivative, endpoint and inequality identities proved in `RESULT.md`. The original schemes' coefficients follow the 2017/2022 cited formulas. There are no claims about behavior for negative or zero initial components, nonsymmetric exchange, or finite-precision implementations.

Independent audit: not performed.
