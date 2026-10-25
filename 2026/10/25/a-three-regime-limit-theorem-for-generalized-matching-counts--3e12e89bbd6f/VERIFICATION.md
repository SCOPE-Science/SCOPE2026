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

The standalone standard-library script `artifacts/verification.py` was run from its packaged path. It passed 65 exact finite convolution, normalization, and mean checks for sizes 0 through 12 and five rational parameter values; 36 comparisons between the explicit Poissonized moved-point mass and its defining finite mixture; and the zero probability of exactly one mismatch. The script explicitly states that these checks do not prove the asymptotic results.

Analytical verification reconstructs the three cases in `RESULT.md`: (i) independent Poisson limits in total variation for the sparse-skill endpoint, (ii) total-variation convergence through a conditional permutation kernel for the near-perfect endpoint, and (iii) a binomial CLT plus a tight residual fixed-point count for the interior regime. No external independent validation or independent audit has been performed.
