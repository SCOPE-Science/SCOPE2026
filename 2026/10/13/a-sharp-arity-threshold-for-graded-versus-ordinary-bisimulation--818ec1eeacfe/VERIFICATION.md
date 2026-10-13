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

# Standalone verification of the finite signatures and sharp-threshold witnesses

Run `python3 verify.py` with Python 3 and its standard library. No external datasets or packages are required. The executable independently builds complete fixed-arity trees, enumerates vertex colorings, computes ordinary versus counting partitions by bottom-up semantic signatures, and periodically checks each with separate global fixed-point partition refinement. It also recursively constructs legal restricted-family graded types and places pairwise different ones at a prescribed tree level.

Successful replay output terminates with:

`VERIFY_OK exhaustive_colorings 41116 parameter_cases 7 independent_partition_comparisons 648 structured_witnesses 14 growth_threshold_checks 9`

The exhaustive cases comprise binary heights 0,1,2,3 (2, 8, 128, and 32,768 colorings) and ternary heights 0,1,2 (2, 16, and 8,192 colorings). They verify no discrepancy in any binary case and find 2,808 discrepant colorings in the ternary height-two case, none with fewer than four ordinary classes. The 14 explicit witnesses cover ternary heights 3–9, quaternary heights 3–6, and five-ary heights 3–5; each has exactly height-plus-two ordinary classes and the prescribed number of distinct graded types at a middle level. Nine further finite-arity inequalities verify that the type-recurrence growth argument starts above its fixed point.

Finite exhaustive enumeration proves those **finite** cases only. The theorem's asymptotic estimates rely on the analytic recurrences, the disjoint-subtree construction, and the level-sum bound given in `RESULT.md`. No independent mathematical or external certification is claimed.
