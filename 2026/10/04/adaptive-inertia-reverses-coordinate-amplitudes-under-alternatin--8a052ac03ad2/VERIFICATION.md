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
The package verifies the exact persistent-alternation response of source-form Adaptive Inertia Algorithm 2.

`verify.py` replays the second-moment bias correction, parameterwise clipping, first-moment recurrence, product bias correction, and parameter update. It checks exact \(\beta_2\) erasure, the three piecewise response branches, strict interior amplitude reversal, and the source-default \(G=(2,1)\) example.

The finite computations are transcription guards. The complete formulas and branchwise monotonicity are proved analytically in `RESULT.md`.
