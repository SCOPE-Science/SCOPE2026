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
The package verifies the exact memoryless Sadam scalar map and its softplus transition.

`verify.py` reconstructs the source update, checks strict magnitude decrease below and at the critical boundary, verifies the ordinary linear limit, the quadratic resonance, the critical \(t^{-1}\) amplitude constant, the exact supercritical symmetric two-cycle, and the strict local cycle multiplier bound.

Finite computation is used only as a transcription and asymptotic guard. The infinite-time statements and sharp threshold are proved analytically in `RESULT.md`.
