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

The proof uses the published canonical type-B set-partition bijection and a separately proved signed-block size/count refinement. The boundary and descent-index rules are explicit in RESULT.md.

The included Python 3 verifier was executed from these artifact bytes and returned `VERIFY_OK`. It exhaustively generates all Stirling permutations of orders 1 through 8 without imposing flattenedness during insertion, then checks the original flattened condition and every exact descent-set coefficient. It separately evaluates the binomial shape formula, reproduces the original source's run-count table through order 10, checks the indicated equal-run-length counts, and compares all order-8 descent profiles with an exact polynomial-time dynamic program.

Checks through finite order are corroboration and not an infinite proof. The general theorem rests on the full decomposition and exact local descent analysis. No independent audit has been performed; an independent priority review is also not claimed.
