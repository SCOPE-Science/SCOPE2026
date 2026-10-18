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
# Verification record

Executed `python tree_crosspolytope_verify.py` on the standalone package file. It returned `VERIFY_OK trees= 13 independent_exact_facet_checks= 360 Brownian_constant= 0.3781319650`. The 360 instances are signed facets from 13 tree presentations of orders 3 to 7. The checker builds the actual simplex vertex Gram matrices, evaluates integer determinants without using the theoretical area identity, calculates pairwise graph distances, and compares the resulting average with the Wiener index. Separate direct checks cover four-vertex star and path Wiener indices. Deterministic Simpson quadrature corroborates only the approximate decimal of the Brownian constant.

For all tree orders, the theorem relies on the algebraic facet-pyramid argument, Rademacher moment expansion, Donsker convergence, uniform integrability and the centered Brownian covariance spectral decomposition. The finite checker neither proves the infinite-order limit nor certifies bibliographic uniqueness. No independent mathematical audit has been carried out.
