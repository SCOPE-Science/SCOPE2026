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
The package verifies the exact one-coordinate Yogi response to a balanced alternating gradient.

`verify.py` checks the first-moment closed form, integer reciprocal-step locking, noninteger two-cycle parity on both sides, the predicted long-run parameter slope, and suppression when the second moment is initialized at the squared-gradient level.

The finite computations are transcription guards. The state cycle and asymptotic drift are proved analytically in `RESULT.md`.
