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

# Reproducibility and limits

The theorem is proved in `RESULT.md` by finite exact matrix perturbation, binomial ratio monotonicity and the Poisson limit. The supporting `checker.py` reconstructs localization eigenvalues directly from incomplete-beta quadratures, which are numerically separate from the analytical closed Hessian expression. Run `python checker.py` with Python 3, NumPy and SciPy; the executed checker returned `PASS: 163 deterministic assertions; numerical eigenvalue Hessians and finite-spin limits`. Its finite tests cannot establish a statement quantified over all integer degrees and all admissible cap fractions. The asymptotic Hessian limit is not a uniform estimate for nonlinear perturbed domains.

Independent mathematical audit and independent validation: not performed.
