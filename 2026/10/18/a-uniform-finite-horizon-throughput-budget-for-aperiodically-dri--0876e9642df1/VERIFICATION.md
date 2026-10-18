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

# Reproducibility and limits

Run `python verify.py` using the Python 3 standard library. The observed output was:

`VERIFY_OK: 3170 exact rational identities/nonnegative dissipations; n=1,2,3; all boundary states sampled`

The verifier independently builds equilibrium-compatible rational rate vectors for three different finite chain dimensions; at numerous rational occupancy points, including each face of the cube, it checks equality of the two sides of the instantaneous storage identity, the quadratic-energy derivative via transport fluxes, and individual nonnegative edge dissipations. It separately checks the closed entrance-edge dissipation formula over a rational grid. These are exact rational computations, not floating-point evidence. They do not prove the theorem for all controls, all initial states, or unbounded dimension.

The analytical proof establishes the required global facts: the equilibrium's existence and uniqueness from the monotone edge-flux recursion, the telescope and inventory-coboundary equalities, the strict positive-curvature lower bound, compact uniformity of its coefficient, and integration over an arbitrary horizon. The one-site constant-input trajectory gives the exact strictly positive transient excess. Aperiodic trajectories are not claimed to converge to periodic or stationary solutions. The result has not received independent validation.
