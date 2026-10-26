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

The accompanying `verify_core_shell.py` provides a standalone reproducibility check of the two-window mass-fraction formulas and covariance limits. It requires Python 3 with SciPy, invokes `python verify_core_shell.py`, and completed 269 assertions. It integrates the actual normalized Thomas–Fermi parabola independently of the closed fraction formula, calculates stationary exponential-age integrals, compares multiple geometric parameters and rates, and verifies the rational strong-reset coefficient \(89/486\) for the illustrated geometry.

The proof of the sign reversal for every admissible geometry, positivity of the weak-reset coefficient, strict negativity of the strong-reset coefficient, and the all-rate existence of a crossing is analytical and is recorded in RESULT.md. Finite numerical checks do not certify an infinite quantifier or uniqueness of the crossover. The model is the leading-order large-particle Thomas–Fermi/GP hydrodynamic model, not an exact finite-particle many-body simulation. No independent audit has been performed.
