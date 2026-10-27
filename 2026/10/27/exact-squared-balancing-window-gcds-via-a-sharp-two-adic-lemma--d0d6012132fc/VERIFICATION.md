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

The original integer recurrence and independent arithmetic tests are implemented in `verify.py`. Execute `python3 verify.py` with Python 3 and no external packages. Checks include 180 window lengths, three consecutive windows, Pell difference GCD identities, exact prefix valuations, and the odd-index balancing valuation lemma. Each squared window sequence satisfies an order-three integer recurrence, so a mismatch in the computed GCD would appear among its first three windows. A finite test remains corroboration, not an infinite proof; the direct algebraic and valuation proof is in `RESULT.md`.

No independent mathematical audit has been performed. Publication priority is not independently certified.
