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

# Exact verification

Run `python verify.py` using SymPy. The script regenerates the five-dimensional right-hand sides from the displayed model, forms both Jacobians by symbolic differentiation, substitutes rational values, checks all five stationary equations and strict interior cutoff bounds, and checks the exact characteristic polynomials and Routh array. It prints `VERIFY_OK` only after all assertions pass.

The certified mathematical conclusion is that the frozen-rate three-dimensional endemic linearization is Hurwitz, whereas the full five-dimensional linearization has exactly two open-right-half-plane eigenvalues. This check uses symbolic arithmetic, not rounded eigenvalues or finite-time integration. It does not certify a nonlinear periodic orbit, an actual Hopf bifurcation, empirical parameters, or global trajectory behavior. Independent audit has not been performed.
