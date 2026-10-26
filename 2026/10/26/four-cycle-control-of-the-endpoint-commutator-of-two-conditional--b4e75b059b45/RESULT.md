# Four-cycle control of the endpoint commutator of two conditional expectations

## Finding
Let \(G=(U\sqcup V,E)\) be any finite simple \(d\)-regular bipartite graph, with \(d\ge 2\), and put uniform probability measure on its edges. Let \(P\) and \(Q\) be the conditional expectations of edge functions onto their \(U\)-endpoint and \(V\)-endpoint, respectively. For an edge \(e\), let \(c_4(e)\) denote the number of unoriented four-cycles containing \(e\), and set \(c_*=\min_{e\in E}c_4(e)\).

**Sharp endpoint formula.** The commutator \(C=PQ-QP\) satisfies
\[
\|C\|_{L^\infty(E)\to L^\infty(E)}
=\|C\|_{L^1(E)\to L^1(E)}
=\frac{2((d-1)^2-c_*)}{d^2}.
\]
Every maximum is realized by a sign-valued edge function. In particular, among all finite simple \(d\)-regular bipartite graphs the optimal global upper bound is \(2(1-1/d)^2\), attained exactly when at least one edge belongs to no four-cycle. The commutator vanishes exactly when every connected component of \(G\) is \(K_{d,d}\).

**Separation from Hilbert stability.** Let \(G_q\) be the point-line incidence graph of a finite projective plane of prime-power order \(q\ge2\). For its two endpoint conditional expectations,
\[
\|C_q\|_{1\to1}=\|C_q\|_{\infty\to\infty}=\frac{2q^2}{(q+1)^2},\qquad
\|C_q\|_{2\to2}=\frac{\sqrt{q(q^2+q+1)}}{(q+1)^2}.
\]
Thus the endpoint norms tend to \(2\), while the Hilbert norm tends to \(0\) at order \(q^{-1/2}\). These are two different norms of the *same* commutator.

## Assumptions and scope
The graph is finite, simple, bipartite and regular of common integer degree \(d\ge2\), not necessarily connected. The edge probability is uniform: \(\mu(\{e\})=1/|E|\). The conditional expectation \(P\) takes the arithmetic mean over edges with the same \(U\)-endpoint; \(Q\) similarly averages over edges with the same \(V\)-endpoint. All operator norms are induced by these normalized finite \(L^p\) spaces. Since the probability is uniform, the induced \(L^1\) and \(L^\infty\) norms are ordinary absolute column- and row-sum norms. Four-cycles are simple and unoriented, counted once per edge they contain. No asymptotic graph family, connectivity, expansion or absence of other cycles is assumed for the endpoint formula.

## Proof
**1. Exact kernel.** Write an output edge as \(e=(u,v)\) and input edge as \(f=(a,b)\). By taking the two conditional expectations in the indicated order,
\[
(PQh)(u,v)=\frac1{d^2}\sum_{b\in N(u)}\sum_{a\in N(b)}h(a,b),\qquad
(QPh)(u,v)=\frac1{d^2}\sum_{a\in N(v)}\sum_{b\in N(a)}h(a,b).
\]
Consequently, on the edge index set,
\[
C_{(u,v),(a,b)}=\frac{\mathbf1_{b\in N(u)}-\mathbf1_{a\in N(v)}}{d^2}.
\]
The matrix is skew-symmetric because \(f=(a,b)\) and \(e=(u,v)\) themselves are edges: the transposed numerator is \(\mathbf1_{v\in N(a)}-\mathbf1_{u\in N(b)}\), its negative.

**2. Absolute row sums and four-cycles.** Fix \(e=(u,v)\). The set of input edges with \(b\in N(u)\) has size \(d^2\), as does the set with \(a\in N(v)\). Their intersection consists of the edges joining \(N(v)\subseteq U\) to \(N(u)\subseteq V\). These include precisely \(d\) edges incident with \(u\), another \(d\) incident with \(v\), and their common edge \(e\), giving \(2d-1\) distinct edges. Any further intersection edge \((a,b)\) (with \(a\ne u\) and \(b\ne v\)) completes one and only one four-cycle \(u-b-a-v-u\). Hence the intersection has size \(2d-1+c_4(e)\). The number of edges on which the numerator of the kernel is nonzero is the symmetric difference cardinality
\[
2\bigl(d^2-(2d-1+c_4(e))\bigr)
=2\bigl((d-1)^2-c_4(e)\bigr).
\]
Every nonzero numerator is \(1\) or \(-1\). Taking the maximum over output edges proves the \(L^\infty\) identity. Skew-symmetry gives the equal \(L^1\) identity. At an output row attaining the maximum, choose each input value to be the sign of that row's kernel, choosing either sign at its zeros. This yields an input taking values only in \(\{-1,1\}\) and attaining the norm.

**3. Sharpness over all regular graphs and the zero case.** For each edge, at most \((d-1)^2\) four-cycles can pass through it: choose a second neighbor at each endpoint. Thus the formula gives \(0\le\|C\|\le2(1-1/d)^2\), with upper equality precisely if \(c_*=0\). This is realizable for every \(d\ge2\): choose a prime \(q\ge d-1\), consider the \((q+1)\)-regular bipartite point-line incidence graph of the projective plane over \(\mathbf F_q\), and decompose its edges into \(q+1\) perfect matchings. Such a decomposition follows inductively from Hall's condition for regular bipartite graphs. Keeping any \(d\) matchings leaves a finite simple \(d\)-regular bipartite subgraph, still free of four-cycles because distinct points determine exactly one line. The upper bound is attained.

If \(C=0\), every edge must satisfy \(c_4(e)=(d-1)^2\), so for any \(e=(u,v)\) all edges between \(N(v)\) and \(N(u)\) are present. Every vertex of \(N(v)\) then has exactly the neighbor set \(N(u)\), since it has degree \(d\); every vertex of \(N(u)\) similarly has neighbor set \(N(v)\). Therefore these two sets form a whole connected component \(K_{d,d}\). Conversely every component \(K_{d,d}\) has maximal four-cycle count at each edge, hence commutator zero. This proves the equivalence.

**4. Projective-plane Hilbert norm.** For a projective plane of order \(q\), let \(n=q^2+q+1\) and let \(A\) be its \(n\)-by-\(n\) incidence matrix, with row/column sums \(d=q+1\). Distinct points lie together on exactly one line, so
\[
AA^{\mathsf T}=qI+J.
\]
The two endpoint-function subspaces of \(L^2(E)\) intersect exactly in the constants, because the incidence graph is connected. After removing constants, the cross-Gram operator between their isometric coordinate parametrizations is \(A/d\), whose singular values are all \(s=\sqrt q/(q+1)\) by the displayed identity. For two orthogonal projections on a two-dimensional principal-angle block of cosine \(s\), their commutator has matrix (up to orthogonal coordinates) with two off-diagonal entries \(\pm s\sqrt{1-s^2}\) and thus norm \(s\sqrt{1-s^2}\). The remaining blocks commute. Substitution gives the stated Hilbert norm. Incidence graphs have no four-cycles, so the endpoint formula with \(d=q+1\) gives \(2q^2/(q+1)^2\). Both limits follow immediately.

## Verification
The included standalone `verify.py` uses only Python's standard library. It reconstructs both conditional expectations as matrices on edge functions, checks their composition against the exact kernel, counts four-cycles independently, and checks every absolute-row-sum identity on eight finite examples. These include complete bipartite graphs, crown graphs, a cycle, and projective planes of orders \(2,3,5\). It also checks the projective-plane incidence identities \(AA^{\mathsf T}=qI+J\) by integer arithmetic. Run `python verify.py` in the directory containing the extracted file. The actual replay produced `ALL_CHECKS_OK 44523`. These finite checks corroborate the formulas but do not replace the universal proof above.

## Relationship to prior work
The original functional-analytic motivation is the distinction between Hilbert-space commutator estimates for two orthogonal projections and strong endpoint estimates. Walters' full 2016 article proves an anticommutator norm theorem and Hilbert-space commutator inequalities, not the edge-support \(L^1\)/\(L^\infty\) four-cycle identity. Abiad–Dalfó–Fiol study spectral and algebraic characterizations of regular and distance-regular bipartite graphs; their full accessible text does not state the present conditional-expectation commutator formula. The graph-theoretic incidence identities used for the projective-plane specialization are classical and are not claimed as new. Earlier special computations of endpoint commutators for other structured supports do not imply the arbitrary-regular-graph formula. The claimed contribution is the sharp four-cycle characterization, equality classification, and exact endpoint-versus-Hilbert separation for this operator family, not generic theory of two projections or the existence of projective planes.

## Limitations
The endpoint formula assumes equal left and right degree \(d\) and uniform edge measure. No formula for arbitrary irregular or weighted supports is proved. The projective-plane example is an infinite family for prime-power orders, not a classification of every graph for which Hilbert convergence and endpoint instability coexist. The formula itself is finite-dimensional and exact; novelty assessment is limited by the primary sources and research records actually inspected, and does not rule out equivalent calculations under other terminology. No independent verification or priority certification is claimed.

## References
1. A. Abiad, C. Dalfó and M. A. Fiol, *Algebraic characterizations of regularity properties in bipartite graphs*, arXiv:1205.5913v1, 2012-05-26. https://arxiv.org/abs/1205.5913
2. S. Walters, *Anticommutator Norm Formula for Projection Operators*, arXiv:1604.00699v1, 2016-04-03. https://arxiv.org/html/1604.00699v1
3. P. R. Halmos, *Two subspaces*, Transactions of the American Mathematical Society **144** (1969), 381–389, as cited and discussed in Walters' reference [1].
