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

# Verification record

The proof in `RESULT.md` is analytic and self-contained. An auxiliary standalone program, `check_fold_boundaries.py`, uses the Python 3 standard library only. Running `python3 check_fold_boundaries.py` prints `PASS: 144 finite consistency checks`.

Actual checks include the map derivative against finite differences, the stationary-root algebra, derivative-zero tangency equations at both thresholds (including negative forcing conjugacy), numerical 0/2/4 simple-crossing censuses away from critical parameters, and the leading \(3/2\)-power coefficient. Such finite numerical tests cannot prove completeness, global invertibility, or the asymptotic formula for all parameters; those conclusions follow from exact derivatives, stationarity equations, monotonicity intervals, and Taylor expansion in `RESULT.md`. The source article is not bundled or redistributed.

The candidate remains restricted to the exact real-parameter range stated in the theorem. Independent review has not been performed.
