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
# Computational verification

Run `python3 verify.py` in the directory containing this document. The checker enumerates all idempotent maps on finite labeled sets and independently derives each trivariate rank coefficient using a separate multinomial partition of root attachments. All rank triples match for dimensions 1 through 5. For dimension 6, it checks all ordered pairs from 1057 idempotents and compares the exact total 113989. A third rooted-component recurrence computes the totals through dimension 11. Successful output ends with `CHECKER_OK`.

The all-dimension theorem is proved by the bijective argument in RESULT.md, not inferred from these finite tests. No independent mathematical audit was performed.
