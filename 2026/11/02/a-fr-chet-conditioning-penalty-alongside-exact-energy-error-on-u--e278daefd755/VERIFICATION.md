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

# Verification

Run `python verify.py` using Python 3.10+; the analytic and exact-rational checks need only the standard library. The optional numerical spectral probe requires NumPy and SciPy, as specified in `requirements.txt`.

The executed checker reported `CHECK_OK 550 exact Galerkin systems; 150 exact Dirichlet moment identities`. It also reported reproducible numerical medians for 100 random meshes with 250 elements, compared with the theoretical limiting medians and error level. Those finite calculations corroborate normalization and identities, not an infinite-time or asymptotic theorem.

The proof is self-contained in `RESULT.md`: elementwise interpolation orthogonality, Dirichlet moments, the exponential-spacing CLT, the empirical-CDF/Poincaré lower eigenvalue estimate, the isolated-small-edge upper eigenvalue argument, and a fixed-resolution interior-collision argument for moment divergence. No independent review was performed.
