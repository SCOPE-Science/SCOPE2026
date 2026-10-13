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

The analytic proof reduces MO-Adagrad to an exact scalar recurrence on the symmetric quadratic family. The crossing-depth maximum is derived by differentiation and the endpoint convergence is proved from positivity of the multiplicative factors together with divergence of the cumulative effective steps.

`artifacts/verify_pareto_capture.py` performs finite consistency checks of the first-step formula, the unique analytic maximizer, both sides of the sharp width threshold, left-right symmetry, and monotone endpoint convergence. These checks support reproducibility but do not replace the quantified proof.

No claim about unequal curvatures, stochastic gradients, higher-dimensional Pareto sets, or the global dynamics after a full-set overshoot is verified.
