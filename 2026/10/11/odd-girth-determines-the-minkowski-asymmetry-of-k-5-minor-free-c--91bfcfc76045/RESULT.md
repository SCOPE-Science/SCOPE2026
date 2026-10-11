# Odd girth determines the Minkowski asymmetry of \(K_5\)-minor-free cut polytopes

## Finding

Let \(G=(V,E)\) be an arbitrary finite undirected simple graph with \(E\ne\varnothing\) and no \(K_5\) minor. Its cut polytope is
\[
P_G=\operatorname{conv}\{\mathbf1_{\delta(S)}:S\subseteq V\}\subseteq\mathbb R^E,
\]
where \(\delta(S)\) is the edge set with exactly one endpoint in \(S\). Let \(g(G)\) be its **odd girth**: the least length of an odd cycle, or \(\infty\) when there is no odd cycle.

For a full-dimensional convex body \(P\), write
\[
s(P)=\inf_{c\in\operatorname{int}P}\inf\{\rho\ge1:c-P\subseteq \rho(P-c)\}
\]
for its Minkowski asymmetry. Then
\[
\boxed{\displaystyle s(P_G)=
\begin{cases}
1,&g(G)=\infty,\\
\dfrac{g(G)}{g(G)-2},&g(G)<\infty.
\end{cases}}
\]
The half-edge vector \(c_* = \frac12\mathbf1_E\) attains this optimum. In particular, within this class, \(P_G\) is centrally symmetric exactly when \(G\) is bipartite. The conclusion applies to disconnected graphs and graphs with bridges or isolated vertices.

Thus every member with a triangle has asymmetry \(3\), every nonbipartite triangle-free member has asymmetry at most \(5/3\), and members of increasing finite odd girth have asymmetry tending to \(1\).

## Assumptions and scope

The graph is finite, simple, and undirected; it has at least one edge and no \(K_5\) minor. No regularity, connectedness, planarity, or transitivity hypothesis is imposed. The statistic is intrinsic Minkowski asymmetry (an affine-invariant optimal reflection dilation), **not** Euclidean diameter, graph-theoretic shortest-path diameter, or a norm-dependent radius.

The classical Barahona–Mahjoub facet description [1] is used for the \(K_5\)-minor-free class; the statement is not extended to graphs with a \(K_5\) minor. The center above is optimal, but uniqueness of optimal centers is neither assumed nor claimed. When \(G\) is bipartite, its cut polytope is a centrally symmetric convex body even if the graph has several components.

## Proof

**1. Full dimension and a canonical feasible center.** Each cut-incidence vector lies in \(\{0,1\}^E\), and the empty cut gives the zero vector. For any edge \(uv\), the vector identity
\[
2\mathbf1_{\{uv\}}=\mathbf1_{\delta(\{u\})}+\mathbf1_{\delta(\{v\})}-\mathbf1_{\delta(\{u,v\})}
\]
shows that differences of cut vectors span \(\mathbb R^E\); hence \(P_G\) is full-dimensional. Averaging the cut vectors uniformly over vertex subsets gives \(c_*\), because every edge is crossed by exactly half the subsets. As the average assigns strictly positive weight to every distinct vertex of this full-dimensional polytope, \(c_*\in\operatorname{int}P_G\).

**2. Switching fixes an optimal center.** For each vertex subset \(T\), define the affine map \(\sigma_T:\mathbb R^E\to\mathbb R^E\) by replacing coordinate \(x_e\) by \(1-x_e\) when \(e\in\delta(T)\), leaving other coordinates unchanged. The map preserves \(P_G\) since
\[
\sigma_T(\mathbf1_{\delta(S)})=\mathbf1_{\delta(S\triangle T)}.
\]
For fixed \(\rho\ge1\), the set of centers satisfying \(c-P_G\subseteq\rho(P_G-c)\) is convex: for every \(x\in P_G\), this is equivalent to \(c+(c-x)/\rho\in P_G\), an affine condition on \(c\). It is also invariant under every \(\sigma_T\). Averaging any feasible center over all switchings sends each coordinate to \(1/2\); thus \(c_*\) is feasible whenever any center is feasible. It therefore minimizes the reflection dilation.

**3. Exact facet-dilation formula.** For a full-dimensional polytope \(P\) with valid facet inequalities \(a_i\cdot x\le b_i\), and an interior point \(c\), the smallest \(\rho\) satisfying the reflected containment is
\[
\rho(P,c)=\max_i\frac{a_i\cdot c-\min_{x\in P}a_i\cdot x}{b_i-a_i\cdot c}.
\]
The denominators are positive by interiority. To see this, test \(c+(c-x)/\rho\in P\) against each facet and optimize over \(x\in P\).

**4. Cycle and edge facet ratios.** The Barahona–Mahjoub description [1, Corollary 3.10] states that for graphs with no \(K_5\) minor, the entire cut polytope is defined by suitable edge bounds \(0\le x_e\le1\) and all inequalities
\[
x(F)-x(C\setminus F)\le |F|-1
\]
where \(C\) is a chordless cycle and \(F\subseteq E(C)\) has odd cardinality. The coordinate bounds have dilation ratio \(1\) at \(c_*\).

Fix one such cycle of length \(\ell\), write \(f=|F|\), and let \(a\) have coefficients \(+1\) on \(F\), \(-1\) on \(C\setminus F\), and zero elsewhere. Its support value is \(b=f-1\). At \(c_*\) the available support slack is exactly
\[
b-a\cdot c_*=(\ell-2)/2.
\]
The restriction of any cut to a cycle contains an even number of edges. Conversely, every even subset of the edges of a cycle is realized by a cut of its vertices; any such assignment extends to a subset of all vertices of \(G\).

If \(\ell\) is odd, \(\ell-f\) is even, so assigning value one to every edge in \(C\setminus F\) and zero to all edges of \(F\) attains \(\min_{x\in P_G}a\cdot x=-(\ell-f)\). Consequently, the ratio for **every** odd-subset cycle facet is
\[
\frac{a\cdot c_*+(\ell-f)}{(\ell-2)/2}=\frac{\ell}{\ell-2}.
\]
If \(\ell\) is even, \(\ell-f\) is odd and any even intersection with the cycle must differ from the all-negative-edge assignment in at least one coordinate. Omitting one negative edge attains
\[
\min_{x\in P_G}a\cdot x=-(\ell-f-1),
\]
so its ratio is exactly \(1\).

**5. Maximization and sharpness.** Hence the optimal dilation at \(c_*\) is the maximum of \(1\) and \(\ell/(\ell-2)\) over the lengths of chordless odd cycles. The function \(\ell\mapsto\ell/(\ell-2)\) decreases strictly on odd integers \(\ell\ge3\). Every shortest odd cycle is chordless: a chord splits an odd cycle into a strictly shorter odd cycle and an even cycle. The largest facet ratio therefore occurs at \(\ell=g(G)\), proving the claimed formula. For a bipartite graph there are no odd cycles and the optimal dilation is \(1\). Since a full-dimensional convex body has asymmetry \(1\) exactly when it is centrally symmetric, the stated symmetry criterion follows.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library and exact integer/rational arithmetic (`fractions.Fraction`). Execute `python3 verify.py` to enumerate all graphs on two through five labeled vertices apart from the excluded \(K_5\), selected six-vertex graphs, odd and even cycles, wheels, complete bipartite graphs, and disconnected examples. It independently forms every chordless-cycle inequality and edge bound, maximizes and minimizes its left side over all cut vertices, then checks the ratio and the reflected-containment inequalities at the predicted scale.

The executed run reported `EXACT_CHECKS_OK graphs=1288 cut_vectors=25286 facet_rows=23906 reflected_inequalities=1867540`. These finite checks independently corroborate local arithmetic and boundary cases. They do not establish the theorem for unbounded graph size; the proof above does.

## Relationship to prior work

Barahona and Mahjoub [1] supply the full cycle-and-edge facet system for graphs without a \(K_5\) minor and switching methods; their paper does not state the odd-girth Minkowski-asymmetry formula. Deza and Dutour Sikirić [2] discuss the switching automorphism group and enumerate facet structures for related cut polytopes, rather than optimize reflection dilation. Nikolaev [3] studies graph diameters and clique numbers of cut-polytope one-skeleta, which do not imply Minkowski asymmetry. Deza and Dutour Sikirić [4] also enumerate facets in graph families; their tables concern faces, not this asymmetry value. The additional step here is an optimal-center argument and explicit minimax evaluation of every governing facet in terms of cycle parity.

## Limitations

The \(K_5\)-minor-free assumption is essential to using the stated exhaustive facet system, and the argument does not determine asymmetry when a \(K_5\) minor is present. The proof identifies an optimal center, not all optimal centers. The formula is an exact mathematical consequence of established facet theory, not an independent new facet characterization. A previously published equivalent characterization under alternative symmetry-measure terminology cannot be categorically excluded. No independent external mathematical audit or publication-priority certification has been performed.

## References

[1] F. Barahona and A. R. Mahjoub, “On the cut polytope,” *Mathematical Programming* 36 (1986), 157–173, DOI: 10.1007/BF02592023, especially Section 3 and Corollary 3.10. Author-hosted full text: https://www.lamsade.dauphine.fr/~mahjoub/Papers/BM86.pdf.

[2] M. Deza and M. Dutour Sikirić, “Generalized cut and metric polytopes of graphs and simplicial complexes,” arXiv:1706.02516v1 (2017), especially Sections 2.1–2.2, https://arxiv.org/abs/1706.02516.

[3] A. V. Nikolaev, “On 1-skeleton of the cut polytopes,” arXiv:2402.13591v1 (first posted 2024-02-21), primary MSC2020 52B05/52B12, https://arxiv.org/abs/2402.13591.

[4] M. Deza and M. Dutour Sikirić, “Enumeration of the facets of cut polytopes over some highly symmetric graphs,” *International Transactions in Operational Research* 23 (2016), 853–860, DOI: 10.1111/itor.12194.
