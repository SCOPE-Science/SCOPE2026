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

# Reproducibility and scope

Run `python check.py` with Python 3 and the standard library. The checker compares independent exact-rational finite-state and last-selection computations, verifies the terminal-run power-sum identity, tests strict balancing, and confirms stationary subset recursions against full finite-state linear systems. The observed run completed 1,188 exact assertions.

The analytical proof, not this finite checker, establishes strict Schur-concavity for all positive sampling weights, all valid finite horizons, arbitrary positive common retention schedules, and homogeneous nontrivial stationary loss. No independent audit or external certification has been performed. Neither the code nor the proof establishes a hitting-time stochastic ordering or handles type-specific loss schedules.
