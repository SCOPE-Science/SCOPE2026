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

# Reproducibility and proof boundary

Run `python3 check_critical.py` with standard Python 3. The code completes 12,859 checks covering exact rational recovery from the payoff matrix, all three critical vector-field reductions, symbolic-rational derivatives of the exact antiderivatives, independently integrated sample trajectories, and large-time asymptotic residuals. No external numerical package, data file, or network service is required.

The universal conclusions come from separation of variables and monotonicity on the specified open intervals; numerical time stepping supplies a cross-check rather than an exhaustive infinite-time certificate. Initial states at equilibrium do not follow the nonconstant critical asymptotics. Spatial and stochastic systems are outside the claim. Publication-priority comparison remains limited by the possibility of unindexed prior analysis.
