# Self-review

## Correctness — PASS

The finding is a precise statement about **all** maximum failed standard zero forcing sets in every labeled rook graph with two dimensions at least two. The maximum/fort equivalence is proved by forcing closure, not assumed. At a blue cell, the exact count of white neighbors is the sum of its row and column occupancies; the four exhaustive occupancy regimes prove both the minimum size and the classification of every minimum fort. Their disjoint counting yields all exceptional multiplicities. The thin-board orbit enumeration uses a complete invariant, the intersection size of two row supports. A native-graph verifier independently checks 20 dimension pairs (360,898 candidate subsets of sizes at most four) and forcing closures in eight of them, without being needed for the infinite argument.

## Originality — PASS, with residual risks

Fetcie–Jacob–Saavedra (2015), Theorem 4.3, already gives the scalar failed zero forcing number for rook graphs with a factor of order at least four; this work does not claim that scalar as new. Abara–Pelayo (2022), Section 3.1, recalls the known value, rather than enumerating all extremal sets. Cameron et al. (2023) establish general fort-hypergraph and Cartesian-product statements. Becker et al. (2024), Sections 2 and 5, count minimal forts of other graph families and give generic join, corona and vertex-sum constructions, not a complete minimum-fort census of Cartesian products of cliques. Alternative names, the line-graph form \(L(K_{m,n})\), and the thin-board complement-of-crown form were included in the comparison. No prior exact all-orders extremizer count or orbit theorem was identified. This is evidence of original content, not proof of worldwide priority.

The closest additional prior result concerns the **largest inclusion-minimal** rook-graph fort, an opposite cardinality extremum. It does not imply the count of **smallest** forts. Other relevant results classify forts of complete multipartite graphs, a different graph family. An unindexed equivalence or a stronger theorem whose consequences were not recognized remains a genuine residual risk.

## Mathematical value — PASS

Counting the configurations attaining a known failed zero forcing maximum is a natural nontrivial refinement: a single construction does not imply how many maximum failed sets exist. Here the full classification exposes three types of thin two-row extremizers, special new configurations in three small rectangles, and a rigid single rectangle orbit for all boards with at least three rows and at least five columns. It determines the minimum cardinality stratum of the fort hypergraph exactly, an object independently motivated by zero forcing and fort-cover formulations. The value rests on the structural phase change and exact multiplicities rather than the known scalar upper bound, routine relabeling or a small numerical improvement.

## Scope and limits

The theorem applies only to standard zero forcing on rook graphs; it counts minimum forts, not all inclusion-minimal forts, not skew/positive-semidefinite forts and not arbitrary graph products. Direct enumeration is finite and corroborative; the complete proof is combinatorial. Publication priority has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
