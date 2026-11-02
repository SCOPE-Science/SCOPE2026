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

# Verification

Execute `python3 alternating_complement_verify.py` using Python 3 with no dependencies. The tested standalone file produces `ALTERNATING_COMPLEMENTS_VERIFY_OK 78 parameter pairs, n<=11`.

The checker recursively enumerates all embeddings by retain/delete decisions; independently generates all block-type words with at most the prescribed number of reversed-block runs; compares exact residual sets for 78 pairs with total source length up to 22; and checks the binomial-run and binomial-tail formulas. The symbolic proof in RESULT.md, not finite enumeration, establishes the result for every nonnegative parameter pair. No independent external audit was performed.
