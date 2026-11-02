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

# Reproducibility and scope of checks

Run `python verify.py` with Python 3.10 or later, SymPy, NumPy and SciPy. The script directly differentiates the Lyapunov function, checks the strict positive determinant of its quadratic form, checks both critical Hopf eigenvectors and their normalization, evaluates the exact linear crossing and cubic coefficients, and checks the cancellation of the first frequency shift. It also integrates four illustrative parameter choices; two above the critical boundary match the predicted small-cycle amplitude and period, and two below approach the appropriate attracting equilibrium. The program completed with its PASS message.

**Limits:** The numerical trajectories are finite approximations; they establish neither all-initial-data convergence nor infinite-lattice existence. Those depend on the stated coercivity, LaSalle invariance, stable-manifold and nondegenerate Hopf arguments. The strict period floor is established analytically through Wirtinger's inequality and equality-case exclusion. No independent mathematical audit has taken place.
