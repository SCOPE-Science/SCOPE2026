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
# Verification of the mathematical result

The executable `verify.py` is standalone Python with only standard-library dependencies. Invoking `python3 verify.py` in its package directory reported `VERIFY_OK: pair equality, 13 equilibria, six saddles, six sinks, and normalized K3 threshold` and the example values \(s\approx-1.543689012692076\), \(u\approx0.521387098369377\) at \(\kappa=1/2\).

The code constructs all thirteen claimed roots using bisection and permutations, evaluates the residuals in the original ODE, and checks the signs of Hessian principal minors and determinants for seven representative coupling strengths. It also verifies the exact identity of the two K2 coupling expressions on three sample states and the strict normalized-triangle inequality at \(\kappa=1/2\).

Finite-precision residual tests, sampled parameters, and the numerical code do not establish the theorem for all strengths. The universal result is proved analytically by the depressed-cubic root classification, sign-factored Hessian blocks, proper gradient potential, and stable-manifold dimension argument in RESULT.md. The exceptional critical strength \(\kappa=1/3\) is treated via the positive quartic energy term; no unsupported claim of exponential attraction is made there. The independent scientific audit has not been performed.
