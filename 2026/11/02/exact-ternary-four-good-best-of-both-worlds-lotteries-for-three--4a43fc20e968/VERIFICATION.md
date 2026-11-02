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

# Verification protocol

Run `python3 verify_ternary.py ternary_lottery_witnesses.json` in a directory containing both supplied files. Python 3 standard library is sufficient. The checker evaluates all 5,053 rational lottery certificates, all six expected envy inequalities, ex-post EFX checks, and Pareto nondomination against 81 possible allocations; it also proves coverage of all 531,441 labeled profiles by exact orbit counting.

Observed output:

```
VERIFY_OK canonical=5053 labeled=531441 all_three_level=392 any_three_level=3767 max_support=4 support_hist={1: 1123, 2: 2091, 3: 1772, 4: 67}
```

All arithmetic in the acceptance checker uses integers and exact fractions. The proof is finite and exhaustive for the stated domain only. The sources establish contextual prior work but do not independently validate the certificates. No independent audit has been performed.
