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

The executable `verify.py` reconstructs the original two-equation vector field, solves its stationary identities using the paper's normalization, verifies rational parametrization, derivative and determinant factorizations symbolically, and checks the fold-polynomial identity. It also calculates full local Jacobian spectra at numerically isolated equilibria for seven distinct quality ratios on both sides of the calculated threshold.

Observed execution: PASS; 126 assertions, including exact symbolic identities and independent ODE-residual checks. The proof in RESULT.md supplies the universal uniqueness and stability arguments; finite numerical sampling is not used to infer universal theorems.

There is no verified nonlinear global basin theorem, finite-population switching-time bound, or independent scientific audit. Publication-priority uncertainties are stated separately.
