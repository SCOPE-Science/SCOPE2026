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

The analytical proof appears in `RESULT.md`. Numerical checks are supplemental and do not prove the stated all-parameter, infinite-domain or limiting assertions.

Run `python check.py` in a Python environment after installing the packages named in `requirements.txt`. This executes 1,708 assertions: exact two-dimensional Laplace transform specializations to known marginals, positivity/monotonicity over varied parameters, numerical differentiation of first and mixed moments, independent sparse finite-difference discretizations of the nonlocal backward equation with the absorption condition, exact mean-normalized discrepancy, large-reset limiting Laplace profiles, and dimensional normalization. The tested finite-difference grid has an explicitly truncated upper boundary; errors were compared against analytical values with stated numeric tolerances.

The derivation of the transform uses continuous-time Feynman–Kac and exact interface matching, and the proof of strict covariance positivity uses a series with positive coefficients for every admissible parameter. Convergence to a common exponential uses continuity of bivariate Laplace transforms. No independent audit or external scientific validation has been performed.
