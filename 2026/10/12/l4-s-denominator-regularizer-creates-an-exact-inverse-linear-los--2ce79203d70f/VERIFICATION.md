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
The package verifies the practical L4-SGD scalar recurrence, including the minimum-loss clamp, forgetting rule, and additive denominator regularizer.

`verify.py` checks finite target lock, the exact post-lock dimensionless recurrence, the proved inverse-linear loss constant, and the geometric post-lock law obtained when the denominator regularizer is formally removed.

The computations are transcription guards. Finite lock and the asymptotic constant are proved analytically in `RESULT.md`.
