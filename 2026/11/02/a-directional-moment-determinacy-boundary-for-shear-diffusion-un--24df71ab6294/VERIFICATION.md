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

The stationary Gaussian-mixture representation, variance polynomial and saddle-point asymptotics are proved in `RESULT.md`. A standalone numerical cross-check is provided as `check.py` and can be run using Python 3, NumPy and SciPy. It evaluates finite-parameter mixture integrals, compares their far-tail ratios with the asymptotic and checks exact low moments; 31 diagnostic checks passed.

Finite quadratures are corroboration rather than proof of infinite tail limits. The proof uses Laplace's method and a published Krein criterion; no independently conducted audit is claimed. The analysis does not address joint multivariate moment determinacy, partial resetting, or a uniform small-shear limit.
