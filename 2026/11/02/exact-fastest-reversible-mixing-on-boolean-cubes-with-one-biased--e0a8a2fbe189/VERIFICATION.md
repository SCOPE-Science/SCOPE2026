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

The exact proof establishes the theorem for all integers \(d\ge1\) and all \(0<a\le1/2\), independent of finite testing. The supporting standalone check is `verify.py`, run with `python verify.py` after installing the packages in `requirements.txt`. It printed:

```
ALL_CHECKS_PASSED 883
```

The checker verifies the symbolic feasibility quadratic and discriminant, the two exact boundary determinant factors and holding probabilities. For \(d=1,\ldots,5\), across five rational stationary biases, it builds the full transition matrix, checks stochasticity/detailed balance/invariance and its spectral norm, and compares against independently generated asymmetric reversible feasible kernels.

These tests do **not** enumerate all Markov kernels or certify infinite quantifiers. The analytic positive-semidefinite obstruction and matching construction supply the mathematical proof. No independent mathematical audit or external certification has been performed; nonreversible chains, arbitrary multi-bit biases, and finite-time mixing are outside the claim.
