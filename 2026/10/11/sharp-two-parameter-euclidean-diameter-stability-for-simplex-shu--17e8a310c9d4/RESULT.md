# Sharp two-parameter Euclidean-diameter stability for simplex shuffles

## Finding

For integers \(m,n\ge2\), the shuffle of two weighted standard simplices by the complete-bipartite graphical zonotope has a sharp two-parameter region on which the added simplices contribute only their own squared difference lengths to the Euclidean diameter.

Explicitly, for the polytope \(P_{m,n}(\alpha,\beta)\) below, with nonnegative real weights,
\[
\operatorname{diam}_2(P_{m,n}(\alpha,\beta))^2
 =mn(m+n)+2\alpha^2+2\beta^2
\quad\Longleftrightarrow\quad
0\le\alpha\le m-1\ \text{and}\ 0\le\beta\le n-1.
\]
If \(\alpha>m-1\), the squared diameter exceeds the displayed baseline by at least \(4n(\alpha-m+1)\); if \(\beta>n-1\), by at least \(4m(\beta-n+1)\). In particular, the unit-weight shuffle has squared diameter \(mn(m+n)+4\) for every \(m,n\ge2\).

## Assumptions and scope

Let \(A=\{1,\ldots,m\}\) and \(B=\{m+1,\ldots,m+n\}\). In the standard Euclidean coordinate space \(\mathbb R^{m+n}\), put
\[
\Delta_A=\operatorname{conv}\{e_i:i\in A\},\qquad
\Delta_B=\operatorname{conv}\{e_{m+j}:1\le j\le n\},
\]
\[
Z_{m,n}=\sum_{i=1}^{m}\sum_{j=1}^{n}[e_i,e_{m+j}],\qquad
P_{m,n}(\alpha,\beta)=Z_{m,n}+\alpha\Delta_A+\beta\Delta_B.
\]
Minkowski summation and scalar multiplication are taken in the displayed Euclidean coordinates. The geometric diameter is the maximum of the ordinary Euclidean distances between **any two points** in the polytope, not a shortest-path distance in its one-skeleton. The polytope lies in the affine hyperplane with coordinate sum \(mn+\alpha+\beta\); we do not rescale the induced metric. The dimensions and weights range over \(m,n\ge2\), \(\alpha,\beta\in[0,\infty)\). At zero weights the corresponding simplex summand collapses to a point.

The construction is the shuffle operation on generalized permutohedra defined by Chapoton and Pilaud [1, Definition 75], specialized to weighted simplices in two disjoint coordinate blocks.

## Proof

**Signed-matrix reduction.** Write \(s_{ij}\in\{-1,1\}\) for \(1\le i\le m\), \(1\le j\le n\). Let
\[
r_i=\sum_{j=1}^{n}s_{ij},\qquad
c_j=-\sum_{i=1}^{m}s_{ij},
\]
and write \(\operatorname{osc}(r)=\max_i r_i-\min_i r_i\), with the analogous definition for \(c\). We first prove the exact identity
\[
\operatorname{diam}_2(P_{m,n}(\alpha,\beta))^2
=2\alpha^2+2\beta^2+
\max_{s\in\{-1,1\}^{m\times n}}
\left(\sum_i r_i^2+\sum_j c_j^2
+2\alpha\operatorname{osc}(r)
+2\beta\operatorname{osc}(c)\right). \tag{1}
\]
Every difference of two points in \(Z_{m,n}\) is
\(\sum_{i,j}t_{ij}(e_i-e_{m+j})\), with independent \(t_{ij}\in[-1,1]\). Differences in the two simplex summands range independently over \(\alpha(\Delta_A-\Delta_A)\) and \(\beta(\Delta_B-\Delta_B)\). A convex squared norm reaches its maximum at a vertex in every independent segment and simplex parameter; thus choose each \(t_{ij}=\pm1\), together with differences \(\alpha(e_p-e_q)\) and \(\beta(e_{m+u}-e_{m+v})\). Since each block contains at least two indices, the maximizing pairs can be chosen distinct; when the oscillation vanishes, any distinct pair works. For such choices the squared norm is
\[
\sum_i r_i^2+\sum_j c_j^2+2\alpha^2+2\beta^2
+2\alpha(r_p-r_q)+2\beta(c_u-c_v).
\]
Maximizing separately over pairs gives (1). The reduction includes all endpoints of the weight ranges, including zero weights.

**Sharp deficit inequalities.** Define
\[
D_A=\sum_{i=1}^{m}(n^2-r_i^2),\qquad
D_B=\sum_{j=1}^{n}(m^2-c_j^2).
\]
Both are nonnegative. Choose rows \(p,q\) attaining the largest and smallest row sums. In any column where their signs differ, that column has at least one sign of each type. If it contains \(h\) positive signs, then its contribution to \(D_B\) is
\(m^2-(2h-m)^2=4h(m-h)\ge4(m-1)\).
Furthermore the number of columns where those two rows differ is at least \((r_p-r_q)/2=\operatorname{osc}(r)/2\). Therefore
\[
D_B\ge2(m-1)\operatorname{osc}(r). \tag{2}
\]
By interchanging rows and columns,
\[
D_A\ge2(n-1)\operatorname{osc}(c). \tag{3}
\]
For \(0\le\alpha\le m-1\) and \(0\le\beta\le n-1\), inequalities (2)–(3) give
\[
2\alpha\operatorname{osc}(r)+2\beta\operatorname{osc}(c)
\le D_B+D_A.
\]
Since \(\sum r_i^2+\sum c_j^2=mn(m+n)-D_A-D_B\), (1) yields the proposed upper bound. Equality is attained when every \(s_{ij}=+1\): the deficits and oscillations vanish, and choosing distinct coordinate vertices in each simplex difference yields exactly the baseline. This proves sufficiency, including equality on both threshold boundaries.

**Necessity and quantitative excess.** Suppose \(\alpha>m-1\). Choose signs \(s_{1j}=-1\) and \(s_{ij}=+1\) for \(i\ne1\), all \(j\). Then the row oscillation is \(2n\), the column oscillation is zero, \(D_A=0\) and \(D_B=4n(m-1)\). Substitution into (1) yields
\[
\operatorname{diam}_2(P)^2\ge
mn(m+n)+2\alpha^2+2\beta^2+4n(\alpha-m+1),
\]
strictly beyond the baseline. Interchanging the blocks proves that \(\beta>n-1\) causes an excess of at least \(4m(\beta-n+1)\). Hence either violated inequality prevents equality. These are exact witnesses, independent of the other weight. The theorem follows.

## Verification

The standalone Python 3 standard-library program `artifacts/verify_shuffle.py` exhaustively evaluates signed matrices, checks (2)–(3) term by term, and independently enumerates vertex coordinate multisets through mixed strict orders of the two blocks. It then maximizes Euclidean squared distances by the rearrangement inequality, obtaining a second calculation that does not use signed matrices. For the seven size pairs \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,4)\), each with seven rational weight pairs on, below, and above the thresholds, the two calculations agree in all 49 cases, and the stated if-and-only-if law holds. Replay using `python3 artifacts/verify_shuffle.py`. The finite checks corroborate rather than prove the universal assertions; the proof above establishes all allowed sizes and real nonnegative weights.

## Relationship to prior work

Chapoton and Pilaud [1, Definition 75] define the shuffle by the same complete-bipartite graphical zonotope and develop face, vertex, and fan combinatorics. Their inspected primary text does not state an ambient Euclidean diameter profile or the two sharp weight thresholds. Agnarsson and Morris [2] study vertices and edges of Minkowski sums of simplices, without this metric formula. Deza and Pournin [3] study the **graph-theoretic** diameter of Minkowski sums, which is not the ambient Euclidean invariant here. Pilaud and Poullot [4] study pivot polytopes and normal-fan isomorphisms, not the metric threshold. None of these stated results implies the quantified formula without new metric analysis. Padrol, Pilaud, and Poullot [5] provide a general deformation-cone framework for graphical zonotopes, but no Euclidean diameter bound for the present shuffle family. The exact graphical-zonotope diameter \(mn(m+n)\) is already a separately known zero-weight value for the complete-bipartite case; it corresponds to \(lpha=eta=0\), not to the positive-weight classification. The exact signed-matrix reduction and sharp discordance inequalities establish the new two-parameter region.

## Limitations

The theorem concerns only the fixed standard-coordinate Euclidean realization and the shuffle of **two** scaled standard simplices, with \(m,n\ge2\), \(\alpha,\beta\ge0\). It does not assert a formula for other realizations, arbitrary generalized permutohedra, negative weights, or graph-theoretic diameters. Above the thresholds it proves strict excess and explicit lower bounds, not the complete diameter formula in the supercritical region. An equivalent result under unsearched terminology remains a literature-discovery risk; the absence of matching phrases is not a proof of historical novelty.

## References

[1] F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896v1 (2022-01-18), Definition 75; subsequent Annales Henri Lebesgue 7 (2024), 1535–1601. https://arxiv.org/abs/2201.06896

[2] G. Agnarsson and W. D. Morris, *On Minkowski sums of simplices*, arXiv:math/0605564v1 (2006). https://arxiv.org/abs/math/0605564

[3] A. Deza and L. Pournin, *Diameter, decomposability, and Minkowski sums of polytopes*, arXiv:1806.07643v1 (2018). https://arxiv.org/abs/1806.07643

[4] V. Pilaud and G. Poullot, *Pivot polytopes of products of simplices and shuffles of associahedra*, arXiv:2410.12658 (2024), introductory results. https://arxiv.org/abs/2410.12658

[5] A. Padrol, V. Pilaud, and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422v1 (2021), deformation-cone theory. https://arxiv.org/abs/2111.12422
