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

The analytical proof establishes the normalized spherical normal-cone probabilities for every unweighted path of order at least five and their stated limits, plus the star comparison. The key estimates are the two-dependent Gaussian maximum Gumbel law, the variance-two endpoint density relative to the variance-six bulk, uniform dominated convergence, and local competitor suppression.

Run `OPENBLAS_NUM_THREADS=1 python verify.py` with NumPy and SciPy installed. The deterministic-seed checks reconstruct the score covariance, compare direct Gaussian simulation with conditional importance sampling at multiple dimensions, and give numerical diagnostics for the rare endpoint and star hub. Numerical tests supplement rather than establish the asymptotic theorem; no independent audit has been carried out.
