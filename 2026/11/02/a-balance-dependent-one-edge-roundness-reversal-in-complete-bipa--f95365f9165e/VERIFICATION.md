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

# Reproducible scientific checks

Run `python verify_one_edge_biclique.py` in a directory containing `requirements.txt` and the verification program, after installing the package versions indicated in the requirements file.

The completed test run printed:

```text
EXACT_FORM_AND_DETERMINANT_IDENTITIES_OK 2376
FULL_MATRIX_CRITICAL_SPECTRA_OK 375
EXACT_UNBALANCED_REVERSAL_CERTIFICATE_OK K_2,8
FOUR_AND_FIVE_POINT_ENDPOINTS_OK
BALANCED_STRICT_IMPROVEMENT_OK
BALANCED_INVERSE_CUBIC_SENSITIVITY_OK 1.90713910690579
FIXED_SMALL_PART_CROSSOVER_ASYMPTOTIC_OK
ALL_ONE_EDGE_BICLIQUE_NEGATIVE_TYPE_CHECKS_OK
```

Exact rational checks compare the block decomposition and determinant against the full powered-distance quadratic form. The sign reversal on the \(K_{2,8}\) deletion-limit metric has an exact integer inequality certificate. Numerical centered-matrix spectra corroborate the all-parameter proof, while multiprecision calculations test but do not prove the asymptotic constants. The universal claim requires the analytical Schur complement, strictness inheritance, and Taylor arguments in `RESULT.md`. Independent scientific audit has not been performed.
