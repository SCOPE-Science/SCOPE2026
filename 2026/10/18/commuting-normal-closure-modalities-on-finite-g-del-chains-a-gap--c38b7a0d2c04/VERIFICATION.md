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

The accompanying `checker.py` generates all endpoint-containing fixed-point sets and all ordered pairs for each integer from 2 through 9. For each pair, it compares direct composition of the upper-rounding tables against the stated common-gap exclusion criterion and checks the count against an independent composition enumeration. The observed counts are 1, 4, 14, 48, 164, 560, 1912, 6528, and the final expected marker is `TWO_S4_CHAIN_COMMUTATION_OK`.

The deductive proof in `RESULT.md` establishes the result for every finite chain size at least two; the finite checker alone does not prove the unbounded quantifier. Existing literature already provides the same integer sequence with other interpretations. Historical priority for the particular paired operator interpretation and characterization is not independently established.
