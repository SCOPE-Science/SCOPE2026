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
The package verifies the full-rank IMTL-G positive-rescaling reversal theorem.

`verify.py` reconstructs the source closed-form coefficient formula, checks the exact three-task coefficients and common projections, verifies that task-gradient rank is preserved at the critical scale, confirms singularity of the normalized equal-projection system there, and checks orientation reversal and all-task conflict below the threshold.

It also checks the general single-negative-coefficient threshold on deterministic test values. The computations are transcription guards; the sign criterion is proved algebraically in `RESULT.md`.
