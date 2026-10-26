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

# Reproducibility

Run `python3 verify.py` with a Python 3 standard-library interpreter. The script checks the exact rational squares and cubic-bound inequalities of an explicit radical witness, numerical location of the unique cutoff under high-precision bisection, 79 interior cycle parameters from both prescribed initial-step branches at 80-digit precision, and the asserted collapsed two-step map near interior cycles. The actual run printed `VERIFY_OK` and an operation count.

The infinite-parameter and finite-time-neighborhood claims are established by the mathematical proof, not by these finite checks. The original recurrence assumes exact division of nonzero consecutive differences; finite precision is outside this verification. Independent audit: not performed.
