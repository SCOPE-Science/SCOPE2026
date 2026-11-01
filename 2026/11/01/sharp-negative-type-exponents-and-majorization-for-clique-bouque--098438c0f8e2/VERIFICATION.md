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

# Reproducibility checks

The analytic certificate is the exact zero-sum quadratic identity (1), the sharp within-blade Cauchy inequality, the weighted rank-one criterion, and the strict concavity argument in `RESULT.md`. These cover arbitrary real exponents and every permitted vector of positive integer blade sizes. No reliance on finite testing is needed for the universal statements.

Run `python verify.py` with Python 3 and SymPy installed. The checker constructs exact rational distance-power matrices, verifies the identity and necessary failure witnesses, uses exact principal minors to check nonnegative-type instances, and exhaustively checks small integer blade compositions against the extremal partition order. The observed result was:

`PASS: 2565 exact metric-signature or partition-majorization checks`

Finite tests cannot certify every integer size or transcendental endpoint; the written proof supplies those steps. Numerical roots in the checker are used only for supplementary finite partition comparisons. Independence assessment has not been performed.
