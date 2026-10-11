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

The global fixed-point count follows from strict convexity of the left identity-line difference and strict concavity of the right identity-line difference, with explicit tangency coefficients. The proof establishes strict endpoint signs, the parameter boundary inequalities, the location and nondegeneracy of both tangencies, and the types of the ordinary fixed points.

The standalone script `verify.py` uses only Python's standard-library exact rational arithmetic. It verifies the four-fixed-point polynomial sign witness and an independent fixed-point-free parameter witness from the motivating paper. The script cannot replace the analytical proof and makes no claims about the infinity of parameter values. A separate scientific-literature comparison remains incomplete for the full text of the 2024 follow-up paper. Independent validation is not performed.
