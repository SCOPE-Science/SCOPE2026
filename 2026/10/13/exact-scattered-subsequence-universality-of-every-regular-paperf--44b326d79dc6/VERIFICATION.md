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

The standalone program `verify.py` was executed against its actual embedded-package source and returned:

```text
VERIFY_OK symbolic_end_transitions=8 symbolic_partial_transitions=64 block_identity_T=0..19999 direct_prefixes_1..524288 defining_subsequence_test_N=0..29 dyadic_levels_m=3..19 discrepancy_range=-8..1 all_10_discrepancies_seen=yes
```

The verification includes symbolic checks of all possible two-state block transitions, finite direct checks of the defining subsequence predicate, and longer direct greedy-prefix comparisons. These finite computations corroborate but do not replace the all-prefix induction given in `RESULT.md`. No external or independent audit was performed.
