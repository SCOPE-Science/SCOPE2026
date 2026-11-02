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

# Reproducibility and verification

Run `python3 check.py` with Python 3 and the standard library from the directory containing `RESULT.md` and this file. The reported output is:

`VERIFICATION_OK exact_assertions=2300 numerical_assertions=863 perfect=0.796812130020 low_detection_limit=1.138090854067 crossing=0.699847881249`

The exact-rational portion independently recomputes each of four positive two-visit observation-cell probabilities, differentiates with respect to the two statistically unknown parameters, forms the Fisher matrix and takes its nuisance Schur complement at 460 rational detector/correlation pairs. It verifies the closed-form denominator via arithmetic equality. The floating-point portion verifies the three numerical reference constants, local sign and order properties, and numerical maxima across a grid of 100 detector efficiencies. The universal proof of a unique global optimum and strict monotonicity is the analytic case analysis in `RESULT.md`, not numerical enumeration.

The numerical root values are approximations. The formulas assume stationary Markov occupancy, known detector efficiency and equal true occupancy one half, while treating that occupancy parameter as statistically unknown. There is no asymptotic result with one site and two observations, no detector misclassification, and no empirical study. An external mathematical review and historical-priority audit have not been performed.
