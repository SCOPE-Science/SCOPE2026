# Review of Perfect Italian domination of half graphs

## Correctness
PASS. The defining equations on the half graph are exact prefix and suffix weight equations. Any function of weight at most \\(3\\) must have a zero in each bipartition class, forcing both side weights to be at least \\(2\\). At weight \\(4\\), both side weights are exactly \\(2\\). If the rightmost positive vertex in the \\(A\\)-side had index at least \\(2\\), then \\(b_1\\) would be positive; that positive weight would prevent every suffix beginning at index at least \\(2\\) from reaching \\(2\\), forcing at least \\(n-1\\) positive \\(A\\)-vertices, impossible for \\(n\\ge4\\). Hence all \\(A\\)-weight is the label \\(2\\) at \\(a_1\\), and the zero condition at \\(a_n\\) forces the label \\(2\\) at \\(b_n\\). The bundled checker exhausts every bounded-weight candidate through \\(n=14\\) and matches the theorem, including the \\(H_3\\) boundary exception.

## Originality
PASS. The 2019 full-text primary study was inspected at its definitions, small-value characterizations, and exact-class section; targeted full-text searches returned no half, chain, or bipartite-permutation occurrence. A 2026 full-text study supplies a polynomial algorithm for the much broader path-convex bipartite class, but its theorem statements give algorithmic solvability rather than a closed half-graph formula or optimizer classification. Exact web searches and semantic published-result searches under perfect Italian, half graph, chain graph, Ferrers graph, and bipartite-permutation formulations did not retrieve an equivalent theorem. The closest stored half-graph and chain-graph results concern different invariants.

## Value
PASS. Half graphs are the canonical strictly nested chain graphs and a standard obstruction/test family in ordered bipartite graph theory. The result turns a general tractability statement into an exact constant value together with a unique optimizer and identifies the sharp boundary at \\(H_3\\). The prefix-suffix rigidity is structural information not supplied by generic algorithms or by complete-multipartite formulas.

Self-review: passed. Independent audit: not yet performed.
