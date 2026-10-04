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
The package verifies the exact scalar AdamW two-cycle and the sharp memoryless-second-moment threshold.

`verify.py` replays the source bias-corrected second-moment recurrence on the alternating orbit for several \(\beta_2\) values, checks the exact cycle amplitude, verifies magnitude contraction below the threshold when \(\beta_2=0\), and compares the analytic two-step cycle multiplier with finite perturbations.

The finite calculations are transcription guards. The threshold, global convergent side, exact orbit, and local multiplier are proved analytically in `RESULT.md`.
