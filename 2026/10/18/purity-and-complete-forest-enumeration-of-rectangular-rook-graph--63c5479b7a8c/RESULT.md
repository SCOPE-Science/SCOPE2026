# Purity and complete forest enumeration of rectangular rook graphs

## Finding

For integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\). Its **induced-forest polynomial** counts subsets of vertices whose induced subgraphs are forests, including the empty set:
\[
F_{m,n}(z)=\sum_{S\subseteq V(R_{m,n})\, :\, R_{m,n}[S]\text{ is acyclic}}z^{|S|}.
\]
The complete two-parameter family has the exponential generating function
\[
\boxed{\displaystyle
\sum_{m,n\ge0}F_{m,n}(z)\frac{u^m v^n}{m!n!}
=\exp\!\left(u+v+\frac{uvz+\frac12uv(u+v)z^2}{1-uvz^2}\right).}
\]
Here the identity is in formal power series; the naturally defined zero-row or zero-column graph has polynomial \(1\).

Every inclusion-maximal induced forest is **maximum**: the induced-forest simplicial complex is pure (equivalently, \(R_{m,n}\) is well-\(f\)-covered). The common cardinality is
\[
\boxed{f(R_{m,n})=\min\{2m,2n,m+n-1\}.}
\]
Let \(M_{m,n}(z)\) count only inclusion-maximal induced forests by size, and assume \(2\le m\le n\). Then
\[
\boxed{\displaystyle
M_{m,n}(z)=
\begin{cases}
(m!)^2z^{2m-1}, &m=n,\\[3pt]
\displaystyle\frac{m!n!}{(n-m)!}[u^n]\left(u+\frac{u^2}{2(1-u)}\right)^{n-m}z^{2m}, &m<n.
\end{cases}}
\]
For \(m>n\), interchange the parameters. All coefficients refer to *labeled* row and column vertices.

A maximal forest is characterized exactly as follows. If \(m=n\), the corresponding selected edges of \(K_{m,m}\) form a spanning alternating Hamilton path. If \(m<n\), every vertex on the side of size \(m\) has selected degree exactly two; after contracting these degree-two vertices, the result is a linear forest on the \(n\) opposite-side vertices whose \(m\) edges carry distinct labels. This produces the enumerator above.

## Assumptions and scope

All graphs are finite, undirected and simple; \(m,n\) are integers at least two. Vertices of the rook graph are board cells \((i,j)\in[m]\times[n]\), and two cells are adjacent exactly when they share a row or column. An induced forest is a set of cells whose induced rook subgraph has no cycle; inclusion-maximal means that adding any omitted cell creates a cycle. The coefficient notation \([u^n]\) means formal coefficient extraction. The claim concerns induced **vertex** forests of the rook graph, not induced vertex forests of the underlying complete bipartite graph.

## Proof

**1. Exact translation.** Associate a selected board cell \((i,j)\) with the selected edge between left vertex \(i\) and right vertex \(j\) in \(K_{m,n}\). A graph \(H\) whose selected edges have degree at least three at some vertex produces a triangle in its line graph. A cycle in \(H\) produces a cycle in its line graph. Conversely, if \(H\) is a linear forest (disjoint union of paths and isolated base vertices), its line graph is a disjoint union of paths, hence a forest. Thus a rook-cell subset induces a forest **if and only if** its selected bipartite edges form a linear forest.

**2. All-size enumeration.** Apply the labeled exponential formula to bipartite linear forests, viewing the two sides as differently labeled species and weighting every selected edge by \(z\). An isolated left or right vertex contributes \(u\) or \(v\). For every \(r\ge1\), a path with \(r\) vertices on each side has \(2r-1\) edges, \((r!)^2\) realizations on prescribed labels, and exponential-series contribution \((uv)^r z^{2r-1}\). A path with \(r+1\) left and \(r\) right vertices has \(2r\) edges and \((r+1)!r!/2\) realizations (reversal identifies the two orientations); its contribution is \(u(uv)^r z^{2r}/2\), and the reverse-side case contributes \(v(uv)^r z^{2r}/2\). Summing these geometric series and exponentiating over disjoint components gives the displayed expression. There is no path component with nonzero edges outside these three possibilities.

**3. Characterization of maximality.** Let \(E\) be a selected bipartite linear forest, including all base vertices as possible isolated vertices. Write \(U\) and \(V\) for its left and right vertices, respectively, of selected degree at most one. Adding a missing edge between \(a\in U\) and \(b\in V\) preserves the degree bound, and it preserves acyclicity exactly when \(a\) and \(b\) lie in different components. Therefore \(E\) is inclusion-maximal if and only if every opposite-side pair from \(U\times V\) lies in the same path component.

If both \(U\) and \(V\) are nonempty, this condition forces each to be a singleton: no path has more than two vertices of degree at most one, and any isolated base vertex is its own component. The two remaining vertices are opposite-side endpoints of the same path, and there can be no other path or isolated component. Thus \(E\) is a spanning Hamilton path with endpoints on opposite sides, which forces \(m=n\). Conversely, every such path is maximal.

If \(m<n\), the preceding case is impossible, so at least one of \(U,V\) is empty. The condition \(V=\varnothing\) would give \(2n\) selected edges, whereas a forest on \(m+n\) base vertices has at most \(m+n-1\) edges; because \(n\ge m\), this is impossible. Consequently \(U=\varnothing\), meaning **all** \(m\) left vertices have degree exactly two. This is sufficient for maximality: adding any missing selected edge would raise a left degree above two. Every maximal set has exactly \(2m\) edges. In the balanced case neither low-degree side can be empty by the same forest edge bound, giving the Hamilton-path description and \(2m-1\) edges. Explicit alternating paths for \(m=n\), and alternating paths covering \(m\) left and \(m+1\) right vertices for \(m<n\), show that maximal sets exist in both cases. Hence every maximal induced forest has the asserted maximum cardinality.

**4. Exact maximal counts.** In the balanced case, every maximal set is a spanning alternating path in \(K_{m,m}\). Exactly one orientation of each undirected path starts on the left, and independently ordering its left and right vertices gives \((m!)^2\) paths.

For \(m<n\), replace every selected degree-two left vertex by an edge between its two right neighbors. The contracted graph on \(n\) right vertices has exactly \(m\) edges, no cycles (including no parallel-edge 2-cycles), and maximum degree at most two: it is a simple linear forest. Conversely every such linear forest, together with a bijection labeling its \(m\) edges by the left vertices, uniquely reconstructs a maximal selected set. A labeled undirected path on \(s\ge2\) prescribed right vertices has \(s!/2\) realizations, while an isolated right vertex has one. Thus its exponential component series is \(B(u)=u+\sum_{s\ge2}u^s/2=u+u^2/(2(1-u))\). A forest with \(n\) right vertices and \(m\) edges has exactly \(n-m\) components, so its number is \(\frac{n!}{(n-m)!}[u^n]B(u)^{n-m}\). Multiplication by \(m!\) assigns the distinct left labels and proves the second enumerator.

## Verification

The standalone program `verification/verify_induced_forests.py` uses the actual rook graph's adjacency masks and a direct depth-first cycle test on induced vertex subsets, independently of the bipartite path enumeration. It checks the complete all-size polynomial and every inclusion-maximal forest against separate recursive path-component enumerators. The run covers ten board profiles and \(370512\) candidate vertex subsets, including balanced and unbalanced cases; the recorded output is `verification/verification_output.txt`. Independent library cycle detection also agreed for all nonempty subsets of the three boards \((2,4)\), \((3,3)\), and \((3,4)\). The finite checks are consistency tests, not proofs of universal quantifiers.

For example, \(F_{2,4}(z)=1+8z+28z^2+48z^3+30z^4\), and its \(30\) maximal forests all have four vertices. For \(R_{3,3}\), \(F_{3,3}(z)=1+9z+36z^2+78z^3+81z^4+36z^5\), and all \(36\) maximal forests have five vertices.

## Relationship to prior work

Jafarpour-Golzari introduced well-\(f\)-coveredness and established general constructions and a classification of when *the complete bipartite graph itself* is well-\(f\)-covered [1]. The rook graph is instead its **line graph**, and the present result proves purity and an exact facet count for this different graph. OEIS A360850 records the number of individual induced paths (equivalently, connected induced trees) in a rook graph [2]; this does not enumerate disconnected induced forests or their maximal members. Williams and collaborators study spanning linear-forest covers in underlying graphs, proving that complete bipartite graphs admit such covers [3]; their invariant is not the vertex-induced-forest polynomial of the line graph. Tankus and Tarsi study greedy maximal linear forests [4]; the available abstract is relevant to possible stronger prior claims about the purity component, but does not establish or exclude the present all-size/facet enumerators. The complete 2007 paper was not available for an implication-level comparison, a residual originality risk.

## Limitations

The theorem is restricted to complete bipartite line graphs with \(m,n\ge2\); it does not assert well-\(f\)-coveredness for arbitrary line graphs or Cartesian products. The exponential expression is formal and does not assert asymptotics or a polynomial-time method for numerical coefficient extraction. Unindexed earlier work on edge-linear forests or rook-graph forest complexes might overlap with some or all statements; bibliographic priority is not independently certified. The proof covers all orders; finite computations do not replace it.

## References

[1] R. Jafarpour-Golzari, *Graphs whose all maximal induced forests are of the same order*, first arXiv version 2021-05-29, arXiv:2105.14339. https://arxiv.org/abs/2105.14339

[2] A. Howroyd, *OEIS A360850: Number of undirected paths in complete bipartite graphs*, initial entry 2023-02-23. https://oeis.org/A360850

[3] D. Williams and collaborators, *LF-Covers and Binomial Edge Ideals of König Type*, arXiv:2310.14410 (2023), Section 2.2. https://arxiv.org/pdf/2310.14410

[4] D. Tankus and M. Tarsi, *Greedily constructing Hamiltonian paths, Hamiltonian cycles and maximum linear forests*, Discrete Mathematics 307 (2007), 1833–1843, DOI:10.1016/j.disc.2006.09.031. (Abstract inspected; full-text comparison unavailable.)
