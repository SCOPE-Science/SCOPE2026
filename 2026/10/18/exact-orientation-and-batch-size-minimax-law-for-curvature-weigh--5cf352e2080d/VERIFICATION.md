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

The mathematical proof uses exact centered finite differences, rank-one metric projectors, binomial second moments of an independent batch, spectral diagonalization in the Hessian metric, and a sharp convex quadratic lower bound for the one-step minimax objective. The all-horizon identity holds specifically at the uniquely optimal orientation, by conditional expectation with fresh independent batches.

`REPRODUCE.py` independently evaluates finite differences, enumerates all binomial batch outcomes for a bounded set of batch sizes, compares direct and predicted conditional energy matrices, tests eigenvalue identities, and checks optimality examples. Its execution completed 5,719 checks. The program and its test ranges are included intact, without a hidden dependency. These finite calculations are cross-checks only; the stated continuum of angles, positive steps, and unbounded batch sizes relies on the written proof.

The comparisons with published literature are limited by indexing and full-text access. The work is not independently audited or certified. The scope excludes general nonlinear and noisy objectives, the curvature exponent chosen for the cited paper's main experiments, and sample-path or high-probability claims.
