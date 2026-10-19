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

The derivation of the conditional Shannon mean, tail-covariance integral, uniqueness, and limiting zero is in `RESULT.md`. `verify_entropy.py` independently evaluates the exact beta integrals with adaptive quadrature, solves sample-specific and limiting scalar roots, and simulates the Dirichlet distribution from normalized independent exponential variables. `requirements.txt` provides the numerical dependencies. Run `python verify_entropy.py` in an environment containing the specified packages. Exact seeds are fixed for simulation repeatability. The printed finite checks and their numerical tolerances are only corroboration of the analytic proof; they cannot certify statements quantified over all sample sizes or all thresholds.

An independent mathematical audit has not been performed. No claim of independent validation is made.
