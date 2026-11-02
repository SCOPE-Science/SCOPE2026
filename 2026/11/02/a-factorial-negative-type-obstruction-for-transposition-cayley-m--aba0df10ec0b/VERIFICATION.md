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

# Verification and reproducibility

`python check.py` is a standalone Python 3 standard-library exact rational certificate. It constructs all eleven Young-content polynomials for the partitions of six, verifies a rational interval isolating the unique critical root, bounds each competing nontrivial eigenvalue above by a strictly negative rational number throughout that interval, checks the regular-character dimensions, and checks the factorial-inequality arithmetic at the extremal cutoff (with its monotonicity inequality).

Expected assertions on a successful run:

```
TRANSPOSE_CYCLE_CONTENT_CERTIFICATE_OK; endpoint nullity 100
FACTORIAL_BOUND_RATIONAL_INEQUALITIES_OK
```

Optionally, with NumPy and SciPy installed, run `OPENBLAS_NUM_THREADS=1 python full_check.py`. This separately constructs all 720 permutations and their intrinsic cycle-count distances, computes the powered-distance matrix and its numerical spectrum, and confirms 101 near-zero eigenvalues including the constant direction. This floating-point comparison is supplementary, not a proof of the infinite-family assertion or a replacement for the rational bounds. The infinite obstruction and factorial inequality are established analytically in RESULT.md. No independent external mathematical audit has been performed.
