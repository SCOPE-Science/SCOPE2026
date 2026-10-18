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

The accompanying `verify_oscillatory_selection.py` was run with Python 3 and SymPy and passed: symbolic reconstruction of the physical map; exact identities for the two resource-cycle points; explicit Jacobian product multipliers; a sharp mean-game mismatch inequality; and 42 nearby, forward-invariant numerical trajectory checks. The code outputs transverse and resource return multipliers `37321/40000` and `4/25`.

The proof in `RESULT.md`, rather than finite numerical sampling, establishes attraction for the infinite-time map. The critical equality case, global basin geometry, stochastic perturbations, and chaotic forcing are not verified or claimed. No independent external audit has been performed.
