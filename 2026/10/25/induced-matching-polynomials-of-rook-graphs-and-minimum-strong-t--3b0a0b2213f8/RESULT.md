# Induced-matching polynomials of rook graphs and minimum strong-total-cover rigidity

## Finding
For integers \(m,n\ge2\), let \(R_{m,n}=K_m\mathbin{\square}K_n\), with a vertex in each cell \((i,j)\) of an \(m\)-by-\(n\) rectangle and an edge between different cells sharing a row or a column. An *induced matching* is a set of edges whose endpoints span exactly those edges. Write \(I_{m,n}(z)=\sum_M z^{|M|}\), including the empty matching. Then
\[
I_{m,n}(z)=\sum_{\substack{h,v\ge0\\h+2v\le m\\2h+v\le n}}\frac{m!\,n!}{2^{h+v}h!v!(m-h-2v)!(n-2h-v)!}z^{h+v}.
\]
Here \(h\) counts within-row (horizontal) edges and \(v\) counts within-column (vertical) edges. Consequently
\[
\alpha_{\mathrm{ind}}(R_{m,n})=\min\!\left\{m,n,\left\lfloor\frac{m+n}{3}\right\rfloor\right\}=:t_{m,n}.
\]

A *strong total cover* is a set of graph vertices and graph edges in which every vertex is either selected or incident with a selected edge, and every edge is either selected or incident with a selected vertex. Its minimum cardinality on \(R_{m,n}\) is \(mn-t_{m,n}\). For the two-row family \(R_{2,n}\), the entire family of minimum strong total covers has cardinality
\[
C_n=\begin{cases}8,&n=2,\\45,&n=3,\\\binom n2\binom{n-2}{2},&n\ge4.\end{cases}
\]
For \(n\ge4\), these optimal covers consist **exactly** of one horizontal edge from each of the two rows, with their four endpoint columns all distinct, and every vertex not among those four endpoints. Thus the full optimum-cover census exhibits a sharp change between lengths three and four.

## Assumptions and scope
Graphs are finite, simple, and vertex/edge-labelled by the stated rows and columns; different selected label subsets count separately. An edge in an induced matching may share neither endpoints nor any adjacency between its endpoints with another chosen edge. Strong total covers may select vertices and edges simultaneously, and their cardinality counts both types equally. The polynomial and minimum-size results apply for all \(m,n\ge2\); the classification and \(C_n\) formula concern precisely two-row graphs.

## Proof
**Induced-matching structure.** Suppose a chosen matching contains a horizontal edge in row \(i\), columns \(j,k\). An endpoint of any other chosen edge may lie in neither row \(i\) nor columns \(j,k\), else it is adjacent to an endpoint of the first edge. Analogously, a vertical edge in column \(j\) uses two rows and one column, with neither its rows nor its column available to any other edge. Therefore distinct chosen edges use disjoint row-coordinate sets and disjoint column-coordinate sets. Conversely these coordinate restrictions guarantee no unwanted adjacency of endpoints. With \(h\) horizontal and \(v\) vertical edges, the row-coordinate resources are \(h+2v\), and the column-coordinate resources are \(2h+v\). This gives the index constraints.

To count them, choose and order the \(h+2v\) occupied row coordinates and \(2h+v\) occupied column coordinates. The first \(h\) occupied rows are assigned to horizontal edges, whose \(2h\) column coordinates are paired; the remaining \(2v\) rows are paired and assigned to the \(v\) remaining singleton columns. Dividing by \(h!v!2^{h+v}\) removes edge order and pair orientation, leaving exactly the displayed factorial coefficient. Empty choices yield the constant coefficient one.

For a prescribed total \(t=h+v\), writing \(v=t-h\), feasibility is equivalent to an integer \(v\) satisfying
\[
\max(0,2t-n)\le v\le\min(t,m-t).
\]
Such an integer exists if and only if \(t\le m\), \(t\le n\), and \(3t\le m+n\). (All endpoints are integers, so interval nonemptiness suffices.) This proves the formula for \(\alpha_{\mathrm{ind}}\).

**Strong-cover equality and rigidity.** Fix any graph \(G\) and a strong total cover with selected vertices \(X\), selected edges \(Y\), and unselected vertices \(U=V(G)\setminus X\). All edges induced by \(U\) must belong to \(Y\), because neither endpoint is in \(X\). Every vertex isolated in \(G[U]\) must be incident with a selected crossing edge; this edge can cover no other isolated vertex in \(U\). Writing \(s(U)\) for the number of isolates, one has
\[
|X|+|Y|\ge |V(G)|-|U|+|E(G[U])|+s(U).
\]
Equality is attainable for every \(U\): select precisely all edges in \(G[U]\) and one crossing edge for each isolated vertex (if such an isolated vertex has no neighbor, the subset cannot be used; all rook graphs here have no isolated vertices). Thus the minimum for fixed \(U\) is this expression. For a nontrivial connected component with \(b\) vertices and \(e\) edges, \(b-e\le1\), with equality precisely when the component is a tree. Taking any one edge from each nontrivial connected component of \(G[U]\) gives an induced matching, so the number of these components is at most \(\alpha_{\mathrm{ind}}(G)\). Consequently every strong total cover has size at least \(|V(G)|-\alpha_{\mathrm{ind}}(G)\). Conversely, an induced matching of size \(\alpha_{\mathrm{ind}}(G)\) together with all vertices not on its edges is a strong total cover of that size. This rederives the known general identity without claiming it as new.

Let \(G=R_{2,n}\) with \(n\ge4\); its induced-matching number is two. If an optimal cover has unselected set \(U\), then its induced subgraph has exactly two nontrivial components, both trees: otherwise the previous component inequality is strict. It may not have additional nontrivial components, even unicyclic ones, because any edge in each would force at least three induced-matching components. If one of its tree components met both rows, it would be adjacent to every other vertex of \(U\) (each row is a clique), contradicting the presence of the second component. Hence one tree component lies entirely in each row. A tree induced inside a clique with at least two vertices must have exactly two vertices, so the components are disjoint horizontal edges. No further isolated vertices in \(U\) are possible, since each row contains an edge and every additional cell in that row is adjacent to an endpoint. The edges must use four distinct columns: otherwise a rung connects the components. Thus exactly four vertices are unselected; all remaining vertices are selected. Both internal horizontal edges must be selected, and there are no other selected edges in an optimum cover. Choose two columns for the first horizontal edge, then two disjoint columns for the second, giving \(\binom n2\binom{n-2}{2}\) covers.

For \(n=2\), the graph is a four-cycle with induced-matching number one; an unselected set realizing a one-unit saving induces either an edge (four possibilities) or a three-vertex path (four possibilities), giving eight covers. For \(n=3\), the graph is the triangular prism with induced-matching number one. A one-unit saving arises from an induced edge (nine cases), an induced three-vertex path (twelve cases), an induced four-vertex path (six cases), or one horizontal edge together with an isolated vertex opposite its unused third column (six choices of unselected vertices). In the last case the isolated vertex admits three independently selectable crossing edges, producing eighteen rather than six covers. The exhaustive classification thus gives \(9+12+6+18=45\). This proves the piecewise census.

## Verification
The accompanying `verify_rook_induced.py` independently constructs rook-graph edges, enumerates induced matchings, compares all coefficients of the polynomial for ten small rectangular orders, and checks nonexistence of smaller strong total covers in four finite instances. `verify_strong_cover_subsets.py` enumerates all vertex subsets, determines their minimum compatible selected-edge cardinalities, and independently checks the exact optimum-cover counts for \(R_{2,n}\), \(2\le n\le8\), including the exceptional values eight and forty-five. Both scripts return `VERIFY_OK` when their assertions pass. Finite tests are corroborations, not proofs of the infinite identities.

## Relationship to prior work
Aprile and Ferrarini's October 16, 2026 preprint *The Strong Total Cover Problem* introduces systematic study of strong total covers and states the general relation between minimum cover size and induced-matching number. This relationship is prior work and is used transparently; it does not give the size-refined induced-matching polynomial of the rook graphs nor the complete census of minimum strong total covers for the two-row family in the inspected text. Earlier research by Yuan, Yang, Zheng, and Gong concerns extremal properties of maximal/maximum induced matchings in connected graphs, not the rectangular enumerator. The rook graph is the line graph of a complete bipartite graph; neither ordinary matchings in rook graphs nor induced matchings in complete bipartite graphs are the same enumerative problem.

## Limitations
The complete strong-total-cover classification is proved only when one rectangular dimension is two, although the polynomial and minimum cover size hold for arbitrary two-dimensional rectangular rook graphs. No claim is made about all minimum covers for \(m,n\ge3\), or about higher-dimensional Hamming graphs. A systematic independent historical-priority check is still required; no independent mathematical audit has been conducted. The two scripts check only finite instances and do not independently certify the infinite proof.

## References
- M. Aprile and L. Ferrarini, *The Strong Total Cover Problem*, arXiv:2610.23312, first posted October 16, 2026; https://arxiv.org/abs/2610.23312; inspected preprint text at https://arxiv.org/html/2610.23312v1.
- B.-J. Yuan, Z.-Y. Yang, L. Zheng, and S.-C. Gong, *Maximal and maximum induced matchings in connected graphs*, arXiv:2410.11288 (2024); https://arxiv.org/abs/2410.11288.
