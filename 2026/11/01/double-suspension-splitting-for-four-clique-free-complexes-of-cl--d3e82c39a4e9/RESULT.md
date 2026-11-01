# Double-suspension splitting for four-clique-free complexes of clique joins

## Finding

Let \(H\) be any **nonempty finite simple triangle-free graph**, possibly disconnected or with isolated vertices, and let \(m\ge 2\) be an integer. Form the graph join \(G=K_m\vee H\): the vertices of a complete graph \(K_m\) are joined to every vertex of \(H\). Write \(\operatorname{CF}_4(G)\) for the simplicial complex of vertex sets containing no clique on four vertices, and \(\operatorname{Ind}(H)\) for the independence complex of \(H\). Then there is an integral homotopy equivalence

\[
|\operatorname{CF}_4(K_m\vee H)|\simeq
\left(\bigvee^{\binom{m}{2}}\Sigma^2|\operatorname{Ind}(H)|\right)
\vee\left(\bigvee^{\binom{m}{3}}S^2\right).
\]

Here \(\Sigma\) denotes unreduced suspension, and a wedge with zero summands is a point. In particular the four-clique-free complex is simply connected, and for each integer \(q\ge1\),

\[
\widetilde H_q(\operatorname{CF}_4(K_m\vee H);\mathbb Z)
\cong\widetilde H_{q-2}(\operatorname{Ind}(H);\mathbb Z)^{\oplus\binom{m}{2}}
\oplus\begin{cases}\mathbb Z^{\binom{m}{3}},&q=2,\\0,&q\ne2.\end{cases}
\]

The reduced homology of a nonempty complex is taken to be zero in negative degrees. This is a homotopy-type statement over the integers, not a field-homology inference.

## Assumptions and scope

All graphs are finite, undirected and simple. The hypothesis \(\omega(H)\le2\) is essential: it excludes triangles in \(H\). The graph \(H\) has at least one vertex. In \(K_m\vee H\), all edges within the clique and all edges between clique and \(H\) are present, and the internal edges of \(H\) are unchanged. All complexes contain the empty face. The result concerns four-*clique*-free sets, not four-independent sets, four-connected-set avoidance, or the ordinary clique/flag complex.

Put \(A=V(K_m)\), \(V=V(H)\), \(L=\operatorname{Ind}(H)\), and \(\Delta_V\) for the full simplex on \(V\). Denote the zero-, one-, and two-skeleta of the full simplex on \(A\) by \(D_A\), \(E_A\), and \(T_A\), respectively. Their faces have cardinality at most one, two and three. The simplicial join is written \(*\).

## Proof

**1. Exhaustive face description.** Let \(\sigma\subseteq A\sqcup V\), and set \(r=|\sigma\cap A|\). Every four-clique in \(K_m\vee H\) would use four clique vertices, or three clique vertices and a vertex of \(H\), or two clique vertices and an edge of \(H\); a four-clique containing at most one clique vertex would require a triangle in \(H\), which does not exist. Therefore \(\sigma\in\operatorname{CF}_4(K_m\vee H)\) precisely in the following cases:

* \(0\le r\le1\), with unrestricted \(\sigma\cap V\);
* \(r=2\), with \(\sigma\cap V\) independent in \(H\);
* \(r=3\), with \(\sigma\cap V=\varnothing\).

No face can contain four clique vertices. Hence, with \(X=\operatorname{CF}_4(K_m\vee H)\),

\[
X=B\cup Y,\qquad
B=\Delta_V*D_A,\qquad
Y=(L*E_A)\cup T_A,
\qquad B\cap Y=L*D_A=:Z.
\]

This equality is an equality of simplicial complexes, not merely of homotopy types.

**2. Collapse a contractible summand in the homotopy category.** The subcomplex \(B=\Delta_V*D_A\) is contractible because \(V\) is nonempty, so \(\Delta_V\) is a nonempty simplex. All inclusions of finite simplicial subcomplexes are cofibrations. Thus contracting \(|B|\) to a point is a homotopy equivalence of \(|X|\) with its quotient; the displayed pushout gives

\[
|X|\simeq |Y|/|Z|.
\]

This is a homotopy equivalence, not an assertion that \(B\) admits an elementary simplicial collapse inside \(X\).

**3. Edge blocks are double suspensions.** For each two-element subset \(e=\{a,b\}\subset A\), let

\[
Q_e=|L*\Delta_e|/|L*\partial\Delta_e|,
\]

where \(\Delta_e\) is the edge simplex and \(\partial\Delta_e\) its two-vertex boundary. Distinct blocks \(L*\Delta_e\) meet only in subcomplexes of \(Z=L*D_A\). Since \(L\) is nonempty, \(L*\partial\Delta_e\) is the unreduced suspension \(\Sigma|L|\), while \(L*\Delta_e\) is contractible. Consequently the homotopy cofiber of this boundary inclusion satisfies

\[
Q_e\simeq\Sigma(L*\partial\Delta_e)\simeq\Sigma^2|L|.
\]

It follows that the quotient of \(L*E_A\) by \(Z\) is a wedge of \(\binom m2\) double suspensions:

\[
|L*E_A|/|Z|\simeq \bigvee_{e\in\binom A2}\Sigma^2|L|.
\]

**4. Triangle attachments are null.** The remaining faces of \(Y\) are exactly the \(\binom m3\) two-simplices of \(T_A\), one for every triple of clique vertices. Their boundaries are loops in the preceding quotient: each of their edges lies in an edge block \(Q_e\). The double suspension of any nonempty space is simply connected, so the wedge of the \(Q_e\) is simply connected. Hence every such boundary loop is nullhomotopic. Attaching the triangle two-cells therefore contributes one free two-sphere per triangle. No higher apex-only cells occur because \(T_A\) is the two-skeleton. Thus

\[
|Y|/|Z|\simeq
\left(\bigvee_{e\in\binom A2}\Sigma^2|L|\right)
\vee\left(\bigvee_{t\in\binom A3}S^2\right),
\]

which is the claim. The simply connectedness and integral homology formula follow immediately. The argument is valid for connected or disconnected \(L\), including contractible \(L\).

**A sharp hypothesis boundary.** If the triangle-free assumption is removed, take \(H=K_3\) and \(m=2\). Then \(K_2\vee H=K_5\), and \(\operatorname{CF}_4(K_5)\) is the two-skeleton of a four-simplex, homotopy equivalent to \(\bigvee^4 S^2\). The formula incorrectly extrapolated to this forbidden case would give \(\bigvee^2 S^2\). This establishes that the triangle-free hypothesis cannot simply be dropped.

## Verification

The standalone file `verify.py` reconstructs the independence complex and the four-clique-free complex independently from graph edges, checks the complete face-cover and intersection identities in Step 1, and performs boundary-matrix reductions over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). It exhaustively checks **every labeled triangle-free graph with one through five vertices**, at clique sizes \(m=2,3,4\), and additional six-vertex paths, cycles and three disjoint edges. This gives \(1329\) independent complex instances and \(3987\) finite-field homology comparisons. The excluded triangle boundary case is checked separately. Execution requires standard Python 3 only and terminates with `ALL_VERIFY_OK`.

These finite checks corroborate, but do not establish, the universally quantified homotopy equivalence. Steps 1--4 supply the all-parameter proof; the computation checks the underlying finite combinatorics and homological implications.

For an explicit nontrivial instance, \(\operatorname{Ind}(C_5)\simeq S^1\). Therefore

\[
|\operatorname{CF}_4(K_3\vee C_5)|\simeq S^2\vee\bigvee^3 S^3.
\]

More generally, Barmak's account of Jonsson's construction shows that for every nonempty finite simplicial complex \(K\) there exists a finite bipartite graph \(H\) with \(\operatorname{Ind}(H)\simeq\Sigma|K|\). Taking \(m=2\) in the theorem realizes \(\Sigma^3|K|\) as a four-clique-free complex of the indicated join form. In particular integral torsion that occurs in \(\widetilde H_j(K;\mathbb Z)\) transfers to \(\widetilde H_{j+3}(\operatorname{CF}_4(K_2\vee H);\mathbb Z)\). This universality is a corollary of the new splitting and a cited pre-existing realization theorem, not a separate independent discovery.

## Relationship to prior work

Ghosh and Selvaraja's February 2026 article develops four-clique-free and higher clique-free complexes using shellability, decomposability and clique attachments; its Theorems 3.3 and 4.2 concern shellability and do not determine the above complete integral homotopy type for clique joins with triangle-free graphs. The manuscript treats links isomorphic to independence complexes in a separate construction, but does not state a double-suspension wedge decomposition for \(\operatorname{CF}_4(K_m\vee H)\).

Barmak's study of star clusters develops the topology of independence complexes. Its Theorem 3.4 states that independence complexes of triangle-free graphs have suspension homotopy type, while Theorem 3.7 records the bipartite realization of suspensions. Neither result concerns four-clique-free complexes of clique joins. The proof here uses a concrete simplicial face partition and a topologically explicit cofiber splitting, rather than assuming a general clique-free suspension theorem.

Known results about Lovász open-neighborhood complexes of clique joins apply to a different simplicial functor: a set of vertices having a common open neighbor is not the same as a set avoiding four-cliques. The correspondence between these two complexes is not assumed and does not supply this theorem.

## Limitations

The graph \(H\) must be nonempty and triangle-free. The conclusion is a nonequivariant homotopy equivalence; it does not determine the induced action of graph automorphisms on integral homology or give an equivariant splitting. It does not assert simplicial collapsibility, shellability, persistence statements, or an analogous formula for arbitrary forbidden clique sizes. The finite verifier alone cannot certify any infinite statement. An equivalent unindexed source or a more general existing theorem about simplicial polyhedral joins remains a residual originality risk.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first public 2026-02-10. https://arxiv.org/abs/2602.09623
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first public 2010-07-02; Theorems 3.4 and 3.7. https://arxiv.org/abs/1007.0418
