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

# Reproducibility and verification

The proof is analytical and given in RESULT.md. The standalone `verify_walk.py` (Python 3, NumPy, SciPy) supplies finite-parameter corroboration: velocity normalization; exact-versus-integral characteristic transforms for several loop weights and arguments; central and remote tail prefactor approximations; small and large loop endpoint transforms; and exact finite-age coin-shift evolution with independent geometric reset. The executed verifier reported 41 passed checks. Its finite-reset evolution is truncated with explicit residual mass `(1-q)**(maxage+1)` and checked below `1e-6`; the calculation checks approximation only and does not certify the infinite-time or weak-parameter limits. Mathematical asymptotics are proved directly in RESULT.md. Independent audit has not been performed.
