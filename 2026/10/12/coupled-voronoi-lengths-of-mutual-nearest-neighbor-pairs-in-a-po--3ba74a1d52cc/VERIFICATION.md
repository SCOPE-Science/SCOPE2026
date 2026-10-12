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

Run `python verify.py` in the directory containing this file. The checker uses NumPy and seeds its pseudorandom generator. It samples independent inter-site gaps under point Palm sampling for three rate choices and verifies the mutual-neighbor event frequency; conditional full Voronoi means, variances, covariance, correlation and joint Laplace and diagonal-survival values; the unconditioned adjacent-cell correlation; and the point-Palm mutual-membership probability, conditional on cell-size bins, against independent numerical integration. It also checks nonnegativity, normalization, and scale-invariant functional values. It runs 1,600,000 independent triplets per rate.

The proof, not the simulation, establishes the law for every real \(\lambda>0\), \(s,t,u\ge0\), and \(v>0\). Independent external validation has not been performed. Historical priority is not independently certified, and the complete Baumstark–Last (2007) paper remained unavailable.
