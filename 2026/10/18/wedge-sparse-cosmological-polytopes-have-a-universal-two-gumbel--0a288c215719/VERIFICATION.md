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

The proof uses exact coordinate identities, a bivariate Gaussian upper-tail integral, local-dependence Poisson approximation, and spherical normalization. The standalone `verification.py` tests independent coordinate constructions, covariance signs and wedge multiplicities, and direct Euclidean support-function/width identities. It does not certify any infinite-graph limit.

The deterministic seeded run succeeded with `VERIFY_OK`: 231 constructed polytope vertices spanning seven finite graph scenarios and 840 direct width comparisons; additional diagnostic simulations used 2,400 samples each for paths and cycles at two sizes, and 1,200 samples each for two complete-graph sizes. The complete-graph finite diagnostics converge slowly and are not claimed to match the limiting moments at those sizes. The moment conclusion is proved only for a uniform maximum-degree bound. The wedge criterion is sufficient rather than necessary. Independent mathematical verification remains unperformed.
