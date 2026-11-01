# Universal weighted detour-spline law on Cartesian-product metric networks

## Finding

Let \(r\geq 2\), and let \(G_1,\ldots,G_r\) be finite, connected, simple metric graphs, each with at least two vertices and strictly positive edge lengths. Assume every edge is **geodesic**: the distance between its endpoints, in its entire factor graph, equals that edge's length. Write \(n_i=|V(G_i)|\), \(b_i=\prod_{j\ne i}n_j\), and
\[
\Lambda=\sum_{i=1}^{r}b_i\sum_{e\in E(G_i)}\ell_e.
\]
Let \(Z=\prod_i|G_i|\) carry the sum-product metric \(d_Z((x_i),(y_i))=\sum_i d_{G_i}(x_i,y_i)\). Let \(Y\subset Z\) be its **metric one-skeleton**: points having at most one nonvertex coordinate. Give \(Y\) its intrinsic shortest-path metric \(d_Y\), and sample independent points \(X,X'\) uniformly by total one-dimensional edge arclength on \(Y\). Put \(\Delta=d_Y(X,X')-d_Z(X,X')\).

**Theorem (all products, all geodesic positive edge weights).** For every \(z\geq0\),
\[
\boxed{\Pr(\Delta>z)=\frac1{\Lambda^2}\sum_{i=1}^{r}b_i(b_i-1)\sum_{e\in E(G_i)}(\ell_e-z)_+^2.}
\]
In particular \(\Delta\geq0\), and its positive mass and every positive real moment are
\[
\Pr(\Delta>0)=\frac{\sum_i b_i(b_i-1)\sum_e\ell_e^2}{\Lambda^2},\qquad
\mathbb E[\Delta^q]=\frac{2\sum_i b_i(b_i-1)\sum_e\ell_e^{q+2}}{(q+1)(q+2)\Lambda^2}\quad(q>0).
\]
Conditional on a positive detour occurring across two different copies of the same factor edge of length \(\ell_e\), its scaled size \(\Delta/\ell_e\) has the \(\mathrm{Beta}(1,2)\) law. If every edge has a common length \(a\), then \(\Delta/a\mid(\Delta>0)\sim\mathrm{Beta}(1,2)\).

**Edge-length tomography.** The detour survival function is a finite quadratic spline. At each positive length \(a\), its second derivative has a downward jump of exactly
\[
\boxed{\frac{2}{\Lambda^2}\sum_{i=1}^{r}b_i(b_i-1)\#\{e\in E(G_i):\ell_e=a\}.}
\]
Thus the complete detour law, together with \(\Lambda\), determines the weighted aggregate of factor edge-length multisets; it need not determine which factor contains a repeated length.

**Exact cumulative-distance correction.** Define \(H(s)=2s(1-s)\) for \(0<s<1\) and \(H(s)=0\) otherwise. For a fixed factor \(i\), denote by \(V_{-i}=\prod_{j\ne i}V(G_j)\) its layer set and put \(d_{-i}(u,v)=\sum_{j\ne i}d_{G_j}(u_j,v_j)\). If \(F_Z,F_Y\) are the distribution functions of \(d_Z(X,X')\) and \(d_Y(X,X')\) under the **same arclength sampling**, then at every real \(t\),
\[
\boxed{F_Z(t)-F_Y(t)=\frac{1}{\Lambda^2}\sum_i\sum_{e\in E(G_i)}\ell_e^2\sum_{\substack{u,v\in V_{-i}\\u\ne v}} H\!\left(\frac{t-d_{-i}(u,v)}{\ell_e}\right).}
\]
Consequently \(F_Y\leq F_Z\), with strict inequality precisely where one of the displayed summands is positive.

## Assumptions and scope

All factor graphs are finite, connected and simple (no loops or multiple edges), and have at least two vertices. Edge lengths are positive and geodesic in their own factors. The latter hypothesis excludes metrically redundant edges whose alternate endpoint route is shorter than the edge. The ambient product uses the sum of **intrinsic factor distances**; it is not an arbitrary Euclidean embedding. The sampling measure is normalized one-dimensional arclength on the product's one-skeleton, not the product's higher-dimensional volume. Vertices are a null set for this sampling measure. The graph product may have any number \(r\ge2\) of factors, and every factor may have unequal edge lengths.

## Proof

**1. Point-pair route classification.** Fix two points in interiors of skeleton edges. Each skeleton edge changes exactly one factor coordinate. If the two edges change different factor coordinates, a path can first complete the starting coordinate, traverse the necessary vertex-to-vertex moves in other factors, and end on the finishing edge, with length exactly \(d_Z\). If both edges change the same factor coordinate but come from distinct underlying edges of that factor, any shortest path in that factor between the two interior points enters and exits via vertices; changes in all other factor coordinates may be inserted at a vertex along that path, again attaining \(d_Z\). If both points lie on the same copy of one underlying edge, their direct subsegment likewise attains \(d_Z\). In every case \(d_Y\ge d_Z\) because \(Y\subset Z\).

The remaining case is two copies of one factor edge \(e=ab\) of length \(\ell\), at **different** layer vertices \(u,v\in V_{-i}\). Parametrize the two points by \(s,t\in(0,\ell)\), both measured from \(a\). Their ambient distance is \(d_{-i}(u,v)+|s-t|\). To change any layer coordinate, a skeleton route must first reach \(a\) or \(b\), and must again leave an endpoint to reach the final interior point. Using the same endpoint gives horizontal cost \(s+t\) or \(2\ell-s-t\). Any route using opposite endpoints has horizontal cost at least \(\ell\), since the factor endpoint distance is \(\ell\), whereas \(\min(s+t,2\ell-s-t)\le\ell\). Hence
\[
d_Y=d_{-i}(u,v)+\min(s+t,2\ell-s-t),\quad
\Delta=2\min\{\min(s,t),\ell-\max(s,t)\}.
\]
This exhaustive classification is valid without symmetry, regularity, or equal edge lengths.

**2. Exact conditional law.** For independent uniform \(S,T\in[0,\ell]\), the two triangles \(S\le T\) and \(T\le S\) show that \(\Delta>z\), for \(0\le z\le\ell\), has total area \((\ell-z)^2\) in the \(\ell\times\ell\) sampling square. Thus \(\Pr(\Delta>z\mid e,u\ne v)=(1-z/\ell)^2\). In a product skeleton, factor edge \(e\) has \(b_i\) copies, and there are exactly \(b_i(b_i-1)\) ordered pairs of distinct copies. Each ordered pair has arclength-pair measure \(\ell_e^2\); all other edge pairs have zero detour. Dividing by \(\Lambda^2\) proves the survival formula. Integrating the survival function against \(qz^{q-1}\) yields the moment formula.

**3. Tomography.** Away from its finitely many knots, the second derivative of \((\ell-z)_+^2\) equals \(2\) for \(z<\ell\) and \(0\) for \(z>\ell\). Its downward jump at \(z=\ell\) is \(2\). Since every coefficient \(b_i(b_i-1)/\Lambda^2\) is positive, the jump locations and sizes recover exactly the asserted weighted aggregate; no cancellation is possible.

**4. Full CDF correction.** For the exceptional edge pair, let \(W=|S-T|\) and \(T_*=\min(S+T,2\ell-S-T)\). For \(0\le a\le\ell\), direct triangular-area integration gives \(\Pr(W\le a)=2a/\ell-(a/\ell)^2\) and \(\Pr(T_*\le a)=(a/\ell)^2\). Their CDF difference equals \(H(a/\ell)\), zero outside \([0,\ell]\). Adding the layer distance \(d_{-i}(u,v)\) and summing over all exceptional ordered edge pairs with mass \(\ell_e^2/\Lambda^2\) gives the stated correction formula. The proof covers all thresholds, including the knots.

## Verification

Two supplied standard-library Python checkers compare the route-classification formula with separate exact-rational shortest-path calculations. The two-factor checker covers 14 combinations of weighted paths, cycles, a star, a triangle, and a diamond (86,336 point-pair comparisons). The multifactor checker covers three- and four-factor products (51,728 comparisons). All 138,064 comparisons passed. The checkers use the finite sample coordinates \(1/7,2/5,4/7,6/7\) and \(1/6,1/3,3/5,4/5\), respectively, and also verify exact elementary CDF identities in the two-factor checker. Reproduce with \`python check_product_detour.py\` and \`python check_product_multifactor.py\` in the directory containing both scripts. Exact-rational finite tests are corroboration, not a proof for all graphs; the four analytic steps above prove the universal statement.

## Relationship to prior work

The original mean-distance-for-shapes literature addresses continuous network distances, while more recent work develops general continuous mean-distance algorithms and metric-graph extremal results. Vertex-distance additivity for Cartesian graph products does not directly control pairs of interior edge points. An earlier special-case calculation for equilateral two-cycle products establishes the \(\mathrm{Beta}(1,2)\) detour law in rectangular toroidal grids; that special case is included here but is not claimed as new. The asserted additional content is the all-factor, arbitrary-geodesic-weights spline law, its exact CDF correction, all positive moments, and edge-length recovery from derivative jumps. The available sources and investigated records did not establish this stronger theorem; literature priority remains subject to further discovery.

## Limitations

Metrically redundant factor edges, graph loops, and multiple edges are excluded: the same-edge route classification may change outside this domain. The inverse statement recovers an aggregate weighted length spectrum, not necessarily the identity of each contributing factor edge or the factor graphs themselves. The metric is the intrinsic sum-product metric and the sampling measure is the one-dimensional skeleton measure. The result does not compare ambient volume-uniform pairs. Historical-priority claims are limited by inaccessible older full texts; no external independent validation has been performed.

## References

- J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471, DOI: 10.1002/jgt.3190060410 (historical context; only publication metadata and abstract available for this comparison).
- J. Cáceres, C. I. Grima, A. Márquez, and A. Moreno-González, *Dilation-free graphs in the \(\ell_1\) metric*, Networks 49 (2007), 168–174, DOI: 10.1002/net.20152 (first made public 2006-11-21; planar dilation question).
- J.-L. De Carufel, C. Grimm, A. Maheshwari, and M. Smid, *Minimizing the Continuous Diameter when Augmenting Paths and Cycles with Shortcuts*, arXiv:1512.02257 (first submitted 2015-12-07; continuous network geometry).
- D. Garijo, A. Márquez, and R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:2103.11676; Results in Mathematics 78 (2023), article 139 (full open-access text checked).
- L. N. Baptista, J. B. Kennedy, and D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952 (full accessible text checked).
