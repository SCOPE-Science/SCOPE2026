# Review of one-spare-color forcing on complete multipartite graphs

## Correctness — PASS
The partition of terminal proper colorings by the use of \(r\) or \(r+1\) colors is exhaustive. A monochromatic terminal coloring cannot acquire any new colored vertices, since every blank sees at most \(r-1\) colors. A split terminal coloring has a unique split part, and it must be fully seeded since every vertex there sees only \(r-1\) external colors. The necessity of at most one other blank part and a constructive sufficiency argument give the claimed bijection. Color choices, seed subsets and the probability normalization are counted with disjoint cases. Exact exhaustive checks on 34 small profiles, totaling 9,213,533 initial states, agreed with the symbolic counts. Only the written argument establishes all parameter values.

## Originality — PASS, with residual literature risk
Farr (2026, arXiv:2609.17108v1) defines the invariant and gives its fundamental properties, selected three-color examples, and the low-palette bipartite treatment; the inspected material does not state the new arbitrary-profile, at-least-three-part, one-spare-color formula. Known bipartite palette-three results and arbitrary-palette results in the two-part case do not imply this theorem because it assumes at least three partite sets. The exact chromatic-palette multipartite case also has a different structural regime. The maximum-degree-two published classification does not dominate the new result. Other multicolor forcing definitions are not equivalent. The strongest residual risk is an equivalent theorem in uninspected or unindexed literature; the full motivating paper was only partially examined.

## Value — PASS
The first palette above the chromatic number is a natural structural threshold for forced coloring. Complete multipartite graphs expose a nontrivial all-or-nothing phenomenon: the only non-total successful seeds require one fully initialized two-color part, while at most one other part remains entirely blank. A complete exact size distribution, the resulting probability polynomial, and the exact minimum-seed count hold for an infinite family with arbitrarily many parts and orders. This contributes an explicit benchmark to a new graph-polynomial invariant, without a claim about other palettes or graph classes.

Self-review: passed. Independent audit: not yet performed.
