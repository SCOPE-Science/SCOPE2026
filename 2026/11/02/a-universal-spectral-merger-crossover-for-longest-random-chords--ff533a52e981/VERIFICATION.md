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

# Numerical and analytic verification

The proof is supplied in `RESULT.md` and uses the exact conditional invariant-line survival integral. The companion `verify_crossover.py` reconstructs that integral independently for planar ellipses with a near-degenerate maximal axis, then compares the normalized tail against the limiting spherical profile. It uses 36,000 deterministic angular midpoint nodes and tests soft ratios 0, 0.5, 1, 2, and 8 at normalized deficits 0.02, 0.005 and 0.001. The maximum final-sample discrepancy was below 0.001, and the independent large-ratio checks at 25, 100, 400 converge toward the analytically derived constant 1/2 (observed 0.50254, 0.50063, 0.50016). Execute with `python verify_crossover.py` (NumPy and SciPy required). These numerical results are neither an infinite-domain proof nor independent validation. No external audit was performed.
