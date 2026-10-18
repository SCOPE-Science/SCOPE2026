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

Verification uses `python3 verify.py` with only the Python standard library. The checker rebuilds the exact rational payoff specialization, compares the derived source/saddle linearizations and the cusp exponent, tests invariant box signs over independent rational sample grids, and integrates selected planar trajectories and the stable-manifold initial-value equation. Numerical trajectories and numerical quadrature are sanity checks; they do not certify infinite-time behavior, exhaustive basins, or the nonzero cusp coefficient. Those follow from the analytic invariant-manifold and comparison arguments in RESULT.md. All calculations refer to the embedded standalone checker, not outside logs. No independent review has been conducted.
