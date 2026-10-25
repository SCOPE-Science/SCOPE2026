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

Run `python3 verify.py` with Python 3. The checker independently builds predecessor-projection functions for every idempotent on each chain of size 1 through 10 and tests all ordered pairs by direct composition, without using the transfer matrices in the commutation test. It independently tests the exclusive-fixed-point gap condition and evaluates the two transfer matrices on every fixed set. It also verifies the recurrence for aggregate counts.

Expected final line: `ALL_CATALAN_IDEMPOTENT_COMMUTATION_TESTS_PASSED 349525`. The verification scope is finite: mathematical claims for all positive integers rely on the proof in RESULT.md, not on this enumeration. No independent external audit has been performed.
