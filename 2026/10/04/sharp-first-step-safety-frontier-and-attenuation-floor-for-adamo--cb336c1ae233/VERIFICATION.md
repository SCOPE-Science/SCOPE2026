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
The package verifies AdaMod's all-history attenuation floor and exact first-step scalar-quadratic safety frontier.

`verify.py` generates nonnegative raw-rate histories, checks the sharp rate bound, directly replays the first AdaMod step for multiple moment coefficients, verifies both sides of the exact objective-safety boundary, and reproduces the implementation-scale amplification examples.

Finite calculations are transcription guards. The universal attenuation floor and all-initialization first-step frontier are proved analytically in `RESULT.md`.
