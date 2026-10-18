# Cubical norming faces and a complete face polynomial for book-graph Lipschitz-free spaces

## Finding
For every integer \(m\ge2\), let \(B_m=K_2\vee\overline K_m\) be the book graph consisting of \(m\) triangles sharing an edge, with unit-edge shortest-path metric. Let \(X_m=\mathcal F(B_m)\) be its real Lipschitz-free Banach space and \(Q_m=B_{X_m^*}\) its dual Lipschitz unit ball, with one hub value normalized to zero. Its dimension is \(m+1\).

**Complete norming-face theorem.** For every \(z\in X_m\setminus\{0\}\), the norming set
\[
J(z)=\{f\in Q_m: f(z)=\|z\|\}
\]
is combinatorially a \(j\)-dimensional cube for some \(0\le j\le m\). Conversely every nonempty proper face of \(Q_m\) arises as some \(J(z)\). The number of distinct norming sets of dimension \(j\) is the coefficient of \(t^j\) in the exact polynomial
\[
\boxed{\sum_{j=0}^{m+1}f_j(Q_m)t^j=(3+2t)(2+t)^m-t^m(1+t).}
\]
Here \(f_j\) counts nonempty \(j\)-faces and the top coefficient \(f_{m+1}(Q_m)=1\) represents \(Q_m\) itself, which is not a norming set for nonzero vectors.

In particular, \(Q_m\) has \(3\cdot2^m\) vertices and \(4m+2\) facets, and its polar \(B_{X_m}\) has \(4m+2\) extreme points and \(3\cdot2^m\) facets. Every extreme point of \(B_{X_m}\) has a norming face with \(2^m\) extreme norming functionals, its vertex figure is a combinatorial \(m\)-cross-polytope, and its vertex degree is exactly \(2m\). The number of nonempty faces of \(Q_m\), including itself, is \(5\cdot3^m-2\).

## Assumptions and scope
Write the two hubs as \(u,v\) and leaves as \(w_1,\ldots,w_m\). Since the graph metric comes from its edges, the dual unit ball consists of normalized real functions \(f(u)=0\), with coordinates \(b=f(v)\), \(x_i=f(w_i)\), satisfying
\[
Q_m=\{(b,x_1,\ldots,x_m): |b|\le1,\ |x_i|\le1,\ |x_i-b|\le1\ (1\le i\le m)\}.
\]
The canonical pairing is the evaluation of normalized Lipschitz functions on zero-mass signed measures. Its polar is the unit ball of \(X_m\). All face dimensions are affine dimensions; a \(0\)-cube means a singleton. The statement concerns \(m\ge2\) and unweighted graph distances.

## Proof
**1. Exact support-function reduction.** Fix any nonzero linear functional
\[L(b,x)=sb+\sum_{i=1}^{m}a_i x_i.\]
Let \(P=\sum_{a_i>0}a_i\), \(N=-\sum_{a_i<0}a_i\), and \(k=\#\{i:a_i=0\}\). For \(b\in[0,1]\), each leaf coordinate ranges over \([b-1,1]\); for \(b\in[-1,0]\), it ranges over \([-1,b+1]\). Consequently, maximizing over the leaf coordinates at a fixed hub value gives, respectively,
\[
\max_x L=\sum_i|a_i|+b(s-N)\quad(0\le b\le1),\qquad
\max_x L=\sum_i|a_i|+b(s+P)\quad(-1\le b\le0).
\]
Suppose first that \(a\ne0\), so \(P+N>0\). The maximizing hub sets are precisely the following five cases, according to \(s\):
\[
\begin{array}{c|ccccc}
\text{condition}&s>N&s=N&-P<s<N&s=-P&s<-P\\
\hline
\text{maximizing }b&\{1\}&[0,1]&\{0\}&[-1,0]&\{-1\}.
\end{array}
\]
At each maximizing \(b\), the coordinates with \(a_i>0\) are fixed at their upper feasible bounds, those with \(a_i<0\) at their lower feasible bounds, and those with \(a_i=0\) remain free in their feasible intervals. Hence each of the three singleton-hub cases exposes a \(k\)-cube. Each of the two interval-hub cases exposes a \((k+1)\)-cube: its \(2^{k+1}\) vertices are indexed by the two endpoints for \(b\) and, independently, the two endpoint choices for each free leaf coordinate; its \(2(k+1)\) facet inequalities are those bounding \(b\) and the \(k\) free coordinates. The combinatorial type is thus a cube, including when \(k=0\).

**2. The exceptional zero leaf functional.** If \(a=0\) and \(s>0\), the support set is the entire facet \(b=1\), an \(m\)-cube; if \(s<0\), it is \(b=-1\), also an \(m\)-cube. If \(a=0=s\), the whole \(Q_m\) is the maximizer and is not a proper face. Every face of a polytope is exposed by some linear functional, so the cases exhaust the entire norming-face structure. The strict inequalities, equalities, and the zero case are disjoint and give different geometric support sets.

**3. Count support faces without duplication.** For \(0\le k\le m-1\), choose the \(k\) zero coefficients in \(\binom mk\) ways and the signs of the \(m-k\) nonzero coefficients in \(2^{m-k}\) ways. For each such sign/zero pattern, there are exactly three \(k\)-dimensional singleton-hub faces and two \((k+1)\)-dimensional interval-hub faces. Their disjoint hub-coordinate ranges, and the fixed upper/lower values of nonzero leaves, make them distinct. The zero-leaf-coefficient case supplies two extra \(m\)-faces and the whole polytope. Therefore the complete face polynomial is
\[
3\sum_{k=0}^{m-1}\binom mk2^{m-k}t^k
+2t\sum_{k=0}^{m-1}\binom mk2^{m-k}t^k+2t^m+t^{m+1},
\]
which simplifies by the binomial theorem to
\[(3+2t)(2+t)^m-t^m(1+t).\]
In particular, the constant coefficient is \(3\cdot2^m\), the \(t^m\)-coefficient is \(4m+2\), and evaluation at \(t=1\) yields \(5\cdot3^m-2\).

**4. Banach-geometric conclusion.** For \(z\ne0\), \(J(z)\) is an exposed proper face of the dual ball. Every proper face of \(Q_m\) is one of those classified above and occurs as \(J(z)\) after positive rescaling of an exposing primal vector. Thus all norming sets are cubes and their exact dimensional counts are determined. Polarity interchanges a facet of \(Q_m\) with a vertex of \(B_{X_m}\), and the face lattice of each vertex figure of \(B_{X_m}\) is dual to that facet's face lattice. Because every facet of \(Q_m\) is an \(m\)-cube, every such vertex figure is an \(m\)-cross-polytope. Each therefore has \(2m\) vertices; these correspond to exactly \(2m\) edges incident to the corresponding primal vertex. The polar face-count identities follow from \(f_j(B_{X_m})=f_{m-j}(Q_m)\) for \(0\le j\le m\).

## Verification
The standalone standard-library Python program `verify_book_faces.py` independently enumerates all possible integer-valued normalized extreme dual potentials, tests connectivity of their tight-edge graphs, constructs every face as an intersection of the \(2+4m\) explicit supporting halfspace boundaries, and computes every face dimension by exact integer elimination. For \(m=2,3,4,5,6\), it reproduces, respectively, the full dual face vectors
\[
(12,20,10,1),\ (24,52,42,14,1),\ (48,128,136,72,18,1),
\]
\[
(96,304,400,280,110,22,1),\ (192,704,1104,960,500,156,26,1).
\]
From the directory containing the program, run `python3 verify_book_faces.py`. Its final output is `ALL EXACT BOOK-GRAPH FACE CHECKS PASSED`. This finite test is corroboration, not the proof for all \(m\); the complete infinite-range proof is given above.

## Relationship to prior work
D'Alì, Delucchi and Michałek (arXiv:1910.05193, first public 2019-10-11) establish the connection between finite metric Kantorovich–Rubinstein/Lipschitz balls and symmetric edge polytopes, and develop general graph methods. Chen, Davis and Korchevskaia (arXiv:2107.12315, first public 2021-07-26) classify face/facet subgraphs generally. Mori, Mori and Ohsugi (arXiv:2312.11287, first public 2023-12-18) treat facet bounds of joins of graphs. Their general constructions and facet-bound results are acknowledged as prior art; neither the identification of this metric family nor its total facet count is independently claimed as new. The full norming-face cubical classification and the evaluated all-dimensional face polynomial were not located in the inspected relevant texts or mathematical-result searches. The general face-subgraph criterion could in principle be specialized to obtain these counts, but the explicit all-dimensional specialization and Banach norming-face classification were not present in those inspections.

## Limitations
The face polynomial is for the dual Lipschitz ball, with the polar coefficients reversed for the Lipschitz-free ball. Cubical means *combinatorially equivalent to a cube*, not affinely congruent to a standard Euclidean cube. The theorem does not classify arbitrary graph metrics or prove uniqueness against unpublished or unindexed sources. Its Banach-space classification is specific to the book-graph family; the total facet count alone is not a novel contribution. Exact finite checks do not replace the all-parameter support-function proof. Independent audit has not been performed.

## References
1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first posted 2019-10-11), https://arxiv.org/abs/1910.05193.
2. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first posted 2021-07-26), https://arxiv.org/abs/2107.12315.
3. A. Mori, K. Mori and H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287 (first posted 2023-12-18), https://arxiv.org/abs/2312.11287.
