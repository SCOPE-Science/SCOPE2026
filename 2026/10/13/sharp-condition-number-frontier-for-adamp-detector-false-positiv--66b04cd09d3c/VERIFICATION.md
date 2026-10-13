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
The package verifies the sharp SPD cosine bound and its AdamP threshold inversion.

`verify.py` checks randomized spectra and vectors against the analytic lower bound, verifies the exact extremal-eigenspace equality witness, tests the no-trigger/trigger sides of the strict detector frontier, and reproduces the default-\(\delta\) numerical thresholds.

The numerical calculations are transcription guards. The universal minimum, equality case, and if-and-only-if detector frontier are proved algebraically in `RESULT.md`.
