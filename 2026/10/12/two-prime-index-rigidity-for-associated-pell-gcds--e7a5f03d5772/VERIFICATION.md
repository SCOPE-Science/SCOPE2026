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

# Reproducible exact-integer checks

Execute `python3 verify.py` with a recent Python 3 interpreter. The program uses only the standard library and exact integer arithmetic. It evaluates the recurrence directly for indices up to 4000, compares an independent modular fast-doubling evaluator, checks all index-gcd instances with at most two distinct prime divisors through 30000, and tests seven explicit high-index cases and the two infinite families across stated finite ranges.

The saved, actually executed output is in `verification_output.txt` and starts with `VERIFY_OK`. All equality checks raise an exception on failure. Prime support for the seven large cases is supplied explicitly; the small cases are factored by trial division. Nothing computational is claimed beyond these finite bounds. The unrestricted statements rely on the Frobenius, lifting, and finite-field order proofs in `RESULT.md`, not on enumeration or test logs.
