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

Exact symbolic checks are provided in `check.py` (Python 3 and SymPy). It reconstructs the first and third polar formulas, computes the three pure-cube coefficient Jacobians at the 52 Fermat incidence points, checks the entire remainder along stationary two-supported directions, and checks the reflecting symmetry for fourth-root ratios. Algebraic properness, upper semicontinuity, and the formal implicit-function argument are proved in RESULT.md and are not certified by a finite enumeration. No independent audit has been performed.
