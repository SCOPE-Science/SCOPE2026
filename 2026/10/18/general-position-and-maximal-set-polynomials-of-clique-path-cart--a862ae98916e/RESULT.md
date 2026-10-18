# General-position and maximal-set polynomials of clique–path Cartesian products

## Finding

For integers \(m,n\geq 3\), let \(G_{m,n}=K_m\square P_n\). Its **general-position polynomial** counts all subsets \(S\subseteq V(G_{m,n})\) with no three vertices on a common shortest path:
\[
\boxed{\Psi_{m,n}(z)=(1+nz)^m+mz^2\sum_{h=0}^{n-2}(n-h-1)(1+hz)^{m-1}.}
\]
The **maximal-set polynomial** counts *inclusion-maximal* general-position subsets, rather than merely maximum-cardinality subsets:
\[
\boxed{\mathcal M_{m,n}(z)=m(n-1)z^2+B_{m,n}z^m+C_{m,n}z^{m+1},}
\]
where
\[
\begin{aligned}
 B_{m,n}&=n^m-2m\sum_{h=1}^{n-2}h^{m-1}
 +m(m-1)\sum_{h=1}^{n-4}(n-h-3)h^{m-2},\\
 C_{m,n}&=m\sum_{h=1}^{n-2}(n-h-1)h^{m-1}.
\end{aligned}
\]
An upper summation index smaller than its lower index denotes an empty sum. All three coefficients of \(\mathcal M_{m,n}\) are positive. Thus the general-position complex has precisely three facet cardinalities \(2,m,m+1\), and its gap between smallest and largest facets is unbounded. In particular, \(\operatorname{gp}^{-}(G_{m,n})=2\), while \(\operatorname{gp}(G_{m,n})=m+1\).

For example, \(\Psi_{3,3}(z)=1+9z+36z^2+33z^3+3z^4\), and \(\mathcal M_{3,3}(z)=6z^2+21z^3+3z^4\). For \(m=3,n=4\), these polynomials are \(1+12z+66z^2+88z^3+18z^4\) and \(9z^2+34z^3+18z^4\), respectively.

## Assumptions and scope

The Cartesian-product graph has vertices \((a,t)\), where \(a\in\{1,\ldots,m\}\) and \(t\in\{1,\ldots,n\}\). Two distinct vertices are adjacent if either their first coordinates agree and their second coordinates differ by one, or their second coordinates agree and their first coordinates differ. All graphs are simple and undirected; all paths are graph-theoretic shortest paths. A *general-position set* means a subset whose intersection with every shortest path has at most two vertices; *maximal* means inclusion-maximal. The formulas apply to every pair of integers \(m,n\ge3\). The dummy polynomial variable \(z\) records selected vertex count, not graph order.

## Proof

**1. Exact geodesic criterion.** Graph distances split across factors:
\[
 d((a,t),(b,u))=\mathbf 1_{a\ne b}+|t-u|.
\]
For three *distinct* vertices \(v_1=(a,t),v_2=(b,u),v_3=(c,w)\), the middle vertex \(v_2\) lies on some geodesic from \(v_1\) to \(v_3\) if and only if both \(u\) lies between \(t\) and \(w\), inclusive, and
\[
 \mathbf 1_{a\ne b}+\mathbf 1_{b\ne c}=\mathbf 1_{a\ne c}.
\]
For the complete-graph factor, the latter condition means \(b=a\) or \(b=c\). This follows directly by separating the two nonnegative triangle inequalities; equality in their sum forces equality in both.

**2. Complete structural description.** For every general-position set \(S\), either (I) no first-coordinate label is repeated, or (II) a *single* label \(a\) occurs twice, at layers \(p<q\), and every other selected vertex has a distinct label different from \(a\) and lies at a layer strictly between \(p\) and \(q\). Conversely, every set of type (I) or (II) is in general position.

Indeed, three copies of the same label at increasing layers are geodesically collinear, so no label occurs three times. If label \(a\) occurs at \(p<q\), a selected vertex with a different label at or outside the closed interval \([p,q]\) forms a geodesically collinear triple with these two copies (use the copy of \(a\) nearer that vertex as the middle point). If another label \(b\) occurs twice at interior layers \(r<s\), then \((a,p),(b,r),(b,s)\) are collinear. This proves necessity. In (I) three selected vertices have pairwise distinct labels, hence cannot satisfy the clique-factor equality. In (II) any triple with all distinct labels cannot be collinear; any triple using both \(a\)-vertices has its third layer strictly inside and its middle label different from \(a\), so the clique-factor equality again fails. This proves sufficiency and disjointness.

**3. Polynomial for all feasible sets.** In case (I), each of the \(m\) labels is either absent or placed at exactly one of \(n\) layers, contributing \((1+nz)^m\). In case (II), choose the repeated label in \(m\) ways and its layers \(p<q\); then each of the remaining \(m-1\) labels is absent or placed at one of \(h=q-p-1\) interior layers. The contribution is \(mz^2(1+hz)^{m-1}\) per \((p,q)\). There are \(n-h-1\) pairs with this interior length \(h\), yielding \(\Psi_{m,n}\).

**4. Inclusion-maximal sets of type (II).** If \(q=p+1\), there is no interior layer, so the pair of repeated-label vertices is a maximal two-element general-position set. These contribute \(m(n-1)z^2\). When \(q\ge p+2\), the type-(II) set is maximal precisely when all remaining \(m-1\) labels are each present in its interior: any absent label can otherwise be added within the interval. A type-(II) set can never be enlarged by a third copy of the repeated label, a copy of an already present other label, or a vertex at an exterior or endpoint layer. Thus these maximal sets have size \(m+1\) and are counted by \(C_{m,n}\).

**5. Inclusion-maximal sets of type (I).** If a label is absent, a new vertex of that label can always be added, so every maximal type-(I) set uses all \(m\) labels exactly once. This gives \(n^m\) assignments before excluding those that extend to type (II). An assignment is extendible if and only if either (E_left) a unique label occupies the smallest selected layer, all other labels occupy higher layers strictly below \(n\), so a second copy of that smallest label can be added at layer \(n\); or (E_right) symmetrically a unique label occupies the largest selected layer and all other labels occupy strictly lower layers above \(1\), so a second copy can be added at layer \(1\). The two events are disjoint from any possibility of adding a new label, because all labels already occur.

The count of each of E_left and E_right is \(m\sum_{h=1}^{n-2}h^{m-1}\): choose the extreme label, its position, then choose the other \(m-1\) layers from the available \(h\) interior positions with repetition allowed. In their intersection, the two extreme labels are distinct, the left extreme occurs at a layer at least \(2\), the right extreme at a layer at most \(n-1\), and each of the remaining \(m-2\) labels is placed strictly between the two. If there are \(h\ge1\) intervening layers, the extremes have \(n-h-3\) possible placements, so the intersection has size \(m(m-1)\sum_{h=1}^{n-4}(n-h-3)h^{m-2}\). Inclusion–exclusion yields \(B_{m,n}\).

**6. Facet sizes and extremal values.** Case (II) gives maximal pairs and maximum sets of size \(m+1\). Case (I) gives maximal sets of size \(m\), for instance a whole \(K_m\)-layer. Since \(m\ge3\), these are three distinct sizes. All coefficients are positive: pairs exist, choosing all \(m\) labels at one common layer gives a maximal type-(I) set, and the span from layer \(1\) to layer \(3\) with every other label at layer \(2\) gives a maximal type-(II) set of size \(m+1\). No other maximal sizes exist by the exhaustive classification.

## Verification

The standalone file `verify.cpp` builds each Cartesian product directly from edges, computes all-pairs shortest-path distances by breadth-first search, marks geodesically forbidden triples using distance equalities, and enumerates all vertex subsets via a feasibility dynamic program. It then independently compares every subset against the claimed structural description, compares every polynomial coefficient to the direct census, and counts every inclusion-maximal feasible set against \(\mathcal M_{m,n}\) for \(m,n\ge3\). It covers 29 products with factor parameters between 1 and 8 and graph order at most 19, totaling 491,210 vertex subsets; seven tested products lie in the theorem's main domain. All tests succeeded. Execute with `g++ -O3 -std=c++17 -o verify verify.cpp && ./verify`. The exact output is in `verification_output.txt`. This exhaustive *finite* check supports—but does not replace—the preceding unrestricted combinatorial proof.

## Relationship to prior work

Tian and Xu determined the largest general-position number for products involving a complete graph, including \(\operatorname{gp}(K_m\square P_n)=m+1\) when \(m\ge2,n\ge3\); this extremal value is not presented as new. Their structural reasoning for maximum sets is related but does not count all feasible configurations or enumerate every inclusion-maximal configuration. Iršič, Klavžar, Rus, and Tuite introduced the general-position polynomial and gave explicit enumerations for other graph operations and Cartesian path grids; the path-grid case covers the thin factor \(K_2=P_2\) but does not give the present \(m\ge3\) family. Kruft Welton, Khudairi, and Tuite studied *lower* general-position numbers and orthogonal sets in Cartesian products and gave a scalar theorem for products of complete graphs, not these two all-set and all-maximal counting formulas. Korže and Vesel studied other Cartesian factors. The substantive claim here is the simultaneous closed forms for \(\Psi_{m,n}\), \(\mathcal M_{m,n}\), and the exact classification behind both.

## Limitations

The theorem concerns ordinary vertex general position, not weak mutual visibility, monophonic position, or its total/dual/outer variants. It requires \(m,n\ge3\); special cases with a path or clique of order less than three are not part of the new theorem. Direct finite verification does not establish an infinite-family result. Accessible-source comparison does not rule out an unindexed earlier equivalent classification, and no independent scientific audit has been performed.

## References

1. J. Tian and K. Xu, *The general position number of Cartesian products involving a factor with small diameter*, Applied Mathematics and Computation, DOI: 10.1016/j.amc.2021.126206. Author-publicly available manuscript, first dated March 2021.
2. V. Iršič, S. Klavžar, D. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696v1 (11 January 2024), https://arxiv.org/abs/2401.05696.
3. E. Kruft Welton, S. Khudairi and J. Tuite, *Lower General Position in Cartesian Products*, arXiv:2404.19451v1 (30 April 2024), https://arxiv.org/abs/2404.19451.
4. S. Klavžar, B. Patkós, D. Rus and I. G. Yero, *On General Position Sets in Cartesian Products*, DOI: 10.1007/s00025-021-01438-x.
5. A. Korže and A. Vesel, *General Position Sets in Two Families of Cartesian Product Graphs*, DOI: 10.1007/s00009-023-02416-z.
