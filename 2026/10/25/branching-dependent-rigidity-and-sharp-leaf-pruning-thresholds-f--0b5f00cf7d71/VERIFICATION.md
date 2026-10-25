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

# Verification

The complete proof appears in `RESULT.md`, using an exact three-state root boundary decomposition, an algebraic three-phase induction and an exact local exchange bijection.

Run `python3 verify.py` using Python 3 standard library. Actual run returned:

```text
VERIFY_OK full_dp_cases= 25 stable_leaf_prunings= 75 sharp_one_group_prunings= 25 brute_minimality_and_counts= 18 brute_optimum_set_classifications= 9
```

The code constructs labelled tree adjacencies, deletes terminal leaves, independently computes optimum sizes and counts from bottom-up rooted subtrees, and enumerates candidate subsets below and at optimum cardinality for the small cases, with nine explicit all-optimum-set classifications. Programmatic checks are finite, not proofs for unbounded branching or height. The stated infinite theorem is justified by its recurrence induction and bijection.

The 2026 binary special case and general-tree algorithm were taken from the original source. Neither an independent audit nor external formal certification has been performed.
