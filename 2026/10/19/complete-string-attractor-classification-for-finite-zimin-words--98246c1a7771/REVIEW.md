# Self-review

## Correctness — PASS
The proof covers all \(n\ge1\), one-based positions, arbitrary finite factors, the unique maximum letter in each factor, and both boundaries of every centered neighborhood. Ruler positions give independent identical contexts around every copy of a letter. Hence the factor-recentering argument proves the attractor iff. Factor classes then yield the exact product polynomial and its smallest coefficient. All small orders and selected larger cases were checked by an independent brute-force occurrence-mask implementation; finite checking is corroborative only.

## Originality — PASS against inspected evidence
The related Zimin-word factor and ranked-matching methods of Głowinski–Rytter [1] are prior knowledge, as is the string-attractor definition and generic alphabet lower bound of Prezza [2]. The recent complete classification of attractors for Fibonacci, period-doubling, and Thue–Morse words [3] applies to different families, while [4] concerns infinite-word settings. Semantic research-record searches under Zimin/ABACABA, factor hypergraph transversals, all-symbol coverage, and the proposed triangular-power formula identified no matching Zimin attractor theorem. The same integer sequence occurs in other objects; numeric coincidence alone is not a coverage result. The principal residual risk is a previously noted maximum-letter recentering lemma already being presented somewhere as the exact factor-hitting-set characterization. See the attached structured comparisons for actual queries and material read.

## Mathematical value — PASS
The complete attractor family is not obtained from an alphabet lower bound alone. The iff statement computes all inclusion-minimal and all minimum-cardinality attractors, gives the entire cardinality distribution and demonstrates rapidly growing positional nonuniqueness in an important recursively compressed word family. The result is an exact all-order classification, not a small arbitrary census; no downstream compression theorem is asserted.

## Limits and closest literature
The alphabet grows with order, and the theorem does not cover binary encodings, cyclic occurrences, substituted Zimin patterns, or arbitrary prefixes. The strongest nearby papers are [1] on Zimin factor representation, [2] on string-attractor foundations, and [3] on exact smallest attractors for other morphic words. Some preceding factors may imply the statement by an unindexed reduction; a specialist literature review remains necessary. There is no independent scientific audit.

References: [1] arXiv:1307.1560; [2] arXiv:1709.05314; [3] arXiv:2602.16152; [4] arXiv:2403.13449.

Self-review: passed. Independent audit: not yet performed.
