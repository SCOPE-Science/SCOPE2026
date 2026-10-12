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
The package verifies the exact CAME stationary-confidence law on constant biregular matrix gradients.

`verify.py` replays both rank-one factor states, source update clipping, momentum, confidence residuals, final direction, density scaling, and the positive- and zero-floor limits.

The computations are transcription guards. The identities are proved algebraically in `RESULT.md`.
