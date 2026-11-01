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

Execute `python checks.py` after installing the required packages from `requirements.txt`. In the saved package this produced `PASS: 47 quadrature, symmetry, and crossover consistency checks`.

The verifier uses the exact Gaussian reset-age variance and numerical quadrature independently of the universal-profile quadrature. It compares positive finite-variance reset densities at several dimensionless points and parameters, checks profile evenness, and checks asymptotic coefficients for small and large arguments. The tests do not prove convergence or infinite asymptotic claims: those are established in RESULT.md by dominated convergence and analytical special-function integration. Standard adaptive numerical quadrature introduces floating-point error; the tolerances in the script are finite-diagnostic tolerances, not theorem constants.

No independent audit or external validation has been conducted.
