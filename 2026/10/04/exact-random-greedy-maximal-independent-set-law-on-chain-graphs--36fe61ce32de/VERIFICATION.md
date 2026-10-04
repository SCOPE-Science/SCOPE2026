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
# Checks performed
The proof was reconstructed from the canonical Ferrers ordering. The maximal-independent-set support was checked directly from neighborhood inclusion. The random-greedy output criterion for a fixed maximal independent set was checked in both directions, after which the two blocking subsystems were verified to use disjoint vertex-priority sets. The first-active-vertex recurrence for \(\Phi\) was then derived by conditioning on the earliest active vertex and deleting the blocked Ferrers prefix.

The standalone script `artifacts/verify_chain_rgmIS.py` was executed from the package path. It enumerates every connected canonical chain degree sequence with total order at most eight, exhaustively enumerates every vertex permutation, computes greedy directly, and compares the complete exact-rational output law against the theorem. It also checks support equality and normalization. The observed output was `VERIFY_OK degree_sequences=127 permutations=2754350 support_points=383 max_total=8`.

# Limits
The exhaustive finite computation checks boundary cases, support classification on small graphs, and rational arithmetic; it is not the proof of the general theorem. The infinite statement follows from the structural classification, disjoint-block factorization, and exact recurrence. Literature comparison was targeted rather than exhaustive across every historical alias of chain/Ferrers/difference graphs. No independent external audit has been performed.
