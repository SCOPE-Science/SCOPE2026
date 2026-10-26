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
# Reproducibility checks

The complete proof uses the absolutely convergent Bessel rank-one series, a unique minimum index tuple in exterior powers, and the monic shifted Jacobi polynomial norm. The identities are valid for every fixed index and every radial order strictly greater than negative one half.

Run `python check.py` with Python 3 and `mpmath`. A 7-dimensional orthogonal-polynomial Galerkin matrix and 13 Bessel-series terms numerically check twelve ratios with bandwidths 0.2 and 0.4, radial orders 0 and 0.5, and indices 0–2. The code also tests the Jacobi squared-norm formula at high precision.

The finite computation is corroboration only and cannot establish the infinite-dimensional spectral asymptotic. No external independent audit or validation has been performed. The precise comparison against the full 1964 historical article remains unavailable.
