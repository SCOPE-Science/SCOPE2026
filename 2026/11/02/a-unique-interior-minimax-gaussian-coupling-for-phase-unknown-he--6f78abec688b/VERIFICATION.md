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

# Reproducible numerical verification

Run `python verify_fourier.py` with Python 3.9 or later. Only the standard library is required. The program checks 6,611 supplementary parameter-grid dominance comparisons, exact analytic balancing and endpoint inequalities over eleven positive diffusion parameters, and 45 independently integrated bivariate normal moments via 96-point tensor Gauss–Legendre quadrature on a truncated standard-normal domain.

Observed output:

```
PASS: 6611 grid dominance checks; 45 independent bivariate Gaussian quadratures; all limits and endpoint inequalities checked
```

The infinite-dimensional phase domain is handled by the analytical covariance diagonalization in `RESULT.md`, not by a finite mesh; finite Gaussian quadrature tests do not certify infinite-parameter results. Rounding matters as the diffusion parameter becomes very large or small. No outside independent audit has been performed.
