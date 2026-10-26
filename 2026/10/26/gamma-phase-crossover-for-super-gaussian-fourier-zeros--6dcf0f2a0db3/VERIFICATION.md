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

The theorem is proved analytically in `RESULT.md`. Run `python verification/check.py` with the pinned major dependency ranges in `verification/requirements.txt`; the saved reproducible output is `verification/check-output.txt`.

The checker independently integrates the defining Fourier transform and localizes 15 representative roots across three shape parameters, compares the uniform first- and second-order Gamma-phase approximations, verifies the integration-by-parts Weibull identity at three points, and computes the candidate crossover from the complex log-Gamma function. These tests are finite numerical corroboration only; they neither establish uniform remainder bounds nor mathematically certify novelty.

Independent mathematical audit has not been performed.
