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

# Reproduction and proof boundaries

Run `python3 verify.py` from this directory using a standard Python 3 interpreter. No third-party package or network connection is needed. The program reports 2,748 exact-rational algebra checks for the stationary moment balances, conditional event regression and logarithmic derivative; 48 bounded checks of the unique maximizing root and large-lag limits; and 12 independent exact-transition Monte Carlo checks over six parameter regimes. Total on the reviewed replay: 2,808 passed checks.

The universal theorem follows from the displayed linear generator equations, state-independent Poisson event sampling, the exact exponential resolvent of the two-dimensional drift and the sign of the concave derivative polynomial. Finite samples, grid checks and asymptotic evaluations are not certificates for all positive real rates or infinitely many event lags. No independent mathematical or publication-priority audit has been performed.
