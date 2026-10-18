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

The supplied `verify.py` enumerates every increasing-tree parent array for orders 2 through 9 and checks all displayed finite leaf probabilities, conditional expectations, per-label covariances, and the aggregate covariance using exact rational arithmetic. It also checks the harmonic aggregate and discrete concavity identity for orders 2 through 60. Reproduce with `python3 verify.py` (standard library only).

The general formulas and limiting peak are proven analytically in `RESULT.md`; exhaustive finite experiments alone cannot establish those infinite statements. Full historical-priority verification and any independent audit remain outstanding.
