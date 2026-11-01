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

# Reproducibility

Run `python3 check_lucas_frame.py`. The checker uses only the Python standard library and enumerates no invalid cyclic strings. It compares exact Fraction-valued two-coordinate moments from independent enumeration with Lucas/Fibonacci counting formulas for lengths 5 through 16, compares all discrete Fourier eigenvalues for lengths 5 through 50, tests the exact sparse-plus-rank-one precision identity for lengths 5 through 18, and checks sharp mode order and parity asymptotic trends on finite examples. Observed output:

```
PASS: exact independent-set moment comparisons 138
PASS: direct DFT versus closed spectra 1265
PASS: inverse-covariance precision identity entries 2079
PASS: finite-mode eigenvalue extremum comparisons 90
PASS: rational uniform-bound inequalities and parity asymptotic tests
```

These finite checks are not a proof of the universal inequalities. The proof is the transfer-matrix, Fourier and strict rational/trigonometric argument in RESULT.md. No independent mathematical audit has been performed.
