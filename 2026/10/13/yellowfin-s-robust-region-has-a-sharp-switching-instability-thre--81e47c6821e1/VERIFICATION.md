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
The package verifies the sharp two-period switching threshold inside YellowFin's robust region.

`verify.py` checks the one-step robust-region spectral radius, exact two-step trace and determinant formulas, the Jury threshold on a deterministic grid of phase pairs, the endpoint Floquet multipliers, and the generalized-condition-number threshold.

The grid checks are transcription guards. Uniformity over every two-phase robust-region pair is proved analytically in `RESULT.md`.
