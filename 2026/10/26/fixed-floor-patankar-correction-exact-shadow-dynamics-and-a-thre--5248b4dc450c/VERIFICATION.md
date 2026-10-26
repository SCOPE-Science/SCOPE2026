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

# Reproducible checks and scope

Run `python verify.py` using Python 3 and NumPy. The program checks the exact-rational first-step defect for multiple timesteps; independently solves the source's two SDIRK predictor systems and final-only corrected resolvent; checks positivity, conservation, and convergence toward the analytically integrated shadow dynamics as the step is refined; and checks all three stationary formulas on a finite grid including branch interfaces. It exits with an assertion failure on any violation. The mathematical proof in RESULT.md establishes the uniform continuum result; finite tests do not prove infinite limits, all-parameter classification, or bibliographic novelty.

The relevant analytic checks are the column-stochastic positive resolvent, the uniform \(O(h^2)\) local expansion and one-step Lipschitz bound, strict monotonicity and branch inequalities for the shadow equilibrium, and direct two-by-two inversion at the exact stationary starting state.

No independent audit or external validation is claimed.
