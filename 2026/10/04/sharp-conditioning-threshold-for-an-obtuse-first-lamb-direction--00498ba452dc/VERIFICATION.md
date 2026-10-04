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
The package verifies the exact first-step LAMB reduction and the sharp two-dimensional conditioning threshold.

`verify.py` checks the explicit rational counterexample, numerically tests the SPD turning-angle bound, reconstructs the rotated sharpness family above \(3+2\sqrt2\), and confirms Euclidean distance increase for many positive step magnitudes.

Finite calculations are transcription guards. The threshold, nonexistence below it, and sharp existence above it are proved analytically in `RESULT.md`.
