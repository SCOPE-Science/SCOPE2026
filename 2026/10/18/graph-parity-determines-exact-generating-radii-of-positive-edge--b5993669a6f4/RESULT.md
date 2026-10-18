# Graph parity determines exact generating radii of positive edge averages

## Finding

Let \(G=(V,E)\) be a finite simple undirected graph with \(E\neq\varnothing\). Assign to every oriented edge \(e=(u(e),v(e))\) a weight \(\theta_e\in(0,1)\), and define the real linear operator
\[
T_{G,\theta}:\ell_\infty(V;\mathbb R)\longrightarrow\ell_\infty(E;\mathbb R),\qquad
(T_{G,\theta}x)_e=\theta_e x_{u(e)}+(1-\theta_e)x_{v(e)}.
\]
Write \(V_+=\{v\in V:\deg_G(v)>0\}\) and \(k=|V_+|\ge2\). Then \(\|T_{G,\theta}\|=1\), and its maximal quantitative generating radius is
\[
\boxed{\quad r(T_{G,\theta})=
\begin{cases}
1,&G\text{ is not bipartite},\\[2pt]
1-\frac{2}{k},&G\text{ is bipartite}.
\end{cases}\quad}
\]
The value depends on graph bipartiteness and the number of non-isolated vertices, but not on its remaining combinatorics, edge orientations, or strictly interior positive weights.

There is a more precise geometric statement. Define
\[
A_G=\{\sigma\in\{-1,1\}^V:\text{some }\{u,v\}\in E\text{ has }\sigma_u=\sigma_v\},
\qquad K_G=\operatorname{conv}(A_G).
\]
The set \(K_G\) is exactly the convex hull of the norm-attaining vectors in the input unit ball. For \(a\in\mathbb R^V\), write \(L(a)=\sum_{v\in V}|a_v|\) and \(m(a)=\min_{v\in V_+}|a_v|\). Choose any cube sign vector \(\sigma\) maximizing \(\sum_v a_v\sigma_v\). Then the support function of \(K_G\) satisfies
\[
h_{K_G}(a)=
\begin{cases}
L(a),&\text{if some edge is monochromatic under }\sigma,\\
L(a)-2m(a),&\text{if every edge is bichromatic under }\sigma.
\end{cases}
\]
If multiple maximizing sign vectors exist, both prescriptions agree whenever their edge conditions differ, because then \(m(a)=0\).

## Assumptions and scope

All spaces and coefficients are real. The graph has finitely many vertices, at least one edge, and no loops or multiple edges. It may be disconnected and may have isolated vertices. Every edge coefficient is strictly between zero and one; endpoint values \(0\) and \(1\) are excluded. There is no restriction that the two weights on distinct edges agree.

For a norm-one operator \(T:X\to Y\), let \(\operatorname{att}(T)=\{x\in B_X:\|Tx\|=1\}\). Define the maximal generating radius, including zero, by
\[
r(T)=\sup\{r\in[0,1]:rB_X\subseteq\overline{\operatorname{conv}}\operatorname{att}(T)\}.
\]
For finite-dimensional \(X\), the compact-operator criterion of Kadets, Martín, Merí and Quero identifies the positive values of this radius with their quantitative \(r\)-generating notion. Their convention names \(r\)-generating only when \(r>0\); a displayed value \(r(T)=0\) means no positive generating radius exists.

## Proof

**1. Norm-attaining faces.** Every edge entry of \(T\) is a convex combination, so \(\|T\|\le1\). Equality follows on the constant-one vertex vector. For \(x\in[-1,1]^V\) and any edge \(e=\{u,v\}\), strict positivity \(0<\theta_e<1\) gives
\[
|\theta_e x_u+(1-\theta_e)x_v|=1
\quad\Longleftrightarrow\quad
(x_u,x_v)=(1,1)\text{ or }(-1,-1).
\]
The norm-attaining set is therefore a finite union of cube faces, one face for each equal-sign choice on the ends of an edge. Every such face is the convex hull of its sign vertices. Thus \(\operatorname{conv}(\operatorname{att}(T))=K_G\).

**2. Exact support function.** Fix \(a\in\mathbb R^V\) and choose a sign vector \(\sigma\) attaining the unconstrained cube maximum \(a\cdot\sigma=L(a)\). If \(\sigma\in A_G\), the support of \(K_G\) equals \(L(a)\) because \(K_G\subseteq[-1,1]^V\). Suppose instead that \(\sigma\) is a proper two-coloring of every edge. Every allowed sign vector \(\tau\in A_G\) differs from \(\sigma\) on at least one non-isolated vertex; otherwise each edge would remain bichromatic. Since \(\sigma\) maximizes \(a\cdot\sigma\), changing coordinate \(v\) decreases this pairing by exactly \(2|a_v|\), possibly zero. Hence
\[
a\cdot\tau\le L(a)-2\min_{v\in V_+}|a_v|.
\]
Conversely, flip precisely a vertex \(v\in V_+\) achieving this minimum. That makes every edge incident to \(v\) monochromatic, leaves other coordinates fixed, and attains the preceding bound. This proves the support formula. A tie between two maximizing sign vectors with different properness status can only involve a zero coefficient on an active vertex, making both support expressions equal.

**3. Non-bipartite graphs.** If \(G\) is non-bipartite, no sign vector is a proper coloring, so \(A_G=\{-1,1\}^V\). Thus \(K_G=[-1,1]^V\) and \(r(T)=1\).

**4. Bipartite graphs and sharpness.** Suppose \(G\) is bipartite, and let \(k=|V_+|\). For arbitrary \(a\), Step 2 gives either \(h_{K_G}(a)=L(a)\) or
\[
h_{K_G}(a)=L(a)-2m(a)\ \ge\ L(a)-\frac{2}{k}\sum_{v\in V_+}|a_v|\ \ge\ \left(1-\frac2k\right)L(a).
\]
Here the first inequality uses the minimum-versus-average bound and the second uses \(k\ge2\). Since the support of \((1-2/k)B_{\ell_\infty(V)}\) is \((1-2/k)L(a)\), separation of compact convex sets yields \((1-2/k)B_X\subseteq K_G\).

For the reverse inclusion at any larger radius, choose a proper two-coloring \(\eta\) of \(G\), assigning arbitrary signs to isolates, and define a dual vector by \(a_v=\eta_v/k\) on \(V_+\) and \(a_v=0\) elsewhere. Then \(L(a)=1\), \(m(a)=1/k\), and \(\eta\) maximizes \(a\cdot\eta\) while coloring all edges properly. Step 2 gives \(h_{K_G}(a)=1-2/k\). Thus no larger centered multiple of the cube fits inside \(K_G\), and \(r(T)=1-2/k\). This also proves the isolated-edge case \(k=2\) with maximal radius zero. \(\square\)

## Verification

A standalone Python standard-library checker in `checks/check_graph_averaging.py` enumerates all \(1094\) nonempty labeled simple graphs on \(2\) through \(5\) vertices. It computes the allowed monochromatic-edge sign vertices directly, checks \(157849\) exact-integer dual support evaluations against the formula, tests the proposed lower radius bound, and checks an exact-rational sharp dual witness for each bipartite graph. Run `python checks/check_graph_averaging.py` from the package root. The observed terminal line is `PASS: 1094 graphs, 157849 exact support inequalities, and all bipartite sharp witnesses`. These finite checks supplement the universal argument in the Proof section; they do not establish its infinite family by exhaustion.

## Relationship to prior work

The quantitative \(r\)-generating definition and the finite-dimensional reduction to the convex hull of exact norm-attainment points are due to Kadets, Martín, Merí and Quero [1], especially Definition 3 and Proposition 2. Corollary 3 of [1] already recognizes the generating case once every cube extreme point is norm-attaining; thus the non-bipartite \(r=1\) branch is a direct application once the edge-face characterization is established. The new graph-specific content is the complete family classification, the exact support function, and in particular the sharp quantitative radius \(1-2/k\) for every bipartite graph, uniformly over arbitrary strictly interior edge weights. The graph dependence is different from the bipartiteness criteria known for numerical indices of Lipschitz-free graph spaces, which concern distinct Banach spaces and distinct invariants [2].

## Limitations

The argument does not cover complex scalars, hyperedges of size larger than two, or degenerate weights at exactly zero or one. It gives the maximal generating radius but not a classification of all linear operators between the same spaces. Literature comparison has a residual risk of an equivalent uncatalogued result.

## References

[1] V. Kadets, M. Martín, J. Merí and A. Quero, *Generating operators between Banach spaces*, arXiv:2306.02645v1, publicly posted 2023-06-05; *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 118, article 90 (2024), doi:10.1007/s13398-024-01582-3, especially Definition 3, Proposition 2 and Corollary 3. Primary MSC2020: 46B04.

[2] *Bipartiteness exactly characterizes numerical index one for finite graph metrics*, publicly indexed research result (2026), distinguishable as a numerical-index statement about Lipschitz-free graph-metric spaces, not generating radii of vertex-to-edge averaging maps.
