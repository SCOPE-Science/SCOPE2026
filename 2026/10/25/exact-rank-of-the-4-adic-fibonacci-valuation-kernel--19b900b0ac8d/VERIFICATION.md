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

The proof is symbolic. It derives every 4-kernel subsequence from the valuation formula, proves the five-generator spanning statement for all depths, and proves independence by exact evaluation at five indices.

The included `verify.py` uses exact integer Fibonacci values through index 10,000 and checks all 4-kernel offsets for depths 1–6 on a finite index range, plus the displayed generator identities and independence witnesses. Its output is `RANK5_FORMULA_OK`; finite checks do not establish the infinite statement.

No independent audit or independent validation is claimed.
