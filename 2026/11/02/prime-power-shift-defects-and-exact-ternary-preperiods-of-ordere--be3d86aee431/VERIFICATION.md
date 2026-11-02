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

The standalone `verify_fubini.py` computes ordered Bell numbers by the integer binomial-block recurrence modulo each test modulus and independently evaluates the rational phase through modular inverses of \(2^p-1\). The completed execution yielded:

```
VERIFY_OK prime_power_grids= 17 modular_shift_checks= 357 sharp_valuation_tests= 37 direct_sequence_terms= 2339
TERNARY_PREPERIODS [(3, 1, 1), (3, 2, 2), (3, 3, 2), (3, 4, 4), (3, 5, 4), (3, 6, 6)]
OTHER_PREPERIODS [(5, 1, 1), (5, 2, 2), (5, 3, 3), (5, 4, 4), (7, 1, 1), (7, 2, 2), (7, 3, 3), (11, 1, 1), (11, 2, 2), (13, 1, 1), (13, 2, 2)]
```

The checked grids cover the first six powers of three, first four of five, first three of seven, and first two of eleven and thirteen. The proof applies to all odd primes, all exponents, and all indices. These finite checks do not certify universal correctness or scientific originality; the rational-function argument supplies the infinite proof.
