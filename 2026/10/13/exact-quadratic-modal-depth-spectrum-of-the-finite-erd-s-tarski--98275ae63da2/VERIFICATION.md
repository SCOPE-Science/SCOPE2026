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

## Executed program

Run the embedded, standalone Python 3 standard-library script with `python3 VERIFIER.py`. The script was executed from the files included in this record, and returned:

```
VERIFY_OK staircase_sizes=59 modal_depth_levels=1829 row_column_selector_sizes=30 direct_boolean_unions=1100 Boolean_modal_algebra_cases=3
```

## Checks

The first check constructs successive depth-bounded modal partitions directly from the propositional truth value and the sets of predecessor-type labels accessible along the two row/column equivalence relations. It compares all intermediate modal class counts to the closed formula and, more strongly, verifies the exact claimed row and column signature groupings at every level for all square sizes \(2\le n\le60\) (1,829 depth levels altogether). The second check directly evaluates the recursive formulas selecting initial row and column segments, including all singleton intersections, on square sizes \(1\le n\le30\).

The third check does not use modal bisimulation partitions. For each \(n=2,3,4\), it enumerates every Boolean union of currently definable atoms, evaluates both modal box operations as set operations, and takes the Boolean atoms of all resulting sets. The resulting depth-wise counts independently reproduce the theorem. The third check considers 1,100 Boolean-union inputs across its three cases. All assertions passed.

## Scope and limitations

These are exhaustive tests only for the explicitly enumerated finite ranges. No computation can establish the statement for every \(n\). The unbounded proof is the alternating-peeling induction in `RESULT.md`. No externally performed mathematical audit or formal proof-assistant certificate is asserted.
