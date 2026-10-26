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

The included `checks/verify.py` uses only Python's standard library and exact integer arithmetic. Execute `python checks/verify.py` from the package root. The script checks trace, determinant, the all-iterate counting identity for periods 1 through 12, the quadratic-form identity on a finite integer grid, the explicit character observation and the integer companion relation. Passing finite arithmetic checks is not evidence for an all-integer exhaustive search; the impossibility for all winding vectors is proved by the completed-square identity in the main text. Nonlinear sensor impossibility uses first cohomology and invariance of domain, not numerical verification.
