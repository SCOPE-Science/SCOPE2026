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

# Reproducibility and boundaries

The result is proved analytically in `RESULT.md`. To reproduce finite checks, run:

```bash
python wheel_opt_verify.py
```

The script uses Python 3, NumPy, SciPy and SymPy and terminates with `ALL_CHECKS_PASS` if its assertions hold. It constructs every edge independently and tests symmetric design predictions against actual eigenvalues, cost constraints, randomly generated asymmetric feasible assignments, and numerical constrained optimizers. Counts are six exact symbolic assertions, 144 direct spectral comparisons, 144 closed Fourier-sum comparisons, 144 first-order and budget comparisons, 2,160 asymmetric allocations, 12 numerical optimizer runs and five near-critical large-wheel comparisons. Numerical constrained optimization is a corroboration only, not a completeness certificate; proof of global uniqueness and all-parameter optimality depends on strict convexity and the spectral reduction.

The source comparison includes complete relevant sections of Ghosh–Boyd–Saberi (2008) and bibliographic-only access to Li–Yang–Zhang (2008). The latter creates a residual originality uncertainty; no claim of exhaustive literature coverage or independent validation is made.
