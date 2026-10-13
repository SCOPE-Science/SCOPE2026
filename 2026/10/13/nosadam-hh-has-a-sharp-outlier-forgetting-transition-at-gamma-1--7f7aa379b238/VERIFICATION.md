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
The package verifies the exact single-outlier memory law for the NosAdam-HH second moment.

`verify.py` reconstructs the source hyperharmonic weighted-average recurrence, checks the closed finite-time formula, tests the polynomial and logarithmic forgetting regimes, confirms a positive limiting imprint in the summable regime, and checks the source comparison exponent \(\gamma=0.1\).

The finite calculations are transcription guards. The phase transition follows analytically from the partial-sum asymptotics proved in `RESULT.md`.
