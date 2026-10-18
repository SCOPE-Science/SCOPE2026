# Graph-edge geometric-mean envelopes in free convex Banach lattices

## Finding

Let \(G=(V,E)\) be any finite simple graph with \(|V|=n\ge2\), at least one edge and no isolated vertices. For real \(1\le p<\infty\), define the continuous positively homogeneous function
\[
F_G(u)=\max_{\{i,j\}\in E}\sqrt{|u_i u_j|},\qquad u\in\mathbb R^n.
\]
Regard \(F_G\) as an element of the real free \(p\)-convex Banach lattice \(\operatorname{FBL}^{(p)}[\ell_1^n]\), with convexity constant one. Its **exact** norm is
\[
\boxed{\|F_G\|^p=\Phi(G):=
\min_{\substack{x_i>0\ (i\in V)\\x_i x_j\ge1\ (\{i,j\}\in E)}}
\frac12\sum_{i\in V}x_i.}
\]
Moreover, \(\Phi(G)=n/2\) if and only if \(G\) has a **fractional perfect matching**: nonnegative edge weights \(w_e\) satisfying \(\sum_{e\ni i}w_e=1\) at every vertex.

For every complete multipartite graph \(G=K_{a_1,\ldots,a_r}\), where \(r\ge2\), all \(a_j\) are positive integers, \(n=\sum_j a_j\), and \(L=\max_j a_j\), one has the explicit sharp profile
\[
\boxed{\|F_G\|^p=\begin{cases}
 n/2,&2L\le n,\\
 \sqrt{L(n-L)},&2L>n.
\end{cases}}
\]
The graph invariant \(\Phi(G)\) is independent of the exponent; the lattice norm is its \(1/p\)-th power. In particular, a star with \(m\) leaves has \(\|F_G\|^p=\sqrt m\), whereas a complete multipartite graph whose largest part occupies no more than half the vertices has \(\|F_G\|^p=n/2\).

## Assumptions and scope

All graphs are undirected, finite and simple, with no isolated vertices. All Banach lattices and scalars are real. We use the canonical function realization of the free \(p\)-convex Banach lattice, with convexity constant one. The coordinate evaluation functions correspond to the standard generators of \(\ell_1^n\). The edge maximum is a continuous positively homogeneous function, so it belongs to the generated lattice by the continuous homogeneous function calculus. For \(p=1\), the expression is the original free Banach-lattice norm; for \(1<p<\infty\), it is the free \(p\)-convex norm. The case \(p=\infty\), isolated vertices, complex scalars and non-graph hyperedges are not asserted.

## Proof

**1. Canonical norm and reduction to edge budgets.** The representation in Jardón-Sánchez–Laustsen–Taylor–Tradacete–Troitsky gives
\[
\|F_G\|^p=
\sup\left\{\sum_{k=1}^m F_G(u^{(k)})^p:\ m\ge1,\ u^{(k)}\in\mathbb R^n,\ \max_{i\in V}\sum_{k=1}^m|u_i^{(k)}|^p\le1\right\}.
\]
Indeed, the weak \(p\)-summing constraint for \(\ell_1^n\) equals the displayed maximum of coordinate sums: the supremum over its unit ball occurs at a signed coordinate vector. Membership is legitimate, not merely a finite ambient function norm: the coordinate evaluations generate every continuous positively homogeneous function of finitely many coordinates through the Banach-lattice function calculus. Alternatively, uniform approximation on the \(\ell_\infty\)-unit sphere in the lattice polynomials converges in the above norm, since \(\|h\|\le n^{1/p}\|h\|_{\infty,S_\infty}\).

Put \(v_i^{(k)}=|u_i^{(k)}|^p\), and choose a maximizing edge for each index \(k\). For an edge \(e=\{i,j\}\), combine all indices assigned to \(e\); the Cauchy–Schwarz inequality yields
\[
\sum_{k\mapsto e}\sqrt{v_i^{(k)}v_j^{(k)}}\le
\sqrt{\Big(\sum_{k\mapsto e}v_i^{(k)}\Big)
\Big(\sum_{k\mapsto e}v_j^{(k)}\Big)}.
\]
Writing the two sums as edge-endpoint budgets \(a_{i,e}\), we obtain
\[
\|F_G\|^p\le
P(G):=\max_{\substack{a_{i,e}\ge0\\\sum_{e\ni i}a_{i,e}\le1}}
\sum_{e=\{i,j\}}\sqrt{a_{i,e}a_{j,e}}.
\]
Conversely, from every feasible family of endpoint budgets construct exactly one vector \(u^{(e)}\) per edge, supported on its endpoints, with \(|u_i^{(e)}|^p=a_{i,e}\). Then \(F_G(u^{(e)})^p=\sqrt{a_{i,e}a_{j,e}}\). Thus \(\|F_G\|^p=P(G)\), and this finite maximum is attained.

**2. Exact multiplicative-price duality.** The edge function \((a,b)\mapsto\sqrt{ab}\) is continuous and concave on the positive quadrant. Maximizing the sum subject to affine budgets is a finite convex-optimization problem with a strictly feasible point. For nonnegative Lagrange prices \(\lambda_i\), the supremum of its Lagrangian is finite precisely when
\[
2\sqrt{\lambda_i\lambda_j}\ge1\quad\text{for every edge }\{i,j\}.
\]
This criterion follows directly by weighted arithmetic–geometric mean: \(\sqrt{ab}\le\lambda_i a+\lambda_j b\) holds for every pair of nonnegative numbers precisely when \(4\lambda_i\lambda_j\ge1\). Otherwise scaling a violating pair makes the supremum infinite. Strong duality, justified by Slater's condition, yields
\[
P(G)=\min_{\lambda_i\ge0,\ 4\lambda_i\lambda_j\ge1}
\sum_i\lambda_i.
\]
Because there are no isolated vertices, every feasible price is strictly positive. Substitution \(x_i=2\lambda_i\) gives the first boxed formula; a minimum is attained because the feasible set is closed inside the compact sublevel set determined by \(x_i\le n\) together with \(x_i x_j\ge1\) and at least one neighbor for each vertex.

**3. The fractional-matching equality criterion.** The feasible dual prices \(x_i=1\) show \(\Phi(G)\le n/2\). If \(w_e\) is a fractional perfect matching, setting both endpoint budgets on edge \(e\) equal to \(w_e\) gives feasible total value \(\sum_e w_e=n/2\), and hence equality. Conversely, suppose \(P(G)=n/2\) and let maximizing endpoint budgets be chosen. The chain
\[
\sum_{e=\{i,j\}}\sqrt{a_{i,e}a_{j,e}}\le
\frac12\sum_{e=\{i,j\}}(a_{i,e}+a_{j,e})
\le\frac n2
\]
can be an equality only if \(a_{i,e}=a_{j,e}\) on every edge and every vertex budget is fully used. Their common values are precisely the required fractional perfect matching.

**4. Complete multipartite classification.** Write \(x_i=\exp(s_i)\). The price objective is convex in \(s\), and all edge constraints become affine: \(s_i+s_j\ge0\). Averaging \(s\) over permutations within each part cannot increase the objective and preserves feasibility. Hence an optimum has one price \(t_h>0\) per part, with \(t_ht_l\ge1\) for all distinct parts.

If all part prices are at least one, their sum is at least \(n\). Otherwise at most one part \(h\) can have \(t_h=s<1\), and every other part price is at least \(1/s\). If its size is \(a\), the full objective before division by two is consequently at least
\[
 a s+\frac{n-a}{s},\qquad 0<s<1.
\]
When \(a\le n/2\), the infimum on this interval is \(n\) (approached as \(s\uparrow1\)); when \(a>n/2\), the strict minimum is \(2\sqrt{a(n-a)}\) at \(s=\sqrt{(n-a)/a}\). Only one part can exceed half the vertices, and the prices described above are feasible for all cross-part edges. This establishes the second boxed formula, including the balanced boundary \(2L=n\).

For explicit primal witnesses, if \(L>n/2\) set \(a=L\), \(b=n-L\), put budget \(1/b\) at each large-part endpoint of an edge joining the large part to the outside and \(1/a\) at the other endpoint; other edge budgets vanish. Every vertex spends one unit, and the sum of \(ab\) identical edge contributions is \(\sqrt{ab}\). If \(2L\le n\), list all vertices consecutively by parts around a circle of circumference \(n\), and pair each half-unit cell with its antipodal cell. No pair lies in the same part because each part has length at most \(n/2\). Symmetrized half-cell pair weights give a fractional perfect matching, attaining \(n/2\) in the primal.

## Verification

The bundled standalone `verify_graph_envelopes.py` enumerates every ordered multipartite size profile of total order \(2\le n\le12\). It constructs exact rational antipodal fractional-matchings in all balanced profiles, checks both endpoint budgets and complementary dual products in dominant profiles, and compares the resulting sharp values. The executable reports 3,711 balanced and 372 dominant profiles, together with 35,832 checked fractional-edge/cross-edge entries. This is finite corroboration, not a substitute for the preceding proof for arbitrary graphs and dimensions.

## Relationship to prior work

The 2021 free-convexity construction supplies the canonical norm and continuous function calculus used here; the 2017 free-lattice construction covers the endpoint \(p=1\); the 2022 monograph-length preprint studies foundational structural, extension and sublattice properties. None of these examined sections states the graph-edge geometric-mean envelope, its exact multiplicative-price dual, the fractional-perfect-matching boundary, or the complete-multipartite dominant-part threshold. The vertex-transitive specialization also admits a direct symmetry-averaging argument from the general norm, and is not presented as an independent discovery. The distinctive content is the graph-wide dual and sharp nontransitive classification.

## Limitations

This is a finite-graph theorem for real free \(p\)-convex Banach lattices with finite exponent. It does not determine the corresponding formula for hypergraphs, complex scalars or \(p=\infty\), nor does it give closed forms for every graph's dual minimum. An equivalent theorem in unindexed literature remains possible. No independent mathematical audit has been performed.

## References

1. H. Jardón-Sánchez, N. J. Laustsen, M. A. Taylor, P. Tradacete, and V. G. Troitsky, *Free Banach lattices under convexity conditions*, first public arXiv version 2021-01-10, arXiv:2101.03510v1, https://arxiv.org/abs/2101.03510 ; open journal full text https://doi.org/10.1007/s13398-021-01155-8 . Sections 2 and 6 and equation (1.1).
2. T. Oikhberg, M. A. Taylor, P. Tradacete, and V. G. Troitsky, *Free Banach lattices*, first public arXiv version 2022-10-02, arXiv:2210.00614v1, https://arxiv.org/html/2210.00614v1 . Sections 1, 2, 4 and 9.
3. A. Avilés, J. D. Rodríguez, and P. Tradacete, *The free Banach lattice generated by a Banach space*, first public arXiv version 2017-06-25, arXiv:1706.08147v1, https://arxiv.org/html/1706.08147v1 . Section 2.
