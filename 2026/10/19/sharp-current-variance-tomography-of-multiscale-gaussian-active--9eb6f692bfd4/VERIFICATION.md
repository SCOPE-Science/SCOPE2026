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

# Verification report

The analytic statements are proved in `RESULT.md`; the accompanying `verify.py` is a reproducibility supplement, not an infinite-case proof or an independent audit.

To reproduce: install Python 3 and the `mpmath` package; from the directory containing these files run `python verify.py`. The checker uses 70-digit arithmetic and reports 60 passing comparisons for mode counts 1, 2, 3, and 4, including different thermal coefficients, rates and strengths. It evaluates the Poisson crossing-rate Gaussian integral, directly integrates stationary force autocovariances as a cross-check of the Green–Kubo formula, reconstructs inequivalent positive-frequency spectral measures having the same prescribed finite current observations and same zero-lag covariance, and tests the high-frequency instability inequality.

These examples do not establish arbitrary-mode correctness or the lower bound; the respective analytic evidence is strict positive definiteness of the finite Hankel matrix and invariance of domain. For a stationary continuous positive-definite general covariance, differentiating the recovered displacement variance twice reconstructs its time covariance; exact spectral-mass perturbations and high-frequency cosine modes establish the non-identifiability and instability claims. Numerical accuracy should not be conflated with practical noisy-data stability.

Assumptions are known gas density, independent particles, stationary centered Gaussian forces, positive and distinct OU rates, known mode count for finite reconstruction, and ideal current ensemble variances. The findings do not claim applicability to interacting or correlated particles, unknown density, or adaptively selected arbitrary observables.
