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

# Verification and boundaries

The proof in `RESULT.md` establishes the exact three-colour model reduction, monotone uniqueness through the threshold, the two explicit supercritical families, and linear ODE stability using strict hyperbolic inequalities for every real interaction magnitude in scope. No infinite-range conclusion rests on computation alone.

To replay finite diagnostic checks, run `python3 check_equilibria.py`. The checker uses only Python's standard library, bisects the two nonlinear scalar branch equations at ten parameter magnitudes, checks all thirteen generated fixed points, verifies stability-sign conditions and finite-difference Jacobians, and tests sample points for the subcritical monotonicity inequality. The observed output was `PASS 568 checks; ten interaction strengths, 13 solutions each`.

Neither numerical residuals nor this self-review constitute an independent proof check or a historical-priority certificate. The analytic theorem asserts a lower bound on supercritical equilibria, not an exhaustive count; the existence of additional equilibria, global stochastic basin probabilities and nonlinear critical stability remain open within this package.
