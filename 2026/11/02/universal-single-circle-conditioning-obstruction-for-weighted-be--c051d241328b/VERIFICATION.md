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

# Reproducible finite checks and analytical verification

Run `python3 verify.py` from the extracted package. It uses only the Python standard library and returns `FINITE_CHECKS_OK 920` after checking finite-degree weighted Bergman monomial diagonals, exact-angle Fourier cancellation to floating-point tolerance, optimal-radius inequalities, nonregular weighted sampling designs and large-degree asymptotic consistency. The checks are finite numerical consistency tests; they are not an independent mathematical audit or a proof of the all-degree limit. The analytical proof is in `RESULT.md` and does not depend on numerical extrapolation. Finite eigenvalues are computed with a real-symmetric Jacobi routine applied to the complex-Hermitian Gram matrix embedding.

The only source dependencies for the mathematics are the explicitly normalized Bergman monomial norm and classical gamma-ratio asymptotics. No external programs, proprietary data or unverifiable numerical certificates are needed.
