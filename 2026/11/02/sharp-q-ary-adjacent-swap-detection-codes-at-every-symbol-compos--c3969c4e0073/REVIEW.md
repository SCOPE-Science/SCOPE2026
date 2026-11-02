# Review of the adjacent-swap detection theorem

**Correctness — PASS.** A swap of unequal neighbours reverses inversion parity. Swapping the first unequal disjoint position-pair gives a disjoint-edge matching covering every word except doubled-pair words, which all have even parity. Matching bounds and parity independence coincide in every composition class. Combinatorial counts of unmatched words establish both exact formulas. Direct literal adjacency and maximum-matching computations reproduced the formulas for 22 finite parameter cases (6,689 vertices and 309 composition profiles); the symbolic matching argument, not the experiment, proves the infinite theorem.

**Originality — PASS with limitations.** This claim expressly excludes the known binary fixed-weight theorem of de Alba et al. (arXiv:1606.06370, Corollary 3.11), and addresses the different multi-symbol, fixed-composition graph. Adamson et al. study unrestricted-position swaps, while Wang et al. study correction with deletions. The 1998 Abdel-Ghaffar paper requires substitution detection too. Neither these sources nor the targeted mathematical records located the all-\(q\) detection optimum or complete composition formula. A possible equivalent general matching result or an unindexed equivalent remains the main risk.

**Value — PASS.** The graph is the natural confusability graph for detecting one adjacent swap, and maximum code cardinality is its fundamental exact coding invariant. The fixed-composition theorem handles prescribed symbol frequencies, a natural constraint in word coding and multiset permutation graphs. The result gives both an explicit optimal construction and a matching upper certificate for every alphabet and every composition, with the parity boundary for odd multiplicities made exact; this is not a finite census or a restated binary result.

**Limitations.** No uniqueness of optimal codebooks or one-swap correction is claimed; finite tests cannot certify all parameters. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
