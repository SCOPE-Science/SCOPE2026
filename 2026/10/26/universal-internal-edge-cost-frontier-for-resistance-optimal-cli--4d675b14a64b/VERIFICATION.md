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

# Reproducibility and evidence

Run `python3 verify.py` with Python 3 and no third-party packages. It constructs grounded graph Laplacians directly from all individual edges, uses exact rational Gaussian elimination to compute inverse matrices, sums pairwise effective resistances, and compares with the theorem's closed expression. It then evaluates the proposed weighted-cost optimizer in eight distinct regimes, including zero internal edges and exact activation equality, and checks cost use and the attained Kirchhoff index against independent full-matrix inversion. Randomized feasible perturbations use a fixed seed and serve only as additional finite evidence.

A successful run reports:

`VERIFY_OK: 8 exact grounded-matrix cases (170 pair resistances); 8 weighted-cost regimes; 256 full-matrix perturbations; bow-tie radical optimum; sharp mixed-cost threshold`

The script is a finite check and cannot certify every graph size, cost vector or exact equality involving irrational weights. The analytical proof in RESULT.md, including strict convexity, grounded inverse, stationary points and the boundary-direction condition, establishes the infinite-parametric assertion. Independent mathematical audit is not yet performed.
