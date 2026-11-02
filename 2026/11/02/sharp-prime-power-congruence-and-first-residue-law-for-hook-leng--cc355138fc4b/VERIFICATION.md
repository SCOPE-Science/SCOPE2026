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

# Reproducibility and limits

The exact integer-arithmetic test is `verify.py`, runnable with `python3 verify.py` without external dependencies. The program constructs \(E(q)^e\) from its logarithmic-derivative recurrence, constructs \(C_t(q)\) independently via an inverse Euler product, and checks that each coefficient of \(F_{p^{2a}}-C_{p^a}\) is divisible by \(p^{a+1}\).

For every tested prime/exponent pair it locates the first coefficient failing divisibility by \(p^{a+2}\), confirms that the first index is \(p^{a-1}\), and compares the full normalized difference modulo \(p\) with the inverse-divisor sum for odd primes or with the two square-theta terms in characteristic two. The expected residue series is constructed directly from its divisor or square definition, not from a precomputed discrepancy table.

Observed output:

`VERIFY_OK cases=12 full_coefficient_checks=1392 dyadic_cases=4`

The tests cover \(p=2,3,5,7,11\) with indicated small exponents and degree bounds between \(100\) and \(120\). They are finite corroboration; only the written binomial and formal-product argument proves the infinite theorem. No independent proof audit has been performed.
