---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Every simple cycle of this block graph is exactly the union of two of its internally vertex-disjoint terminal paths. In a block with k negative and r-k positive path products there are k(r-k) negative cycles; ranks on its negative/positive paths are r-k/k respectively. For any negative cycle, a maximum-rank edge belongs to a minority path, or to either path when tied. A flip reduces d=min(k,r-k) by precisely 1, and decreases negative-cycle count by r-2d+1>=1. Different blocks are edge-disjoint, and a global lower bound on flips is sum d, so every legal trajectory is a shortest route to balance. The stochastic law follows by conditioning on the first updated negative cycle in a tied block: each negative/positive path pair is equally likely and each edge in that pair is a tie maximizer, giving E[len_negative/(len_negative+len_positive)]. Independently enumerated every path-parity class and all legal transitions for several 3-/4-path bundles; tested the exact tie law 134/315 for lengths (2,3,4,5), negative paths 1 and 3.

## originality

PASS

This is specifically a cycle-based extension using counts of all negative simple cycles, not the original triangle-based BED dynamics. Classical minimum balancing and block decomposition are prior mathematics. The additional all-tie-break geodesicity and length-sensitive stochastic endpoint law were not located as direct results; a 1978 primary paper remains inaccessible in full.

## value

PASS

The result gives an all-choice shortest-path guarantee for a well-defined simple-cycle best-edge rule on a nontrivial unbounded-cycle-rank class; arbitrary overlapping negative cycles make a general convergence analysis nontrivial. The strict energy decrement and path-length-sensitive final polarity quantify dynamics, beyond merely the minimum frustration index. The block structure and rule are motivated natural boundaries, not an unmotivated slice of arbitrary signings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
