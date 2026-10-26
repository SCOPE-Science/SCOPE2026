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

The provided standard-library-only program `verify_rank3.py` was executed with `--crosscheck`. It generated `rank3_manifest.csv` for all 255 nonzero vectors in \(\{0,1,2,3\}^4\) and reported:

```
canonical_profiles=255 rank3_theories=22 sharp_kernel_order=9
direct_EF_pairwise_inequivalence=231/231
direct_EF_selected_equivalence_tests=4/4
```

The rank-three invariant is implemented directly as iterated sets of atomic three-variable types, avoiding approximate hashes or floating-point arithmetic. The cross-check uses a separate memoized minimax recursion for the three-move Ehrenfeucht–Fraïssé game. Full correctness for arbitrarily large finite star forests also relies on the textual proof of component truncation; exhaustive enumeration of finite test graphs alone would not establish it. The script uses standard-library modules only. Independent validation has not been performed.
