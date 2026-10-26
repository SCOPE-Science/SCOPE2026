# Scientific review: three-clique fair-coalition partitions

**Correctness — PASS.** The elementary component-occupancy lemma shows that each 1-fair dominating set with at most four selected vertices is a size-three transversal. The excess argument excludes partitions with fewer than three merged vertices; the three-doubleton construction attains the bound; a full excess-three block-size analysis gives the optimizer types. Direct adjacency-based enumeration reproduces the counts, including the exceptional three-clique cases. The proof applies to every three-component profile of integers at least three; finite experiments are not presented as an infinite proof.

**Originality — PASS (self-review, residual risk).** The founding paper [1] supplies the definition and a general upper bound, but treats paths, cycles and small cubic graphs, not the exact three-clique enumeration. The later \(k\)-fair paper [2] and ordinary \(k\)-coalition paper [3] examine different parameter ranges or domination conditions. No matching exact statement or stronger implying statement was identified through the consulted research-record searches. This does not prove global novelty; an unindexed equivalent under cluster-graph, 1-fair domatic or transversal-coalition terminology remains possible.

**Value — PASS.** The first nontrivial three-component cluster family exhibits a sharp, component-size-independent three-block deficit from the all-singleton partition. Classifying all equality partitions and giving the exact labelled-vertex enumerator makes the result structurally more informative than a scalar graph invariant. The size-three exceptions contribute two additional, explicitly counted combinatorial patterns, while every component size at least four forces a unique pair-type pattern.

**Limitations.** The result concerns three cliques of sizes at least three, does not count coalition-partner choices, and has not undergone independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.

## Closest literature

[1] S. Alikhani, A. Jafari and M. Safazadeh, *Fair coalition in graphs*, arXiv:2507.15080 (initial release 20 July 2025).

[2] A. Jafari and S. Alikhani, *\(k\)-Fair Coalitions in Graphs*, arXiv:2509.11358.

[3] C. Kaneshiro, *On \(k\)-coalition partitions of graphs*, arXiv:2608.05403.
