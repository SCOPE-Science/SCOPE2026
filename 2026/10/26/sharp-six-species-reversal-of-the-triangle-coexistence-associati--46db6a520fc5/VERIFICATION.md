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

Run `python verify.py` with a standard Python 3.9+ installation and no external packages. The program constructs adjacency matrices from the stated edge lists, checks the triangle-forming degree-preserving edge switch and exact clustering, expands determinants and Cramer's-rule numerators over all permutations, checks exact-rational principal minors, and exhaustively enumerates the \(2^{\binom n2}\) labeled simple graphs for each \(2\leq n\leq5\). Canonical relabeling checks identify the only two degree families for which triangle counts can differ. The script prints `ALL EXACT CHECKS PASSED` on success. The six-vertex threshold is proved by positivity and spectral definiteness analysis in RESULT.md; finite checks do not substitute for its continuous-parameter proof.

This package has not been independently audited. Graph classes above five vertices, nonlinear coupling perturbations, and post-bifurcation long-time behavior were not exhaustively checked or certified.
