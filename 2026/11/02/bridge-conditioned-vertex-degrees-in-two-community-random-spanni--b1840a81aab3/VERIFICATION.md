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

# Reproducibility and verification

Execute `python verify.py` with a stock Python 3.9+ installation; no external packages, data or network access are required. The actual packaged checker completed successfully: `PASS 250 exact assertions; direct Prufer enumeration, separate determinant, marginals and covariance`.

The code independently enumerates every Prüfer code at the tested orders and determines the spanning-tree degree and cross-community edge count from each decoded tree. It checks the bivariate generating polynomial coefficients, total normalizer, direct factorial-moment covariance, both binomial marginals and independent weighted-Laplacian determinants. It further tests the conditional means for one, two and the maximal possible number of cross-community edges, their opposite-sign differences for unbalanced parts, and balanced conditional flatness.

The claims for arbitrary finite \(m,n\ge2\) and arbitrary positive real conductances follow from the written algebraic Matrix–Tree proof, not from enumeration. Numerical finite experiments cannot certify novelty or historical priority. There has been no independent audit.
