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

The accompanying `check_two_scale.py` is a standalone finite checker. Run with `python check_two_scale.py` in an environment with NumPy and SciPy. It performs 66 numerical-quadrature comparisons with an exact algebraic pair-facet volume expression, and 12 independent vertex-hull comparisons in dimensions two through four. For label bounds \(n=2,3,4\), these convex-hull volumes agree with the exact formulas reported in the original literature. The source code also tests each enumerated hull vertex against the subset-sum facet description.

Finite checks support the integration and facet bookkeeping, but cannot prove the all-dimensions asymptotic. The analytic proof in `RESULT.md` proves the tail and overlap bounds. The statement is fixed-\(n\), not uniform as both parameters grow. No independent audit has been performed.
