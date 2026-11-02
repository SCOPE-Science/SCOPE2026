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

# Verification of the temporal-memory theorem

The standalone `verify.py` runs with Python 3 and `mpmath` and prints a passing assertion count. It was executed from the self-contained package as `python verify.py` and returned **PASS: 271 deterministic mathematical consistency assertions.**

Checks compare the exact killed-generator matrix for finite two-point rate distributions with the separate renewal-resolvent prediction, including integrated correlation and positive finite-time correlation at several rates, refresh parameters and lags. Gamma-law Stieltjes integrals are compared with their incomplete-gamma formula and differential identity. Numerical small-refresh tests cover both Stieltjes singularities, all five correlation-time regimes, deterministic-rate recovery, and numerical Laplace inversion probes of the incomplete-gamma and logarithmic-lag profiles.

The printed check count refers only to computational assertions in the supplied source and is reproducible with `mpmath`. Mathematical infinity, uniqueness of the stationary pullback process and convergence for arbitrary rate-density laws rely on the proof in `RESULT.md`, not on these finite numerical checks. The finite gamma-family probes do not establish the result for every law, and no independent mathematical audit is claimed.
