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

Analytical checks: evaluate the dimensionless killed first-passage transform, independently derive the marked-Poisson survival identity, verify the upper-endpoint Laplace coefficient and its quadratic cancellation, and apply the exact conditional successful-flight delay inequality. These steps verify distributional limits under the stated fixed-parameter scaling only.

Numerical checks: `python verify_recruitment.py` passed 92 deterministic comparisons, including Brownian Laplace moments, integrated arrival hazards, Gumbel centering for three subcritical values, and finite-delay inequalities. Runtime dependencies are Python 3, NumPy and SciPy. Finite quadrature and finite parameter tests are not proofs of infinite asymptotics.

No independent audit or independent validation has been performed. Full-text coverage by some closely related 2026 literature was not established.
