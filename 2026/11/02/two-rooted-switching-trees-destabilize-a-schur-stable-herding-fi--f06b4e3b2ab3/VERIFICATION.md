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

## Reproduction
Run `python verify.py` in the directory containing this file with Python 3 and SymPy installed. The program builds every recurrence and switching matrix as an exact rational or polynomial matrix and executes nine symbolic equality checks. It directly checks both factor determinants; no floating-point eigenvalue result is needed.

## Analytic steps separately checked
The Schur reduction and strict Jury inequalities in RESULT.md prove single-filter stability throughout \(0<\beta<25/8\). The monodromy determinant changes sign at \(\beta=75/32\) while the characteristic polynomial is monic, proving a real Floquet multiplier greater than one for every \(75/32<\beta<25/8\).

## Limits
The alternating schedule is externally prescribed and is not certified realizable under distance-based endogenous switching. No assertion is made about the full nonlinear herding trajectory under the original selection rule. Independent audit has not been performed.
