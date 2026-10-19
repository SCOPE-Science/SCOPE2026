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

# Verification and limits

The exact rational checker `verify_one_defect_cube.py` was executed from its supplied path. It reported `VERIFY_OK 489 exact arithmetic checks`. It tests the full weighted-cube Krylov matrix over two large prime fields, independently computes principal-block characteristic-polynomial gcds with rational polynomial arithmetic, and checks exceptional four-cube eigenvector relations in an exact quadratic number field. These finite checks are corroborative; the proof of the general theorem is analytic and contained in RESULT.md. The checks cover selected rational conductances, not all real values. The all-real statement follows from spectral decomposition, Jacobi eigenvector nonvanishing and determinant interlacing. No independent audit has been performed.
