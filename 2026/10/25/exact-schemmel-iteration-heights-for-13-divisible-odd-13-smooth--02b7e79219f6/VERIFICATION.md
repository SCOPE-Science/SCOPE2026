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

# Verification record

Run `python3 verify.py` with Python 3.9 or newer and the standard library. The program independently computes the multiplicative second Schemmel totient on exact integers, not only exponent-vector recurrence, for 6480 exponent tuples with a positive exponent of 13. It also checks 52,488 more exponent-vector trajectories and nine large boundary cases. It reports `VERIFY_OK` only if every comparison agrees. The proof's buffer invariant is given in `RESULT.md`; these finite tests are not an infinite certificate. Independent audit has not been performed.
