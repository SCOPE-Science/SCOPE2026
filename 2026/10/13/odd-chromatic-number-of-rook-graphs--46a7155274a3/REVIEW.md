# Review of Odd chromatic number of rook graphs

## Correctness
PASS. In a proper rook-graph coloring, each color occurs at most once in a given row and at most once in a given column. For a cell, any color other than its own therefore occurs in the open neighborhood zero, one, or two times, and it occurs oddly exactly when it belongs to one of the row and column color sets but not the other. This proves the row-set criterion. For \(m<n\), every proper \(n\)-coloring has full \(n\)-color row sets and \(m\)-color column sets, so it is odd. For the square, \(n\) colors give equal row and column sets everywhere. With \(n+1\) colors, the number of rows omitting any fixed color equals the number of columns omitting it, forcing at least one row and column to omit the same color and therefore fail the criterion. The cyclic \(n+2\)-color construction has distinct row and column omission pairs and is proper. The direct checker independently agrees in all enumerated small cases.

## Originality
PASS. The initiating paper defines the exact neighborhood-parity predicate and concentrates on planar bounds; it already covers only the small square boundary \(R_{2,2}=C_4\). The 2022 graph-products paper proves boundedness for subgraphs of strong products with bounded-treewidth structure, not an exact complete-by-complete Cartesian formula. The 2026 exact Cartesian-product paper lists path-path, cycle-path, cycle-cycle, complete-path, and complete-cycle families, but not complete-complete products. Searches using rook, Hamming, line-graph, Latin-rectangle, and complete-Cartesian aliases found no equivalent theorem. A database result for complete multipartite graphs is inapplicable to the non-multipartite rook family apart from small degenerate cases.

## Value
PASS. Rook graphs are canonical Cartesian products and line graphs of complete bipartite graphs. The theorem exposes a sharp structural phase transition invisible to ordinary chromatic number: rectangular boards need exactly their clique number and every optimum is automatically odd, while square boards require two extra colors. The proof identifies the mechanism as a balance law for omitted row and column colors, and the construction is explicit for all orders.

Self-review: passed. Independent audit: not yet performed.
