# The general-position polynomial of rook graphs via labeled star forests

## Finding

**Theorem.** For integers \(m,n\geq 1\), let \(R_{m,n}=K_m\square K_n\) be the rook graph on the \(m\times n\) board: distinct cells are adjacent exactly when they share a row or column. A set \(S\subseteq V(R_{m,n})\) is in *general position* when no three of its vertices belong to a common geodesic. Define its general-position polynomial by
\[
\Psi_{m,n}(z)=\sum_{\substack{S\subseteq V(R_{m,n})\\S\text{ in general position}}}z^{|S|}.
\]
Extend this definition formally to empty boards by \(\Psi_{0,n}=\Psi_{m,0}=1\) for all nonnegative indices. Then the complete two-parameter family has the exponential generating function
\[
\boxed{\sum_{m,n\geq0}\Psi_{m,n}(z)\frac{u^m v^n}{m!\,n!}=\exp\!\left(u e^{vz}+v e^{uz}-uvz\right).}
\tag{1}
\]
Equivalently, it has the coefficient-exact recurrence
\[
\boxed{\Psi_{m+1,n}(z)=\sum_{j=0}^{n}\binom nj z^j\Psi_{m,n-j}(z)
+n\sum_{k=1}^{m}\binom mk z^{k+1}\Psi_{m-k,n-1}(z),}
\tag{2}
\]
valid for \(m,n\geq0\), with the second sum interpreted as zero for \(n=0\). The bases \(\Psi_{0,n}=\Psi_{m,0}=1\) uniquely determine every polynomial.

There is also a direct combinatorial description: under the canonical identification \(R_{m,n}\cong L(K_{m,n})\), a set is in general position if and only if its selected edges in \(K_{m,n}\) form a graph whose nontrivial connected components are stars. In particular, writing \([z^d]\) for coefficient extraction, the degree and leading coefficient of \(\Psi_{m,n}\) are
\[
\begin{array}{c|c|c}
\text{parameter range}&\deg\Psi_{m,n}&[z^{\deg\Psi_{m,n}}]\Psi_{m,n}\\ \hline
\min(m,n)=1&\max(m,n)&1\\
m=n=2&2&6\\
\min(m,n)=2,\ \max(m,n)\geq3&m+n-2&2^{\max(m,n)}\\
m,n\geq3&m+n-2&mn.
\end{array}
\tag{3}
\]
The extremal cardinality for \(m,n\geq2\) is already known; the main result is the **complete** cardinality enumerator and its star-forest generating function, with the leading multiplicities as further consequences.

## Assumptions and scope

All graphs are finite, simple, undirected. \(K_t\) means the complete graph of order \(t\), \(\square\) its Cartesian product, and \(L(H)\) the line graph of \(H\). In the ordinary graph \(R_{m,n}\), cells with equal row coordinate or equal column coordinate are adjacent. Two cells with distinct row and column coordinates have distance exactly two, and there are exactly two shortest length-two paths between them, passing through the opposite corners of their rectangle. Counting distinguishes labeled rows and labeled columns; no quotient by graph automorphisms is taken. The case \(m=0\) or \(n=0\) is solely a compatible empty-board convention.

For an edge subset \(E'\subseteq E(K_{m,n})\), the *selected-edge graph* has the same \(m+n\) labeled base vertices and selected edges \(E'\). A *star forest* means that every non-isolated component is a star, including a one-edge star; isolated vertices are allowed. A path of length three considered below need **not** be induced. The entire polynomial, not only its degree or highest coefficient, is counted by (1) and (2).

## Proof

**Step 1: general-position triples and three-edge paths.** Each rook-graph vertex is an edge between one row and one column vertex of \(K_{m,n}\). Any three rook vertices lie on a common geodesic if and only if one of them is a midpoint of a shortest path between the other two. The latter endpoints must have distinct row and column coordinates, and the midpoint must be a corner sharing a row with one endpoint and a column with the other. In the bipartite selected-edge graph these three different edges trace a path of length three between four distinct row/column vertices. Conversely, any such selected three-edge path gives precisely this forbidden rook-graph geodesic. Hence \(S\) is in general position exactly when its selected-edge graph contains no three-edge path as a (not necessarily induced) subgraph.

**Step 2: path avoidance forces stars.** A connected bipartite graph without a three-edge path as a subgraph is a star. Indeed, if a connected component has a spanning tree that is not a star, that tree contains such a path. If it has a star spanning tree, with at least three vertices, any additional edge joins two leaves and makes a triangle, impossible in a bipartite graph. Thus the component is exactly the spanning star. The one-vertex and one-edge cases are immediate. Therefore Step 1 gives a size-preserving bijection between general-position rook-graph vertex subsets and edge-selected star forests in the complete bipartite incidence graph.

**Step 3: labeled component enumeration.** Label the \(m\) row vertices and \(n\) column vertices separately and weight every selected edge by \(z\). In the bivariate exponential formula for labeled two-sort structures, an isolated row vertex contributes \(u\); an isolated column vertex contributes \(v\); and an isolated selected edge contributes \(uvz\). Row-centered stars of degree at least two contribute \(u(e^{vz}-1-vz)\), since their nonempty collection of at least two distinctly labeled column leaves carries the indicated exponential series. Similarly, column-centered stars of degree at least two contribute \(v(e^{uz}-1-uz)\). Each star forest is a unique unordered set of these disjoint components, and an isolated edge is counted exactly once (not once for each possible center). Therefore the component generating series is
\[
 u+v+uvz+u(e^{vz}-1-vz)+v(e^{uz}-1-uz)
 =ue^{vz}+ve^{uz}-uvz.
\]
Exponentiating the component series yields (1) as an identity of formal power series in \(u,v\) with polynomial coefficients in \(z\). This proves the enumerator for all nonnegative sizes, with no convergence assumption.

**Step 4: polynomial recurrence.** Let \(F(u,v,z)\) denote the left side of (1). Formal differentiation gives
\[
 \partial_uF=\left(e^{vz}+vz(e^{uz}-1)\right)F.
\]
Expand \(e^{vz}=\sum_{j\geq0}v^jz^j/j!\) and \(vz(e^{uz}-1)=\sum_{k\geq1}v u^kz^{k+1}/k!\). Comparing coefficients of \(u^m v^n/(m!n!)\) yields (2). Empty sides of the bipartition admit only the empty selected-edge set, providing the bases. Computing ascending \(m\) and \(n\) and representing coefficients as integer arrays gives a finite polynomial-arithmetic algorithm for each requested \((m,n)\). Every dependency on the right has strictly smaller row index than the left; there is no circularity.

**Step 5: sharp degree and extremal multiplicities.** If \(\min(m,n)=1\), the rook graph is a complete graph on \(\max(m,n)\) vertices, all subsets are in general position and \(\Psi_{m,n}=(1+z)^{\max(m,n)}\).

Now assume \(m,n\geq2\). A star forest with \(t\) nontrivial components, on \(s\leq m+n\) vertices incident with selected edges, has exactly \(s-t\) selected edges. For \(t=1\), the largest possible star has \(\max(m,n)\) edges, while for \(t\geq2\) there are at most \(m+n-t\leq m+n-2\) selected edges. Two stars centered at a row vertex \(r\) and a column vertex \(c\), selecting all \(n-1\) other columns at \(r\) and all \(m-1\) other rows at \(c\), attain \(m+n-2\). Thus the degree equals \(m+n-2\) throughout this range, as known independently from general-position-number theory.

For \(m,n\geq3\), a maximum configuration cannot be one star because \(\max(m,n)<m+n-2\). It must consist of exactly two nontrivial stars covering all \(m+n\) base vertices. Their centers cannot both be rows (then at least one of the \(m\geq3\) rows would be uncovered), nor both be columns. Hence one center is a row \(r\), the other a column \(c\). Coverage forces precisely the two disjoint stars just constructed; \(r\) and \(c\) are recovered uniquely from their centers. There are exactly \(mn\) choices. When \(m=2<n\), the selected-edge graph of size \(n\) is either one full row-centered star (two choices), or exactly two row-centered stars partitioning the \(n\) columns into two nonempty labeled groups (\(2^n-2\) choices). In the latter case, a component consisting of one edge is of course counted under its unique row assignment. No three-component configuration of size \(n\) is possible since \(s-t\leq(n+2)-3<n\). This gives \(2^n\) total; interchange sides for \(n=2<m\). Finally, \(R_{2,2}\) is the four-cycle, and all six two-vertex sets, and no larger sets, are in general position. Thus (3) holds in every claimed range.

The proof uses exact structural bijections and formal power series, not finite enumeration. \(\square\)

## Verification

The standalone `verify.py` evaluates recurrence (2) over integer coefficient arrays. Independently, for every rectangular board with \(mn\leq16\) and positive side lengths, it tests every vertex subset for a forbidden geodesic triple by rook-graph distance, compares the size distribution with the recurrence, and separately checks whether the associated selected-edge incidence graph has only star components. In total this covers 50 boards and 576,650 tested subsets. Exact recurrence, symmetry, low-degree and extremal checks cover an additional 484 ordered parameter pairs with \(1\leq m,n\leq22\). The actual console output is included in `verification_output.txt` and ends in `VERIFY_OK`. These finite checks test the derivation, not every member of the infinite two-parameter family; the proof above is the infinite argument.

Examples in ascending degree are \(\Psi_{2,3}(z)=1+6z+15z^2+8z^3\) and \(\Psi_{3,3}(z)=1+9z+36z^2+48z^3+9z^4\), verified by two independent counting routes.

## Relationship to prior work

Iršič, Klavžar, Rus and Tuite introduced the general-position polynomial and worked out several graph families and Cartesian products of *paths* [1]. This defines the invariant but does not provide the polynomial of Cartesian products of two complete graphs. Anand et al. previously characterized general-position sets by induced clique components and distance conditions [2]; their general structural theorem is compatible with the present star-forest specialization, but does not count all selected star forests over arbitrary two-sided labeled board sizes. The established formula \(\operatorname{gp}(K_m\square K_n)=m+n-2\) for \(m,n\geq2\) is credited to earlier Cartesian-product work and is summarized in [3]; the scalar maximum is not new. Earlier studies of Cartesian products and general-position numbers [4] do not contain the bivariate polynomial enumeration. The 2025 survey [3] also records maximum and general-position-polynomial results for *path* grids, not the full rook family. Domination polynomials of rook graphs count a different property and do not imply the current result.

A universal graph characterization may be specialized to produce the admissible star-forest condition, so that condition alone is not asserted to be a previously unknown principle. The substantive enumerative contribution is the exact bivariate labeled exponential series, its coefficient recurrence, and the resulting full distribution and leading multiplicities.

## Limitations

The result concerns ordinary general position (no selected triple on a shortest path) for the Cartesian product of two complete graphs, not total/dual/outer general position, direct products or path-grid products. It does not assert unimodality, real-rootedness or an asymptotic law. The source searches and primary-text comparisons support—but cannot certify absolute—novelty; an equivalent count might exist under the terms `star forest`, `three-edge-path-free subgraph`, `rook placement` or `bipartite graph species`, outside the indexed records inspected. Computational checks alone do not establish the all-parameter theorem.

## References

[1] V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first publicly submitted 2024-01-11), subsequently published in *Results in Mathematics*, DOI: 10.1007/s00025-024-02133-3.

[2] B. S. Anand, S. V. Ullas Chandran, M. Changat, S. Klavžar, E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460.

[3] *The General Position Problem: A Survey*, arXiv:2501.19385, §2.3.4 and §2.4.1 (general-position polynomials and Cartesian products; used here as secondary coverage context).

[4] J. Tian and K. Xu, *The general position number of Cartesian products involving a factor with small diameter*, *Applied Mathematics and Computation* (2021), DOI: 10.1016/j.amc.2021.126206.
