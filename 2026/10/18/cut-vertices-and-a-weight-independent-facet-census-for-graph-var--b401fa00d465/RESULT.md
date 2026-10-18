# Cut vertices and a weight-independent facet census for graph variation Banach balls

## Finding
Let \(G=(V,E)\) be a finite simple graph, \(|V|=n\ge1\), and assign strictly positive real weights \(w_{ij}\) to the edges. Define the graph variation norm on real vertex signals by
\[
N_G(f)=\max_{i\in V}|f_i|+\sum_{\{i,j\}\in E}w_{ij}|f_i-f_j|.
\]
For a sign vector \(s\in\{-1,1\}^{V}\), write \(C_w(s)=\sum_{\{i,j\}\in E:s_i\ne s_j}w_{ij}\). **The entire unit ball has exactly \(2^n\) vertices**:
\[
B_{N_G}=\operatorname{conv}\left\{\frac{s}{1+2C_w(s)}:s\in\{-1,1\}^V\right\}.
\]
All the displayed vertices are exposed, even when \(G\) is disconnected. Consequently, for every real coefficient vector \(c\),
\[
N_G^*(c)=\max_{s\in\{-1,1\}^{V}}\frac{|\sum_i c_i s_i|}{1+2C_w(s)}.
\]

For a positively weighted path \(P_n\), \(n\ge2\), with successive weights \(w_1,\ldots,w_{n-1}\), the unit ball has exactly
\[
\boxed{(n+2)2^{n-2}}
\]
facets, regardless of the weights. More precisely, each facet has a unique supporting inequality
\[
\sigma f_j+\sum_{i=1}^{n-1}w_i\epsilon_i(f_{i+1}-f_i)\le1,
\]
where \(j\in\{1,\dots,n\}\), \(\sigma,\epsilon_i\in\{-1,1\}\), and the adjacent signs obey \(\epsilon_{j-1}=\sigma\) if \(j>1\) and \(\epsilon_j=-\sigma\) if \(j<n\). Every such inequality defines a facet, and no other facets exist.

## Assumptions and scope
The graph is finite, the vertex signals and weights are real, and each existing edge has strictly positive weight. The norm is the *sum* of the sup norm and graph total variation, not the maximum of two seminorms. The path facet law is for the full-dimensional ball in \(\mathbb R^n\), without fixing a base vertex or quotienting constants. The convention for the empty edge set gives the ordinary cube.

## Proof
**1. Graph coarea decomposition.** For any nonzero \(f\) put \(r=\|f\|_\infty\) and \(s_i(t)=1\) if \(f_i>t\), otherwise \(-1\), for \(-r<t<r\). Integrating each coordinate gives \(f_i=\tfrac12\int_{-r}^r s_i(t)\,dt\). For each edge, the signs differ on an interval of length \(|f_i-f_j|\), so \(\int_{-r}^r C_w(s(t))\,dt=\sum_{ij\in E}w_{ij}|f_i-f_j|\). Hence
\[
f=\frac12\int_{-r}^r s(t)\,dt,
\qquad
N_G(f)=\frac12\int_{-r}^r[1+2C_w(s(t))]\,dt.
\]
The normalized signal \(f/N_G(f)\) is therefore a convex combination of displayed points, with weights \([1+2C_w(s(t))]dt/[2N_G(f)]\). Conversely each displayed point has norm one, proving equality of the unit ball and their convex hull. Only finitely many sign patterns occur in the integral.

**2. Every sign point is exposed.** Orient each edge arbitrarily. For a given sign vector \(s\), define
\[
L_s(f)=\frac1n\sum_i s_i f_i+\sum_{(i,j):s_i\ne s_j}w_{ij}\frac{s_i-s_j}{2}(f_i-f_j).
\]
Each term is bounded above by its corresponding summand in \(N_G(f)\), so \(L_s(f)\le N_G(f)\). Equality in the first term \(\frac1n\sum_i s_i f_i\le\|f\|_\infty\), when \(f\ne0\), requires simultaneously \(f_i=s_i\|f\|_\infty\) for all \(i\). This makes the equality direction the positive ray of \(s\). On the unit sphere it is exactly \(s/(1+2C_w(s))\). Thus each vertex is uniquely exposed by \(L_s\). The support formula for \(N_G^*(c)\) follows from the vertex representation.

**3. Full list of path facets.** On a path, the norm is the maximum of the \(n2^n\) linear forms
\[
F_{j,\sigma,\epsilon}(f)=\sigma f_j+\sum_{i=1}^{n-1}w_i\epsilon_i(f_{i+1}-f_i).
\]
For such a form to define a genuine facet, there must be a full-dimensional open set of signals on which it uniquely maximizes the norm. Such an open set forces \(j\) to be the unique absolute-value maximizer, with sign \(\sigma\), and every adjacent increment to have the indicated nonzero sign \(\epsilon_i\). The local maximum conditions imply \(\epsilon_{j-1}=\sigma\) when \(j>1\) and \(\epsilon_j=-\sigma\) when \(j<n\).

Conversely, suppose these conditions hold. Take \(f_j=\sigma\) and recursively choose the other coordinates with arbitrarily small nonzero differences having the prescribed signs, with the two neighboring coordinates moving toward zero from \(f_j\). All other coordinates can remain strictly in \((-1,1)\) by making the step magnitudes sufficiently small. Thus \(j\) is uniquely absolute-maximal, all increments are nonzero with exactly the prescribed signs, and \(F_{j,\sigma,\epsilon}(f)=N_G(f)\) is the unique maximizing linear form on a full-dimensional open cone. Intersecting this cone with \(F_{j,\sigma,\epsilon}=1\) yields a relatively open \((n-1)\)-dimensional patch of the unit sphere, proving the facet property. No other facet exists because every point of the ball boundary maximizes one of the finitely many forms, and every facet has a relative interior point with a unique defining linear form among distinct forms. All admissible forms are distinct: their gradients in the edge-difference basis and constant coordinate identify \(\epsilon\), \(j\), and \(\sigma\) (strictly positive weights are essential here).

The two endpoints each contribute \(2^{n-1}\) admissible inequalities (two choices of \(\sigma\), and \(n-2\) free edge signs). Each of the \(n-2\) interior vertices contributes \(2^{n-2}\) inequalities. Summing gives \(2^n+(n-2)2^{n-2}=(n+2)2^{n-2}\). This remains correct for \(n=2\), where there are no interior indices.

**4. Minimum-cut decision for the dual norm.** For \(\lambda\ge0\), the inequality \(\max_s c\cdot s/(1+2C_w(s))>\lambda\) is equivalent to \(\max_s(c\cdot s-2\lambda C_w(s))>\lambda\). Writing \(s_i=2x_i-1\), \(x_i\in\{0,1\}\), converts the right-hand maximization into minimization of a sum of arbitrary linear binary unary terms and nonnegative edge-disagreement costs \(2\lambda w_{ij}|x_i-x_j|\). The latter is the standard binary \(s\)-\(t\) minimum-cut energy. The absolute value is handled by also testing \(-c\).

## Verification
The standalone `verification/verify.py` uses exact rational linear algebra. It checked exposed graph-BV sign vertices and the predicted path-facet count for paths through six vertices, several rational weight assignments, and nonpath graphs, with 880 exact assertions passing. These finite tests are independent sanity checks; the claims for all finite graphs and all positive real edge weights are established by the proof above, not by finite enumeration.

## Relationship to prior work
Graph total variation and its cut-based coarea geometry are well-established, including the graph-variation framework in Hansen and Bianchi (2023). The graph-side convex-hull proof intentionally uses this classical layer-cake principle. The contribution isolated here is the fully exposed vertex representation for the sum of graph variation and sup norm, together with the explicit complete and weight-independent facet census on every finite weighted path. Work on discrete \(\ell_\infty\)-gradient minimization studies a different maximum-gradient functional, not this additive variation norm or its weighted-path facet spectrum.

## Limitations
No assertion is made for infinite graphs, zero or negative edge weights in the facet theorem, unbounded signals, complex signals, or higher-order variation. The algorithmic statement is a min-cut *threshold reduction*; it is not a claim of strongly polynomial exact rational optimization in the presence of arbitrary real oracle input. The argument uses standard coarea machinery, and unindexed earlier facet classifications of equivalent polytopes remain a bibliographic risk.

## References
1. M. Hansen and F. Bianchi, *Total Variation Graph Neural Networks*, arXiv:2211.06218 (first posted November 11, 2022); Proceedings of Machine Learning Research 202 (2023). https://arxiv.org/abs/2211.06218
2. *Structural analysis of an L-infinity variational problem and relations to distance functions*, arXiv:2001.07411, https://arxiv.org/abs/2001.07411.
3. A. Chambolle, A. Giacomini, L. Lussardi, *Continuous limits of discrete perimeters*, arXiv:0902.2313, https://arxiv.org/abs/0902.2313.
