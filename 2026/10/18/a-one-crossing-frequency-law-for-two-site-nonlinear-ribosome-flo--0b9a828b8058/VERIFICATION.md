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

# Verification notes

The calculation uses the analytic transfer response \((i\omega I-B)^{-1}v\), not numerical integration as an infinite proof. The one-crossing result follows from \(\operatorname{adj}(i\omega I-B)=\operatorname{adj}(-B)+i\omega I\) for real \(2\times2\) matrices and symmetry of the quadratic form. The denominator is strictly positive because the autonomous equilibrium is Hurwitz.

The included `verify.py` executes with standard Python 3 and checks exact rational flux, Jacobian, Jacobi matrix, matrix-adjugate, response and threshold identities, plus bounded floating-point checks of the explicitly derived maximizing constant and representative frequencies. Independently, the nonlinear forced ODE was integrated with high-accuracy adaptive solvers at frequencies \(3\), \(6\), \(8.2\), and \(12\) for amplitudes near \(0.025\); the measured second-order gains had the predicted signs and approached the exact rational coefficient. The integration is not a substitute for the analytic perturbation argument, nor does it establish uniform error bounds in frequency.

The source's analytic periodic fixed-point argument establishes a smooth second variation; the specific example is analytic and has half-period forcing symmetry, giving an even amplitude expansion through the fourth-order remainder. The sign at the critical frequency is not established; no general nonperturbative or multiple-input assertion is made.
