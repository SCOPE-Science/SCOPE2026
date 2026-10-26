# Research review: Petersen spanning-tree pivot geometry

## Correctness — PASS

The objects and moves are explicitly defined as 9-edge subsets of \(KG(5,2)\) and incident-edge exchanges preserving the spanning-tree property. The count of 2,000 trees has independent exact support from the Laplacian cofactor and from disjoint-set enumeration. For each missing edge, its fundamental cycle admits exactly two endpoint pivots, yielding degree 12. The standalone program checks its independent exchange-neighbor and fundamental-path constructions against each other for every state, exhaustively performs 2,000 breadth-first searches, and cross-checks the histograms by an automorphism-orbit-weighted second enumeration. The extremal 150 pairs and their two orbits are directly enumerated. Exact integer computations have been run to completion with `VERIFY_OK`. Finite exhaustive computation proves the finite claim, not any unasserted infinite-family statement.

## Originality — PASS (best knowledge, with residual risk)

The relevant archive-era anchor is Knuth's 2011 combinatorial-generation treatment, which later pivot-exchange papers explicitly cite. The inspected full-text 2021 fan-graph pivot-Gray-code paper and 2025 outerplanar pivot-exchange paper do not treat the Petersen graph or supply a distance census for its spanning trees. The known exact count of 2,000 trees, ordinary basis-exchange connectivity, and the endpoint-pivot degree count are not claimed as original. Targeted published-finding corpus queries, literature searches, aliases (pivot, rotation, edge exchange, Gray code), and numerical/table lookups did not find the asserted 8-diameter or 150 extreme-overhead pairs. A negative search does not establish uniqueness: a nonindexed earlier computation remains the primary risk.

## Value — PASS

Pivot exchanges require the two changed edges to share a vertex, unlike general graphic-matroid basis exchange. Sharp distances for this stricter local reconfiguration are natural quantities connected with Gray-code generation and short transformation sequences. On a canonical nonplanar cubic graph, the exact diameter \(8\) is larger than the unrestricted exchange diameter bound of \(6\); the four-move maximum detour is localized to only 150 pairs, with a nontrivial two-orbit splitting on 60 distinguished trees. The complete pair-distance and detour tables are a meaningful, reusable benchmark rather than an arbitrary slice or routine recounting of spanning trees.

## Closest literature and limitations

Knuth, *The Art of Computer Programming* Vol. 4A (2011), Section 7.2.1.6; Cameron–Grubb–Sawada, arXiv:2108.09363 (2021), inspected in full HTML; Behrooznia–Mütze, STACS 2025, doi:10.4230/LIPIcs.STACS.2025.16, inspected in full HTML. Their results concern broader combinatorial generation or different graph families and do not imply this numerical shortest-pivot metric. Computational claims are exact for this graph only. Residual risk: unindexed prior computations; no independently performed audit.

Self-review: passed. Independent audit: not yet performed.
