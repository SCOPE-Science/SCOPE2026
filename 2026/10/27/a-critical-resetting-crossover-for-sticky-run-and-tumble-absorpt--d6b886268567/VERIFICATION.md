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

Execute `python verify.py` with Python 3 and `mpmath`. The script performs deterministic comparisons of two-state telegraph backward equations, independent resetting-renewal identities, finite-parameter Pareto-binding transforms against the critical limit for both desorption protocols, the limiting Lévy integral, tail coefficients, and protocol thresholds. In this package it reports `PASS: 158 deterministic analytical/numerical checks`.

The exact renewal identity and asymptotic proof are in `RESULT.md`. Numerical checks are finite sampling checks and do not prove infinite-time asymptotics, distributional convergence, scientific priority, or independent review. An independent audit has not been performed.
