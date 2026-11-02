# Wiener–leaf degree law and edge census for triangular-graph connected-domination exchange

## Finding

Let \(n\ge3\), put \(m=n-1\), and let \(T_n=L(K_n)\) be the triangular graph: its vertices are the two-element subsets of \([n]\), adjacent when they intersect. Construct \(\mathcal R_n\) with one vertex for each **minimum connected dominating set** of \(T_n\); two such sets are adjacent if one can be obtained from the other by deleting exactly one selected vertex and inserting exactly one previously unselected vertex (a *token jump*).

A minimum connected dominating set corresponds to a tree \(F\) on exactly \(m\) of the \(n\) ground vertices, leaving one ground vertex isolated; the already-known cardinality and number of such sets are \(n-2\) and \(n(n-1)^{n-3}\), respectively [3]. Let \(W(F)=\sum_{\{u,v\}\subseteq V(F)} d_F(u,v)\) denote the ordinary Wiener index, and let \(\ell(F)\) be its number of leaves. The following hold:

**Theorem (exchange-degree law).** The degree of the solution represented by \(F\) is
\[
\boxed{\deg_{\mathcal R_n}(F)=W(F)+(m-1)(\ell(F)-1).}
\]
All exchanges split uniquely into \(W(F)-(m-1)\) moves preserving the omitted ground vertex and \((m-1)\ell(F)\) moves changing it.

**Theorem (whole exchange graph).** The graph \(\mathcal R_n\) is connected. Its order (included as known context, not a novelty claim) is \(n m^{m-2}\); its exact number of edges is
\[
\boxed{
|E(\mathcal R_n)|=\frac n2\left[
\frac12\sum_{s=1}^{m-1}\binom ms s^s(m-s)^{m-s}
+(m-1)\left(m(m-1)^{m-2}-m^{m-2}\right)
\right].}
\]
It is regular if and only if \(n\in\{3,4\}\). For every \(m\ge6\), a double broom with two leaves attached at each end of a path on \(m-4\) vertices has exchange degree exactly four greater than that of an \(m\)-vertex path, despite its strictly smaller Wiener index. These assertions describe the **token-jump** solution graph, not the token-slide graph.

For example, for \(n=3,4,5,6,7,8\) the edge counts are \(3,36,540,9420,187845,4227048\), respectively.

## Assumptions and scope

All graphs are finite, simple, and undirected. The induced subgraph on a selected subset \(S\) of vertices of \(T_n\) must be connected, and every vertex outside \(S\) must have a neighbor in \(S\). A vertex of \(T_n\) means an edge of the ground complete graph \(K_n\); exchange moves need not respect adjacency in \(T_n\). The ground tree \(F\) has precisely \(m\) vertices and \(m-1=n-2\) edges. The singleton edge case \(m=2\) is included in the Wiener–leaf formula, with two leaves.

## Proof

**1. Minimum solutions.** View any nonempty chosen set of vertices of \(T_n\) as a set of edges \(E(H)\) in \(K_n\). Connectivity of the chosen vertices in \(T_n\) is equivalent to connectivity of the graph formed by these edges on their nonisolated endpoints. Domination of every vertex of \(T_n\) means that any edge of \(K_n\) meets a chosen edge. Thus \(H\) has at most one isolated ground vertex. If it has \(q\) nonisolated ground vertices, then \(q\ge n-1\), and connectedness requires at least \(q-1\ge n-2\) chosen edges. Equality forces \(q=n-1\) and a tree on these vertices, and every such tree dominates every ground edge. This recovers the known minimum \(n-2\) and the count from choosing an omitted vertex and applying Cayley's formula on the remaining \(m\) vertices.

**2. The two types of exchange.** Fix such a tree \(F\), with omitted ground vertex \(a\). If an exchange leaves \(a\) omitted, it must replace an edge of \(F\) by a ground nonedge joining two vertices of \(F\). Adding the new edge forms one cycle, and any edge on the unique original \(F\)-path between its endpoints can be deleted. Conversely every valid fixed-support exchange has exactly this form. The number is \(\sum_{\{u,v\}\notin E(F)}d_F(u,v)=W(F)-(m-1)\), since the sum over adjacent pairs is \(m-1\).

If the omitted vertex changes to \(b\in V(F)\), the deleted edge must be the unique edge at a leaf \(b\); otherwise the remaining nonisolated tree does not have the required support and connectivity. The added edge necessarily joins \(a\) to one of the \(m-1\) surviving vertices. Every such choice is valid, and each resulting exchange has a unique pair \((b,\text{attachment vertex})\). The number is \((m-1)\ell(F)\). Their sum gives the claimed degree.

**3. Connectivity.** Spanning trees of \(K_m\) on a fixed labeled support are connected under fundamental-cycle edge exchanges: repeatedly insert an edge of a target tree not presently selected and remove a different edge of the resulting cycle, increasing their common edge count. For two supports with distinct omitted vertices \(a\) and \(b\), choose a common vertex \(c\). On the first support, exchange to the star centered at \(c\). Remove its edge \(cb\) and insert \(ca\), yielding the star centered at \(c\) on the other support. Fixed-support exchanges finish the transformation. Such a common \(c\) exists for every \(n\ge3\), so \(\mathcal R_n\) is connected.

**4. Global edge count.** Write \(\mathcal T_m\) for all labeled trees on a fixed \(m\)-element ground set. By the degree formula and the \(n\) choices of the omitted vertex,
\[
2|E(\mathcal R_n)|=n\left(\sum_{F\in\mathcal T_m}W(F)
+(m-1)\sum_{F\in\mathcal T_m}\ell(F)
-(m-1)|\mathcal T_m|\right).
\]
Cayley's formula gives \(|\mathcal T_m|=m^{m-2}\). The Prüfer word of length \(m-2\) avoids a prescribed ground vertex exactly when that vertex is a leaf, hence
\(\sum_{F\in\mathcal T_m}\ell(F)=m(m-1)^{m-2}\), including \(m=2\).

For any tree, removing an edge partitions its vertices into components of orders \(s\) and \(m-s\); this edge contributes \(s(m-s)\) to its Wiener index. For any prescribed nontrivial vertex subset of size \(s\), a tree having exactly one connecting edge between it and its complement consists of two independently chosen internal trees and one crossing edge. Multiplying the \(s^{s-2}(m-s)^{m-s-2}\) internal choices by \(s(m-s)\) choices of the bridge and \(s(m-s)\) for the Wiener contribution gives \(s^s(m-s)^{m-s}\); singleton components follow the same identity by the usual single-vertex-tree convention. Each unordered split is counted twice, so
\[
\sum_{F\in\mathcal T_m}W(F)
=\frac12\sum_{s=1}^{m-1}\binom ms s^s(m-s)^{m-s}.
\]
Substitution and division by two yield the exact stated edge count.

**5. Regularity and the four-move discrepancy.** For \(m\ge3\), a star has \(W= (m-1)^2\), \(\ell=m-1\), and hence degree \((m-1)(2m-3)\). An \(m\)-vertex path has \(W=m(m^2-1)/6\), two leaves, and degree \(m(m^2-1)/6+m-1\). Their difference is
\[
\deg(\mathrm{star})-\deg(\mathrm{path})
=-\frac{(m-8)(m-3)(m-1)}6.
\]
For every \(m\ge4\) except \(m=8\), this proves nonregularity. For \(m\ge6\), let \(B_m\) be the double broom described above. Its four pendant-edge cuts contribute \(4(m-1)\) to the Wiener index, and its backbone-edge cuts contribute \(\sum_{s=3}^{m-3}s(m-s)\). Since a path contributes \(\sum_{s=1}^{m-1}s(m-s)\), one has \(W(B_m)=W(P_m)-(2m-6)\). With \(\ell(B_m)=4\), the degree law gives \(\deg(B_m)=\deg(P_m)+4\), resolving \(m=8\) and proving the discrepancy for every \(m\ge6\). For \(m=2\) and \(m=3\), all labeled trees of that order have the same shape and therefore the same degree. Consequently regularity holds precisely for \(n=m+1\in\{3,4\}\).

## Verification

The accompanying standard-library `CHECK.py` implements the connected domination condition **directly on the line graph**, without treating the tree characterization as a built-in predicate. It exhaustively checks every subset of vertices of \(T_n\) for \(3\le n\le6\) (\(33,864\) subsets altogether), proves by enumeration that no smaller connected dominating set exists in those cases, constructs every minimum set, and compares its actual token-jump neighbors with the Wiener–leaf degree law. The observed vertex/edge counts for \(n=3,4,5,6\) are respectively \((3,3)\), \((12,36)\), \((80,540)\), \((750,9420)\); all solution graphs are connected. It also computes the path–star identity and double-broom gap for \(3\le n\le17\) (broom cases only when defined). Execution ends with `ALL_CHECKS_PASSED total_graph_subsets=33864`. The infinite claims follow from the proof, not from this finite experiment.

## Relationship to prior work

Connected dominating set reconfiguration and the distinction between token jumping and token sliding are established topics [1,2]. The known minimum size and number of minimum connected dominating sets of triangular graphs were recorded independently in OEIS A373395 [3], and are **not** asserted as new. The original graph family, tree representation, and the standard spanning-tree exchange move likewise serve as known prerequisites. What is assessed here is the combined **all-solution degree formula involving Wiener index and leaf count**, its global exact edge census, connectedness in the full support-changing exchange graph, and its regularity classification with the exceptional double-broom witness. None of the directly inspected comparison materials states this combination. A literature search cannot rule out differently phrased preexisting formulas; that remains a priority risk.

## Limitations

The theorem applies only to the optimal-cardinality **token-jump** connected-domination reconfiguration graph of \(L(K_n)\). It does not provide an exact diameter formula or extend automatically to token sliding, other line graphs, or nonoptimal connected dominating sets. Comparisons of indexed findings and the inspected survey/sequence do not establish absolute novelty; specialized tree-exchange literature may contain equivalent formulas.

## References

[1] D. Lokshtanov, A. E. Mouawad, F. Panolan, S. Siebertz, *On the Parameterized Complexity of Reconfiguration of Connected Dominating Sets*, arXiv:1910.00581v1, first publicly posted 2019-10-01, https://arxiv.org/abs/1910.00581.

[2] N. Bousquet, A. E. Mouawad, N. Nishimura, S. Siebertz, *A survey on the parameterized complexity of the independent set and (connected) dominating set reconfiguration problems*, arXiv:2204.10526, https://arxiv.org/abs/2204.10526; accessible HTML https://ar5iv.labs.arxiv.org/html/2204.10526.

[3] OEIS Foundation, A373395, *Number of minimum connected dominating sets in the n-triangular graph*, formula and historical contributors, https://oeis.org/A373395 (entry authored June 2024; formula credited June 20, 2024).
