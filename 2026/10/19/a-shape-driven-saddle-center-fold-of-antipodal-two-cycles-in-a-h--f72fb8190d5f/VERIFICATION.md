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

# Reproduction of mathematical checks

The analytic proof is in `RESULT.md`. With Python 3 and no nonstandard dependencies, run `python verify.py` in this directory. The verifier uses exact fractions to test the transition's fourth-order Taylor coefficients and deterministic floating-point tests for orbit existence regimes, direct two-step map recurrence, potential differentiation, derivative-ratio monotonicity and small-parameter fold scaling. It reported **PASS: 687 deterministic finite checks** during preparation.

The code is deliberately a finite falsification/consistency test, not a computer proof of uniqueness of a maximum on a continuum or the asymptotic theorem. Those conclusions follow from the positive-series coefficient-ratio argument and Taylor expansion in `RESULT.md`. The numerical comparison tolerance is recorded in the script. No independent mathematical audit has yet been performed. The exact orbit count covers only centrally symmetric primitive period-two cycles.
