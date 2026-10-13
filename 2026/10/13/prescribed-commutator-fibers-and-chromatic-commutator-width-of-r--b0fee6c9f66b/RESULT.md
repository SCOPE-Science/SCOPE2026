# Prescribed commutator fibers and chromatic commutator width of radical-square-zero quiver algebras

## Finding

Let \(Q=(V,E)\) be any finite loopless quiver with nonempty finite vertex set, allowing multiple arrows and oriented cycles. Let \(k=\mathbb F_q\) for an arbitrary prime power \(q\), and let \(A=kQ/J^2\), where \(J\) is the arrow ideal. For \(z=\sum_{e\in E}z_e e\in J\), define the ordered prescribed additive-commutator fiber
\[
F_q(z)=\bigl|\{(x,y)\in A^2:xy-yx=z\}\bigr|.
\]
For \(S\subseteq E\), let \(\kappa(S)\) be the number of connected components (including isolated vertices) in the *undirected* spanning multigraph with vertex set \(V\) and edge multiset \(S\). Define \(v_e(z)=q-1\) when \(z_e=0\), and \(v_e(z)=-1\) otherwise. Then the complete prescribed-value law is
\[
\boxed{F_q(z)=q^{|E|}\sum_{S\subseteq E}q^{2\kappa(S)}\prod_{e\in S}v_e(z).}
\tag{1}
\]
Every target outside \(J\) has no commutator representations. In particular, the right-hand side of (1) is nonnegative despite its alternating appearance; it depends on \(z\) only through its arrow support.

Let \(G_z\) be the simple undirected graph on \(V\) whose edges are the underlying vertex pairs of arrows \(e\) with \(z_e\ne0\). Then
\[
\boxed{F_q(z)>0\quad\Longleftrightarrow\quad\chi(G_z)\le q^2.}
\tag{2}
\]
Here \(\chi\) denotes ordinary proper vertex chromatic number. If \(G\) is the simple undirected graph underlying all arrows, the additive commutator width of \(A\) relative to its full commutator subspace \([A,A]\), defined as the smallest \(r\ge0\) such that every element is a sum of at most \(r\) additive commutators, is
\[
\boxed{\operatorname{cw}(A)=\min\{r\ge0:\chi(G)\le q^{2r}\}.}
\tag{3}
\]
Consequently, finite-dimensional radical-square-zero quiver algebras have **unbounded additive commutator width** at each fixed field: take any orientation of the complete graph on \(n\) vertices. For \(q=2\), a complete graph on four vertices has width one, while one on five vertices has width two.

## Assumptions and scope

All algebras are finite-dimensional associative unital \(k\)-algebras, where \(k\) is the field of \(q\) elements. The quiver is loopless (arrows never begin and end at the same vertex); multiple arrows and oriented cycles are allowed. Because products of two arrows vanish in \(A\), every diagonal idempotent class and every arrow class is a basis element and \(J^2=0\). The algebra dimension is \(|V|+|E|\). No restriction on the characteristic of \(k\) is needed.

All commutators are associative additive commutators \([x,y]=xy-yx\), not group commutators, Lie brackets of independently presented Lie algebras, or derivations. The commutator subspace \([A,A]\) is the linear span of all such commutators. When \(E=\varnothing\), formula (1) gives \(F_q(0)=q^{2|V|}\), and (3) gives width zero because \([A,A]=0\). The symbol \(\kappa(S)\) always counts components on the **whole** fixed vertex set, not just vertices incident to \(S\).

## Proof

Write the basis primitive idempotents as \(e_i\) for \(i\in V\), and the individual arrow basis elements as \(e\in E\). For an arrow from \(s(e)\) to \(t(e)\), multiplication modulo \(J^2\) gives \(e_{s(e)}e=e=ee_{t(e)}\), and any other idempotent-arrow product vanishes. Thus for
\[
x=\sum_{i\in V}a_i e_i+\sum_{e\in E}X_e e,\qquad
 y=\sum_{i\in V}b_i e_i+\sum_{e\in E}Y_e e,
\]
the diagonal part of \([x,y]\) is zero and its coefficient at an arrow \(e\) is precisely
\[
(a_{s(e)}-a_{t(e)})Y_e-(b_{s(e)}-b_{t(e)})X_e.
\tag{4}
\]
There are no interactions between the two variables attached to distinct arrows, since \(J^2=0\). Also \([e_{s(e)},e]=e\), proving that \([A,A]=J\) (and showing that every individual arrow basis element is a single commutator).

For each vertex define a label \(c_i=(a_i,b_i)\in k^2\). Fix the entire vertex labeling \(c:V\to k^2\). For a fixed target coefficient \(z_e\), equation (4) is a linear equation in \((X_e,Y_e)\in k^2\). If \(c_{s(e)}\ne c_{t(e)}\), at least one coefficient is nonzero, so this linear functional is surjective with exactly \(q\) solutions for **each** \(z_e\). If the endpoint labels coincide, it has \(q^2\) solutions when \(z_e=0\), and no solutions when \(z_e\ne0\). Multiplying independent contributions from all arrows gives
\[
F_q(z)=q^{|E|}\sum_{c:V\to k^2}
\prod_{e\in E}\Bigl(1+v_e(z)\mathbf1_{\{c_{s(e)}=c_{t(e)}\}}\Bigr).
\tag{5}
\]
For \(z_e=0\), the factor is \(q\) on equal labels and \(1\) otherwise. For \(z_e\ne0\), it is \(0\) on equal labels and \(1\) otherwise. This establishes (5) even in characteristic two.

Expand the finite product in (5) over all subsets \(S\subseteq E\). For a chosen \(S\), the indicator requires equality of vertex labels across every arrow in \(S\), so labels are constant on each connected component of \((V,S)\). Exactly \((q^2)^{\kappa(S)}=q^{2\kappa(S)}\) such labelings exist. This proves (1) directly and identifies the subset sum with the multivariate Tutte / Fortuin--Kasteleyn polynomial at color parameter \(q^2\). The graph-polynomial identity itself is classical; its use here follows from (4) and (5).

Every summand in (5) is a nonnegative integer. For a target \(z\), a factor corresponding to an arrow with \(z_e\ne0\) vanishes exactly when its endpoints have equal labels. Thus a positive summand exists exactly when the labeling \(c:V\to k^2\) is a proper \(q^2\)-coloring of the simple support graph \(G_z\). This proves (2). It also shows that zero entries of the target impose **no** coloring restrictions.

To prove (3), first let \(r\ge1\) and suppose \(z=\sum_{j=1}^r[x_j,y_j]\). For each vertex collect its \(2r\) diagonal coefficients from the \(x_j\) and \(y_j\) into a vector \(C_i\in k^{2r}\). For every arrow \(e\), the coefficient \(z_e\) is a sum of \(r\) functionals, each having coefficient vector obtained from the corresponding endpoint-label difference. If \(C_{s(e)}=C_{t(e)}\), **all** these functionals vanish, so \(z_e=0\). Hence if every arrow coefficient of \(z\) is nonzero, the vectors \(C_i\) must give a proper coloring of \(G\) by at most \(q^{2r}\) colors. Taking the full-support target with every coefficient \(z_e=1\) proves that a width bound \(r\) forces \(\chi(G)\le q^{2r}\).

Conversely, suppose \(\chi(G)\le q^{2r}\). Choose any proper vertex labeling by vectors in \(k^{2r}\), interpreted as \(r\) consecutive pairs of diagonal coefficients \((a_i^{(j)},b_i^{(j)})\). For any target \(z\in J\), and for each arrow \(e\), at least one of the \(r\) pairs has distinct endpoint labels, so at least one of the \(r\) corresponding linear functionals on \((X_e^{(j)},Y_e^{(j)})\) is nonzero. Their joint sum is therefore surjective onto \(k\); choose the radical coefficients independently for each arrow to realize the arbitrary desired coefficient \(z_e\). This constructs \(z=\sum_{j=1}^r[x_j,y_j]\). When there are no arrows, \(\chi(G)=1\) and the zero-width case follows separately. Formula (3), including the unbounded complete-graph example, follows.

## Verification

The accompanying standalone program `verify.py` independently enumerates all element pairs and all target fibers for quivers with \(q=2,3\), including a two-arrow Kronecker quiver, a directed path, and a directed triangle. It independently computes the spanning-subset formula and checks it against a vertex-coloring calculation, all against direct multiplication. It also checks the chromatic-width jump for complete graphs on four, five, and nine vertices over \(\mathbb F_2\) (exact chromatic search on the smaller examples, and the elementary complete-graph argument for nine vertices). Running `python verify.py` prints `VERIFY_OK` if all assertions hold.

These finite computations are consistency tests, **not** an exhaustive proof for all quivers and finite fields. The proof of the arbitrary-quiver and arbitrary-prime-power statements is the symbolic argument above; the program's direct field arithmetic covers only prime fields of order two and three.

## Relationship to prior work

Quiver algebras with square-zero Jacobson radical are a standard representation-theoretic family; see the pre-2017 discussions of radical-square-zero algebras and natural quivers cited below. The classical multivariate Tutte / Fortuin--Kasteleyn identity already gives the graph-theoretic equality between spin assignments and component-weighted subset sums; this identity is **not** claimed as new.

Earlier commuting-pair counts for radical-square-zero quiver algebras yield the zero-target specialization of (1), in which **every** edge weight is \(q-1\). The specialization is not a new finding here. The additional claims here are the **simultaneous prescribed-target formula for arbitrary supports**, the necessary-and-sufficient chromatic membership criterion (2), and the exact commutator-width law (3), including unboundedness. These are stronger statements than a formula for the zero fiber: zero-fiber counts sum over all vertex labelings but do not determine which nonzero target is attainable, or the minimum number of commutators needed to realize all targets.

The previously described two-vertex multiple-arrow (Kronecker) commutator distribution is recovered as an isolated special case of (1); it does not determine the genuinely multivertex chromatic behavior in (2)--(3). In particular, full-support targets for complete-graph quivers force arbitrarily many commutators as the number of vertices increases, whereas a two-vertex quiver always has width one when it has arrows.

## Limitations

The quiver must be loopless, and the algebra must be the radical-square-zero path algebra, not an arbitrary quotient with nonzero products of arrows. The formulas do not address higher radical powers, finite local base rings, group commutators of the unit group, or commutator widths outside the linear span \([A,A]\). The oriented graph contributes only through its underlying undirected multigraph, so this method cannot distinguish orientations at the level of these additive commutator fibers. Graph coloring can be computationally difficult for large inputs; (1) is an exact finite sum, not a polynomial-time algorithm. The graph-polynomial identity and the zero-target specialization predate this work. An undiscovered equivalent formulation through bilinear incidence varieties, word maps, or graph coloring remains a bibliographic possibility; no independent review has been performed.

## References

1. "Singular equivalence of finite dimensional algebras with radical square zero," arXiv:1603.04191v1 (first public version 14 March 2016), https://arxiv.org/abs/1603.04191. A historical source for the radical-square-zero algebra setting.
2. F. Li and L. Chen, "The natural quiver of an artinian algebra," arXiv:1407.1616v1 (first public version 7 July 2014), https://arxiv.org/abs/1407.1616. Background on quiver presentations.
3. A. D. Sokal, "The multivariate Tutte polynomial (alias Potts model) for graphs and matroids," arXiv:math/0503607v1 (25 March 2005), https://arxiv.org/abs/math/0503607. The classical graph-polynomial spin/subset identity.
4. "Commutator fibers and commuting probabilities of finite Kronecker path algebras," https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-commutator-fibers-and-commuting-probabilities-of-finite-kronecke--75cb49b6c27d. Previously published two-vertex special case.
