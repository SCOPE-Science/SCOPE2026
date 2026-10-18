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

The four case arguments in RESULT.md prove the equivalences for arbitrary nonempty worlds and arbitrary real-valued valuations; finite computation is corroboration only.

`python3 verify.py` exhaustively checks 69,904 finite accessibility-row/atomic-valuation pairs with values from the four-element rational test grid. It also tests rational finite prefixes of the analytic infinite countervaluations.

Expected output:
```
FINITE_GODEL_ROW_ATTAINMENT_OK 69904
INFINITE_DECAYING_ROW_BOX_PATTERN_OK
NON_C0_ROW_DIAMOND_PATTERN_OK
GODEL_UNIFORM_WITNESSABILITY_CHECK_OK
```

No computational experiment can prove the universal finite-superlevel characterisation for arbitrary infinite sets. That conclusion uses the direct supremum argument and explicit countable countervaluations.
