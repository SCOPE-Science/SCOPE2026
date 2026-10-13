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
The package verifies the sharp full-rank two-task conflict window for uniform Aligned-MTL.

`verify.py` reconstructs source-form alignment from the task Gram eigendecomposition, checks randomized full-rank pairs against the closed sign formulas, tests both sharp norm-ratio boundaries, and verifies the equal-norm aggregate identity in conflict and positive-alignment regimes.

The computations are transcription guards. The phase diagram is proved analytically in `RESULT.md`.
