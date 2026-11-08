---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For x∈A,y∈B the internal-pair potential W=within(A)/a+within(B)/b has ΔW equal to the sum of both agents’ cost reductions; therefore any strictly mutually improving swap increases W and terminates after at most binom(n,a)−1 swaps. A sorted-type gap decomposition gives contribution k−j²/a−(k−j)²/b at prefix k, individually maximized by j_k=floor(ak/n+1/2). The rounded sequence is a feasible 0–1 increment path and global W maximizer (equilibrium). Social cross cost is minimized by maximizing unweighted within-pair sum, whose prefix optimizer is j_k=clamp_{[max(0,k−b),min(a,k)]}(floor((a−b+2k)/4+1/2)), also a feasible path. Exact K2,5 seven-agent witness [0,0,0,0,1,3,4] has minimum cross cost 15 but minimum equilibrium cross cost 17, PoS17/15; independent brute all 21 pair allocations reproduced both and 9 labeled equilibria. Median star center minimizes cost and is equilibrium; triangle inequality gives sharp PoA≤n−1 for nonconstant profiles.

## originality

PASS

Bilo et al. IJCAI 2023 analyze exactly continuous absolute-distance Schelling swaps, but their FIP and price-of-stability-one theorems are for regular graphs; K_{a,b} with a≠b is irregular. Their inspected full text does not give these two explicit sorting-based optimization rules or irregular strict PoS witness. Best-knowledge PASS with possibility equivalent rearrangement theorem already known.

## value

PASS

Potential identity extends finite improvement to all complete bicliques despite unequal degrees, while explicit distinct O(nlog n) sorting constructions locate stable and welfare-optimal allocations. The exact 17/15 obstruction makes the equilibrium-efficiency boundary mathematically substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
