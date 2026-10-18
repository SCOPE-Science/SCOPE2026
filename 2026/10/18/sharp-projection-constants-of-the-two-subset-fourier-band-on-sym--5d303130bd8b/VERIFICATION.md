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

# Reproducibility

Run `python checker.py` from the same directory. The script uses only Python standard library modules. It counts permutation fixed points and two-cycles exactly for every permutation at five consecutive group sizes and compares the exact rational mean absolute character kernel against the closed formula. It also checks the zero/negative strata and the recurrence estimates at additional finite sizes. It does not validate all dimensions by enumeration; an independent mathematical audit has not been performed.
