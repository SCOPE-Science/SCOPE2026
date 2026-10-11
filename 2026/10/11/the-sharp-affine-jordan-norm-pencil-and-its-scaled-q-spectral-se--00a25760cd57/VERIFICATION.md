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

# Reproduction and proof limits

Run `python verify_jordan_pencil.py` with Python 3, SymPy and NumPy available. The code checks the symbolic sine-sum reduction \(S_0-S_1-(n+1)|x_1|^2=0\), the exact ground-state factorization in dimensions \(2\) through \(9\), the characteristic polynomials in dimensions \(2,3\), and first-order singular-vector stationarity plus sampled global comparisons in the same finite dimensions.

Observed outputs on the bundled file:

```
JORDAN_PENCIL_EXACT_GRAM_AND_TRIG_IDENTITY_OK
JORDAN_PENCIL_NUMERIC_SINGULAR_STATIONARITY_OK
```

The trigonometric reduction is symbolic in the parameters \(n,z\), but the finite-size matrix checks are **not** an exhaustive proof across all \(n\). The all-dimensional norm minimizer, the strict complex uniqueness and the spectral-set equivalence are proved by the analytic steps in RESULT.md. No independent audit is claimed. The exact singular-value prescription does not yield an asserted elementary radical expression in arbitrary dimension.
