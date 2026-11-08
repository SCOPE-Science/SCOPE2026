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

## Verification scope

The executable `checker.py` uses Python standard library only. Run `python3 checker.py` to obtain the exact status `NESTED_S5_EXACT_CHECKS_OK 3873`.

It checks every deterministic effective-set cardinality and exact Bell-Stirling factorial-moment formula on carriers of one through five vertices. It also checks, for every pair of equivalence partitions and all truth assignments through four vertices, that the global nested possibility formula is true exactly when no first-agent class is contained entirely in the second-agent unmarked closure.

The analytic results rely on Stam's exact urn distribution, its literature-supported concentration, the computed conditional indicator covariance and the factorial-moment limits. These steps are given in `RESULT.md`; finite enumeration alone cannot establish them. No independent validation or historical-priority certification was performed.
