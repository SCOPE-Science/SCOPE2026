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

The model equations and the exact endemic equilibrium were independently substituted into the original vector field. The Jacobian entries, trace, determinant, discriminant scaling, and central frequency-to-damping identity are reconstructible from the displayed rational expressions in `RESULT.md`.

Run `python3 CHECK.py` to reproduce 245 exact-rational parameter checks (across admissible infection strengths and avoidance ratios), two explicitly rational Jacobian spectra, and one illustrative set of time-domain sign changes calculated by fourth-order Runge–Kutta with step length \(10^{-3}\). No packages other than the Python standard library are required. The computations previously returned `Exact rational cases: 245 ; example spectrum: PASS` and finite-time differences of signs \(+,-,+,-\) at times \(1,5,15,25\).

**Limits of computation:** Finite cases and numerical trajectories do not prove exact optimization, the infinite family of turnover speeds, or infinitely many future crossings. Those claims rely on the algebraic discriminant, derivative sign, strict spectral gap, and nonlinear variation-of-constants argument in `RESULT.md`. The statement at defective repeated eigenvalues is specifically a spectral exponential rate, allowing polynomial prefactors. Independent audit has not been performed.
