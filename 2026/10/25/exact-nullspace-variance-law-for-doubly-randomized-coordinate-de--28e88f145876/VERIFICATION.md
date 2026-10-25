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

# Verification of the exact second-moment formula

The stated DSBGD step is algebraically identical to Xia–Zhou's independent row/coordinate sampling on a rank-one operator with \(A_{ij}=c_i\). The key checks are the scalar defect recurrence, the orthogonal splitting between the range direction and zero-sum nullspace direction, and the vanishing conditional cross term when the coordinate index is sampled uniformly. For every deterministic admissible step sequence, repeated conditional expectations yield the exact finite-time identities. A positive first increment gives the strict lower bound on the limiting nullspace variance. A pathwise exponential bound on the defect and the finite total mass of nonnegative increments establish the limiting claims.

Run `python verify.py` with Python 3 and no third-party dependencies. The checker exhaustively enumerates 0–6 steps for the two-row, two-coordinate rational example and several small variable-step problems. It compares finite enumeration against algebraic solution-error and residual moments, independently verifies the exact rational two-by-two expression, and checks positivity of the nullspace contribution. Expected result: `EXACT_RATIONAL_CHECKS_PASS 12` followed by `TWO_BY_TWO_Q 65/128 ASYMPTOTIC_MSE_FLOOR 17/126`.

These finite tests do not certify the limiting result or the universality over all admissible step sequences. Those are established in the written proof. No claim is made about noisy observations, arbitrary rank-deficient operators, dependent sampling, floating-point effects or independently audited correctness.
