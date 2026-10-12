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
# Reproducibility and limits

The analytic proof in `RESULT.md` establishes the finding. It requires no unproved numerical lemma, no infinite extrapolation from finite tests, and no unavailable auxiliary data. The conditional threshold is unique by strict monotonicity; Taylor remainders are controlled on the event \(\max_i|E_i|\le(1-r)^{-1/4}\), whose complement has exponentially small probability relative to the claimed first-order scale. The exact normal moments and strict Mills inequality then determine the coefficient and its sign.

The standalone `VERIFY.py` uses Python 3 with NumPy and SciPy and evaluates a deterministic one-dimensional integral for the bivariate Gaussian case. Execute `python VERIFY.py` in the same directory. It checks 12 level/weight/correlation combinations: four pairs and three correlations \(r=0.99,0.997,0.999\), comparing finite quotients with the closed-form derivative and requiring observed convergence. These are quadrature comparisons with floating-point error and test no dimension above two. They are corroboration, not a proof of the analytic universal statement.

The theorem is pointwise at fixed \(p\), dimension and weights. Independent validation has not been performed.
