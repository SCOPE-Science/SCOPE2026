# The generalized total chromatic number of \(K_{3,n}\)

## Finding

Let \(\mathcal O\) be the class of edgeless graphs and \(\mathcal D_1\) the class of forests. A generalized \((\mathcal O,\mathcal D_1)\)-total coloring uses a common palette for vertices and edges: the vertex coloring is proper, edges of each color form a forest, and an edge has neither endpoint's color. Then for the finite simple complete bipartite graph \(K_{3,n}\),
\[
\chi''_{\mathcal O,\mathcal D_1}(K_{3,n})=4\qquad(n\ge3).
\]

## Proof

Three colors do not suffice. In a proper vertex coloring the palettes on the two shores are disjoint. If both shores are monochromatic, every edge must use the remaining color, giving a monochromatic four-cycle. Otherwise, with three colors one shore uses two colors and the other is monochromatic. Since both shores have at least three vertices, two vertices on the two-color shore have the same color. All edges from these two vertices to the other shore must use a single color, again giving a monochromatic four-cycle. Fewer than three colors cannot suffice, since any edge and its endpoints need three distinct colors.

For four colors, give the three vertices on the size-three shore colors \(1,2,3\), and all vertices of the opposite shore color \(4\). Color the full stars centered at the three vertices on the size-three shore by \(2,3,1\), respectively. The stars partition the edge set, each used edge color is a star and every edge avoids both endpoint colors. Thus four colors suffice for all \(n\ge3\).

## Relationship to prior work and scope

Borowiecki and Broere [1, Theorem 6 and its sharpness example] prove \(\chi''_{\mathcal O,\mathcal D_1}(K_{3,3}-e)=4\). By restriction to this subgraph, that result already excludes three colors for every \(K_{m,n}\) with \(m,n\ge3\). In the other direction \(K_{1,n}\) is a star and \(K_{2,n}\) has an acyclic three-vertex-coloring (give distinct colors to the size-two shore and a common third color to the other shore). Thus the three-color threshold for complete bipartite graphs is a direct consequence of [1, Theorems 1 and 6] and is not a new assertion here.

The contribution is the matching four-color construction for the entire nonplanar family \(K_{3,n}\). The planar four-color upper bounds in [1, 2] do not apply, and the even-palette case of [1, Theorem 1] applied to an acyclic four-vertex-coloring gives five, not four. Reusing the vertex colors on edges is essential when \(n\ge5\): disjoint palettes would leave at most two edge colors, and two forests on \(n+3\) vertices account for at most \(2(n+2)<3n\) edges. The color rotation on the three stars keeps the two requirements compatible without imposing any bound on \(n\).

No exact value is asserted for larger smaller-shore sizes. The 2011 framework article [3] was not checked in full; an unlocated earlier equivalent construction is possible.

## Verification

The proof holds for every \(n\ge3\); it does not rely on computation. The companion `verify.py` tests the star construction for \(3\le n\le100\) and separately stress-tests three-colorability for \(1\le m\le n\le6\), stopping at the first successful assignment in positive cases.

## References

1. M. Borowiecki and I. Broere, *Hamiltonicity and Generalised Total Colourings of Planar Graphs*, Discussiones Mathematicae Graph Theory 36 (2016), 243–257, [doi:10.7151/dmgt.1874](https://doi.org/10.7151/dmgt.1874), especially Theorems 1 and 6.
2. J. A. Schreib, *The Borowiecki–Broere Generalized Total Coloring Conjecture for Planar Graphs*, [arXiv:2610.00091v1](https://arxiv.org/abs/2610.00091v1), Theorem 1.1.
3. M. Borowiecki, A. Kemnitz, M. Marangio, and P. Mihók, *Generalized total colorings of graphs*, Discussiones Mathematicae Graph Theory 31 (2011), 209–222, [doi:10.7151/dmgt.1540](https://doi.org/10.7151/dmgt.1540).
