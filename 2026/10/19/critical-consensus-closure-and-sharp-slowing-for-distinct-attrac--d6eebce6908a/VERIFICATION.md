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

# Verification

The complete proof is in RESULT.md; no numerical run is treated as a proof of infinite-time convergence.

Execute `python CHECK.py` (Python 3, SymPy and SciPy) to inspect exact three- and four-node path Laplacians, both critical spectra, the coefficient \(\kappa=1/18\), Taylor coefficients of the scalar critical drift and its reciprocal-square flow, and a numerical trajectory. It uses no external downloads and tests algebra from its own source, not a stale external file.

The numerical trajectory check evaluates increasing times and the quantity \(q(t)^{-2}-2t/9+(2/5)\log t\). Existence of the limiting constant is proved in RESULT.md using integrable-error estimates, not inferred from plots or finite horizons.

The global theorem is conditional on symmetric nonnegative adjacency matrices, a connected attractive graph, and at least one repulsive edge. The sharp generic rate further requires a simple mean-zero kernel. Cases with multiple critical zero modes, nonsymmetric dynamics or stochastic forcing are not assessed. Independent external audit has not been performed.
