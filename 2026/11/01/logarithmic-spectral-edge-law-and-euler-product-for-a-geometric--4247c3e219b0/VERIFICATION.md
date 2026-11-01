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

# Verification and scope

The analytic proof supplies every infinite-dimensional claim. Its crucial checkable identities are the explicit bidiagonal coefficients, the diagonal of \(I-A^*A\), the rational trace series, and the Fredholm determinant product. The rescaled operator's isolated zero mode and rank-one eigenvalue bounds prove the logarithmic counting law. These are reconstructed in `RESULT.md` with the actual formulas and hypotheses.

`CHECK.py` uses only Python's standard library to check finite rational Jacobi coefficients, Haar weights, trace truncations and the factorization of finite determinant products for \(q\in\{5,6,8,11\}\). It is a supplementary consistency check; finite degree, floating point tests, timeouts and program completion do not certify the full spectral theorem. No independent audit was performed.
