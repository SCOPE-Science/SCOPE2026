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

The proof is deductive: for any composite-base prime support of size at least two and any proposed period/threshold, Chinese remaindering produces two indices in the same arithmetic progression whose final nonzero digits are provably unequal. The positive and negative prime-power cases are taken from the 2012 primary article, Theorem 7 and Proposition 10. Neither experimental evidence nor a search result is used as a substitute for these universal statements.

Run `python3 verify.py` with Python 3.8 or later. The standalone standard-library code constructs exact congruence witnesses for 22 mixed-prime bases and 16 proposed periods; evaluates the actual last-nonzero digits for 75 bounded witness pairs; and compares four positive-period prime-power bases at 128 indices each. Expected output:

```text
VERIFY_OK mixed_prime_period_witnesses 352 direct_witness_evaluations 75 prime_power_positive_period_cases 512
```

These finite calculations verify code and illustrative arithmetic, not the conjecture over infinitely many bases/periods. The published prime-power theorem is not recreated or independently certified. Scientific comparison with the original preprint, a later analytic-function paper and a numerical sequence table is documented separately; unindexed prior art could affect priority. Independent mathematical audit has not been performed.
