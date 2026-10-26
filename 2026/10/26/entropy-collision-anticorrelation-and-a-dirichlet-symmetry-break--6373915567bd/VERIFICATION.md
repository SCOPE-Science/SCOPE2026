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

Run `python verify.py` in a Python environment with `mpmath`. The program compares the closed covariance with a separately evaluated unsimplified array of Dirichlet mixed moments and their logarithmic derivatives; for two shapes, numerical beta integrations supply an additional check. For several dimensions it compares symmetric second differences against the analytic tangent quadratic coefficient on both sides of the critical shape. At the time of scientific review the standalone script printed `PASS 20 raw-moment / quadrature / local-curvature checks`.

The finite numerical cases are not a proof of universal negativity or uniqueness. The exact covariance formula, pairwise monotonicity inequality, analytic tangent expansion and trigamma integral comparison in `RESULT.md` provide the all-parameter argument. Numerical beta integration with integrable endpoint singularities has finite quadrature error; the script uses a corresponding finite absolute tolerance. No external validation, independent mathematical audit or verification of exhaustive historical priority was conducted.
