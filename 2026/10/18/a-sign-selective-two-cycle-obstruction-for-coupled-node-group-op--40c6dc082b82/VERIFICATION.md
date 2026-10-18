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

# Reproducibility and limitations

Run `python3 verify.py` using Python 3 standard library. The standalone script checks the three central algebraic constructions in exact rational arithmetic on 1,167 generated joint-degree distributions: weighted Cauchy–Schwarz, nonnegative secant coefficient, and exact shifted-Jacobian determinant at three positive real shifts each. It then constructs the attracting two-cycle for eight sigmoid steepness values greater than two and checks its local stability and 24 perturbed trajectories. The checks completed successfully.

The two-cycle exclusion, spectral exclusion, and persistence theorem are proved for the stated arbitrary parameter ranges in `RESULT.md` by explicit algebra and the implicit-function theorem, not by finite experiment. There is no independent external audit or full finite-network stochastic validation. Published-literature searches do not certify originality.
