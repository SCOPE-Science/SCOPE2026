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
The package verifies the exact two-level response of the AdaNorm gradient-norm correction.

`verify.py` replays the historical-norm recurrence for randomized alternating amplitudes, checks the closed even and odd formulas, verifies the first corrected low-step index, and checks monotonicity and sharpness of the asymptotic contrast law.

The numerical calculations are transcription guards. The exact response, onset index, and universal contrast cap are proved algebraically in `RESULT.md`.
