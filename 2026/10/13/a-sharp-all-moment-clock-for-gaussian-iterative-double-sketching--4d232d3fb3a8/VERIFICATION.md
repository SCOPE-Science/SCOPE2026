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
The package verifier (`verify.py`) uses only the Python standard library and runs in a fresh process.

It reproduces the exact source Algorithm 1 on the one-column least-squares input using the shared Gaussian-prefix matrix, compares all source iterates with the closed scalar recurrence, and independently constructs the normalized-noise polynomial and remainder. It checks leading coefficient degrees, exact rational one-step mean-square identities, threshold edge cases, and the small-denominator scaling mechanism.

These finite computations validate transcription and representative algebraic identities, not the unbounded-integral proof. The all-positive-moment integrability theorem follows analytically from the chi-square density near zero and the nonvanishing leading coefficient as proved in `RESULT.md`.
