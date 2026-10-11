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

Execute `python3 artifacts/verify.py` using a standard Python 3 interpreter. The actual run returned:

`VERIFY_OK: 13 exact Legendre moments, two spherical-grid tests, 29,441 split-projection checks`

Exact-rational checks cover the cosine-transform eigenvalue integral for degrees zero through twenty-four; deterministic direction samples test the product-versus-angle inequality for three axes and four tetrahedral normal lines. Direct projected-area inequalities and the asymptotic deficit normalization are also checked. These are supplementary finite sanity checks, **not** certificates of universal quantification. Infinite-dimensional integration and nonnegativity are proved analytically in the accompanying RESULT.md via the spherical harmonic projectors and the explicit uniform norm bound.

No independent audit or independent validation has been performed. The theorem's stated sharpness pertains only to weak barriers. Full publication-coverage of unindexed literature is not certified.
