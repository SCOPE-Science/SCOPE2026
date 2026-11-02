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

Run `python verification/verify.py` with Python 3, SymPy, SciPy and NumPy installed. The program checks the exact eigenvector normalization, quadratic Hessian evaluations, inverse-resolvent formula, first Lyapunov coefficient, second-harmonic periodic forcing solution, its first-harmonic Fourier projections, and the exact cancellation yielding frequency coefficient \(1/4\).

It also solves the *nonlinear full-flow* shooting equations for six small-cycle parameter selections: \(b\in\{1/2,1,2\}\) and \(\alpha\in\{-0.005,-0.0025\}\). At \(b=1,\alpha=-0.005\), the computed return period is about \(6.2753386302\), compared with the asymptotic prediction \(6.2753313255\), and the physical \(x\)-amplitude is about \(0.100360193\), compared with its leading approximation \(0.1\).

The symbolic checks cover algebraic formulas for every symbolic positive \(b\); the six numerical examples do **not** prove asymptotics for all positive \(b\) or infinite-time dynamics. The analytical Hopf and Poincaré–Lindstedt proof supplies these statements. No independent mathematical audit has been performed.
