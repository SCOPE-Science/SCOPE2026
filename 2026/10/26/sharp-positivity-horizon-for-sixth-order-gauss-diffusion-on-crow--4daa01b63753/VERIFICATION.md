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
Execute `python3 crown_verify.py` with Python 3 standard library only. The script uses exact formal integer polynomial arithmetic in two variables to clear the three positive rational denominators and to certify every coefficient of the three off-diagonal expressions is strictly positive. The exact asserted coefficient counts are 40, 32 and 48; the powers of time start at 2, 3 and 1, respectively. It also performs 36 independent full rational-matrix evaluations and entrywise comparisons on graph orders from 6 through 16.

## Logical limits
The polynomial identity is an exact finite certificate for all \(u=n-2\ge1\) and \(h>0\); the coefficient-sign implication and derivative/limit proof are mathematical arguments external to finite tests. The numerical horizon examples only illustrate the exact unique-root theorem, and no floating-point root is used to justify it. No independent audit or external certification has been performed.
