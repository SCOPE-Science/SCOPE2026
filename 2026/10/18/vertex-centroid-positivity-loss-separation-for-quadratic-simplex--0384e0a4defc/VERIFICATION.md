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

The standalone `check.py` verifies the moment identities for \(3\le n\le35\), the exact Dirichlet Simpson-index variance, the barycenter reproducing formula for quadratic monomials, and the exact \(n=3\) vertex absolute mass. It also checks the numerical values of the two asymptotic constants. The checker prints `VERIFY_OK exact_or_precision_checks=333`.

These tests do not establish infinite-dimensional or high-dimensional limits. The latter are proved by the exact kernels, the exponential limit of a scaled Dirichlet coordinate, a bivariate central limit theorem, and uniform integrability. There is no external validation certificate.
