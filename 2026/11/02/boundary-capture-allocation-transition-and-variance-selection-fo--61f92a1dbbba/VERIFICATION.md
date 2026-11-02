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

# Reproducibility and verification

Run `python check.py` with Python 3 and SymPy. It symbolically reconstructs both backward moment recursions, verifies the collision boundary equations, simplifies the exact mean and its derivative, and derives the critical-rate second-moment and variance expressions. It also confirms reparametrized agreement with the general telegraph first-passage mean reported in the archival literature and separately checks the published symmetric-boundary second moment.

The checker additionally performs 84,000 reproducibly seeded event-driven first-passage trajectories across six parameter points (including perfectly reflecting, asymmetric, and critical cases), and 1,008 deterministic allocation comparisons. The assertions completed successfully in the supplied execution environment. Monte Carlo and finite allocation sampling test consistency only; they are not certificates for the infinite set of positive model parameters.

The exact algebraic derivative sign proves global optimality over every feasible allocation, and the exact critical variance expression proves its unique minimizer up to left–right exchange. One model limitation is the fixed *sum of per-collision capture probabilities*, which cannot be freely substituted by a different boundary reaction budget. The result is not independently audited or experimentally validated.
