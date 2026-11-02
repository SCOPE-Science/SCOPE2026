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

Run `python CHECK.py` in an environment with Python, NumPy and SciPy. The observed execution passed 106 finite numerical assertions, checking radial odds monotonicity, the unique-threshold condition, multiple shape/rate and dimension settings, the two-correction high-dimensional radius, and an independently quadrature-evaluated Bayes risk. The symmetric unit-shape limiting error was 0.31606027941427883, versus numerical finite-dimension error 0.32706969976134914 at dimension 64.

Run `python SYMBOLIC.py` with SymPy to verify exact Gaussian saddle coefficients and the stated optimal corrections; its exact symbolic assertions passed. These computations are bounded finite checks and algebraic diagnostics, not independent scientific certification or a replacement for the analytic arguments in `RESULT.md`.

The proof establishes finite-dimensional decision uniqueness and a dimension threshold through strict covariance inequalities, the high-radius limit through a one-saddle argument, the high-dimensional correction through local Laplace expansion, and the positive Bayes-error floor through conditional laws of large numbers. Uniformity when switching rates themselves vary with dimension is unproved. Independent scientific audit has not been performed.
