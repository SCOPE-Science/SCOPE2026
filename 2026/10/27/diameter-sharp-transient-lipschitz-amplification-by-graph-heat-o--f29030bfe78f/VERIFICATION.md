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

The analytic argument uses positivity and shared mass of finite heat kernels, an independent two-Poisson-clock representation for the prescribed trees, and explicit one-Lipschitz test functions. The finite numerical cross-checks are reproducible by running `python branch_heat_check.py` with NumPy and SciPy. The code checks 64 lumped finite-dimensional cases and 12 comparisons against full graph Laplacians. These checks do not certify the infinite branching limit; its proof is the displayed Poisson-tail estimate and an exact diameter argument. The result has no independent mathematical audit.
