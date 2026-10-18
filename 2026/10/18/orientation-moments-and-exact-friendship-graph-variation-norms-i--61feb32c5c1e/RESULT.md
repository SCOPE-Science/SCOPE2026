# Orientation moments and exact friendship-graph variation norms in free convex Banach lattices

## Finding
Let \(G=(V,E)\) be a finite undirected simple graph, with \(n=|V|\ge2\) and at least one edge. Denote by \(\delta_{e_i}\) the evaluation generator associated with the \(i\)-th unit vector of \(\ell_1^n(\mathbb R)\). The positive graph-variation lattice element is
\[
T_G=\sum_{\{i,j\}\in E}|\delta_{e_i}-\delta_{e_j}|\in \operatorname{FBL}^{(p)}[\ell_1^n].
\]
For an edge orientation \(\sigma\), let \(b_i(\sigma)\) be the number of edges directed out of \(i\) minus those directed into \(i\). For every \(1<p\le\infty\), put \(q=p/(p-1)\), with \(q=1\) at \(p=\infty\). Then
\[
\boxed{\|T_G\|=\max_{\theta\in\mathcal P(\operatorname{Orient}(G))}
\sum_{i\in V}\left(\sum_{\sigma}\theta_\sigma |b_i(\sigma)|^q\right)^{1/q}.}
\tag{1}
\]
Here \(\theta\) ranges over all probability distributions on the finite set of orientations. At \(p=1\), exactly \(\|T_G\|=2|E|\). For each \(1<p\le\infty\), the upper bound \(\|T_G\|\le2|E|\) is attained **if and only if** \(G\) is bipartite. For \(1<p<\infty\), an optimizing distribution in (1) may be chosen with at most \(n\) orientations.

For the friendship graph \(W_r\) made from \(r\ge1\) triangles by identifying one vertex of each triangle (and retaining their other vertices distinct), one has the all-exponent exact identity
\[
\boxed{\|T_{W_r}\|=6r\left(\frac23\right)^{1-1/p}\qquad(1\le p\le\infty),}
\tag{2}
\]
using \(1/\infty=0\). This non-vertex-transitive family has a fixed normalized departure from bipartiteness for every exponent above one, however many triangles are attached.

As additional consequences, the cycle \(C_n\), \(n\ge3\), satisfies
\[
\|T_{C_n}\|=2n\left(\frac{2\lfloor n/2\rfloor}{n}\right)^{1-1/p},\qquad 1\le p\le\infty.
\tag{3}
\]
For the complete graph \(K_n\), \(n\ge2\), and \(1<p\le\infty\),
\[
\|T_{K_n}\|=n^{1/p}\left(\sum_{j=1}^n|n+1-2j|^q\right)^{1/q}.
\tag{4}
\]
The endpoint \(p=1\) equals \(n(n-1)\), consistently with the limiting interpretation of (4).

## Assumptions and scope
All Banach lattices and functions are real. Every graph is finite, simple and undirected; isolated vertices are permitted, but the graph has a nonempty edge set. At \(p=\infty\), the free AM-space is given its canonical supremum norm. Under the concrete free-lattice representation, the element \(T_G\) is the positively homogeneous function \(u\mapsto\sum_{\{i,j\}\in E}|u_i-u_j|\) on \(\ell_\infty^n\). The choice \(1\le p\le\infty\) refers to the free-lattice convexity parameter, not to a graph metric. In (1) the simplex has one coordinate for each orientation of \(G\); the formula is a finite-dimensional optimization, not a claim that evaluating it is polynomial-time.

## Proof
**1. Free-lattice variational norm and orientation duality.** For \(1<p<\infty\), the standard free \(p\)-convex norm representation (Jardón-Sánchez et al., Section 6) gives
\[
\|T_G\|=\sup_{N\ge1}\;\sup_{\sum_{a=1}^{N}|u_i^{(a)}|^p\le1\ (i\in V)}
\left(\sum_{a=1}^{N}\left(\sum_{\{i,j\}\in E}|u_i^{(a)}-u_j^{(a)}|\right)^p\right)^{1/p}.
\tag{5}
\]
Indeed, the weak \(\ell_p\) constraint on \(\ell_\infty^n\)-valued test vectors becomes the displayed independent coordinate constraints because the unit ball of \(\ell_1^n\) has extreme points \(\pm e_i\). For a real vector \(u\), the graph variation \(\sum_E|u_i-u_j|\) is the maximum of \(\sum_i b_i(\sigma)u_i\) over orientations \(\sigma\): orient every edge in the direction that makes its signed difference nonnegative. Duality between finite \(\ell_p\) and \(\ell_q\) norms then transforms the right-hand side of (5) into
\[
\sup_{N}\;\sup_{a_1,\ldots,a_N\ge0,\ \sum_a a_a^q=1}\;
\max_{\sigma_1,\ldots,\sigma_N}\;
\sup_{\sum_a|u_i^{(a)}|^p\le1}
\sum_{i\in V}\sum_{a=1}^{N}a_a b_i(\sigma_a)u_i^{(a)}.
\tag{6}
\]
The innermost supremum separates over \(i\). Hölder equality makes its value
\(\sum_i(\sum_a a_a^q|b_i(\sigma_a)|^q)^{1/q}\). Grouping the weights \(a_a^q\) by orientation yields a probability vector \(\theta\) and exactly the right side of (1). Conversely, every such \(\theta\) is realized in (6) by choosing one index per orientation, coefficients \(a_\sigma=\theta_\sigma^{1/q}\), and the coordinate-wise Hölder extremizers. This proves (1) for finite \(p>1\). At \(p=\infty\), the canonical norm equals \(\max_{|u_i|\le1}\sum_E|u_i-u_j|\), which by the same orientation duality is \(\max_\sigma\sum_i|b_i(\sigma)|\). The right-hand side of (1) for \(q=1\) is linear in \(\theta\) and has this same maximum.

At \(p=1\), triangle inequalities in the free norm give \(\|T_G\|\le\sum_E\|\delta_{e_i}-\delta_{e_j}\|=2|E|\). Conversely, use the \(n\) test vectors \(u^{(a)}=e_a\) in the free \(1\)-convex norm representation. Every coordinate satisfies \(\sum_a|u_i^{(a)}|=1\), while \(\sum_a\sum_E|u_i^{(a)}-u_j^{(a)}|=\sum_i\deg(i)=2|E|\).

**2. Sharp equality test.** For every orientation, \(|b_i(\sigma)|\le\deg(i)\), so (1) yields \(\|T_G\|\le\sum_i\deg(i)=2|E|\). If equality holds for an optimizing distribution and \(1<p\le\infty\), then \(|b_i(\sigma)|=\deg(i)\) at each vertex for every orientation of positive probability (vertices of degree zero impose no restriction). Thus at every nonisolated vertex all incident edges point uniformly inward or uniformly outward. An edge joins one source to one sink; consequently every component is bipartite. Conversely, orient every bipartite component from one color class to the other; the resulting divergence satisfies \(|b_i|=\deg(i)\), attaining the upper bound with a point-mass distribution. This proves the equivalence.

**3. Exact friendship graph.** Write the hub as \(0\) and its \(2r\) leaves as \(1,\ldots,2r\), paired into \(r\) triangles. In any orientation let \(k\) be the number of triangles in which the hub is a source or sink, so its contribution in that triangle is \(\pm2\). On a remaining triangle the hub has one incoming and one outgoing edge. Therefore \(|b_0|\le2k\). Exactly \(2r-k\) leaves have divergence of magnitude \(2\); all other leaves have divergence zero. For every \(q\ge1\), the pointwise bound \(|b_0|^q\le(2r)^q(k/r)\) follows from \(k^q\le r^{q-1}k\).

The objective in (1) is concave in its moment vector \((\mathbb E_\theta|b_i|^q)_i\) and invariant under the automorphism group of the friendship graph, which permutes the triangles and swaps the leaves of each triangle. Average an arbitrary distribution over this group; Jensen's inequality can only increase the objective. The resulting leaf moments are all equal. Put \(t=\mathbb E_\theta k/r\in[0,1]\). The hub contribution is bounded by \(2r\,t^{1/q}\), and each leaf's contribution by \(2(1-t/2)^{1/q}\). Hence
\[
\|T_{W_r}\|\le2r\max_{0\le t\le1}\left[t^{1/q}+2(1-t/2)^{1/q}\right]
\le6r(2/3)^{1/q},
\tag{7}
\]
where the last step is Jensen concavity for the three nonnegative quantities \(t,1-t/2,1-t/2\), whose sum is \(2\). Equality is achieved by the following explicit probability distribution. With probability \(2/3\), orient every hub edge outward, orient the remaining edge of each triangle arbitrarily and symmetrically, independently across triangles. Then \(|b_0|=2r\), and each leaf is active (divergence magnitude \(2\)) with probability \(1/2\). With probability \(1/3\), give the hub one inward and one outward edge in every triangle and orient the leaf-to-leaf edge so that both leaves have divergence magnitude \(2\); then \(b_0=0\). Each leaf is consequently active with total probability \((2/3)(1/2)+1/3=2/3\), matching the hub's activity probability. Thus the hub moment is \((2/3)(2r)^q\) and each leaf moment is \((2/3)2^q\), saturating (7). The case \(p=1\) is already proved, giving (2) for all exponents.

**4. Cycles and complete graphs.** For a vertex-transitive graph the automorphism average makes every vertex moment equal and cannot decrease (1), so
\[
\|T_G\|=n^{1-1/q}\max_\sigma\left(\sum_i|b_i(\sigma)|^q\right)^{1/q}
\qquad(1<p\le\infty).
\tag{8}
\]
In a cycle, every divergence lies in \(\{-2,0,2\}\); vertices with nonzero divergence alternate as source or sink, so there are at most \(2\lfloor n/2\rfloor\) of them. This is attainable by alternating edge directions with at most one neutral vertex. Substitution into (8), followed by the separately checked \(p=1\) endpoint, gives (3).

In a complete graph let \(c=(n-1,n-3,\ldots,1-n)\), the divergence vector of a transitive orientation. For any orientation, if \(b^{\downarrow}\) is its decreasing rearrangement, the sum of its largest \(k\) entries is at most the number \(k(n-k)\) of crossing edges, while the corresponding partial sum of \(c\) equals \(k(n-k)\). Both vectors have total sum zero, so \(c\) majorizes \(b\). Convexity of \(t\mapsto|t|^q\) shows \(\sum_i|b_i|^q\le\sum_i|c_i|^q\), with equality for the transitive orientation, yielding (4). This argument holds also at \(q=1\).

**5. Attaining-distribution support.** For \(1<p<\infty\), let \(v_\sigma=(|b_i(\sigma)|^q)_i\) and \(P=\operatorname{conv}\{v_\sigma\}\subset\mathbb R^n\). The objective \(H(v)=\sum_i v_i^{1/q}\) is strictly increasing in every coordinate. If \(P\) is lower-dimensional, Carathéodory's theorem represents any maximizer with at most \(\dim P+1\le n\) vertices. If \(P\) is full-dimensional, no maximizer of \(H\) can be interior: a small positive shift in every coordinate would remain in \(P\) and strictly increase \(H\). Hence a maximizing point is on a proper face of dimension at most \(n-1\), and again admits a representation using at most \(n\) vertices. All vertices of \(P\) arise from some orientations; duplicate moment vectors cause no difficulty.

## Verification
A standalone Python program `verify.py`, using integer and exact rational arithmetic, enumerates all orientations of complete graphs of orders \(2\) through \(6\), cycles of orders \(3\) through \(11\), and friendship graphs with \(1\) through \(4\) triangles. It tests the complete-graph majorization bounds, the cycle support bound and witnesses, the friendship pointwise moment inequalities, and the exact two-design witness moments for integer \(q\) from \(1\) through \(5\). It reports 168,146 majorization comparisons; 169,330 complete-graph moment comparisons; 4,088 cycle support comparisons; 23,400 friendship pointwise comparisons; and 20 friendship witness-moment checks. All passed. The script independently reconstructs the required orientation vectors from edges. Its finite tests are a supplementary reproducibility check, not a substitute for the all-dimensional, all-exponent proof above. Execute with `python3 verify.py`.

## Relationship to prior work
The starting input is the published functional representation of the free \(p\)-convex lattice norm, established by Jardón-Sánchez, Laustsen, Taylor, Tradacete and Troitsky. Oikhberg, Taylor, Tradacete and Troitsky study the general structural theory of these lattices; Oikhberg studies their unit-ball geometry. The score-vector polytope of graph orientations is connected to classical tournament-score and graphical-zonotope ideas, including the work of Sánchez and Kolesnik, but these sources do not state the mixed coordinate-moment optimization (1), the bipartiteness equality classification for this lattice element, or the non-transitive friendship profile (2). The orientation reduction and equality witnesses above are distinct additional deductions from the general norm representation. No priority claim is made beyond the inspected material.

## Limitations
The formula is for real scalars and finite graphs, and the full exact friendship evaluation is only asserted for the specified windmill family. The general orientation simplex has exponentially many vertices; no efficient algorithm for arbitrary graphs is asserted. The finite enumerations test bounded orders and integer conjugate exponents and do not prove the infinite families; those are established by the analytic derivation. Independent validation has not been performed. Equivalent statements hidden in older graph-variation or nonlinear summing literature remain a possible originality risk.

## References
1. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices under convexity conditions*, arXiv:2101.03510 (first posted 2021-01-10), Section 6, https://arxiv.org/abs/2101.03510.
2. T. Oikhberg, M. A. Taylor, P. Tradacete and V. G. Troitsky, *Free Banach lattices*, arXiv:2210.00614 (first posted 2022-10-02), Section 2 and structural sections, https://arxiv.org/abs/2210.00614.
3. T. Oikhberg, *Geometry of unit balls of free Banach lattices, and its applications*, arXiv:2303.05209 (first posted 2023-03-09), Sections 1–3, https://arxiv.org/abs/2303.05209.
4. M. Sánchez and B. Kolesnik, *The geometry of random tournaments*, arXiv:2009.09322 (first posted 2020-09-19), introduction and score-polytope discussion, https://arxiv.org/abs/2009.09322.
