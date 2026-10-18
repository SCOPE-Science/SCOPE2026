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

# Reproducibility and boundaries

Run `python verify.py` with Python 3 and its standard library. The script checks 2,925 rational order comparisons for the permitted trust-switch directions, verifies exact four-agent neighbor lists and the prime two-cycle, and reproduces the non-star-shaped three-agent contrast from the motivating paper.

Analytical completeness does not come from grid enumeration. The proof uses exact convex-hull containment, persistent vertex-label sets on a finite periodic orbit, and a dimension-free reduction to a scalar monotone map. Open and closed radial membership endpoints are handled because star-shapedness imposes weak monotonicity on the two trust indicators, without any continuity assumption.

The calculation does not certify global convergence or all possible recurrence beyond finite periodic trajectories. No independent audit is claimed.
