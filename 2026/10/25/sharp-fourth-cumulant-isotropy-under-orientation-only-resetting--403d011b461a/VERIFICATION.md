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

Run `python verify.py` from a directory containing that script, with `numpy` and `scipy` available. The script implements a separate generator-derived differential system for angular Fourier-weighted displacement moments up to order four. It checks \(90\) parameter/time/direction configurations, the exact rational angular-cancellation polynomial, and the critical angular invariance numerically. This is independent of the time-covariance integral used in the analytic proof but is not a mathematical proof of identities for uncountably many parameter choices; the analytic generator proof is in `RESULT.md`.

The stationary-angular initial condition is necessary for the stated finite-time formulas. Starting at the reset angle supports their asymptotic cumulant-growth coefficients instead. No claim of independent scientific audit or external certification is made.
