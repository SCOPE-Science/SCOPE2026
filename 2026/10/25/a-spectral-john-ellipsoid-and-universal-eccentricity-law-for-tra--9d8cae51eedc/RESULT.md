# A spectral John ellipsoid and universal eccentricity law for transitive bipartite stable-set polytopes

## Finding
Let \(G\) be a finite, connected, simple, bipartite graph that is both vertex-transitive and edge-transitive, with \(N\) vertices and common degree \(d\ge3\). Its stable-set polytope is
\[
P_G=\operatorname{conv}\{\mathbf1_S:S\subseteq V(G)\text{ is independent}\}\subset\mathbb R^N.
\]
Write \(A_G\) for the adjacency matrix and \(H=dI_N+A_G\) for the signless graph Laplacian. There is a **unique** \(r\in(1,\sqrt2)\) solving
\[
\frac{d r(r+2)}{2N}\operatorname{tr}\bigl((drI_N+H)^{-1}\bigr)=1.\tag{1}
\]
Set \(a=1/(r+2)\), \(k=2(r+2)/(dr)\), and \(Q^{-1}=k(drI_N+H)\). The unique maximal-volume inscribed ellipsoid, in the standard Euclidean metric and original indicator coordinates, is
\[
E_G=\bigl\{x:(x-a\mathbf1)^TQ^{-1}(x-a\mathbf1)\le1\bigr\}.\tag{2}
\]
**Every** one of its \(N+Nd/2\) nonnegativity and edge facets is tangent to \(E_G\). Its exact Euclidean volume is \(\pi^{N/2}/(\Gamma(N/2+1)\sqrt{\det Q^{-1}})\). The squared-semiaxis condition number is exactly
\[
\frac{\lambda_{\max}(Q)}{\lambda_{\min}(Q)}=\frac{r+2}{r}\in(1+\sqrt2,3).\tag{3}
\]
For **any sequence** of graphs obeying these assumptions with degrees \(d\to\infty\), the scalar \(r\to\sqrt2\) and the squared-semiaxis condition number tends to \(1+\sqrt2\). This includes hypercubes and crown graphs of growing degree, not only complete bipartite graphs.

## Assumptions and scope
The graph is simple, connected, bipartite, vertex-transitive and edge-transitive, and \(d\ge3\). Vertex and edge transitivity are used separately to make the two facet-support values constant over their respective orbits. The vertex-space dimension is \(N\); the ellipsoid is not a matching-polytope ellipsoid in edge coordinates. The inequality description is
\[
P_G=\{x\in\mathbb R^N:x_v\ge0\ (v\in V),\ x_u+x_v\le1\ (uv\in E)\}.\tag{4}
\]
This description is exact because the unsigned vertex-edge incidence matrix of a bipartite graph becomes an oriented incidence matrix after changing row signs on one part; its transpose, augmented by coordinate bounds, is totally unimodular. All vertices of (4) are integral and consequently are indicator vectors of independent sets. The graph has no isolated vertices, so each coordinate is at most one. These inequalities define distinct facets: the coordinate face contains the origin and every other singleton indicator vector, and for an edge \(uv\), each \(w\notin\{u,v\}\) is nonadjacent to at least one endpoint (bipartiteness excludes triangles); this gives \(N\) affinely independent tight stable-set vertices. No further facets are needed.

## Proof
**Spectral scalar.** Let \(\mu_1,\ldots,\mu_N\) be the eigenvalues of \(H\) and put \(z_j=\mu_j/d\). Positive semidefiniteness of the unsigned incidence Gram matrix and the bound \(\|A_G\|\le d\) show \(0\le z_j\le2\). Also
\[
\frac1N\sum_j z_j=1,\qquad
\frac1N\sum_j(z_j-1)^2=\frac1d.\tag{5}
\]
Define \(R(r)=r(r+2)(2N)^{-1}\sum_j(r+z_j)^{-1}\). Each summand increases strictly with \(r>0\) because
\[
\frac{d}{dr}\frac{r(r+2)}{r+z}=
\frac{r^2+2zr+2z}{(r+z)^2}>0.\tag{6}
\]
At \(r=1\), the chord inequality \((1+z)^{-1}\le1-z/3\) for \(0\le z\le2\) gives \(R(1)\le1\). This inequality is strict for \(d\ge3\): if all eigenvalues lay in \(\{0,2d\}\), then \(\operatorname{tr}(H^2)=2Nd^2\), but direct expansion gives \(\operatorname{tr}(H^2)=N(d^2+d)\), forcing \(d=1\). At \(r=\sqrt2\), strict Jensen convexity gives
\[
R(\sqrt2)>
\frac{\sqrt2(2+\sqrt2)}{2(1+\sqrt2)}=1,\tag{7}
\]
since the spectral variance in (5) is positive. Continuity and strict monotonicity prove existence and uniqueness of the root in (1), with \(1<r<\sqrt2\).

**Tangencies.** Set \(S=drI_N+H\). Define \(b=1-2a=r/(r+2)\). For the ellipsoid (2), the squared support radius of a nonnegativity facet is \(Q_{vv}\). Vertex transitivity and (1) yield
\[
Q_{vv}=\frac{1}{Nk}\operatorname{tr}(S^{-1})=
\frac{2}{kd r(r+2)}=a^2.\tag{8}
\]
For each edge \(e=uv\), set \(z_e=e_u+e_v\). Since \(H=\sum_{e\in E}z_ez_e^T\), edge transitivity and \(|E|=Nd/2\) imply
\[
\begin{aligned}
z_e^TQz_e&=\frac1{k|E|}\operatorname{tr}(HS^{-1})\\
&=\frac{N-dr\operatorname{tr}(S^{-1})}{kNd/2}\\
&=\frac{2r}{kd(r+2)}=b^2.
\end{aligned}\tag{9}
\]
Thus all the inequalities in (4) are attained by supporting hyperplanes of (2), and the ellipsoid is contained in (4).

**Global maximality, not merely symmetry.** Use the positive weights
\[
w_v=\frac2{r+2}\quad(v\in V),\qquad
w_e=\frac{2r}{d(r+2)}\quad(e\in E).\tag{10}
\]
After the affine map \(y=Q^{-1/2}(x-a\mathbf1)\), the contact vectors on the unit sphere are \(-Q^{1/2}e_v/a\) and \(Q^{1/2}z_e/b\). Their weighted vector sum is zero because every vertex meets \(d\) edges and \(w_v/a=d w_e/b=2\). Their weighted second moment is
\[
Q^{1/2}\left(\frac{w_v}{a^2}I_N+
\frac{w_e}{b^2}H\right)Q^{1/2}
=Q^{1/2}\,k(drI_N+H)\,Q^{1/2}=I_N.\tag{11}
\]
These two identities, with strictly positive weights and actual facet tangencies, are John's sufficient optimality certificate; hence (2) is the **unique** maximal-volume inscribed ellipsoid. The determinant formula follows immediately.

**Eccentricity and limit.** Bipartiteness and connectedness imply that \(H\) has eigenvalue zero (the signed bipartition vector), while \(H\mathbf1=2d\mathbf1\). All its eigenvalues lie between these two extremes, so (3) follows from (2). Finally, (5) implies that the empirical distribution of \(z_j\) concentrates at one as \(d\to\infty\). Therefore \(R(r)\) tends uniformly on \([1,\sqrt2]\) to \(r(r+2)/(2(r+1))\). The latter has its unique root at \(r=\sqrt2\). Monotonicity and the fixed bracket give \(r\to\sqrt2\), yielding the asserted universal condition-number limit.

## Verification
The standalone `checker.py` constructs complete bipartite graphs, crown graphs, hypercubes and even cycles, computes the spectral root and ellipsoid matrix, and checks all individual facet tangencies and both John moment equations against direct matrices. Its observed output includes `VERIFY_OK graphs= 13 facet_norms= 893`. These finite numerical checks do not substitute for the proof of (1)–(11); the cycle tests exercise the method outside the new degree-at-least-three scope.

For one explicit noncomplete example, the crown graph on two parts of size four is cubic and has \(r\approx1.296539169755\). For the three-dimensional cube graph, the parameter has the same value (the graphs are isomorphic); for the four-dimensional cube, \(r\approx1.329701905030\).

## Relationship to prior work
The stable-set polytope and its identification with chain polytopes for comparability graphs are standard. Aliniaeifard, Benedetti, Bergeron, Li and Saliola (arXiv:1804.00360, first public 2018-04-02) study their vertex-edge graphs and diameter, not the John ellipsoid. Kohl, Olsen and Sanyal's *Unconditional Reflexive Polytopes* (2020), Section 4, gives the perfect-graph facet description and duality, not the ellipsoid or eccentricity limit.

Related published mathematical findings calculate John ellipsoids of **complete** two-level chain polytopes (corresponding to complete bipartite graphs), of balanced complete multipartite stable-set polytopes, and of vertex/edge-transitive **fractional matching** polytopes. The complete-bipartite specialization and the even-cycle specialization of the present spectral formula are therefore not advanced as independent discoveries. The broader statement applies to noncomplete, vertex/edge-transitive bipartite graphs of degree at least three (e.g., crown graphs and hypercubes), where the incidence-space dimensions and facet structures differ from fractional matching polytopes. The new full-family spectral equation, all-facet John certificate and universal high-degree eccentricity law are the claimed additions. Relevant record summaries were accessible, but some potentially overlapping full records were not; see limitations.

## Limitations
This theorem requires both vertex and edge transitivity and bipartiteness; it does not assert the same formula for irregular graphs or general vertex-transitive graphs. It determines the ellipsoid volume through a determinant rather than a closed expression involving only \(N,d\), because the graph spectrum matters. No independent validation has been performed. A possibly equivalent general ellipsoid principle under incidence-matrix transposition remains a bibliographic risk; the available abstract/record material did not resolve every such comparison.

## References
1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first posted 2018-04-02, https://arxiv.org/abs/1804.00360 .
2. M. Kohl, M. Olsen and R. Sanyal, *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry, DOI:10.1007/s00454-020-00199-8, https://link.springer.com/article/10.1007/s00454-020-00199-8 .
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948; K. Ball, *Ellipsoids of maximal volume in convex bodies*, Geometriae Dedicata, 1992. Standard John-contact criterion.
