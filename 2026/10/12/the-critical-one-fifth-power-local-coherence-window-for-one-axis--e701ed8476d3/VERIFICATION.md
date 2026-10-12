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

Compute the covariance matrix analytically using the one-site and two-site expectations in RESULT.md, and use its determinant to avoid subtractive cancellation in the small eigenvalue. `verify.py` uses `mpmath` for high-precision evaluations at increasing spin counts and `sympy` for the decisive sixth-order coefficient. `check_small_n.py` independently constructs finite-dimensional density matrices and compares all relevant moments using `numpy`.

Run `python verify.py` and `python check_small_n.py` after installing those libraries. The analytic argument proves the limit for all integers \(n\to\infty\), for fixed positive \(a,c\); finite evaluations establish neither full asymptotic uniformity beyond stated compact sets nor originality. The squeezing criterion is the mean-spin-normalized Wineland definition. The residual question of global time optimality is left open.
