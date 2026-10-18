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

# Verification and limits
The accompanying `verify_repunit_lengths.py` is runnable with Python 3 using only standard-library functions. It compares \(n\mid R(n)\) by the exact modular-power test \(10^n\equiv1\pmod{9n}\) against factorization and multiplicative-order reconstruction for every \(1\le n\le120000\); checks the necessary quadratic character; and checks four distinct prime-order examples with three exponent choices. The observed output was:

`SELF_DIVIDING_REPUNIT_EXACT_REGRESSION_OK range=1..120000 hits=27 primitive_examples=4`

The infinite quantifiers are proved by prime-factor arguments and classical theorems, not by this computation. No estimate of the actual asymptotic count of self-dividing lengths is claimed. Residual originality uncertainty concerns possibly unindexed or implicitly covering literature. No independent audit has been performed.
