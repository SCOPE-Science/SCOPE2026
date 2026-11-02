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

The analytic proof is in `RESULT.md`. Execute `python verify.py` with Python 3, NumPy and SciPy. This checks Boolean edge-boundary inequalities by enumerating every vertex in several dimension-eight halfspace sections, the exact offset-integrated expected vertex count for a box with unequal edges, and numerical rate-function comparisons for the half-length law \((\delta_{1/2}+\delta_{3/2})/2\) against the cube for five nontrivial cut fractions. The two calculated limiting tail constants are checked numerically. Successful local execution printed `ALL_CHECKS_PASSED`.

The numerical tests neither prove the large-deviation principle nor certify the absolute priority of the findings. Those depend on the written mathematical argument and the bounded source comparison. No independent review has been undertaken.
