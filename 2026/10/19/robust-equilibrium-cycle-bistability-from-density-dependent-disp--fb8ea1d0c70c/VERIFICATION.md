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

The standalone `verify_exact.py` requires only Python's standard library and runs with `python verify_exact.py`. It constructs the Beverton–Holt map and strictly positive density-dependent staying/emigration functions with rational arithmetic, verifies the synchronized equilibrium and both points of the prime two-cycle, reconstructs the one-step and two-step Jacobians, and checks the strict exact Schur inequalities.

The calculation verifies algebraic identities and local multiplier inequalities for the specified model, without treating numerical iteration as a proof of global convergence. The analytic argument in `RESULT.md` proves convergence of isolated patches and of the constant-dispersal comparison by monotone bounds; it proves open persistence under small perturbations by hyperbolic continuation. There is no claim of full basin classification or an independent audit.
