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

For a quadratic \(f\), expanding \(f(x+hb)-f(x)\) gives the exact projected-gradient error. Summing squared orthogonal basis coefficients proves identity (1) in `RESULT.md`. A balanced Rayleigh-quotient basis attains the minimum; an eigenbasis attains the maximum. Rotationally invariant spherical fourth moments and averaging over adversarial orientation establish the sharp Haar minimax law. The mathematical proof is in `RESULT.md`, independent of finite experiments.

Reproduction command: `python verify.py` using NumPy and SymPy. Actual replay result: four exact rational/symbolic examples, 900 deterministic numerical identities/inequalities, and 54,000 Haar frames, all passed. Numerical moment comparisons use a specified seed and finite error tolerance; they are not exhaustive evidence for an infinite theorem.

The \(C^3\) sign-symmetrization result controls the **bias of the mean estimator**, not its mean-square error or whole-optimizer convergence. Floating-point evaluation noise, evolving hint subspaces and adaptive rotations are outside the proved domain.
