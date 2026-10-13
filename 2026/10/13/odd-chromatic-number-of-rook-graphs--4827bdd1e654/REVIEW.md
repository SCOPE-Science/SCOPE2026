# Self-review

## Correctness

PASS. In a proper rook coloring, a neighborhood color has odd multiplicity at \((i,j)\) exactly when it belongs to the symmetric difference of the row and column color sets. This gives the exact criterion \(R_i\ne C_j\). The cyclic construction reaches the clique lower bound when \(m<n\). In the balanced case, \(n\) colors force all row and column palettes to agree, and \(n+1\) colors are impossible because the number of rows missing a color equals the number of columns missing it, forcing one equal missing-color pair. The \(n+2\) construction separates distance-two row omissions from consecutive column omissions.

The independent finite checker evaluates the defining neighborhood multiplicities directly and agrees with the theorem throughout its stated test ranges.

## Originality

PASS. The closest primary source is Liu--Dou--Yang's 2026 paper on the same invariant and Cartesian product operation. Its inspected full text treats path/cycle products and complete-by-path or complete-by-cycle products, not \(K_m\square K_n\). Broader graph-product work gives bounds rather than this exact formula. Published-result searches using rook, line-graph, complete-bipartite, Cartesian-product, and neighborhood-parity aliases found no covering exact result.

The nearest same-invariant database result concerns complete multipartite graphs, a distinct class that does not contain general rook graphs. Residual risk remains from alternate rook-graph terminology and concurrent 2026 work.

## Value

PASS. This is an all-parameter exact classification of a canonical product family, with a sharp balanced-versus-unbalanced transition and explicit optimal colorings. The local row-column criterion is structural rather than a one-off computation and explains the two-color surcharge.

Self-review: passed. Independent audit: not yet performed.
