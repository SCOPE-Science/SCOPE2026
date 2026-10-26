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

The theorem is proved by formal power series manipulations, polynomial gcd cancellation, and a local ramification argument. No computer calculation substitutes for the irreducibility proof.

Run `python3 CHECKER.py` alongside `CHECK_OUTPUT.txt`. The checker generates each periodic mask of specified period at most seven, obtains its gcd-reduced additive polynomial, and checks the first 2048 formal coefficients. It separately computes 65536 terms using the four-state base-four automaton and compares them against the period-three digit-mask definition.

The checks cover 254 masks and 520192 coefficient identities. They are bounded, so they do not prove the unlimited-parameter theorem. The ramification proof establishes that theorem; its prerequisites are explicitly stated in `RESULT.md`.
