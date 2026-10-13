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

# Reproducibility and independent-check limits

The mathematical derivation in `RESULT.md` proves the finite-sample identity for all stated parameters. A separate numerical checker `check_crossing.py` performs 56 independent conditional-Gaussian quadrature comparisons, sign and threshold checks across 41 positive autocorrelations, and Monte Carlo covariance comparisons on six synthetic Gaussian AR(1) models (250,000 draws each, deterministic seed). It reports 349 passing deterministic and randomized checks.

Run `python check_crossing.py` in an environment with Python, NumPy and SciPy. Quadrature and simulation are illustrative numerical validations only, not a proof for infinitely many parameter values. No independent scientific or publication-priority audit has been performed. The historical literature comparison is subject to the access limits documented in `REVIEW.md`.
