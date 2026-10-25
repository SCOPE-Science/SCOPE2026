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

# Verification
The algebraic proof is in RESULT.md. Run `python verify_rgadi.py` with NumPy installed. The checker separately evaluates the two-stage source recurrence, the convex-combination single-step update, and the weighted power-Krylov factor; it checks numerical residuals and symmetry for independent nonsymmetric stable examples. It also verifies the exact scalar combinatorial recurrence for weights and a diagonal Vandermonde rank witness.

These numerical experiments cannot certify all dimensions and parameters. Correctness rests on the exact algebra and polynomial independence in RESULT.md. Publication-priority comparison and numerical software complexity are not independently certified.
