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

The all-height proof is in `RESULT.md`, which states the existing geometric criterion separately from the newly derived arithmetic enumeration. The standard-library Python program `verify.py` independently checks the exact arithmetic formula and strict-expanding denominator on all 64 height boxes from 2 through 65. It does not use the classification \(t^2/d\in\{0,1,2,3\}\) for its positive decisions: it tests matrix-power traces and discriminants directly for the dimension-two possible exponents from the source paper. The maximal tested height is 65; this is a finite consistency test, not an exhaustive infinite certificate.

Run command: `python3 verify.py`

Observed result: `PASS 64 height boxes (H=2..65), independent integral matrix-power criterion; exact counts and expansion denominators`. The check uses arbitrary-precision integer arithmetic, including exact square-root tests; there is no numerical root-tolerance requirement. The general proof uses strict inequalities at the eigenvalue-unit-circle boundary and handles the excluded double-root companion case explicitly.

Independent audit has not been performed.
