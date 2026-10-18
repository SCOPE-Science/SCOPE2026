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

# Reproduction and verification

Run `python3 CHECKER.py` with Python 3.10 or later and no external dependencies. The package's checker performed 653 scalar assertions successfully. Checks include independent Simpson integration of the stationary density and squared displacement on a centered interval, normalization, the wall-reaction probability-flux identity, direct differentiation of the variance factor, a bounded numerical search for extrema, and convergence toward the stated critical asymptotics.

The full proof is in RESULT.md. Finite grids do not establish global uniqueness or the asymptotic theorem; those conclusions rely on the analytic comparison, positive variance factor and exact stationarity equation. The results are conditional on the precise two-state drift–diffusion and boundary-local-time conversion convention. No independent audit or external mathematical certification has been performed.
