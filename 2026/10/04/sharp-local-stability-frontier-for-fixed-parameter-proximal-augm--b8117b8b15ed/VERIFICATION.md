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

The proof was checked from the exact fixed-parameter proximal augmented-Lagrangian subproblem and multiplier update. In the inactive-box neighborhood, the update is exactly linear, so the stability calculation has no linearization remainder.

`artifacts/verify_palm_scalar.py` uses Python standard-library rational arithmetic. It checks the trace and determinant of the state matrix, all three Jury-Schur numerators, the rate-optimal double-root identity, a parameter choice with globally strongly convex primal subproblems but unstable coupled dynamics, and exact small-amplitude two-cycles at both stability boundaries.

The finite replay does not replace the all-parameter proof. Multidimensional coupled KKT modes, adaptive parameters, inexact primal solves, and inequality constraints are outside the final claim.
