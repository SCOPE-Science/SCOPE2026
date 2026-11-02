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

Run `python verify.py` using Python 3.11+ and SymPy 1.12+. This is a standalone verifier of the algebraic identities and representative rational stage fractions; it does not query external services or data.

The verifier executed from the package source and printed:

```
VERIFY_OK symbolic identities, antithetic imaginary conservation, 2652 left-half-plane pairs, iid divergence at z=-5
```

**Analytical verification:** `RESULT.md` reconstructs the scheme multiplier from the original stage equations, multiplies the pair exactly, and proves the complex norm-difference identity. This is sufficient for the whole-plane contraction conclusion. The converse is based on a second-order imaginary-axis expansion for arbitrary fractions together with the exact mean constraints. The independent-stage failure is an exact covariance positivity argument for two decreasing functions of a nondegenerate stage fraction. The rational-stage finite tests only cross-check these formulae.

**Coverage and limits:** The random dependence is within each consecutive pair; pair ordering, intermediate-step amplification, nonlinear convergence, and arbitrary nonnormal-matrix dynamics are not covered. The result requires the constant-coefficient linear scalar stability equation and a common fixed step. No independent audit or external experimental validation is asserted.
