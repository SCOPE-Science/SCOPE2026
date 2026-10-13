# Three-color threshold for generalized total colorings of complete bipartite graphs
## Finding
Let \(K_{m,n}\) be a finite simple complete bipartite graph with \(1\le m\le n\). Write \(\mathcal O\) for the class of edgeless graphs and \(\mathcal D_1\) for the class of forests. A generalized \((\mathcal O,\mathcal D_1)\)-total coloring is a coloring of vertices and edges such that vertex color classes are independent, edge color classes are forests, and every edge has a color different from the colors of both endpoints.

Then \(K_{m,n}\) admits a generalized \((\mathcal O,\mathcal D_1)\)-total coloring with three colors if and only if
\[
m\le 2.
\]
Hence
\[
\chi''_{\mathcal O,\mathcal D_1}(K_{m,n})=3
\]
for \(m\in\{1,2\}\), and at the first excluded shore size one has the exact infinite-family formula
\[
\chi''_{\mathcal O,\mathcal D_1}(K_{3,n})=4\qquad(n\ge3).
\]

## Assumptions and scope
All graphs are finite and simple. The two shores of \(K_{m,n}\) are denoted by \(A\) and \(B\), with \(|A|=m\) and \(|B|=n\). Colors need not all appear on vertices, but every vertex and every edge receives one color from the common palette. Properness of the vertex coloring means that no color can occur on both \(A\) and \(B\).

The theorem classifies three-colorability for every complete bipartite graph and determines the exact generalized total chromatic number for the full subfamilies with smaller shore size one, two, or three. It does not assert the exact value for smaller shore size at least four.

## Proof
Every nonempty complete bipartite graph needs at least three colors. Indeed, the endpoints of any edge have distinct vertex colors, and that edge must avoid both endpoint colors.

Suppose now that three colors are available. Let \(p\) be the number of vertex colors used on \(A\) and \(q\) the number used on \(B\). Since every vertex of \(A\) is adjacent to every vertex of \(B\), the two shore palettes are disjoint. Thus \(p,q\ge1\) and \(p+q\le3\). Up to interchanging the shores, there are only two cases.

First suppose \(p=q=1\). If the shore colors are \(1\) and \(2\), every edge is forced to have color \(3\). Its color class is therefore all of \(K_{m,n}\), which is a forest exactly when one shore has size one. Under \(m\le n\), this is exactly \(m=1\).

Next suppose \(p=2\) and \(q=1\). Let the nonempty color classes in \(A\) be \(A_1\) and \(A_2\), colored \(1\) and \(2\), and color all of \(B\) with \(3\). Every edge from \(A_1\) to \(B\) is forced to color \(2\), while every edge from \(A_2\) to \(B\) is forced to color \(1\). Hence the two nonempty edge-color subgraphs are
\[
K_{|A_1|,n}\quad\text{and}\quad K_{|A_2|,n}.
\]
Here \(n\ge2\). A complete bipartite graph with both shores of size at least two contains a four-cycle, so both displayed graphs are forests exactly when \(|A_1|=|A_2|=1\). Thus \(m=2\). The symmetric case \(p=1,q=2\) gives no additional possibility under \(m\le n\).

Conversely, if \(m=1\), color the two shores \(1\) and \(2\) and every edge \(3\); the edge-color class is a star. If \(m=2\), color the two vertices of the smaller shore \(1\) and \(2\), color the larger shore \(3\), and color all edges incident with the first small-shore vertex \(2\) and all edges incident with the second \(1\). Each nonempty edge-color class is a star. This proves the three-color threshold and the exact value \(3\) when \(m\le2\).

For \(K_{3,n}\) with \(n\ge3\), the threshold just proved excludes three colors. Four colors suffice explicitly: color the three vertices of the size-three shore \(1,2,3\), color every vertex of the other shore \(4\), and color the three incident stars \(2,3,1\), respectively. Each edge color class is a star and every edge avoids both endpoint colors. Therefore the exact value is \(4\).

## Verification
The proof above is infinite and does not rely on finite enumeration. The accompanying `verify.py` independently reconstructs the definition. It exhaustively checks every vertex three-coloring for every \(K_{m,n}\) with \(1\le m\le n\le6\); with three colors, endpoint avoidance forces each edge color uniquely, after which every monochromatic edge subgraph is checked for acyclicity. The script also checks the explicit four-color construction for \(K_{3,n}\) for every \(3\le n\le100\).

Replay output:

`ALL CHECKS PASSED; three_color_parameter_cases=21; three_color_vertex_assignments=1872; three_color_range=1<=m<=n<=6; four_color_K3n_cases=98; four_color_range=3<=n<=100`

## Relationship to prior work
Borowiecki, Kemnitz, Marangio, and Mihók introduced generalized total colorings in 2011. Their indexed abstract states exact results for paths, cycles, and, for selected graph properties, complete graphs. Borowiecki and Broere later studied the planar \((\mathcal O,\mathcal D_1)\) case and conjectured a four-color bound. Schreib's 2026 preprint proves that conjecture and, more strongly, proves that every proper four-coloring of a finite simple planar graph extends to the required edge-forest coloring. The full public text of that preprint contains no occurrence of “bipartite” or “complete bipartite.”

The present result is not implied by the planar theorem. The families \(K_{1,n}\) and \(K_{2,n}\) are planar, but the theorem here sharpens the available four-color upper bound to the exact value three. In the other direction, \(K_{3,n}\) is nonplanar for \(n\ge3\), so the planar theorem does not cover the infinite sharp-four family proved here.

Targeted searches using the exact invariant, complete-bipartite notation, the \((\mathcal O,\mathcal D_1)\) formulation, and the three-color threshold found no statement implying this classification.

## Limitations
No exact value is claimed here for \(K_{m,n}\) when \(m\ge4\). The 2011 framework paper was available through indexed metadata and its abstract, while a line-by-line inspection of its full text was not completed in this run; consequently an older unindexed formulation remains a residual originality risk. The direct searches and the explicit scope stated in that abstract found no complete-bipartite theorem, but absence from search is not itself a novelty proof.

The finite verifier is a stress test only. The infinite theorem is justified by the palette dichotomy and the explicit constructions in the proof.

## References
1. J. A. Schreib, *The Borowiecki–Broere Generalized Total Coloring Conjecture for Planar Graphs*, arXiv:2610.00091v1, first public 2026-09-07.
2. M. Borowiecki, A. Kemnitz, M. Marangio, and P. Mihók, *Generalized total colorings of graphs*, Discussiones Mathematicae Graph Theory 31 (2011), 209–222, doi:10.7151/dmgt.1540.
3. M. Borowiecki and I. Broere, *Hamiltonicity and Generalised Total Colourings of Planar Graphs*, Discussiones Mathematicae Graph Theory 36 (2016), 243–257, doi:10.7151/dmgt.1874.
