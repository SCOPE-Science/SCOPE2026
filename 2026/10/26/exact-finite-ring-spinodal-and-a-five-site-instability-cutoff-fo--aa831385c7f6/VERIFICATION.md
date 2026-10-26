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

# Verification and boundaries

The reproducible program `verify.py` uses NumPy and SymPy and is executed as `python verify.py`. It reads no external data and uses no random state. It passed 318 deterministic assertion groups on the final code before packaging.

Symbolic checks establish equality between two expressions for the Fourier determinant, its quadratic activity-boundary polynomial, and the maximized quadratic density factor. Numerical checks independently differentiate the original nonlinear spatial mean-field flow to obtain full finite Jacobians for rings of lengths 3 through 11, match all their eigenvalues to Bloch-block predictions, and check the sign-based stability classification for 108 parameter sets. Additional checks straddle the exact transition at five longer-ring sizes and three translational-diffusion settings, verify unconditional small-ring stability, and test the density optimum and the predicted inverse-square finite-size shift.

The infinite parameter and ring-length claims are proved by the explicit determinant/trace algebra in `RESULT.md`, not by these finite tests. The spatial Jacobian uses centered finite differences only for an independent check. Boundary cases such as the conserved uniform mode and the nonconserved neutral pair at criticality are treated in the proof. No analysis of nonlinear bifurcation type or actual finite-particle stochastic transition is claimed.
