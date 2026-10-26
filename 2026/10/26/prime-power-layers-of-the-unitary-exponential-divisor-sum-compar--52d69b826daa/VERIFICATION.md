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

The independent audit has not been performed.

The exact finite verifier is `verify.py`. It recomputes prime lists by the sieve of Eratosthenes, directly compares the two multiplicative divisor sums at all tested prime pairs, checks the integer cutoff, recomputes the prime-counting expression, and checks the rational constants for exponents \(2\) through \(6\). Running `python verify.py` produced:

`VERIFY_OK exponents=2..6 X=10000,100000,1000000 counts_at_1000000={2: 861, 3: 261, 4: 63, 5: 124, 6: 28}`

The infinite asymptotic relies on the prime number theorem, partial summation, and proved tail bounds, not on extrapolating numerical evidence. The scope is fixed \(a\ge2\), and no claim is made about the full natural density of the divisor-sum comparison or the infinitude of equality cases.
