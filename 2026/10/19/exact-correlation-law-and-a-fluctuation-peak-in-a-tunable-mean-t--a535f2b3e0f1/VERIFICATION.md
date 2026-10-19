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

# Reproduction and limits

Run `python verify.py` using Python 3 and SymPy. The program constructs the exact four-dimensional piecewise-affine transfer matrix, verifies its invariant density, normalization and mean, computes and factors its characteristic polynomial, reconstructs the first three covariances, and checks the full rational resolvent identity as a symbolic expression over rational functions in the parameter and generating variable. It verifies the exact Green–Kubo expression, the derivative defining the variance peak, and the triple-eigenvalue collision and noncancellation at the resonance.

An independent integration routine represents \(T_b^n\) as piecewise affine on exact rational subintervals obtained by preimage splitting. It integrates \((x-m_b)(T_b^n(x)-m_b)\rho_b(x)\) exactly and checks agreement with transfer iterates for \(b\in\{1/5,1/4,1/3,2/5\}\) and all integers \(0\le n\le8\), totaling **36 independent exact covariance comparisons**. The recorded local execution completed without assertion failure.

The symbolic identities verify calculations, not the hypotheses of primitive-Markov mixing or the martingale central limit theorem; the analytical proof gives those arguments. Finite integration tests are not an infinite proof. There is no claim of independent certification, numerical convergence rate, coverage of nonexpanding parameter values, or exhaustive literature priority.
