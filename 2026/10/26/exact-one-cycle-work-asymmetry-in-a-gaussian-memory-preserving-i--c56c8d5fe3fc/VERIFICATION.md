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

# Reproduction and verification

Run `python verify.py` with NumPy and SciPy installed. The program checks seven nontrivial physical parameter sets and a separate exactly symmetric configuration, reporting `PASS 114 deterministic numerical and algebraic comparisons`.

Independent covariance computation uses a continuous-time OU Lyapunov equation for the free bath and a discrete-time Lyapunov equation for the periodic measurement-feedback recursion. The resulting prefeedback variance and cross-covariance are compared with the closed form in `RESULT.md`. Eigenvalue checks establish trace and determinant of the work form; comparisons test its moment generating function, Bessel-density normalization and positive-work probability by numerical quadrature, the exponential signed-work density ratio and the work variance.

These are finite checks of analytic identities, not exhaustive validation. The theorem follows from the algebraic stationary covariance equations and exact Gaussian diagonalization in `RESULT.md`. Numerical integration tolerances do not certify arbitrary input parameters. The results do not assert independent validation or priority over uninspected literature.
