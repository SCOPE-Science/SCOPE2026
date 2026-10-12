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

# Reproduction checks

Run `python3 verify.py` from this package (Python standard library only). Successful execution prints a line beginning `VERIFY_OK` and reports 52 exact rational scalar identities, 3 high-precision directed-network parameter tests and 3 reducible boundary cases.

The program checks the algebraic cancellation \(\rho r^3+(r-s)^2(r+2s)=3s(r-s)^2+\rho ar^2\) under the scalar root equation; positivity of the monotonicity derivative; strict logarithmic derivative below one; a concrete contraction bound for finite positive examples; recovery of both steady-state differential equations; and the anchor-order relation. Boundary examples include a reducible identity matrix. The finite calculations are **not** an exhaustive proof of all network sizes or all real parameters.

The proof for arbitrary finite dimensions is in `RESULT.md`, with the uniformly positive derivative, box invariance, log-sup Banach contraction, max/min principle, and Jacobian inverse positivity giving the decisive infinite-parameter steps. The result does not establish convergence of ODE trajectories, their local stability, or nonexistence of a zero-opinion equilibrium. No independent audit has been performed.
