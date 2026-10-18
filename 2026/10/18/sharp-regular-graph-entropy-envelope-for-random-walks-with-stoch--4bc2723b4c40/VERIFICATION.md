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

# Verification and scope

The standard-library `verify.py` recomputes finite stationary laws using exact fractions and Gaussian elimination, compares Markov-row entropy directly with the collision formula, and checks multiple regular families, reset roots and rational resetting rates. It also compares the regular-tree resolvent with girth-envelope bounds on cycles. The mathematical proof of the general theorem, including strictness and uniform convergence, appears in RESULT.md; computational tests alone do not establish it. The strict universal envelope concerns only observed vertex trajectories, not tagged action trajectories. No independent audit was performed.
