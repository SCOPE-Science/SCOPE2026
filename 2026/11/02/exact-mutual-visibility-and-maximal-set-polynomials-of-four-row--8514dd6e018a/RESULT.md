# Exact mutual-visibility and maximal-set polynomials of four-row rook graphs

## Finding

Write \(R_{4,n}=K_4\square K_n\) for the Cartesian product of complete graphs, where \(n\ge 2\). A mutual-visibility set \(S\) requires, for each two vertices of \(S\), a shortest path between them with no other vertices of \(S\) internally. Let \(V_n(z)=\sum_S z^{|S|}\), summed over **all** mutual-visibility sets (including the empty set). Put \((a)_{t}=a(a-1)\cdots(a-t+1)\) for \(0\le t\le a\), and \((a)_0=1\). Then

\[
\begin{aligned}
V_n(z)={}&\sum_{t=0}^{\min(6,n)}\binom nt(6)_t z^{2t}(1+4z)^{n-t}\\
&+4nz^3\sum_{t=0}^{\min(3,n-1)}\binom{n-1}{t}(3)_t z^{2t}(1+4z)^{n-1-t}\\
&+nz^4(1+4z)^{n-1}.
\end{aligned}
\]

For \(n\ge6\), let \(M_n(z)\) sum \(z^{|S|}\) over **inclusion-maximal** mutual-visibility sets. Their entire polynomial is

\[
\begin{aligned}
M_n(z)={}&[n4^{n-1}+12(n)_2+4(n)_3]z^{n+3}\\
&+12(n)_3 2^{n-3}z^{n+4}\\
&+[4(n)_4 4^{n-4}+6(n)_5 2^{n-5}]z^{n+5}\\
&+(n)_6 4^{n-6}z^{n+6}.
\end{aligned}
\]

Every coefficient displayed here is strictly positive, so the inclusion-maximal sizes are exactly \(n+3,n+4,n+5,n+6\) for \(n\ge6\). In particular, under the **uniform distribution on inclusion-maximal sets**, rather than a random greedy construction,

\[
\Pr(|S|=n+6)=1-\frac{64}{n^2}+O(n^{-3})\qquad (n\to\infty).
\]

The previously established minimum maximal-set size \(n+3\) is **not** claimed as new. The contributions here are the two complete enumerators, the four-stratum multiplicities, and their distributional consequence.

## Assumptions and scope

Graphs are finite, simple and undirected. Vertices of \(R_{4,n}\) are \((i,j)\) with row \(i\in\{1,2,3,4\}\) and column \(j\in\{1,\ldots,n\}\); distinct vertices are adjacent if and only if they share a row or share a column. The cardinality-polynomial counts labeled vertex sets, not graph-isomorphism classes, orders of selection, or shortest-path choices. Maximal means inclusion-maximal, not necessarily maximum-cardinality. The full polynomial \(V_n\) holds for all integers \(n\ge2\); \(M_n\) and the four-size statement are asserted for integers \(n\ge6\).

## Proof

**1. Rectangle obstruction.** Same-row or same-column vertices are adjacent, hence automatically mutually visible. For two selected cells in distinct rows and columns, the distance is two, with exactly two possible intermediate cells: the other two corners of their Cartesian rectangle. Those endpoints lack an internally unselected shortest path precisely when both other corners are selected. Consequently a set is mutually visible if and only if **no two columns share a selected pair of rows**. This agrees with the earlier Cartesian-product visibility/rectangle characterization [1].

**2. Exhaustive structures and \(V_n\).** For each column \(j\), let \(C_j\subseteq\{1,2,3,4\}\) be its selected rows. Regard each unordered row pair \(e\) as one of the six edges of \(K_4\). A column \(C_j\) consumes exactly the pairs in \(\binom{C_j}{2}\), and no pair may be consumed by two columns. In particular, all columns of size two consume distinct pairs. If a column contains three rows \(T\), then its three internal pairs are consumed, and every size-two column can only consume an edge between the omitted fourth row and a row of \(T\); there are at most three such distinct edges. No second triple is possible, because two triples from four rows intersect in at least two rows. A column of size four consumes all six pairs and precludes every other nonsingleton column.

Thus configurations split disjointly into: (A) \(t\) size-two columns labeled by distinct edges of \(K_4\), with the other columns empty or singleton; (B) one size-three column (four choices of its row triple), \(t\) size-two columns labeled by distinct edges joining the omitted row to that triple, and all other columns empty or singleton; (C) one size-four column, all others empty or singleton. In case (A), choose the \(t\) columns and injectively assign row pairs, obtaining \(\binom nt(6)_t z^{2t}(1+4z)^{n-t}\). Case (B) contributes \(4n\binom{n-1}t(3)_t z^{3+2t}(1+4z)^{n-1-t}\). Case (C) contributes \(nz^4(1+4z)^{n-1}\). Summation proves the first polynomial, including all boundary terms.

**3. Criterion for maximality.** Every column in a maximal set is nonempty: an empty column can receive one vertex. A singleton occupying row \(i\) can receive a second selected row unless the pair \(\{i,k\}\) has already been consumed in another column, for every \(k\ne i\). Thus singleton row \(i\) must have all three incident row pairs already consumed. A size-two column occupying rows \(u,v\) can gain another row \(w\) if both \(uw\) and \(vw\) are unconsumed elsewhere; therefore it is blocked precisely when for every \(w\notin\{u,v\}\), at least one of \(uw,vw\) is already consumed. These conditions test every possible one-vertex extension, and the no-rectangle property is hereditary, so they are necessary and sufficient for inclusion-maximality.

**4. A four-row classification of maximal configurations.** A size-four column may be placed in any of \(n\) columns; every other column is any of four singletons, giving \(n4^{n-1}\) sets, each of size \(n+3\).

For a size-three column \(T\), write \(d\) for the omitted row. The only eligible size-two columns consume distinct pairs \(di\), \(i\in T\). Let their number be \(t\). The triple itself is extendible to all four rows if \(t=0\), while for \(t=1,2,3\) it is blocked. All \(t\) size-two columns are also blocked because adding any other row repeats an internal pair of \(T\). The rows permitted in a singleton column are exactly the \(t\) vertices \(i\in T\) for which \(di\) was used, and also \(d\) when \(t=3\). Hence the singleton alphabet has sizes \(1,2,4\) for \(t=1,2,3\). Choosing the triple column, its four possible row triples, and injectively distributing \(t\) of the three links over distinct columns yields respectively
\[
12(n)_2 z^{n+3},\quad 12(n)_3 2^{n-3}z^{n+4},\quad4(n)_4 4^{n-4}z^{n+5}.
\]

Finally suppose all nonsingleton columns have size two. Form the simple graph \(F\subseteq K_4\) of row-pairs consumed by those columns. For the size-two columns to be unextendible, every edge \(uv\in E(F)\) must satisfy: every other row \(w\) is adjacent in \(F\) to at least one of \(u,v\). This condition forces \(F\) to be connected and have at least three edges (otherwise some edge has a nonneighbor outside its endpoints). A connected three-edge graph on four vertices is either a star or a path, but an end edge of the path fails the condition. A connected four-edge graph is either \(C_4\) or a triangle with a pendant edge, but the latter fails at the edge opposite the pendant attachment. Both five-edge \(K_4-e\) and six-edge \(K_4\) satisfy the condition. Thus the only possibilities are \(K_{1,3},C_4,K_4-e,K_4\).

Because \(n\ge6\), any \(F\) with at most five edges leaves at least one singleton column, which must use a degree-three vertex of \(F\). The four-cycle has none and so cannot occur. A star has exactly one such vertex; there are four choices of center, and its three distinct edges can be assigned to an ordered triple of columns in \((n)_3\) ways, contributing \(4(n)_3z^{n+3}\). A \(K_4-e\) has two degree-three vertices; there are six choices for its missing edge, and its five distinct edges can be assigned to columns in \((n)_5\) ways, contributing \(6(n)_5 2^{n-5}z^{n+5}\). The complete \(K_4\) has four degree-three vertices and six distinct edges, contributing \((n)_6 4^{n-6}z^{n+6}\). Adding these contributions to the size-three/four cases proves the second polynomial.

**5. Asymptotic sampling.** The \(n+6\) coefficient is \((n)_6 4^{n-6}\). The dominant competing \(n+5\) term divided by it is exactly \(64/((n-4)(n-5))\). Every other ratio is \(O(n^{-3})\) or exponentially small. Dividing the maximum-size count by the total number of maximal sets and expanding proves \(1-64/n^2+O(n^{-3})\).

## Verification

A standalone Python 3 checker (`verify.py`, no third-party dependencies) independently represents the selected rows of each column by a four-bit mask. For \(n\le4\), it explicitly checks the original two-intermediate-vertex shortest-path definition against the row-pair characterization. For \(2\le n\le5\), it examines every one of the \(2^{4n}\) subsets and checks every possible one-vertex extension. For \(n=6\), a separate repeated-row-pair pruning recursion enumerates all 1,401,445 admissible configurations. It independently counts their sizes and maximal subsets and compares them with the formula coefficients.

The complete counts of admissible sets at \(n=2,3,4,5,6\) are respectively \(189,1952,18521,165120,1401445\). The maximal-set counts grouped by size at \(n=6\) are \((9:6984),(10:11520),(11:31680),(12:720)\). All checks pass; these finite checks supplement but do not replace the proof for all \(n\).

To reproduce: run `python3 verify.py` in the directory containing the extracted standalone file. It prints per-parameter counts and `ALL_CHECKS_PASS`.

## Relationship to prior work

Cicerone, Di Stefano, and Klavžar [1] established the Cartesian product mutual-visibility connection to the Zarankiewicz/rectangle-free problem; the present proof takes that structural correspondence as known and computes an explicit four-row cardinality distribution. Brešar and Yero [2] showed that the lower mutual-visibility number for products of complete graphs is the sum of the factor orders minus one; thus the minimum maximal-set size \(n+3\) is an existing consequence, not a novel scalar. Bujtás, Klavžar, and Tian [3] introduced visibility polynomials and supplied general identities involving maximal visible sets; those identities do not themselves provide the explicit four-row maximal-set census proved here. The row-pair injectivity formulation is equivalent to counting \(K_{2,2}\)-free subgraphs of \(K_{4,n}\); the new coefficients remain subject to possible priority from specialized bipartite graph enumeration literature.

## Limitations

The maximal-set formula is limited to \(n\ge6\); smaller \(n\) can admit additional terminal configurations, notably all four double-occupied columns arranged as a row-pair four-cycle when \(n=4\). These claims enumerate labeled subsets only and provide no general \(K_m\square K_n\) maximal-set formula for variable \(m\). The asymptotic statement assumes **uniform sampling among maximal sets** and does not describe random sequential greedy construction. The findings have not received independent mathematical audit. Priority cannot be ruled out against unpublished, unindexed or differently formulated enumerations of maximal \(C_4\)-free bipartite graphs.

## References

[1] S. Cicerone, G. Di Stefano, S. Klavžar, “On the mutual visibility in Cartesian products and triangle-free graphs,” arXiv:2112.13024 (first public submission 2021-12-24), https://arxiv.org/abs/2112.13024 .

[2] B. Brešar, I. G. Yero, “Lower (total) mutual visibility in graphs,” arXiv:2307.02951 (first public submission 2023-07-06), https://arxiv.org/abs/2307.02951 .

[3] C. Bujtás, S. Klavžar, J. Tian, “Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets,” Aequationes Mathematicae 99 (2025), DOI:10.1007/s00010-025-01197-y, https://doi.org/10.1007/s00010-025-01197-y .
