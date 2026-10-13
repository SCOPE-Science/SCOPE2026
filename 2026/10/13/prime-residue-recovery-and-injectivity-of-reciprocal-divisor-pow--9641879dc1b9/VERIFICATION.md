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
# Verification details

The complete proof is in `RESULT.md`. `VERIFY.py` reproduces finite arithmetic checks independently from exact prime factorization and integer divisor-power sums. Run `python VERIFY.py` in a standard Python 3 environment; no external data or packages are used.

Expected successful lines:
```
CHECK 2 Mersenne-exponent 20647 protected-only 6830 distinct 6830 forbidden-primes 87
CHECK 4 Mersenne-exponent 20647 protected-only 14670 distinct 14670 forbidden-primes 130
CHECK 6 Mersenne-exponent 20647 protected-only 6830 distinct 6830 forbidden-primes 87
CHECK 8 Mersenne-exponent 20647 protected-only 17318 distinct 17318 forbidden-primes 148
CHECK 12 Mersenne-exponent 20647 protected-only 14670 distinct 14670 forbidden-primes 130
BOUNDARY_OK
```

All tests use exact integers and exact reduced pairs, not floating-point equality. Finite search neither proves absence of larger counterexamples nor certifies publication novelty. The universal conclusions depend on the written multiplicative-order proof, not on the test range. Independent audit: not performed.
