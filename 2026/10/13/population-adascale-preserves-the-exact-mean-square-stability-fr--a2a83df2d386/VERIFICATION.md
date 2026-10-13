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
The package verifies the exact population-gain AdaScale law on scalar random-curvature quadratics.

`verify.py` enumerates complete two-point batch-average distributions, reconstructs the gain from curvature moments, checks the direct expected squared multiplier against the closed formula, verifies the scale-independent sharp boundary and unique optimal base rate, and checks the fixed linear-scaling comparison.

Finite enumeration is a transcription guard. The arbitrary-distribution theorem depends only on the first two curvature moments and is proved analytically in `RESULT.md`.
