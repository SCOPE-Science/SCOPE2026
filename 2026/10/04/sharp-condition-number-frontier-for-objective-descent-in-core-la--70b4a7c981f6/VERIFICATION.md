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
The package verifies the exact condition-number frontier for core LARS on SPD quadratics.

`verify.py` checks the analytic extremizer, equality at the boundary, objective increase immediately above it, dense endpoint-mixture scans, and random higher-dimensional spectra.

Sampling is only a transcription guard. The continuum extremum is proved analytically in `RESULT.md`.
