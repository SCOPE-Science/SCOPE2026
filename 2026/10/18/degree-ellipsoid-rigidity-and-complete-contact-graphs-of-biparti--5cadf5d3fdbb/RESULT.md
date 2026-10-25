# Degree-ellipsoid rigidity and complete contact graphs of bipartite graphical discotopes

## Finding

Let \(G=(V,E)\) be a finite simple graph without isolated vertices, let \(n=|V|\), \(m=|E|\), and denote its positive vertex degrees by \(d_i\). For each edge \(\{i,j\}\), define the filled Euclidean unit disk
\[
D_{ij}=\{s e_i+t e_j:s^2+t^2\le1\}\subset\mathbb R^V,
\qquad
K_G=\sum_{\{i,j\}\in E}D_{ij}.
\]
Its **unique John ellipsoid**, for every such graph, is
\[
\boxed{J_G=\Bigl\{x:\sum_{i\in V}\frac{x_i^2}{d_i^2}\le1\Bigr\}.}
\]
If \(G\) is connected and \(n\ge3\), the entire set \(\partial K_G\cap\partial J_G\) is precisely \(\{\pm d_i e_i:i\in V\}\), of cardinality \(2n\).

Suppose additionally that \(G\) is connected and bipartite with nonempty vertex classes \(A,B\), where \(|A|=p\), \(|B|=q\), and is **biregular**: every vertex in \(A\) has degree \(d_A\) and every vertex in \(B\) has degree \(d_B\). Write \(m=p d_A=q d_B\). Then its **unique Löwner ellipsoid** is
\[
\boxed{L_G=\Bigl\{x:\sum_{i\in V}\frac{x_i^2}{m d_i}\le1\Bigr\}.}
\]
Its complete contact locus \(K_G\cap\partial L_G\) consists of the arcs
\[
\boxed{
\begin{aligned}
x_i&=d_A\varepsilon_i\cos\theta &&(i\in A),\\
x_j&=d_B\eta_j\sin\theta &&(j\in B),\\
&0\le\theta\le\frac\pi2, &&\varepsilon\in\{\pm1\}^p,\quad\eta\in\{\pm1\}^q.
\end{aligned}}
\]
For \(n\ge3\), these arcs form the embedded graph \(K_{2^p,2^q}\). It has exactly \(2^{p+q}\) arcs, \(2^p+2^q\) distinct endpoints, and first Betti number
\[
\boxed{\beta_1=(2^p-1)(2^q-1).}
\]
These statements concern **filled coordinate-plane disks**, not coordinate line segments.

## Assumptions and scope

All constructions use the ambient standard Euclidean metric and the center of each summand disk is the origin. The first assertion requires only positive degrees; the exact inner contact locus assumes connectedness and at least three vertices. The outer ellipsoid and full outer contact locus assume connected, bipartite, **biregular** graphs; the conclusion is not extended to non-biregular graphs. The graph \(K_{1,1}\) is a single disk: both ellipsoids are that disk and its contact set is its boundary circle, so the graph-count formula is stated for \(n\ge3\).

The John ellipsoid means the unique maximum-volume ellipsoid *inside* \(K_G\). The Löwner ellipsoid means the unique minimum-volume ellipsoid *containing* \(K_G\). Contact sets here are intersections of boundaries of the discotope and the corresponding ellipsoid, not tangent hyperplanes counted with multiplicity.

## Proof

**1. A pair of universal sharp support bounds.** For \(u\in\mathbb R^V\), Minkowski additivity gives
\[
h_{K_G}(u)=\sum_{\{i,j\}\in E}\sqrt{u_i^2+u_j^2}.
\]
Write \(v_{ij}=u_i e_i+u_j e_j\). Since \(\sum_{\{i,j\}\in E}v_{ij}=\sum_i d_i u_i e_i\), the Euclidean triangle inequality gives
\[
\sqrt{\sum_i d_i^2u_i^2}\ \le\ h_{K_G}(u).
\]
Cauchy–Schwarz and the identity \(\sum_{\{i,j\}\in E}(u_i^2+u_j^2)=\sum_i d_i u_i^2\) give
\[
h_{K_G}(u)\ \le\ \sqrt{m\sum_i d_i u_i^2}.
\]
The support functions at the two ends are exactly those of \(J_G\) and \(L_G\), respectively. Hence \(J_G\subseteq K_G\subseteq L_G\) for **every** graph without isolated vertices (the second inclusion need not be minimal).

**2. Optimality of the inner ellipsoid and its exact contacts.** The convex body \(K_G\) is invariant under every independent coordinate sign change because every disk is invariant under such reflections. Uniqueness of the John ellipsoid forces it to share these symmetries, hence to be centered at zero and have a diagonal quadratic form. For any contained coordinate-axis ellipsoid of semiaxes \(a_i\), its support at \(e_i\) is \(a_i\), whereas \(h_{K_G}(e_i)=d_i\). Therefore \(a_i\le d_i\) for all \(i\). The explicitly contained \(J_G\) simultaneously achieves every upper bound, so it maximizes \(\prod_i a_i\). Uniqueness proves the assertion without restricting to regular graphs.

The inclusion is tangent in both support directions \(\pm e_i\), giving contacts \(\pm d_i e_i\). Conversely an intersection point of their boundaries has a common supporting hyperplane; thus the support triangle inequality above is an equality for some nonzero normal \(u\). Equality of Euclidean triangle norms requires all nonzero vectors \(v_{ij}\) to be positively collinear. In a connected graph on at least three vertices, this is possible only when \(u\) has exactly one nonzero coordinate: if the support of \(u\) has three vertices, no edge vector can cover all its coordinates; if it has two vertices, connectedness ensures an incident edge from the pair to a third vertex, breaking collinearity. Hence all contacts have been listed. This argument does not assert a finite contact set for the one-edge graph.

**3. Exact equality in the outer bound.** Suppose \(G=A\sqcup B\) is connected and bipartite. Equality in the Cauchy–Schwarz upper bound requires the \(m\) positive numbers \(\sqrt{u_i^2+u_j^2}\), indexed by edges, to be identical. The edge equations say that \(u_i^2+u_j^2=c\) for every edge; along paths of even length this forces \(|u_i|\) to be constant within \(A\) and within \(B\). As the graph is connected, there are only two moduli. Normalize them to \(\cos\theta\) and \(\sin\theta\), with \(0\le\theta\le\pi/2\), and assign independent signs \(\varepsilon,\eta\) to all coordinates.

For these normals each constituent disk has a unique exposed point, since its normal projection has norm one; summing their contributions gives exactly the displayed point \(x(\theta,\varepsilon,\eta)\). Its quadratic outer-ellipsoid value is
\[
\sum_{i\in A}\frac{d_A^2\cos^2\theta}{m d_A}+
\sum_{j\in B}\frac{d_B^2\sin^2\theta}{m d_B}
=\cos^2\theta+\sin^2\theta=1.
\]
Conversely, if a point of \(K_G\) lies on \(\partial L_G\), its unique outer-ellipsoid normal makes both support functions equal, forcing precisely this equality case. Thus the parametrization is complete, including the endpoint cases \(\theta=0,\pi/2\).

**4. Minimality of the enclosing ellipsoid, with an explicit contact certificate.** Put \(n=p+q\) and choose \(\cos^2\theta=p/n\), \(\sin^2\theta=q/n\). The contact point corresponding to any independent sign choice has coordinates \(d_A\varepsilon_i\sqrt{p/n}\) on \(A\) and \(d_B\eta_j\sqrt{q/n}\) on \(B\). Apply the diagonal linear transformation with entries \((m d_i)^{-1/2}\), taking \(L_G\) to the Euclidean unit ball. Because \(m=p d_A=q d_B\), these \(2^n\) contact points become *all* sign vectors \((\pm1,\ldots,\pm1)/\sqrt n\), with mean zero and covariance \(I_n/n\).

For any ellipsoid \(\{z:(z-c)^T Q^{-1}(z-c)\le1\}\) containing these sign points, averaging the inequalities gives \(\operatorname{tr}(Q^{-1})/n+c^TQ^{-1}c\le1\). Arithmetic–geometric mean then gives \(\det Q\ge1\), with equality only for \(Q=I_n\) and \(c=0\). Hence the unit ball is their unique Löwner ellipsoid. Since the transformed discotope contains those points and is itself contained in the ball, the same uniqueness holds for the whole body. Undo the transformation to obtain \(L_G\).

**5. Contact topology.** At \(\theta=0\), only the signs on \(A\) matter, yielding exactly \(2^p\) distinct endpoints. At \(\theta=\pi/2\), only the signs on \(B\) matter, yielding \(2^q\) others. Every pair of endpoint choices determines one arc with \(0<\theta<\pi/2\), and no two such open arcs intersect (all coordinates are nonzero there and identify their signs). This is exactly a geometric embedding of \(K_{2^p,2^q}\), so its cycle rank equals its number of edges minus its number of vertices plus one, or \((2^p-1)(2^q-1)\). No completeness assumption on the original graph was needed.

## Verification

The accompanying standalone Python checker tests both support bounds on 8,500 seeded direction profiles drawn from connected paths, stars, rectangular complete bipartite graphs, even cycles and a sparse incidence graph, then verifies 1,348 exact-axis/outer-contact profiles and 193 normalized covariance entries. It uses only the Python standard library and is run as `python graph_discotope_checker.py`. Its output is `PASS support_inequalities=8500; exact_axis_and_outer_contacts=1348; normalized_covariance_entries=193; ...`. These checks are finite corroborations only; steps 1–5 are the complete proof for all admissible graphs.

As exact, nonnumerical intermediate certificates, the two support inequalities are the triangle inequality for the vectors \(v_{ij}\) and Cauchy–Schwarz for the list of edge norms. The covariance certificate in step 4 is algebraic and establishes global Löwner minimality, rather than merely best diagonal approximation.

## Relationship to prior work

Gesmundo and Meroni introduce and develop the face and algebraic-boundary geometry of discotopes, notably finite Minkowski sums of two-dimensional disks. Mathis and Meroni study a different operation—fiber bodies of zonoids and discotopes. Both furnish the underlying natural convex-body class but their inspected relevant analyses do not classify John–Löwner ellipsoids of graph-indexed disk sums.

An existing classification for **regular** graphical discotopes gives spherical extremal ellipsoids and a bipartite/nonbipartite outer-contact distinction; the present theorem recovers its regular bipartite case as a special case. Its new portions are the all-graph degree-dependent John ellipsoid, the complete optimal inner contact set for arbitrary connected graphs, and the nonregular biregular bipartite Löwner ellipsoid with its explicitly embedded contact graph. Related graphical zonotope and symmetric-edge-polytope ellipsoid results concern line-segment sums or root-vector hulls, not disk sums, so their formulas are not interchangeable with these.

## Limitations

No formula for the **minimum-volume enclosing ellipsoid** is claimed for arbitrary non-biregular graphs: \(L_G\) remains a valid enclosing ellipsoid there but can fail to be minimal. The precise contact-locus topology requires connectedness and biregularity of a bipartite graph. The special case of an isolated edge has infinitely many John contacts. Prior work may contain the same result under general zonoid-ellipsoid or convex-body equality-case terminology; independent bibliographic and mathematical auditing has not been performed.

## References

- L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406, first submitted 26 May 2021; *Discrete & Computational Geometry*, 2022. https://arxiv.org/abs/2105.12406.
- F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241, first submitted 1 November 2021; *Le Matematiche* 77 (2022), 143–171. https://arxiv.org/abs/2111.01241.
