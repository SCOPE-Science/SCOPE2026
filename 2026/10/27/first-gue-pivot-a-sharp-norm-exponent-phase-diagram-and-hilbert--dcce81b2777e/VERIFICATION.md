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

# Reproducibility and boundaries

Run `python verify_pivot_phase.py` after installing the versions in `requirements.txt`. The script executes deterministic Gaussian angular integrals, half-normal first-pivot integrals, finite exact endpoint comparisons, numerical Gaussian-tail coefficients, and the fixed-exponent and logarithmic-window asymptotic predictions. All assertions use explicit finite tolerances and print their tested values. No randomized seed or external network service is required.

The infinite-dimensional and large-matrix asymptotic conclusions are proved in `RESULT.md` by Gaussian polar reduction, Laplace's method, and concentration of an extreme-value integral; finite quadrature serves as an independent arithmetic consistency check. Large-size numerical convergence becomes slow when \(p\) is very close to 2, so the script uses representative exponents away from the singular point for fixed-\(p\) checks and small nonzero window parameters for the critical-scale checks. The exactness of the analytical constants is not inferred from quadrature.

The established formulas concern only the first pivot and are conditional on the specified entry normalization and real-imaginary coordinate convention. Scientific novelty beyond the examined records and independent validation remain open to external assessment.
