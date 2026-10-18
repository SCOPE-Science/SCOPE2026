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

The analytic solution was checked directly against both coupled backward generator equations at interior points on both half-lines, against the one-sided active capture boundaries, and against the inactive value and derivative transmission conditions. The stationary average agrees algebraically with the two conditional probabilities. The source specifies independent particle resetting that does not alter the gate state.

The accompanying standalone `check.py` uses only the Python standard library. Run `python check.py`. In the completed run, 135 deterministic residual/limit/boundary checks and four independent 12,000-trajectory event-interval Brownian-bridge simulation comparisons passed. Finite simulations cannot establish universally quantified statements; these follow from the derivations in `RESULT.md`.

The claim covers the exact left/right capture-side event, not a pathwise limit that would identify sides at a permanently active target. The simultaneous high-reset and small-reset-position limit assumes strictly positive reset locations throughout. Originality comparisons are subject to possible unrecognized broader backward-equation or splitting-probability literature. No independent scientific audit was performed.
