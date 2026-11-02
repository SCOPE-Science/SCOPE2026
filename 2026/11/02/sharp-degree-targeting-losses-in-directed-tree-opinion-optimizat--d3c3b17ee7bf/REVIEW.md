# Scientific review

## Correctness — PASS

The proposed ratio is proved using the exact finite Neumann expansion of Friedkin–Johnsen influence on directed in-trees, a bounded-degree descendant-count upper estimate, and a b-ary deep tree isolated by a long attenuating path from the unique largest-indegree decoy. The construction has a uniform bounded decoy gain, while the deep subtree achieves the stated logarithmic/power-law orders. Path padding establishes lower bounds at every sufficiently large integer order, not just a sparse sequence. For the exact alternative, transposed forward influence passes through in-trees and directed cycles, with explicit positive-denominator closure. Computations from the actual standalone package compare exact-rational results with independent linear-system elimination and brute-force small-set choices. Scope: fixed degree, directed in-arborescences for the ratios; functional digraphs for the algorithm.

## Originality — PASS with residual priority risk

The 2023 source fully establishes the top-influence product criterion and studies highest-in-degree selection as an experimental baseline. The 2016 rooted-tree PageRank theorem already gives a level-count identity and studies link modification. Neither inspected statement asserts the sharp *worst-case approximation-ratio hierarchy* for choosing the unique in-degree maximizer on bounded-degree directed trees. The 2005 approximation-from-in-degree study is especially relevant, but its available abstract concerns Web degree correlations; full text was not examined. Searches of other influence-centrality and 2026 sampling literature, and comparisons to indexed theorem summaries, did not reveal a dominating quantified bound; absence of a located theorem is not a proof of absolute priority. We credit all known constituent centrality formulas and avoid claiming them as new.

## Mathematical value — PASS

The result resolves a precise algorithmic/structural question about a baseline used in the motivating paper. For each fixed maximum in-degree it gives a *sharp* phase diagram: local-degree targeting is boundedly competitive at indegree two, logarithmically unreliable at degree three, and polynomially unreliable at higher degrees, even with uniform opinions and a uniquely defined heuristic choice. The matching obstruction is an explicit family of connected trees, and the linear-time exact alternative demonstrates that the loss is a heuristic deficiency rather than an inherent difficulty on functional networks. This is a meaningful motivated complete asymptotic classification, not merely a numerical counterexample.

## Closest literature and residual limits

Sun and Zhang (2023), Theorem 4.1 and Section 6: exact centrality-product intervention and experimental in-degree heuristic, but no matching structural worst-case rate. Arratia and Marijuán (2016), Theorem 3: rooted-tree PageRank level counts, a known ingredient, not the extremal gap. Fortunato et al. (2005): in-degree–PageRank approximation under degree correlations, abstract accessible but full text not assessed. Shrinate and Tripathy (2024): general signed-system influence with no identified degree-gap theorem. Sun et al. (2026): fast sampling-based opinion optimization with no identified theorem of this precise extremal form. Residual risk: specialized PageRank-versus-degree approximation bounds might be indexed under other terminology. Scope restrictions and arithmetic-only complexity are stated in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
