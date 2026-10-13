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

The accompanying `verify.py` is a standalone Python 3 standard-library program. Run `python3 verify.py` from the directory containing the packaged files.

Observed successful execution:

```text
VERIFY_OK direct_term_closures 11189 census_parameter_cases 36 rank_boundary_checks 693
```

The checker exhaustively enumerates the specified small ordered generator tuples, builds their finite term closure under conjunction, disjunction, and Heyting implication, and compares it to the independently evaluated positivity/local-level condition. It separately counts successful tuples and checks the coefficient formula in 36 parameter cases. Rank thresholds are independently checked for 693 combinations of chain size and coordinate count. This finite testing does not prove the theorem for all parameters and does not verify the asymptotic collision law, which is proved mathematically in RESULT.md.

No independent audit or external certification is asserted.
