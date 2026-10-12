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
The package verifies the exact isotropic AdaSGDMax recurrence at zero second-moment memory.

`verify.py` reconstructs the running maximum of squared gradient norms, checks the subcritical geometric law, one-step annihilation, resonant two-cycle, supercritical one-reset trajectory, exact second-iterate return, and reciprocal peak/contraction law across deterministic parameter grids.

The computations are transcription guards. The complete classification is proved algebraically in `RESULT.md`.
