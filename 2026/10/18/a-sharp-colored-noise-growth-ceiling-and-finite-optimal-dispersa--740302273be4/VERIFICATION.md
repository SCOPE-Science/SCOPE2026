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

The mathematical claims are proved by stationary contraction, exact logarithmic-growth identities, Gaussian integration by parts on causal OU paths, and two stationary moment budgets. No external independent audit has been performed.

Reproduction: run `python verification.py` with NumPy installed. The code uses reproducible seeded trajectories, exact updates of the OU forcing, and symmetric drift-splitting for the scalar log ratio. It checks equality of two independent growth estimators to stochastic integration precision and compares observed growth with the analytical upper ceiling. Stationary moments are also sampled. These numerical estimates are finite-time approximations; the strict all-parameter inequalities and limiting assertions are mathematical deductions, not conclusions from simulations.

At fixed positive migration and noise correlation parameters, the small-noise limiting coefficient follows from dominated convergence in the exact response identity. At fixed positive noise intensity and correlation rate, the large-migration coefficient follows after rescaling response time. The small-migration endpoint is established by the explicit two-parameter moment-budget estimate in the proof.

Limitations: no uniqueness assertion for the optimizing migration rate, no exact optimal value, no sharp small-migration equivalent, and no claim for unequal, correlated environmental processes or more than two patches.
