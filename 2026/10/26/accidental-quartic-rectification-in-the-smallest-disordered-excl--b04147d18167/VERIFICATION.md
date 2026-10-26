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

# Verification and limits

Run `python verification.py` with a standard SymPy installation. The reproducibility program builds a continuous-time generator directly from allowed site hops, solves stationary six-state systems with rational arithmetic in twelve parameter/bias cases, independently derives the two-opposite-state reduction, and verifies symbolic identities for the full current and response coefficients. It also reconstructs the exact three-site one- and two-particle formulas and their reversal parity.

The mathematically essential verification is the transition table, stationary elimination, and exact positivity estimate in `RESULT.md`. Symbolic computation cross-checks those derivations; deterministic checks do not replace the stationary generator proof. No Monte Carlo approximation is used in an infinite or all-bias claim. The independent audit channel has not been exercised and no independence is asserted.
