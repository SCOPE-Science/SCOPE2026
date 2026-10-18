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

Run `python3 verify.py` to reproduce the exact integer-bitmask checks. The program uses no nonstandard dependencies. Its successful output begins with `VERIFY_OK`; the seeded tests are deterministic.

The program checks every one-agent Kripke relation and Boolean valuation on one through three worlds, every two-agent relation and valuation on one through two worlds, 80,000 random additional cases, all depth-zero idempotence cases on up to three worlds, and the exact `n`-round directed-path witnesses for `n=1,...,29`. Every tested iteration is compared with the `n` upper bound and with the predicted sink-pruning recurrence whenever the latter's condition holds.

These finite computations do not prove an all-size or infinite-carrier statement. The abstract upper bound follows from the strictly descending subsets of a finite world set, and sharpness follows from the explicit directed-path argument in RESULT.md. No independent audit has been performed.
