# Dissociation and maximal-set polynomials of bicliques with a deleted matching

## Finding
Let \(m,n\ge3\) and \(0\le t\le\min\{m,n\}\). Delete \(t\) pairwise independent edges from \(K_{m,n}\), obtaining \(G_{m,n,t}\). A dissociation set induces maximum degree at most one; it is maximal if no vertex can be added while preserving that condition. Denote by \(D_G(z)\) the size-generating polynomial of all dissociation sets, including the empty set, and by \(M_G(z)\) that of inclusion-maximal dissociation sets. Then
\[
\boxed{D_{G_{m,n,t}}(z)=(1+z)^m+(1+z)^n-1+mnz^2+t(m+n-2)z^3+\binom t2z^4}
\]
and
\[
\boxed{M_{G_{m,n,t}}(z)=z^m+z^n+(m-t)(n-t)z^2+t(m+n-2t)z^3+\binom t2z^4.}
\]
These identities enumerate *every* admissible set by cardinality, with vertices distinguished (no quotient by graph automorphisms). In particular, among this entire three-parameter family the unique well-dissociated graph (all inclusion-maximal dissociation sets have the same size) is \(G_{4,4,4}\cong Q_3\). For each crown graph \(G_{r,r,r}\) with \(r\ge5\), the minimum inclusion-maximal dissociation-set size is four while the maximum is \(r\); the gap \(r-4\) is unbounded even within connected \((r-1)\)-regular bipartite graphs.

## Assumptions and scope
All graphs are finite, simple, and undirected. Name the shores \(X=\{x_1,\ldots,x_m\}\) and \(Y=\{y_1,\ldots,y_n\}\), and delete exactly the edges \(x_i y_i\) with \(1\le i\le t\). The matching indices are distinct, and the remaining cross-edges are present. For \(S\subseteq V(G)\), \(G[S]\) is the induced subgraph, and
\[
D_G(z)=\sum_{S:\,\Delta(G[S])\le1}z^{|S|},\qquad
M_G(z)=\sum_{\substack{S:\,\Delta(G[S])\le1\\ S\text{ inclusion-maximal}}}z^{|S|}.
\]
An inclusion-maximal dissociation set is not the same as a dissociation set of maximum cardinality. The restrictions \(m,n\ge3\) are essential to the explicit maximality classification below; the displayed formulas are not claimed at shores of sizes one or two.

## Proof
Write \(A=S\cap X\), \(B=S\cap Y\), \(a=|A|\), and \(b=|B|\). A selected \(x_i\) has exactly
\[
b-\mathbf 1_{\{i\le t,\ y_i\in B\}}
\]
neighbors within \(S\); similarly, a selected \(y_j\) has exactly
\[
a-\mathbf 1_{\{j\le t,\ x_j\in A\}}
\]
selected neighbors. If both shores are represented, these degrees must be at most one, so \(a,b\le2\). We classify the four possible mixed sizes directly.

For \((a,b)=(1,1)\), every one of the \(mn\) choices is dissociated. For \((2,1)\), the single selected \(y_j\) must be one of the \(t\) matched vertices, and \(x_j\) must be one of the two selected left vertices; the other can be any of the remaining \(m-1\) vertices. Thus there are \(t(m-1)\) sets. Dually, there are \(t(n-1)\) sets with \((a,b)=(1,2)\). For \((a,b)=(2,2)\), both selected vertices in each shore must be matched to exactly the selected vertices in the other shore, since each selected vertex needs one of its two potential cross-edges deleted. Thus the shore index sets coincide with a two-element subset of \(\{1,\ldots,t\}\), giving \(\binom t2\) sets. Every pure-shore subset is independent, and their empty-set overlap is counted twice. Summing these disjoint cases proves the first polynomial.

For inclusion-maximality, a pure-shore dissociation set can be enlarged within its shore unless it is the entire shore. Each entire shore is maximal, because every opposite-shore vertex would have at least \(m-1\ge2\) or \(n-1\ge2\) neighbors. This contributes \(z^m+z^n\).

Consider a mixed pair \(\{x_i,y_j\}\). If \(i=j\le t\), its two vertices are nonadjacent; appending any \(x_k\) with \(k\ne i\) gives a single edge \(x_k y_i\) and an isolated \(x_i\), so the pair is not maximal. Otherwise, if \(i\le t\), append the missing-edge partner \(y_i\), which is isolated from the sole selected left vertex \(x_i\); this does not change the existing edge \(x_i y_j\). Dually, if \(j\le t\) and \(i\ne j\), append \(x_j\). These cases cover every pair with at least one index at most \(t\). Conversely, if \(i>t\) and \(j>t\), the pair induces an edge and every additional vertex has an edge to one of its saturated endpoints. Therefore the maximal mixed pairs number exactly \((m-t)(n-t)\).

A dissociated triple has, up to exchanging shores, \(A=\{x_j,x_k\}\), \(B=\{y_j\}\), where \(j\le t\) and \(k\ne j\). If \(k\le t\), it extends by \(y_k\), giving a dissociated four-set. If \(k>t\), then every unused right vertex is adjacent to \(x_k\), which already has degree one, while every unused left vertex is adjacent to \(y_j\), which also already has degree one. Thus such a triple is maximal exactly when its second left vertex is unmatched. It contributes \(t(m-t)\), with the opposite-shore version contributing \(t(n-t)\); their sum is \(t(m+n-2t)\). Finally, each mixed four-set already saturates every selected vertex at degree one, and any additional vertex from either shore is adjacent to at least one already saturated selected vertex. Hence all \(\binom t2\) four-sets are maximal. This establishes the second polynomial.

To classify well-dissociated members, first suppose \(t<\min(m,n)\). A maximal pair exists, as does a maximal full shore of size at least three, so maximal sizes differ. Next suppose \(t=\min(m,n)<\max(m,n)\), and, without loss of generality, \(t=m<n\). There is a maximal triple (because \(t(n-t)>0\)) and a maximal whole shore of size \(n>3\), so again sizes differ. Finally, \(m=n=t=r\ge3\) gives
\[
M_{G_{r,r,r}}(z)=2z^r+\binom r2 z^4.
\]
The polynomial has only one exponent precisely when \(r=4\). The resulting graph \(K_{4,4}-M_4\) is the standard three-dimensional cube. For \(r\ge5\), its two nonzero degrees yield minimum maximal size four and maximum size \(r\), proving the stated unbounded gap.

## Verification
The standalone `verify.py` independently builds adjacency lists for all \(3\le m,n\le7\) and all \(0\le t\le\min(m,n)\), tests *every* vertex subset against the original induced-degree condition, and determines inclusion-maximality by attempting every possible one-vertex extension. It compares the full coefficient lists with both formulas and checks the well-dissociated classification. All 130 parameter triples pass, with output `VERIFY_OK 130 graph parameter triples; all subsets checked`. Run with `python verify.py` in a standard Python 3 environment; no external packages are required. The brute-force tests verify finite cases only; arbitrary-parameter validity comes from the preceding proof.

## Relationship to prior work
Bock, Pardey, Penso, and Rautenbach study maximum dissociation sets and their relationship to independent and induced matching numbers, including hardness and graph-structure results. They do not provide a counting polynomial for all sets or an inclusion-maximal-set size distribution in bicliques with a deleted matching. Tu, Xiao, and Lang define the dissociation polynomial and prove a coefficient-related extremal inequality for cubic graphs, rather than the exact three-parameter biclique polynomial.

An independently accessible earlier classification of complete-multipartite dissociation sets shows that mixed sets in an undeleted complete bipartite graph have size at most two. Its biclique specialization agrees with the present \(t=0\) identity, but does not imply the additional triple and quadruple terms or the maximality classification for \(t>0\). Independent results on generalized windmills classify a different graph family. Work on non-CIS pairs of matching-deleted bicliques shares the graph construction but concerns clique–stable-set intersections, not induced maximum degree at most one. Comparisons were by mathematical implications, not merely by paper titles.

## Limitations
The theorem concerns deletion of an independent matching, not an arbitrary forbidden edge set, and requires both shore sizes at least three. The uniqueness of the well-dissociated member is relative to that family, not a classification of all well-dissociated graphs. The finite verifier is corroborative; an unindexed or differently phrased equivalent result may exist. No independent mathematical audit or publication-priority certification is asserted.

## References
1. F. Bock, J. Pardey, L. D. Penso, D. Rautenbach, “Relating dissociation, independence, and matchings,” *Discrete Applied Mathematics* 322 (2022), 160–165; arXiv:2202.01004, first posted 2022-02-02. https://arxiv.org/abs/2202.01004
2. J. Tu, J. Xiao, R. Lang, “Counting the number of dissociation sets in cubic graphs,” *AIMS Mathematics* 8 (2023), 10021–10032; DOI:10.3934/math.2023507. https://www.aimspress.com/article/doi/10.3934/math.2023507
3. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, “The complexity of dissociation set problems in graphs,” *Discrete Applied Mathematics* 159 (2011), 1352–1366; DOI:10.1016/j.dam.2011.04.023.
4. “Dissociation polynomials of complete multipartite graphs and their coefficientwise extremizers,” published mathematical research note (2026).
5. “Dissociation polynomial and all maximal dissociation sets of generalized windmills,” published mathematical research note (2026).
