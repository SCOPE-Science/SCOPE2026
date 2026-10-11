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

The standalone verification file `verify_representation.py` enumerates every acyclic parent assignment fixed by each representative conjugacy class, for both bipartition-swap statuses, for each integer \(3\le n\le7\). Each assignment is checked to be equivariant and acyclic directly, without invoking the orbit formula being tested. Signed edge-orbit counts produce Lefschetz traces and match the closed formulas and the two rational-module character formulas in all 82 tests. The run completed:

```
checked_range=3..7
conjugacy_class_swapped_cases= 82
invariant_forest_total= 102580
character_criterion=direct_lefschetz_equals_closed_formula_equals_module
VERIFY_OK
```

Exact command: `python3 verify_representation.py` (Python standard library only). The unconditional equivariant Euler-character proof handles all integers \(n\ge3\); these finite calculations provide independent numerical checks and cannot establish the all-parameter assertion or the separately reported nonequivariant wedge theorem; actual homology-module identification is conditional on that input. Other integral-module and equivariant homotopy invariants are not computed.
