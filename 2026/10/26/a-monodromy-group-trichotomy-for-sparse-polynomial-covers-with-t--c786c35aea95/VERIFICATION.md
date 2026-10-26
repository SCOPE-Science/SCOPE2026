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

The exact branch-cycle formulas and the full universal group proofs are in RESULT.md. The finite verifier from this package was run with SymPy; the result was:

`VERIFY_OK nonsymmetric_d=3..14 symmetric_k=2..9 exact_group_orders`

The script calculates exact permutation-group orders using Schreier--Sims, checks product cycle lengths and ramification cycle types in the signed family, and reports an assertion failure on any discrepancy. This computation does not establish the universal theorem. No independent audit or formal proof assistant verification has been performed.
