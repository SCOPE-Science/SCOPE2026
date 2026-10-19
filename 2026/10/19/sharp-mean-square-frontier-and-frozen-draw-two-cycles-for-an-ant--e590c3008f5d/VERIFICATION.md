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

Run `python verify.py` with NumPy and SciPy. The standalone program executes 295 numerical checks using independently evaluated two-point Gibbs weights, Gauss–Hermite integration, moment coefficients and finite-dimensional period-two calculations.

Analytical checks beyond the numerical sample are the exact exponential-weight simplification, the size-biased Gaussian negative-covariance inequality, the small-input Taylor expansion, the nonnegative-supermartingale argument, and the frozen-map scalar monotonicity and linearization. Finite checks do not certify universal quantifiers; those are addressed by the analytic proof in RESULT.md.

Independent audit: not performed. No external verification or formal certification is claimed.
