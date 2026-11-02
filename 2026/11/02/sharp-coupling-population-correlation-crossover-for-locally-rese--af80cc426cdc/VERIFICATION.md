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

# Verification evidence and limits

Run `python3 verify_correlation.py` with the accompanying program. It uses only the Python standard library and independent generator equations for the **uncentered** first and second moments; it does not assume the centered covariance closure as its input. The verified cases are 512 exact rational parameter configurations (population sizes 2, 3, 4 and 7; positive confinement, reset and diffusivity; multiple coupling strengths; both deterministic and random reset locations), ten exact-form lag/spectral regression diagnostics and nine large-population boundary-layer comparisons. All 531 checks pass with the packaged program.

The analytic proof establishes the stationary existence/uniqueness, all-parameter formulas, strict covariance positivity and the critical scaling. Numerical exponential evaluations and finite rational cases are diagnostics, not certificates for infinite-size limits, exhaustive prior-work uniqueness or publication priority.
