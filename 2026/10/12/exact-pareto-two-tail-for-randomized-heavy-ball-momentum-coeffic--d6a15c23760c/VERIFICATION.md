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

The proof is analytic. It isolates the unique singular corner in the three-uniform coefficient distribution and evaluates the limiting triangular area after a \\(1/t\\) rescaling.

`artifacts/verify_momentum_tail.py` evaluates the exact leading constant for \\(k=1\\) of the deterministic-boundary anytime schedule and numerically integrates the exact conditional tail probability. The scaled probabilities approach the analytic constant.

The numerical calculation is supporting evidence only. The general tail asymptotic and moment threshold are proved in `RESULT.md`.
