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

# Reproduction and boundaries

Run `python verify_star.py` with NumPy and SciPy available. The script constructs Hamiltonians independently of the closed form, groups repeated numerical eigenvalues into their full orthogonal projectors, computes their entrywise squares, and compares against the displayed exact formula. It also evaluates the formula using Python rational fractions and determines the exact matrix rank by rational row reduction for independently chosen integer parameters.

Expected output (floating-point error tolerance applies to the independent eigensolver):

```
VERIFY_OK exact_rank_profiles=315 independent_spectral_profiles=405 matrix_entries=17280 max_entry_error=1.221e-15
```

This is a finite test, not an exhaustive argument over every real coupling. The manuscript proves the all-parameter assertion by invariant-subspace reduction, a positive-definite Schur-square lemma on the leaf subspace for at least three spokes, and exact low-dimensional determinant calculation. The status of external audit is not performed. The source dissertation is only comparable through its accessible abstract, an explicit originality risk.
