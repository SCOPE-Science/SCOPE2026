# Scientific review

## Correctness

PASS. Deletion-ball intersections reduce exactly to rooted suffix-tree parent–child edges and common-parent sibling cliques. Each terminal-letter component is partitioned into one four-element clique and six parent–child pairs, proving the upper bound seven. Equality enforces one choice per group. The two exhaustive cases for the short clique yield the local polynomial \(P\), and disjoint terminal-symbol components produce \(P^4\). The minimum and maximum total lengths follow from the extreme nonnegative coefficients of the explicitly computed polynomial. A complete independent search of all \(2^{16}\) local subsets confirms every local coefficient; the proof supplies the global implication.

## Originality

PASS on accessible evidence, subject to a concrete residual risk. The source paper of Cohen, Yaakobi, and Yakhini (2026), especially its Theorem 6, establishes the optimum cardinality but not the count or length-composition distribution of *all* maxima. The 2025 rank-modulation paper studies another error model. Related published results on maximum fixed-length deletion codes address different channel outputs, not nonrepeating variable-length suffix-tree codewords. Equivalent enumeration via classical rooted-tree packings could be unindexed; no uniqueness certification is claimed.

## Value

PASS. A complete classification of optimum codebooks is natural for the quaternary alphabet used for nucleotide rankings. The cardinality optimum alone gives no information about design diversity or the word-length budget. Here exactly \(4{,}096\) maximum codebooks attain the sharp total ranking length \(88\), a combinatorial decrease of 16 positions compared with an exhibited full-length-heavy optimal construction. The polynomial gives all intermediate tradeoffs without assigning unmeasured synthesis costs.

## Scope and remaining risk

No claims are made about arbitrary-position deletions, stochastic channels, optimal physical synthesis cost, or fixed-length codewords. A possible equivalent formulation in unindexed graph-packing literature remains open to human literature review.

Self-review: passed. Independent audit: not yet performed.
