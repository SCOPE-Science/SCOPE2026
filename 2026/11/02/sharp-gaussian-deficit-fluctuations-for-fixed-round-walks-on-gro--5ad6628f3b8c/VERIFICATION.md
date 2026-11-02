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

The standalone command `python3 checker.py` requires only Python's standard library. Its exact rational checks compare a stage-count Markov recurrence against separately derived one- and two-point absence probabilities, check the all-\(n\) variance formula at \(q=2\) for finite test sizes, and directly enumerate small draw trajectories. It reports `CHECKS_PASS=961`.

The infinite-size claims are established by the analytic martingale argument in `RESULT.md`. Key independently reconstructible steps are: exact \(a_i=(1-1/i)^q\) conditional regression; the martingale telescope \(\prod_{j=i+1}^n a_j=(i/n)^q\); uniform bounded increments; \(L^2\) convergence of the unseen fraction; convergence of predictable quadratic variation to \(q^2/((q+1)^2(2q+1))\); and conditional Lindeberg because every scaled increment has magnitude at most \(q/\sqrt n\). Numerical or exact finite tests alone do not certify the limit theorem.

The formal scientific scope is fixed integer \(q\ge2\), independent uniform self-loop transitions, and one new label per stage. General graphs, varying durations and a quantified normal-approximation error are not established. Historical priority and independent audit remain open.
