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
The package verifies the GradNorm powered-target consistency theorem.

`verify.py` checks the universal normalized lower bound, constructs positive task weights attaining it on both sides of \(\alpha=1\), verifies the strict Jensen phase for heterogeneous rates, and confirms exact attainability of the mean-renormalized powered targets.

The calculations are transcription guards. The lower bound, sharpness, phase transition, and correction are proved analytically in `RESULT.md`.
