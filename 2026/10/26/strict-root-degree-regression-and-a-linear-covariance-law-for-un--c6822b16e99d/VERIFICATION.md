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

The included `verify.py` runs with Python 3 standard library and independently enumerates all Dyck paths of semilength at most nine. It checks the exact root-degree counts and contour-area sums against the coefficient formulas, the strict conditional regression, the first-step difference, and the exact mean degree. For dimensions 10 through 60 it tests rational coefficient ratios and strict conditional comparisons. It checks finite negative covariances, without claiming these finite checks prove general statements. The analytic argument in `RESULT.md` proves the unrestricted result and the asymptotics.

The independent-audit channel is not performed; these are internal mathematical and finite reproducibility checks only.
