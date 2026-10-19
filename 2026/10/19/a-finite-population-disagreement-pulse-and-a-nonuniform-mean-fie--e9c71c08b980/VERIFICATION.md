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

# Reproducibility

Run `python3 verify.py` with Python 3 and no nonstandard packages. The script explicitly enumerates every ordered listener–persuader pair and both Bernoulli outcomes in small heterogeneous rational population states. It separately evaluates the predicted generator identities, matrix determinant and eigenvalues, unique maximum, and large-population logarithmic and population-scale limits.

The packaged standalone program reports 240 successful exact/numerical assertions. Exact rational generator checks validate the closed ODE coefficients; floating-point tests only corroborate quantitative constants and asymptotic approximations. They do not prove claims about arbitrary sizes, long times or limiting distributions. Those are established by the analytical derivation in RESULT.md. No independent mathematical audit has been conducted.
