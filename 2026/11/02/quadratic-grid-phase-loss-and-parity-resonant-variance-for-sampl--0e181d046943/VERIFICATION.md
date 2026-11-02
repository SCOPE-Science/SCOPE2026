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

# Reproducibility and verification

The proof is analytic and self-contained: the adjoint identity reduces the problem to exact cellwise signed integration, Taylor's theorem controls the switch-cell difference uniformly over grid shifts, and a convergent Fourier series supplies all shifted-phase moments. Its validity is not based on a finite experiment.

Run `python3 verify.py` using Python 3 standard library. The standalone code exercises the exact rational two-switch polynomial case on 512 rational grid/shift pairs and checks the explicit Taylor-error bound. It checks the exact phase integrals \(\mathbb E g(U)=1/12\), \(\mathbb E g(U)^2=1/80\) and \(\operatorname{Var} g(U)=1/180\), plus the two-switch even/odd leading variance ratio \(16\). It also approximates the shift-integrated mean and variance with 1024 rational phase samples for four grid sizes, using exact rational integration prior to float averaging.

These tests are not exhaustive over \(C^2\) coefficients, shift phases, grid sizes or harmonic frequencies. The exact coefficients and uniform remainders rely on the mathematical arguments in `RESULT.md`. At switch positions on a grid boundary the gap contribution is zero. For the two-switch polynomial, \(1/180\) and \(1/2880\) are leading variance coefficients and not exact finite-step variances.

Self-review: passed. Independent audit: not yet performed.
