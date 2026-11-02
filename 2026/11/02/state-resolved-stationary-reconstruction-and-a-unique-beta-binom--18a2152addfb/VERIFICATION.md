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

The formulas were reconstructed from the stationary transport-generator equations and their boundary conditions. The included `state_checker.py` independently evaluates exact rational state-resolved moment recurrences and the explicit beta–binomial stationary law, yielding 4,200 successful assertions on its tested finite grid.

Run `python3 state_checker.py` in the same directory. Exact finite arithmetic checks do not replace the all-parameter proof. The all-rate reconstruction uses the previously established stationary total marginal and does not claim a new derivation of that marginal. No independent scientific audit has been performed.
