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

Run `python checker.py` in an environment with NumPy and SciPy. The executable constructs the anchored polytope from every original complete-bipartite edge inequality rather than importing any proposed closed-form vertex description. Eight direct convex-hull computations were compared with the beta-integral volume and correct Gram-Jacobian conversion; eight independent exact integer-lattice leading Ehrhart coefficients matched the analytic volume; four independent rejection-sampling diagnostics matched the Dirichlet marginal means and beta cumulative distributions. All checks finished with `VERIFY_OK geometry_hull_cases= 8 ehrhart_enumerations= 8 independent_sampling_cases= 4`.

The analytic proof in `RESULT.md` is required for all-dimensional correctness and the weak convergence: no finite simulation, lattice enumeration, or numerical comparison alone proves it. The functions use pseudorandom rejection sampling solely as finite diagnostics. No independent mathematical review has occurred.
