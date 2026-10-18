# Scientific review — Italian domination polynomial on chain graphs

## Correctness — PASS

The scope is precisely connected bipartite chain graphs with at least two nonempty canonical twin-class pairs, with numeric labels in \(\{0,1,2\}\) and the standard Italian defense condition. Each assignment uniquely determines two zero frontiers: the first \(A\)-class with a zero and the last \(B\)-class with a zero. Because neighborhoods are nested and all labels are nonnegative, defense of all zeros on each side reduces *exactly* to a weight-at-least-two condition on one prefix or suffix of the other side. The class-polynomial products enforce zero-frontier membership, and deleting degree-zero and degree-one terms enforces the two conditions. These independent restrictions multiply, and disjoint frontier pairs add. There is no unverified infinite enumeration step. A standalone brute-force implementation reconstructed graph edges and checked 793620 assignments on 76 profiles, comparing 1143 frontier cells exactly. These tests supplement, not replace, the proof.

## Originality — PASS (qualified by access and priority limits)

The closest primary contribution by Shao and Zhao [1] addresses all-weight Italian domination on paths, trees and cycles, not a closed formula for non-complete-bipartite chain graphs. Padamutham and Palagiri [2] established the minimum Italian/Roman-\(\{2\}\) domination number for chain graphs, which does not determine the all-weight polynomial; the new expression refines that result. A published chain-graph Roman-domination polynomial [3] counts the stricter version requiring a two-labeled neighbor for each zero, so it cannot be read as the Italian polynomial. A published all-weight Roman-\(\{2\}\) polynomial for complete multipartite graphs [4] covers the \(p=1\) complete-bipartite boundary but does not provide the formula for \(p\ge2\). Das and Santra [5] give optimization algorithms for Roman-type domination on convex bipartite graphs, not these all-weight coefficients. Targeted record and literature searches found no implication covering the full formula. The full contents of every nearby document were not accessible; lack of a search hit is not a mathematical proof of priority.

## Value — PASS

The mathematical gap is the full coefficient distribution of Italian dominating functions on an entire natural nested-neighborhood graph class, beyond the already known minimum weight and beyond tree/cycle counting algorithms. The theorem gives an explicit \(p(p+1)\)-term product-and-truncation formula for every possible positive class-size vector and hence counts every weighted feasible defense plan without enumerating exponential numbers of labelings. The coefficient at weight four distinguishes two noncomplete chain graphs with equal bipartition sizes \((3,3)\) and the same minimum weight four (counts four versus six), showing that the new information is not a restatement of the previous extremal parameter. Arbitrary class sizes and cycles make this a meaningful infinite-family determination, not a hand-picked finite census.

## Sources, boundaries and residual risk

[1] Shao–Zhao, *Counting Weight-k Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, https://arxiv.org/abs/2610.00108 (abstract, introductory material and contribution summary inspected; deeper full text not inspected).

[2] Padamutham–Palagiri, *Complexity of Roman {2}-domination and the double Roman domination in graphs*, DOI:10.1016/j.akcej.2020.01.005 (abstract and indexed Section 4 / Theorem 7 material inspected; entire PDF unavailable).

[3] *Roman domination polynomial of chain graphs*, published published-finding corpus record `2026/10/4/SCOPE-roman-domination-polynomial-of-chain-graphs--e846e0fa619b` (indexed published summary inspected).

[4] *Weight enumerator of all Roman {2}-dominating functions on complete multipartite graphs*, published published-finding corpus record `2026/10/4/SCOPE-weight-enumerator-of-all-roman-2-dominating-functions-on-complet--4a62f97e627e` (indexed published summary inspected).

[5] Das–Santra, *Roman-Type Domination on Convex and Chordal Bipartite Graphs: Algorithms and Hardness*, arXiv:2607.15026 (abstract inspected; full content unavailable).

Residual risks are an earlier equivalent enumeration under Ferrers/chain-graph terminology or uninspected appendices in the compared literature. The theorem does not address general convex bipartite graphs, disconnected graphs or other domination variants. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
