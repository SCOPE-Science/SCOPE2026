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
The source one-sample AdaLoss recurrence is reconstructed in `verify.py` for positive exact and perturbed optimum targets. The checker uses only the Python standard library. It independently verifies the modal update on rotated two-dimensional quadratics, the signed accumulated discrepancy identity, convergence of the centered square-root-exponential/logarithmic asymptotic profiles, and geometric convergence with exact centering.

Finite numerical calculations are transcription checks, not the proof of all-time behavior. The proof and restrictions are given in `RESULT.md`.
