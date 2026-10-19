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

# Verification of the information-state theorem

The mathematical proof is contained in `RESULT.md`. Its key independently reproducible algebraic facts are the exact Schur-block form, the Stein-divergence decrement and its equality condition, and the three-eigenvalue formula for the derivative of the two-step information update.

## Replay

Use Python 3 with the dependency declared in `requirements.txt`, then run:

```
python verify.py
```

The archived run prints `PASS 2565 deterministic numerical assertions`, also recorded in `verification_output.txt`. The verifier tests randomly constructed positive-definite information matrices, orthonormal subspace bases of several ranks, the Schur formula and divergence decrement, convergence for cyclic persistent-excitation schedules, exact two-direction Jacobian eigenvalue formulas, finite-difference derivatives, and small-angle asymptotic coefficients. The seed is deterministic and the script has no network access.

## Limits

Finite floating-point comparisons are not certifications of universal positivity, global convergence, local nonlinear sharpness, or asymptotic expansions. Those conclusions follow from the explicit proof and its quantified hypotheses. The verifier does not test noisy parameter tracking or regressors with unequal retained singular values. Independent mathematical audit remains unperformed.
