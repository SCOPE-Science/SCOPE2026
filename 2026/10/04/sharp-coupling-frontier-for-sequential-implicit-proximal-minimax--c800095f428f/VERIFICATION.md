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

The proof reconstructs the exact two-block iteration matrix from the sequential implicit solves. Stability uses the necessary-and-sufficient Jury conditions for a real quadratic characteristic polynomial. Rate optimality uses the discriminant split and an analytic derivative argument on the dominant negative root.

`artifacts/verify_sequential_implicit_bilinear.py` checks the reconstructed matrix, trace, determinant, Jury expressions, finite boundary multiplier, discriminant collision, optimal factor, representative monotonicity around the optimum, and the simultaneous full-resolvent comparison.

The finite replay is a consistency check rather than a proof of the all-parameter statement. Unequal curvatures, unequal block steps, stochastic sampling, constraints, and inexact subproblem solves are outside scope.
