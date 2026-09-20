# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The upper bound rests on a local rigidity lemma. If a selected vertex in \(G\square H\) had two selected neighbours in the same factor direction, their factor endpoints would form a 2-path whose middle vertex is the unique common neighbour because the corresponding factor has no triangles or 4-cycles. The product geodesic is therefore unique and runs through the selected middle vertex, violating mutual visibility. Hence the induced connected selected subgraph has maximum degree at most two and is a path or cycle.

For four consecutive vertices of an induced path or a cycle of length at least five, the factor directions must alternate. The repeated factor contributes a unique two-edge geodesic and the other factor contributes one edge. Every shuffle of these three forced factor steps passes internally through one of the two selected middle vertices, so the endpoints are not visible. An induced 4-cycle is a Cartesian square, and its opposite vertices have only the two length-two geodesics through the other selected corners. Thus no connected mutual-visibility set has order at least four.

A Cartesian corner built from one edge of each factor is a connected mutual-visibility triple because the missing fourth square vertex provides an external geodesic for the two leaves. This proves the exact value. The same-direction obstruction also classifies every maximum triple, and summing \(d_G(g)d_H(h)\) over all possible centres gives \(4|E(G)||E(H)|\).

A standalone verifier checks the definition directly on every unordered pair drawn from the eight connected graph-atlas factor types of orders 2 through 5 with girth at least five. It verifies all three-subsets, all four-subsets, and the maximum-set count for 36 products of order at most 25. All checks agree with the theorem. Finite computation supports but does not replace the proof.

Correctness status: PASS.

## Originality

The primary source introducing connected mutual visibility, Tonny K B and Shikhi M, arXiv:2609.18877v1 (submitted 16 September 2026), was inspected. It defines \(\mu_c\), proves that \(\mu_c(X)=2\) exactly when \(g(X)\ge5\), and studies geodetic graphs, joins, block/cactus structure, defect graphs, and complexity. The inspected version does not state a Cartesian-product theorem.

The closest older product literature concerns different visibility parameters. Cicerone--Di Stefano--Klavžar (arXiv:2112.13024) studies ordinary mutual visibility in Cartesian products. Di Stefano's original paper determines ordinary mutual visibility on grids. Korže--Vesel (Results in Mathematics 79 (2024), 116) studies ordinary mutual visibility in products of paths and cycles. Bujtás--Klavžar--Tian determine the lower mutual-visibility number of rectangular grids and exhibit a three-vertex corner as a maximal ordinary mutual-visibility set; this does not determine the maximum connected mutual-visibility number.

Searches using the exact invariant name together with `Cartesian product`, `grid`, `product graph`, and synonymous mutual-visibility terminology found no statement equivalent to the present high-girth-factor theorem, maximum-set classification, or count.

No specific inaccessible paper was identified as especially likely to contain the same connected-parameter result. The main residual risk is chronological rather than access-based: the invariant is only a few days old, so a parallel preprint or unindexed result could exist. Older inaccessible or partially indexed product papers overwhelmingly concern ordinary, total, lower, or game variants, which are not equivalent to connected mutual visibility.

Originality status: PASS, to the best of our knowledge, subject to the preceding very-recent-literature risk.

## Value

The theorem gives a broad exact product result immediately after the introduction of the connected invariant. It is stronger than a grid computation: every product of two connected nontrivial high-girth graphs has the same value, and all maximizers are classified and counted. For rectangular grids it creates an unbounded separation from ordinary mutual visibility, since \(\mu(P_m\square P_n)=2\min\{m,n\}\) for \(m,n\ge4\) but \(\mu_c(P_m\square P_n)=3\). The local factor-direction argument is also a reusable obstruction for other visibility questions on Cartesian products.

Value status: PASS.

## Limitations

The theorem assumes both factors have girth at least five and does not classify mixed or low-girth factors. It applies to exactly two Cartesian factors; higher products can have larger connected mutual-visibility sets. The verifier covers finite small instances only. Because the invariant was introduced extremely recently, parallel unindexed work is a non-negligible originality risk. Independent audit and independent validation have not been performed.
