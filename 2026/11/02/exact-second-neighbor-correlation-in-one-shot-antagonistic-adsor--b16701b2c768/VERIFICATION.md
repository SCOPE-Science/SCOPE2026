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

The theorem is proved analytically using conditional independence of two exterior half-lines, an exact intervention at the intermediate site, the linear one-sided shielding ODE and a strictly convex auxiliary function. The proof gives every quantifier and the \(0<t\le1\), \(0<\alpha<1\) parameter boundary. The claim is independent of and stronger than the finite numerical tests.

`checker.py` was replayed from the actual package directory with `python checker.py` and returned `PASS 8859 independent rational/numerical assertions`. It independently enumerates random-order attempts and independent colours using exact rational arithmetic on finite paths of length 5, 7 and 9, checks the second-neighbor joint probability and one-point density against the infinite formula, compares the one-point density with the publicly available 2023 result, and checks symbolic-identity-based closed forms and strict sign on a broad parameter grid. Errors on truncated paths are boundary effects and were not treated as exact equalities.

Limits: The checker explores finitely many paths and parameter points; the infinite proof uses the factorial decay of decreasing-time ancestor chains and a pointwise analytic positivity argument. Independent external mathematical review is not recorded.
