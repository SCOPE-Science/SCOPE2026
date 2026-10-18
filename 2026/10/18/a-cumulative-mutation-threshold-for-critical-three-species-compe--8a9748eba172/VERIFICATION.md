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

Execute `python3 verify.py` from the directory containing these files. The standalone program requires only Python 3 and no network access. On its completed test run it reported:

```
power q=1.0: at t=350, budget=1.4652, KL=1.923341756e-05
power q=2.0: at t=350, budget=0.249288, KL=0.02811517477
power q=0.5: at t=400, budget=9.51249, KL=3.700743418e-17
PASS: 288 exact/algebraic, entropy, limiting-ratio and trajectory checks
```

The exact tests use rational arithmetic for the independently constructed original and normalized vector fields, the total-logistic identity and entropy derivative, across 35 choices of positive densities, positive critical-line coefficients and mutation intensity. They also check the entropy-dissipation inequality and near-uniform ratio numerically. Finite-step Runge–Kutta samples show consistency with predicted budget behavior. Near machine precision, empirical entropy is not a reliable asymptotic-rate estimator: the \(q=0.5\) sample simply confirms strong finite-time contraction. Analytical arguments in RESULT.md, not sampled trajectories, establish the omega-limit and all-measurable-schedule assertions.

No independent scientific audit has been performed. The package does not claim formal verification of every infinite-time conclusion.
