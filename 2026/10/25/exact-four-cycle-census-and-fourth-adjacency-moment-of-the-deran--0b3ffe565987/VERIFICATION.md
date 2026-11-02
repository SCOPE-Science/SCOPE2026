---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS. For opposite corners of a simple four-cycle in the ambient transposition Cayley graph, their two-step difference is either a three-cycle or a product of disjoint transpositions. The first forms a K_(3,3) parity-coset on a unique set of three positions; retaining derangements yields precisely 9 squares when zero positions intersect the image set, 1 when one intersects, and none when at least two intersect. The outside partial permutation count is the explicitly specified diagonal-avoidance B0/B1. Two commuting disjoint transpositions produce a unique square on four positions; all four corners avoid the diagonal exactly when the matching permutation avoids a pair of 2x2 forbidden rook boards with polynomial (1+4x+2x²)²(1+x)^(n-4). Each such square has four possible starting corners, establishing the factor 1/4. The degree identity deg(pi)=binom(n,2)-n+c2(pi), exact one- and two-selected 2-cycle sums and elementary closed-four-walk partition prove the fourth moment. Independent code reconstructed the graph directly and computed all square types and tr(A^4) for n=4,5,6; results (Q3,Q4,trA4)=(0,3,144),(60,60,3360),(1800,1305,70560) agree. Finite enumeration is corroboration, not the proof for n>6.

## originality

PASS

PASS, best-of-knowledge with known state graph and degree/bypass results excluded. A transposition Cayley subgraph of derangements is mathematically identical to the crown-graph perfect-matching switch graph; Jain already studied this precise alpha(n), including degree and local alternative routes, but its stated theorems do not supply the complete two-class 4-cycle census or tr(A^4). General perfect-matching switch-chain and Gray-code papers are broader algorithmically, not exact square counts. No retrieved published finding matched the asserted two-support formula. A hidden exact rook-board count or rephrased count of alternating length-eight matching transformations could cover it.

## value

PASS

PASS. The minimum nonbacktracking cycle structure is a natural invariant of the switch-state graph governing local ambiguity of two matching switches; the three-position and commuting four-position contributions distinguish two mechanisms. The exact fourth adjacency moment is a natural spectral statistic derived from a complete infinite-family census, not a single artificial finite example, and provides a natural baseline for subsequent walk/spectral studies. No mixing-time or full spectrum improvement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
