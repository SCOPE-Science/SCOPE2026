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
# Verification of the determinant-pencil Fourier criterion

The standalone `mutual_annihilation_check.py` can be executed with Python 3, without third-party packages, by running `python3 mutual_annihilation_check.py` beside this file. It uses exact finite-field arithmetic throughout.

Observed outputs from the code in this package:

```text
EXACT_FIELD_OK 2 nullity 126 rank 130 brute_frequencies 256
EXACT_FIELD_OK 3 nullity 3072 rank 3489 brute_frequencies 6561
EXACT_FIELD_OK 4 nullity 29700 rank 35836 brute_frequencies 213
EXACT_FIELD_OK 5 nullity 161280 rank 229345 brute_frequencies 0
ALL_EXACT_MUTUAL_ANNIHILATION_CHECKS_OK
```

For the prime fields of orders two and three, every actual Fourier coefficient is computed by summing the character over all mutually annihilating pairs, independently of the projective line count; these are compared to the derived formula. For the four-element field, 213 deterministic frequencies are directly evaluated with the additive character induced by the field trace. For all four field sizes, every frequency pair is enumerated for the determinant-pencil formula and its zero count is checked against the closed polynomial. The field of order five is checked through this exact formula and count, not by direct raw Fourier sums.

These tests do not certify all prime powers. The proof in `RESULT.md` provides the universal argument. The counting argument and analytic claim have not received independent mathematical validation.
