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
The package verifies the exact two-component cyclic-SGD limit underlying the SWA finding.

`verify.py` samples stable parameter choices, compares simulated phase limits with the closed two-cycle, checks the arithmetic SWA bias and objective excess, and verifies the cross-phase curvature identity.

The computations are transcription guards. The formulas are proved algebraically in `RESULT.md`.
