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

Analytical reproduction: Substitute the positive-force parameterization into every stationary equation and differentiate the two-force logarithmic potential. Its negative-definite Hessian gives uniqueness, and its axis KKT derivatives equal the invasion-number excesses. Symmetrize the continuous-time Jacobian using the explicitly positive weight matrix; check the weighted Cauchy–Schwarz bound and equality conditions. Finally, conjugate the admissible discrete Jacobian by the strain-sign diagonal to obtain a nonnegative matrix with Perron root less than one.

Programmatic reproduction: With `numpy` and `scipy` installed per `requirements.txt`, execute `python verify.py`. The checker prints an exact-reference two-node equilibrium and both invasion numbers; it verifies force consistency, positive states, weighted-Jacobian symmetry and strict negative spectrum for 51 seeded randomly generated feasible coexistence states. The exact two-node analytic expressions and spectral identities appear in `RESULT.md`.

Limits: No finite sample proves an all-parameter theorem, novelty, or a global stability result; these depend respectively on the written proof and documented comparison of accessible literature. Independent audit and validation have not been performed.
