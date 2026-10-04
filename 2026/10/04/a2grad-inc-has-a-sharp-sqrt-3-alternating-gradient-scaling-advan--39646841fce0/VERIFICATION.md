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
The package verifies the practical A2Grad period-two input-response law.

`verify.py` reconstructs the empirical innovation, checks the source recurrences for A2Grad-uni, A2Grad-inc, and A2Grad-exp, verifies the exact incremental unrolling, and checks convergence of the normalized scale and inner-step constants.

The finite computations are transcription guards. The exact unrolling and all asymptotic constants are proved analytically in `RESULT.md`.
