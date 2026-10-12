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
The package reconstructs the source discrete PID recurrence on diagonal SPD quadratics.

`verify.py` compares the direct three-state update with the eliminated two-step parameter recurrence, checks the strict Jury conditions against characteristic roots over random curvatures, verifies the exact all-spectrum endpoint criterion, and tests the hard derivative-gain boundary.

It also checks that the exact best isolated-mode spectral radius is \(\sqrt{\alpha+K_d(1-\alpha)\lambda}\) and verifies the loss-rescaling instability mechanism.

Finite computations are transcription guards only. The exact mode reduction and necessary-and-sufficient stability inequalities are proved in `RESULT.md`.
