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
The package verifies the stationary-gradient singular-value law for the original matrix Shampoo recurrence.

`verify.py` constructs matrices with prescribed singular spectra, accumulates the source left and right Gram matrices directly, computes inverse fourth roots numerically, and checks the closed-form preconditioned singular values, condition number, target equalization threshold, polar-limit error, and cumulative scaled displacement.

The numerical checks are transcription guards. The finite-time identities and asymptotic limit are proved analytically in `RESULT.md`.
