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

The theorem is derived from the normalized ODE and a ratio-coordinate stable-manifold calculation; the high-ratio uniform bootstrap and both area integrals are displayed in RESULT.md. `verify.py` uses only the Python standard library to reproduce the root and coefficient figures and to compare sample trajectories on opposite sides of the asymptotic divider. The numerical integration is a finite experiment, not a proof of convergence for every initial condition.

The boundary \(z_-=1\) is included in the lower-slope branch because the negative curvature places the divider below the upper edge of the square. No finite simulation certifies the uniqueness of the entire small-square basin split; that claim rests on the analytic saddle-sector, invariant-strip, and large-ratio estimates. No independent audit has been performed.
