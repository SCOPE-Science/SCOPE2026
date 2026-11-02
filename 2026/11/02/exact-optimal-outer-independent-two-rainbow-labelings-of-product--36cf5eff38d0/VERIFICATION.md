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

# Reproducible checks

Run the included `check.py` with Python 3.10 or newer. The code uses only the standard library and constructs the categorical-product adjacency relation directly; its tests do not import the claimed formulas as a feasibility oracle.

An execution of `python3 check.py` completed with output:

```
VERIFY_OK: 4 complete four-symbol enumerations; 16 independent matrix enumerations; 179 large-parameter witnesses
```

The four complete label enumerations cover \((m,n)=(2,2),(2,3),(2,4),(3,3)\), including the exceptional values. The sixteen matrix enumerations apply the rainbow condition to graph neighbor sets for every two-color assignment after choosing a maximum empty fiber in additional small instances. The 179 constructions verify existence for larger pairs. Critical symbolic steps (fiber rigidity, the weight identity, the equivalence with two-column support, inclusion-exclusion, and the small-exception counts) are detailed in `RESULT.md` and do not depend on the finite tests. No independent audit is asserted.
