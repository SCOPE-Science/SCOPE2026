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

# Reproducibility and proof checks

The accompanying standalone `verify.py` uses deterministic SciPy quadrature and algebraic moment identities. It compares independently normalized on/off gamma-Gaussian positional likelihoods with an exact mode-posterior identity, checks conditional excess-variance saddles and inverse-distance posterior scaling at increasing radii, and verifies gamma-sum and Beta moment factorizations for several unequal switching rates and dimensions. Execute `python verify.py` with a Python environment containing SciPy and NumPy.

The infinite-radius claims require the analytic stationary-density calculation and two-sided Laplace concentration proof in `RESULT.md`; finite quadrature assertions do not certify a limit or publication priority. Neither independent scholarly audit nor external verification has occurred.
