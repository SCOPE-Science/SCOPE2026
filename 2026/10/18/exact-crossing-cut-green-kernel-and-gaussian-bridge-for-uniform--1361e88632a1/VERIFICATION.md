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

Reproduction uses `python verify.py` with only Python 3 standard-library modules. The verifier exhaustively visits all uniform perfect matchings on 4, 6, 8, 10, and 12 labeled endpoints and checks 450 exact-rational identities involving means, covariance entries, inverse-covariance coefficients, determinant, and one-step transition probabilities. These computational checks are finite and are not used as a proof of the functional central limit theorem.

The unrestricted finite-dimensional covariance is derived by exact counting of specified matching edges. The inverse is obtained from centered martingale innovations; the continuous Gaussian limit uses predictable quadratic variation, a bounded-jump martingale functional CLT, and endpoint reversal/tightness. These latter arguments are analytic and not computationally certified here.
