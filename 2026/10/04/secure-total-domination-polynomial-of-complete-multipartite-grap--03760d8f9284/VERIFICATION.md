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

The proof uses only the adjacency structure of a complete multipartite graph. The critical reduction is that a set is total dominating exactly when at least two partite sets are occupied. Secure replacement is then checked by support size: support at least three is automatically stable under one defender swap, while support exactly two has precisely the two one-defender obstructions stated in the theorem.

The standalone script `artifacts/verify_secure_total_multipartite.py` reconstructs the graph from its part sizes and checks the secure-total-domination definition directly. It separately implements the structural criterion and the closed coefficient formula. Exhaustive replay over all ordered part-size profiles with two through five parts, each size at most four, and total order at most nine produced:

`VERIFY_OK graph_types=297 subset_checks=87788 coefficient_checks=2589 max_order=9`

The computation is not used as an infinite proof. It checks boundary cases including complete graphs, stars, complete bipartite graphs, multiple singleton parts, and pairs of non-singleton parts. No claim is made for a different notion sometimes called total secure domination in which the post-swap set need only dominate rather than totally dominate.
