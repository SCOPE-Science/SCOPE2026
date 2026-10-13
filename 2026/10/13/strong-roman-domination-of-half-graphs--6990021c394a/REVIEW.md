# Review of Strong Roman domination of half graphs

## Correctness
PASS. The lower bound is reconstructed from the exact nested neighborhoods. The smallest-index zero vertex on the \(B\)-side can only be defended by an \(A\)-vertex that is adjacent to every zero vertex of \(B\); this forces an excess label of \(\lceil(n-\beta)/2\rceil\) above the positive baseline. The largest-index zero vertex on \(A\) gives the symmetric excess. The resulting separable bound is minimized exactly at one positive vertex per side for odd \(n\), and at one or two positives per side for even \(n\), with the one-sided boundary cases checked separately. The endpoint construction attains the bound. For odd \(n\), equality plus adjacency forces the two positive vertices to be \(a_1\) and \(b_n\), and their labels are then forced. The even nonuniqueness construction satisfies the defining defender loads exactly. The bundled checker exhaustively tests 449,345 bounded-weight labelings for \(3\le n\le7\).

## Originality
PASS. The 2017 foundational full text was inspected at the definition, complexity, bounds, and tree sections; it introduces strong Roman domination and proves bipartite NP-completeness but contains no half-graph or chain-graph specialization. The 2018 same-invariant paper explicitly lists MSC \(05C69\) and studies other special graph families; targeted full-text searches found no chain or Ferrers result. Exact searches and semantic searches under half graph, chain graph, Ferrers graph, and bipartite permutation graph did not locate a theorem implying the parity formula or odd-order uniqueness. Nearby exact strong-Roman results concern complete multipartite graphs or unrelated extremal constructions and do not imply the nested-neighborhood theorem.

## Value
PASS. Half graphs are canonical chain graphs and a standard extremal model for nested bipartite neighborhoods. The result gives a closed parity law on an infinite bipartite family despite strong Roman domination being hard even on bipartite graphs, and it identifies a sharp structural transition: odd orders have a unique optimum concentrated at the two opposite universal endpoints, while every even order has a second qualitatively different optimum. This is a natural exact benchmark rather than an arbitrary finite slice.

Self-review: passed. Independent audit: not yet performed.
