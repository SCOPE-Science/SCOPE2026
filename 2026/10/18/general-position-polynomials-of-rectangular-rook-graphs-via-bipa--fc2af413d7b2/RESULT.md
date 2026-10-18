# General-position polynomials of rectangular rook graphs via bipartite star forests

## Finding

Let \(m,n\ge1\) be integers, and let \(R_{m,n}=K_m\square K_n\) be the rook graph: vertices are the \(mn\) cells of an \(m\)-by-\(n\) board, adjacent when they share a row or a column. A set of vertices is in **general position** if no three distinct members occur on one graph geodesic. Define its full subset enumerator by
\[
P_{m,n}(z)=\sum_{S\subseteq V(R_{m,n}),\ S\text{ in general position}}z^{|S|}.
\]

**Theorem.** Such sets correspond bijectively, preserving size, to spanning star forests of the complete bipartite graph \(K_{m,n}\): the edge set of the forest consists of the cells of \(S\), and its connected components are stars or isolated vertices. Their complete bivariate exponential generating function is
\[
\boxed{\sum_{m,n\ge0}P_{m,n}(z)\frac{x^m y^n}{m!n!}=\exp\!\left(xe^{zy}+ye^{zx}-zxy\right).}
\]
Here the extension to a zero-sized part is \(P_{m,0}(z)=P_{0,n}(z)=1\). For positive \(m,n\) the following finite coefficient-free sum is exact:
\[
\boxed{P_{m,n}(z)=\sum_{q=0}^{\min(n,\lfloor m/2\rfloor)}\binom nq
\sum_{\substack{k_1,\ldots,k_q\ge2\\K:=k_1+\cdots+k_q\le m}}
\frac{m!}{(m-K)!\prod_{i=1}^q k_i!}\,z^K(1+(m-K)z)^{n-q}.}
\]
For \(q=0\), the inner sum means the unique empty tuple with \(K=0\).

For example,
\[
P_{2,n}(z)=(1+2z)^n+nz^2,\qquad
P_{3,3}(z)=1+9z+36z^2+48z^3+9z^4,
\]
\[
P_{4,4}(z)=1+16z+120z^2+416z^3+632z^4+240z^5+16z^6.
\]

The number of largest general-position sets, i.e. the leading coefficient of \(P_{m,n}(z)\), is explicitly
\[
\boxed{[z^{\deg P_{m,n}}]P_{m,n}(z)=
\begin{cases}
1,&\min(m,n)=1,\\
6,&m=n=2,\\
2^{\max(m,n)},&\min(m,n)=2,\ \max(m,n)\ge3,\\
mn,&m,n\ge3.
\end{cases}}
\]
The corresponding degrees are \(\max(m,n)\) in the first and third cases, \(2\) when \(m=n=2\), and \(m+n-2\) when both sides are at least three. The last degree is a previously known general-position number, not a newly claimed numerical extremum.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. A star includes \(K_{1,k}\) for \(k\ge1\); an isolated vertex is also an allowed forest component. The polynomial counts **vertex subsets**, not ordered lists or partitions, and the bipartite side sizes can be unequal. No connectivity condition is imposed on the selected set or on the forest. The convention for a Cartesian product with one factor \(K_1\) is the usual complete graph on the other factor's vertex set.

## Proof

**1. Geodesic-to-path correspondence.** Two nonadjacent rook-graph cells have different rows and columns and are at distance \(2\). Thus three distinct cells violate general position precisely when they form the vertices of a rook-graph path of length \(2\) whose endpoints are nonadjacent. Under the correspondence \((i,j)\leftrightarrow a_i b_j\), a cell is an edge in \(K_{m,n}\). Three distinct cells have this geodesic configuration precisely when their three bipartite edges form a simple path with three edges, denoted \(P_4\): the two outer edges are disjoint, and the middle edge meets one endpoint of each. Conversely any such \(P_4\) gives a violating rook geodesic.

**2. Forbidden paths and star forests.** A connected graph without a (not necessarily induced) \(P_4\) has no spanning tree that is non-star: any non-star tree contains \(P_4\). Since the selected-edge graph is bipartite, if its spanning tree is a star then every extra edge must also touch that centre, and those edges are already in the tree. Therefore each connected component is a star, including the one-edge case, or an isolated vertex. Conversely no star forest contains \(P_4\). The bijection and preservation of the size statistic follow.

**3. Exponential generating function.** Components with no edges contribute \(x+y\); a star whose centre lies on the row side and whose degree is at least two contributes \(x(e^{zy}-1-zy)\); a column-centred star of degree at least two contributes \(y(e^{zx}-1-zx)\); and the one-edge component contributes \(zxy\). These are disjoint descriptions with no centre ambiguity. Their sum is exactly \(xe^{zy}+ye^{zx}-zxy\). The labeled, two-sort exponential formula for disjoint components proves the displayed bivariate EGF, including both zero-part boundary conventions.

**4. Finite sum.** In a selected star forest, mark the \(q\) columns whose selected degree is at least two. Their selected row-neighbourhoods are pairwise disjoint; otherwise there would be a three-edge path. Choose those columns in \(\binom nq\) ways. For specified neighbourhood sizes \(k_i\ge2\) with sum \(K\le m\), the number of disjoint ordered row choices is \(m!/((m-K)!\prod_i k_i!)\). Every remaining column either chooses no edge or exactly one edge incident to one of the \(m-K\) unused rows: choices contribute \(1+(m-K)z\) per column. No edges from a remaining column can touch a used row, else a three-edge path arises. Multiplying by \(z^K\) and summing gives the finite formula, with every star forest represented once.

**5. Extremal coefficients.** A forest on \(m+n\) vertices has \(m+n-c\) edges where \(c\) is its number of components. If both sides have at least three vertices, one spanning star is impossible; two components are possible only with two nontrivial stars whose centres lie on opposite sides. Indeed two star components with both centres on the same side would leave at least one further vertex of that side isolated. If the centres are \(a_i\) and \(b_j\), the unique maximizing edge set is \(\{a_i b_k:k\ne j\}\cup\{a_\ell b_j:\ell\ne i\}\), of size \(m+n-2\). The \(mn\) choices of two centres are distinct. If \(m=1\), all subsets are allowed and the full vertex set is the unique maximum. If \(m=2\) and \(n\ge3\), a maximum has \(n\) edges; the finite-sum characterization forces every column to select exactly one of its two row edges, giving \(2^n\) maximum sets. The transposed case is symmetric. When \(m=n=2\), every two-cell set works and there are \(\binom42=6\) maxima, while no three-cell set works. This proves all boundary cases.

## Verification

The included pure-Python program `verify_rook_general_position.py` compares three separate implementations: literal enumeration of all subsets and direct geodesic tests, the displayed column-centre finite sum, and a root-component star-forest recurrence. It checked 17 positive board-size pairs, including 104306 literal subsets in ten smaller cases, with exact integer coefficients; it separately checks the degree and maximal-set multiplicities. Run it using `python verify_rook_general_position.py`. Finite experiments support, but do not replace, the unrestricted combinatorial proof.

## Relationship to prior work

General-position sets and their general graph structure were studied by Anand and collaborators in 2018/2019. The general-position number of Cartesian products of complete graphs, in particular \(m+n-2\) for \(m,n\ge3\), is established by Klavžar, Patkós, Rus and Yero (2021), so the degree here is not asserted to be new. The 2024 general-position polynomial framework studies other graph families and the Cartesian product of paths; Rather (2026) supplies formulas for complete multipartite graphs, not Cartesian rook graphs. Cody and Detore (2026) place the \((3,2)\)-independence condition in a broader recent framework; the present theorem refines its rook-graph specialization into an exact complete counting polynomial and maximum-set multiplicity. The star-forest formula is independently proved here rather than attributed to those sources.

## Limitations

This theorem concerns the Cartesian product of complete graphs, not arbitrary Cartesian products or complete multipartite graphs. Its proof is self-contained for all positive board dimensions. The numerical extremal degree in the nondegenerate case is previously known. No assertion of exhaustive bibliographic priority or externally independent mathematical validation is made. Similar formulas under different names such as bipartite star-forest enumerators remain a bibliographic risk.

## References

1. B. Cody and R. Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351 (first public version 2026-01-07), https://arxiv.org/abs/2601.04351 .
2. V. Anand, S. M. Chandran, M. Changat, S. Klavžar and collaborators, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460, https://arxiv.org/abs/1812.08460 .
3. S. Klavžar, B. Patkós, G. Rus and I. G. Yero, *On General Position Sets in Cartesian Products*, Results in Mathematics 76 (2021), https://doi.org/10.1007/s00025-021-01438-x .
4. *General Position Polynomials*, Results in Mathematics 79 (2024), https://doi.org/10.1007/s00025-024-02133-3 .
5. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930, https://arxiv.org/abs/2603.06930 .
