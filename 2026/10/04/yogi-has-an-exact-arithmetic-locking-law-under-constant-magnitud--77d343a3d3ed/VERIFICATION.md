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
The package verifies the exact constant-gradient orbit of source-form Yogi Algorithm 2.

`verify.py` checks finite locking for reciprocal-integer values, exact two-cycles for noninteger reciprocal values, the cycle-width identity, source-reported beta-two values, asymptotic parameter-update magnitudes, and Adam's geometric second-moment convergence.

The numerical calculations are transcription guards. The complete orbit classification is proved analytically in `RESULT.md`.
