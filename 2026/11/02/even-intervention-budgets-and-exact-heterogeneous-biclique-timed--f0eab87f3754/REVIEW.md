# Self-review

## Correctness — PASS

The proof works with the same non-progressive timed-target intervention convention as the 2023 primary source. Bipartite natural updates separate into disjoint alternating vertex-time strands, each with identical optimal saturation cost by one-step shifting from an empty natural state. The global optimum is twice that cost because full adoption saturates both strands, and a full part automatically propagates full positivity to its opposite side with no further targeting. On a biclique, the natural successor cardinality is exactly the threshold cumulative count independently of the active vertices' identities; the weighted state graph is therefore both sound and complete. Every edge cost is a realizable minimum added intervention count. Dijkstra yields the optimum and predecessor arcs yield a constructive schedule. The uniform-threshold formula is proved by an upper construction and a first-natural-activation lower bound.

The bundled independent exhaustive full-state test compared every threshold multiset on bicliques of part sizes up to three (168 cases). A separate all-graph test checked 3860 small bipartite graph/threshold pairs for even optimum, and 3025 uniform biclique parameter combinations checked the formula. These support but do not establish infinite correctness; the included proof supplies that.

Risks/limits: the result does not cover asynchronous updates, nonbipartite graphs for the parity claim, or graphs other than bicliques for the efficient count compression. The all-graph computational test happens also to include isolated zero-threshold vertices, which is beyond the declared theorem.

## Originality — PASS, with residual priority uncertainty

The primary 2023 paper was inspected in its accessible full arXiv text and PDF, including definitions, Example 1, Theorems 2–3 and 8, the double-cover proof in Appendix B.3, and the future-work discussion. Its earlier parity splitting is explicitly recognized. Its star and strict-majority \(K_{2,2\ell}\) examples, general bounds, and tree algorithm do not provide the arbitrary-heterogeneous biclique count-state algorithm or the exact minimum formula. The available non-progressive *static* target-set paper and *progressive* dense-graph research address different objectives. The most similar research-record hits concern irreversible conversion or discounted hitting domination, neither of which implies the timed non-progressive statement.

Risk: a specialized biclique timed-threshold algorithm may exist under different terminology or in unindexed literature. This is a best-knowledge primary-material and record comparison, not a mathematical proof of uniqueness or publication priority.

## Mathematical value — PASS

The problem is already known to be hard on unrestricted networks and to admit a special exact tree algorithm. Complete bipartite networks model fully connected interactions between two communities and include graphs far outside the tree class. Heterogeneous individual adoption thresholds are natural, and timed controls cannot generally be replaced by static seed sets. The result replaces a potentially exponential space of intervention histories by an exact \(O(ab\log(a+b))\) count-state search, recovers actual optimal schedules, and yields an exact closed formula for uniform thresholds. The four-by-four example shows a genuinely multi-round, two-intervention cascade; the universal even-cost structure restricts every bipartite optimum. This is a motivated tractability boundary and structural theorem, not a mere table recomputation.

Self-review: passed. Independent audit: not yet performed.
