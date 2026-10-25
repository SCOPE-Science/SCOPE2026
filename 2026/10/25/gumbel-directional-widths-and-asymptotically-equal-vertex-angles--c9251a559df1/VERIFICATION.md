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

# Verification details

Analytic checks: reconstruct the exact Gaussian width representation in the intrinsic sum-zero hyperplane; calculate that incident standardized signed Gaussian increments have absolute correlation \(1/2\) and joint half-normal exceedance at most \(4e^{-2u^2/3}\); partition fixed exceedance factorial moments by intersecting-edge components; check spherical norm concentration. For the normal cones, compute the far-edge maximum probability by integrating against the uniform upper-tail variable and dominate with a matching; bound the near-edge correction using the joint Gaussian bound. The star proof uses opposite leaf extrema and the shared hub coordinate.

The executable `geometry_gumbel_checker.py` produced `geometry_gumbel_checks.json` using deterministic seeds. It recorded 508 direct vertex-support comparisons (maximum floating discrepancy zero), four size-1400 distributional simulations and an additional 130,000-direction angular diagnostic on a size-72 path. The limits are analytical; finite simulations do not prove weak convergence, uniqueness across all literature, or generalize to unbounded-degree graphs.

Self-review has passed; an independent mathematical audit has not been performed.
