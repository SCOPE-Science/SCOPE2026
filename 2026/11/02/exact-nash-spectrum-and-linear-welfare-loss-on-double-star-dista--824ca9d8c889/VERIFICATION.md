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

# Verification of the exact double-star Nash spectrum

The finite checker `verify_double_star.py` constructs each labeled double star from its edge list, enumerates all unordered set partitions by recursion, computes each player's utility from BFS distances inside their current induced subgraph, and checks all unilateral deviations to an existing coalition and to a singleton. It independently derives the global maximum and complete multiset of Nash-equilibrium welfare values, then compares these quantities with the theorem's formulas.

Invoke `python3 verify_double_star.py`. All \(15\) pairs with \(1\le a,b\le4\) and \(a+b\le7\), plus \((4,4),(1,6),(2,5)\), passed. In total there were **217,219** exhaustive labeled partitions. The balanced \((4,4)\) case contributes 115,975 partitions. This is a bounded finite check, not a proof for all positive integers.

The general proof is in `RESULT.md`. Its critical exact identities are \(u_{\mathrm{left\ leaf}}=1-q\), \(u_{\mathrm{right\ leaf}}=1-p\), and \(W(p,q)=2(1+p+q-pq)\); every possible connected coalition configuration is covered by separating or joining the hubs. No external independent scientific audit has been performed.
