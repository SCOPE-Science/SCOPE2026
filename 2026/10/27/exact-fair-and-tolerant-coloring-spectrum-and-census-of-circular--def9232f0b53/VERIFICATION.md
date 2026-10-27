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
# Verification procedures

The proof requires two independent structural implications, proved in `RESULT.md`: with four colors, the two-step swap of the two column colors forces a genuine period four, and with three colors the missing-color recursion forces a three-step layer swap. The count uses distinct labels and proves the necessary and sufficient seed constraints.

The packaged `fat_prism_verifier.py` independently imposes local three-neighbor FAT constraints and uses backtracking over ordered color pairs, rather than the recursion from the proof. Running `python3 fat_prism_verifier.py` yields:

```
VERIFY_OK local_census_cases=36 prism_orders=3..20 two_color_constructions=98
```

The 36 instances are the exact three- and four-color enumerations for orders 3 through 20. The other 98 checks concern the two-color construction at orders 3 through 100. Finitely many computed examples do not prove the universal formulas, and verification is not an independent audit. The limiting status is self-review only.
