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

The file `checks/verify.py` is the included exact-symbolic checker. With Python and SymPy installed, run `python checks/verify.py`; its successful terminating output is `VERIFY_OK: characteristic polynomial, discriminants, EP3 Jordan chain, two EP2 roots, K_mn bright blocks and star-center EP2`.

The checker verifies polynomial and matrix identities exactly in symbolic arithmetic, and tests selected finite parameter cases. The universal spectral conclusions additionally use the discriminant sign theorem for real cubics, elementary recurrence uniqueness of tridiagonal eigenvectors, and orthogonal invariant-block decomposition, all proved in `RESULT.md`. The finite loops are not offered as proofs for all graph sizes or real couplings. Independently performed auditing or validation is absent.
