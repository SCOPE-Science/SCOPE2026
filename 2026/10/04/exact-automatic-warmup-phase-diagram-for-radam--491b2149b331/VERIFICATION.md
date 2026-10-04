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
The package verifies the exact RAdam rectification-activation phase diagram for the source gate \(\rho_t>4\).

`verify.py` evaluates the published statistic, computes threshold roots, checks the polynomial identity, verifies representative activation indices, and tests the asymptotic root law.

The calculations are transcription guards. Root uniqueness, the exact phase partition, and the asymptotic are proved analytically in `RESULT.md`.
