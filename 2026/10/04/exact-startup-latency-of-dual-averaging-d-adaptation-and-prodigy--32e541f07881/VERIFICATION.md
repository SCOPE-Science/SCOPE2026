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
The package verifies the exact first-growth cutoffs for dual-averaging D-Adaptation and Prodigy on a one-dimensional constant-subgradient objective.

`verify.py` directly replays both source recurrences, checks the closed forms up to the first increase, and uses exact rational arithmetic with integer-square certificates to prove \(R_1,\ldots,R_7<1<R_8\) and \(P_1,\ldots,P_4<1<P_5\).

The finite radical comparisons are certified exactly. The recurrence formulas and the common-objective constant-subgradient condition are proved algebraically in `RESULT.md`.
