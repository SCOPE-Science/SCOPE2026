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
# Reproducibility checks

Run `python verify.py` with Python 3 (standard library only). The program reconstructs the stationary second/fourth moments using the five-observable triangular generator system and compares the resulting kurtosis with the factored quartic using exact rational arithmetic at 80 parameter triples. It also brackets the two confinement zero crossings for positive resetting, reconstructs the critical activity at resetting rate one, and checks numerical weak- and strong-reset fold limits. All checks passed on the supplied program.

The infinite positive-root count, uniqueness of the fold, square-root opening, and limiting statements rely on the analytical Descartes, Taylor and coercive-limit proofs in RESULT.md, not on numerical sampling. The calculated constants are numerical approximations. Independent scientific review and external priority certification have not been performed.
