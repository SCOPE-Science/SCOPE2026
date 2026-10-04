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
The proof uses the exact scalar switched-affine update. For fixed sign, the state matrix is reconstructed from the SAM gradient and normalized EMA momentum, rather than inferred from the final threshold.

`verify.py` checks: the period-two state equations over multiple parameter choices; the characteristic polynomial and Jury boundary; the determinant/discriminant rate plateau; and the alternating magnitude growth for standard zero-momentum starts at and above \(s=2(1+\beta)\).

The executable checks are finite and serve only as algebra/transcription guards. The existence, local stability, and divergence statements are established analytically in `RESULT.md`. No stochastic, adaptive-preconditioner, or multidimensional validation is claimed.
