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

# Verification record

`CHECKER.py` recomputes the two phase-resolved joint age densities by direct adaptive quadrature of the Gamma survival and Brownian tail. It tests six physical/Gamma parameter regimes at three positive positions each, comparing the phase weight to the predicted shape-independent limit and the standardized duration means/variances to the unit-normal limit. The run produced 90 assertion passes. None of these finite-position checks proves an infinite-position limit; the analytical saddle and regenerative occupation derivation in `RESULT.md` establishes the theorem.

The marginal stationary tail constant is independently derived from the Gamma mixing integral and the precise cycle normalization in the proof. A direct finite-threshold truncation produces corrections, so an asymptotic statement must not be treated as exact at finite positions. No independent external audit or certification has been performed.
