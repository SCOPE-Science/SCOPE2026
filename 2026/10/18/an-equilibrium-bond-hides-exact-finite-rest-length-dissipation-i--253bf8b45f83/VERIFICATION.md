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

# Verification summary

The equations of motion, reversible relative-generator density, stable stationary center representation and Stratonovich heat differential are derived directly in RESULT.md. The assertion of zero bond-only entropy production is path-level, since the bond diffusion and all of its transition kernels do not involve the stiffness asymmetry. The full-system entropy-production quadratic coefficient is a positive spectral multiplier for every finite spring rest length.

The included `verify.py` was executed successfully against NumPy/SciPy. It checks three independent linear OU Lyapunov solutions against the exact zero-rest-length formula; three radial Green-function reconstructions of that same formula; and convergence/positivity of the radial coefficient at positive rest lengths 0.4, 0.8 and 1.5. Numerical truncation is not a rigorous certificate; strict positivity follows analytically from reversibility and the spectral theorem. The singular radial direction at zero has measure zero under the nondegenerate two-dimensional diffusion, with the energy chain rule justified by approximation.

No tests establish extensions beyond equal bath temperatures, equal monomer friction, a common isotropic trap, or interaction laws with an autonomous relative coordinate. No independent audit has yet been performed.
