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

Execute `python3 VERIFY.py` using Python 3 and its standard library. The checker provides an exact-integer recursive optimizer with an interval-heap implementation, reconstructs selected proxy actions, and independently enumerates all possible time-stamped directed approval choices (including wrong-way choices) for small inputs. It verifies feasibility, rootedness, parent-action trust-horizon inequalities and objective equality.

A deterministic random seed generates 3,900 exact small-instance comparisons, with 2,510 feasible cases. Instances range over \(2\leq n\leq6\), \(2\leq L\leq4\), heterogeneous arbitrary trust horizon entries and variable positive integer welfare weights. The fixed four-voter all-final-round-approval obstruction passes its separate feasibility checks. The reproduced output is:

```
PASS: minimal four-voter obstruction; 3900 independent exact-enumeration tests, 2510 feasible
```

The proof is analytic; this finite verification does not certify behavior for unbounded numbers of voters or rounds. The implementation's exact maximum over integer scores uses no floating-point approximations. The general bound is an operation count for integer-word arithmetic. Full prior-literature completeness and independent mathematical validation are not established.
