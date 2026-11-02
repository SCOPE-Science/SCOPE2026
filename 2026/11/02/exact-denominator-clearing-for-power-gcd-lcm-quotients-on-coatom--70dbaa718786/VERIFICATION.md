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

# Reproducibility and mathematical limits

Run `python3 verify.py` under Python 3.10 or later with no third-party packages. The program generates divisor lattices and all deleted-coatom subsets, computes the quotient using exact `fractions.Fraction` Gauss–Jordan elimination, extracts the exact least common multiple of all entry denominators, and compares it with the theorem's integer formula. It separately checks the Schur complement's bottom-row formula using explicit Möbius convolutions of all relevant divisors.

The observed transcript is:

```
VERIFY_OK matrix_cases= 1062 nonintegral_cases= 261 mobius_row_entries= 4512 examples= {'(6, (2, 3), 2)': 1, '(12, (2,), 1)': 3, '(12, (2,), 2)': 5, '(30, (2, 3), 1)': 5, '(30, (2, 3, 5), 1)': 11, '(60, (2,), 1)': 3, '(60, (3,), 1)': 1}
```

The script tests integer exponents 1, 2 and 3 and integers from 2 through 99 with at most 18 positive divisors. All computations use exact integers and rational fractions. The infinite result rests on the incidence-factorization and Möbius-inversion proof in `RESULT.md`, not on extrapolation from these finite tests. The closest general divisibility literature supplies qualitative criteria, not an independently verified historical uniqueness claim. Independent mathematical audit has not been performed.
