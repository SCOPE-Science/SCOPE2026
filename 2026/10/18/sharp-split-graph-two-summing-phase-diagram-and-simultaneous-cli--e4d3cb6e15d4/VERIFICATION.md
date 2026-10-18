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

The analytical proof establishes all dimensions, nonnegative edge amplitudes, and both sides of the transition. For independent computational corroboration run `python verify_split.py` with Python, NumPy and SciPy. This constructs incidence matrices in the full vertex coordinate space; it does not use the closed-form eigenvalues as its numerical objective. A reproducible checker execution reported:

```
PASS 35 spectral-formula and orbit-optimizer comparisons
PASS 8 unrestricted simplex-weight optimizations and first-order certificates
PASS 6 heterogeneous clique-edge screening checks
PASS 9 high-imbalance asymptotic checks
ALL VERIFIED 58 configurations
```

The code is a numerical corroboration, not an infinite-range certificate. The proof's essential exact steps are (i) the finite-dimensional domination/minimax formula, (ii) the three Laplacian eigenvalues, (iii) the sharp initial derivative and interior Cauchy equality, and (iv) the concavity-supported probability-simplex optimality conditions for all extra clique edges. There is no independent external audit.
