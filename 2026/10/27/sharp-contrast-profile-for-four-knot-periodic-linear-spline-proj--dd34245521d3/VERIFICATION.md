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

## Reproducibility

Run `python3 check_periodic4.py` with Python 3 standard library. The checker reconstructs the four-node Gram matrix, obtains its inverse by rational Gauss–Jordan elimination, verifies the signed spline-integral norm against the closed formula for 221 positive rational contrasts and checks the factored bounds. It also checks inversion symmetry and six derivative comparisons. The degree-six and derivative polynomial factorizations in RESULT.md establish the claims for all positive real contrast parameters.

## Scientific limits

Computational samples are not offered as a proof of the complete infinite parameter domain. The analytic proof is contained in RESULT.md. Independence and publication have not been externally evaluated.
