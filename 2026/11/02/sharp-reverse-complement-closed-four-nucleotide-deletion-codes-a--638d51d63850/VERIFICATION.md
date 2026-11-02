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

# Computational verification and scope

From a directory containing `verify.py`, `optimal_rc24.tsv`, and `optimal_rc22_no_self.tsv`, run `python3 verify.py`. The script uses only Python 3 standard-library modules. The verified output is:

```
VERIFY_OK
eligible_orbits=136; fixed=16; pairs=120; deletion_outputs=64
strand_closed_max=24; max_search_nodes=104470; optimizer_count=160; count_search_nodes=214187
fixed_word_distribution=2:4,4:44,6:76,8:36; symmetry_classes=28
no_self_max=22; max_search_nodes=4848; optimizer_count=44; count_search_nodes=19219
```

The run rebuilds deletion masks and each involution orbit from definitions; separately checks both explicit inventory tables, direct deletion shadows and closure, complete weighted clique upper bounds, equality counts and the eight-symmetry-orbit decomposition. The upper-bound pruning is justified in `RESULT.md`, rather than being inferred merely from a successful test output. This exhaustive finite proof applies only to four-letter source words, not to arbitrary blocklength. Historical priority and independent external mathematical checking remain unperformed.
