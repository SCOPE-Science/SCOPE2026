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

# Computational verification and limits

Run `python kernel_quadrature.py` for fixed-reset-rate covariance evaluated by independently integrated Gaussian/outer-Laplace quadrature and compared with the closed kernel. Run `python verification.py` for seven direct Mellin quadratures and high-time finite truncated-rate checks. The actual scripts form part of this package and require Python, NumPy and SciPy. The analytic proof in RESULT.md—not the numerical output—supports the all-positive-rate and asymptotic quantifiers. The numeric tests do not independently establish publication priority.
