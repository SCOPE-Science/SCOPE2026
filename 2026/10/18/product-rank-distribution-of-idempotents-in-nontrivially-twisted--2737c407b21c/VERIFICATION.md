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

The proof supplies a complete factorization of every idempotent in the relevant two-sided annihilator algebra into a projected core and radical lift. It identifies the rank of a two-idempotent product as the rank of the product of their core projections, then counts all relevant image/kernel intersections using the Gaussian subspace formula. The resulting rank-triplet coefficient is valid for arbitrary field order, dimension, defining matrix, and nonzero nonidentity twist.

Execute `python3 verify_product_ranks.py`. The self-contained script uses exact arithmetic for prime fields and \(\mathbb F_4\); it enumerates all candidate matrices and directly checks the defining equations for 24 complete small ambient field/twist cases, then compares every product-rank coefficient. It separately checks the entire \((q,t,s)=(3,2,1)\) sandwich algebra, exhaustively enumerating its \(3^9=19683\) matrices and \(36100\) idempotent-pair products. All tests finish with `ALL_EXACT_CHECKS_PASSED: 24 ambient field-twist cases, plus full Munn case`.

The finite checks do not establish the infinite theorem or global novelty, and no independent mathematical audit has been performed.
