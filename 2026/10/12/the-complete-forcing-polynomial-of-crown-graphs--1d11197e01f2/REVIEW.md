# Scientific review

## Correctness — PASS

The theorem's complement criterion is proved in both directions. Every pair of arcs supported on disjoint index pairs is a frame of a nice four-cycle for \(n\ge4\); every directed three-cycle is a frame of a nice six-cycle for \(n\ge5\). Conversely, the elementary intersecting-pair classification reduces all complements to stars or triangles, whose possible matchings have at most two or three edges. The only potential four-cycle frames have missing diagonal cross-edges, and the only three-edge triangle frames are the two explicit directed cycles, which are non-nice when \(n=4\). On \(\operatorname{Cr}_3\) the graph is a single six-cycle. The resulting disjoint support types give the polynomial by exact inclusion–exclusion. The standard-library verifier checks every candidate complement through the *definition using ordered pairs of perfect matchings* at orders three, four, and five; it separately checks the support-based enumerator through order seven. Finite tests support, rather than replace, the symbolic proof.

## Originality — PASS, with stated access risk

He and Zhang (2023), DOI `10.1007/s10878-023-01078-7`, already treat the minimum complete forcing number of dense balanced bipartite graphs; this scalar value is not claimed as new. Their accessible abstract and first publisher-preview page state numerical results and constructions, but the remaining primary full text was unavailable, so any uninspected all-set classification is a residual risk. Ebrahimi, Nemayande and Tohidi (2024), arXiv:2409.17306v1, was examined in its full HTML text: it defines the nice-cycle equivalence and gives general numerical bounds rather than this exact cardinality enumerator. Searches for crown-graph complete-forcing distributions, perfect-matching frame avoidance, and directed-star/triangle formulations did not identify a stronger result. Related existing results on zero forcing and crown domination have different objects or vertex-state dynamics. Database absence alone is not treated as a proof of originality.

## Value — PASS

Complete forcing is a motivated edge-set invariant encoding simultaneous uniqueness of every perfect matching. Existing results for dense bipartite classes address the optimum but not the number or structure of all nonminimum choices. The full cardinality polynomial and exact if-and-only-if membership rule describe every one of those exponentially many candidate edge subsets. The boundary at order four, the directed-cycle correction at larger orders, and the extremal multiplicities are structural rather than mere numerical substitutions. This full distribution is useful for enumeration, probabilistic models of random edge subsets, and benchmarking matching-uniqueness algorithms.

## Limitations and relationship to literature

All formulas concern \(K_{n,n}-M\) with \(n\ge3\), and no corresponding claim is made about all dense bipartite graphs. The full text of the especially relevant 2023 He–Zhang paper was subscription restricted; overlap beyond its accessible abstract and preview remains possible. Computational replay covers finite orders, and there has been no independent external review.

Self-review: passed. Independent audit: not yet performed.
