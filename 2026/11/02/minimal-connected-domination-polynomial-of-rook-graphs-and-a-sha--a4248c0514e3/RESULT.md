# Minimal connected domination polynomial of rook graphs and a sharp gap in cardinalities

## Finding
For integers \(m,n\ge2\), write \(R_{m,n}=K_m\square K_n\). A vertex set \(D\) is **connected dominating** if every vertex is in \(D\) or adjacent to it and the induced graph \(R_{m,n}[D]\) is connected. It is **inclusion-minimal connected dominating** if no proper subset has these two properties. Define
\[
M_{m,n}(z)=\sum_{D\text{ inclusion-minimal connected dominating}}z^{|D|}.
\]
Let \(\bigl\{{a\atop b}\bigr\}\) be the number of partitions of an \(a\)-element labeled set into \(b\) nonempty blocks (with the usual zero convention), and put \(q=\min(m-1,n-1)\). Then
\[
\boxed{M_{m,n}(z)=\sum_{c=1}^{q}\binom nc\,m^{c-1}c!\bigl\{{m-1\atop c}\bigr\}z^{m+c-1}+\sum_{r=1}^{q}\binom mr\,n^{r-1}r!\bigl\{{n-1\atop r}\bigr\}z^{n+r-1}.}
\]
The two summations correspond to disjoint combinatorial families. For \(2\le m\le n\), the cardinality support is precisely
\[
\{m,m+1,\ldots,2m-2\}\ \cup\ \{n,n+1,\ldots,n+m-2\}.
\]
In particular the smallest and largest possible cardinalities are \(m\) and \(m+n-2\). The support is not an interval exactly when \(n\ge2m\), in which case every size from \(2m-1\) through \(n-1\) is absent. There are \(n\) minimum sets when \(m<n\), and \(2n\) when \(m=n\). The number of maximum sets equals
\[
\begin{cases}
 m\,n^{m-2}(m-1)!\bigl\{{n-1\atop m-1}\bigr\},&m<n,\\
 2m!m^{m-2},&m=n.
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, undirected. Both parameters are integers at least two, with no assumption that they coincide. The terms *minimal* (inclusion-minimal) and *minimum* (smallest cardinality) are distinct. The displayed polynomial counts labeled vertex subsets, not graph-isomorphism classes. The assertion covers all such parameters and all cardinalities; it is not a formula merely for minimum sets.

## Proof
**1. Convert to a bipartite edge problem.** Identify the cell \((i,j)\) of \(R_{m,n}\) with the edge \(i j\) joining row vertex \(i\in[m]\) and column vertex \(j\in[n]\) in \(K_{m,n}\). Under this identification \(R_{m,n}=L(K_{m,n})\). A nonempty chosen rook set \(D\) corresponds to a bipartite edge set \(F\) and its incident subgraph \(H=(R\cup C,F)\) on occupied row and column vertices. The rook induced graph \(R_{m,n}[D]\) is connected exactly when \(H\) is connected (ignoring isolated unoccupied vertices). Furthermore \(D\) dominates the rook graph precisely when all rows are occupied or all columns are occupied: if a row and a column are both unoccupied, their crossing cell is not dominated; conversely every cell sharing an occupied row or an occupied column has a selected neighbor or is selected itself.

**2. Characterize minimality.** Suppose \(D\) is inclusion-minimal connected dominating. If \(H\) has a cycle, deleting any cycle edge keeps \(H\) connected, all its occupied vertices incident, and the domination condition, contradicting minimality. Thus \(H\) is a tree. If both shores are fully occupied, removing any leaf edge retains a connected nonempty tree and leaves the opposite shore fully occupied; since \(m,n\ge2\), this is a proper connected dominating subset. Hence precisely one shore is fully occupied. If all \(m\) rows are occupied and only \(c<n\) columns are occupied, any occupied column of degree one would permit deletion of its leaf edge, because all row vertices remain occupied, contradicting minimality. Thus all \(c\) occupied columns have degree at least two. Since a bipartite tree with \(m+c\) vertices has \(m+c-1\) edges, summing degrees on the column shore gives \(m+c-1\ge2c\), so \(1\le c\le m-1\), as well as \(c\le n-1\). The opposite orientation is symmetric.

Conversely, suppose \(H\) is a tree spanning every row and a proper nonempty subset of columns, and each occupied column has degree at least two. The edge set dominates and is connected. Deleting an edge incident to a degree-one row vertex leaves that row unoccupied and at least one column unoccupied, so domination fails. Every remaining edge has two endpoints of degree at least two; its deletion splits the edge set into two nonempty connected pieces, so the rook induced graph becomes disconnected. Thus no one-edge deletion is connected dominating. This implies full inclusion-minimality: if a proper subset of a connected dominating set were connected dominating, start with that subset and successively reintroduce the remaining selected vertices along a spanning tree of the connected induced graph, ending with a selected vertex whose removal still leaves a connected superset of the smaller dominating set. This would provide a one-vertex deletion preserving both properties. The same argument holds after interchanging rows and columns.

Therefore every minimal connected dominating set corresponds uniquely to one of two types of bipartite trees: all rows plus a proper collection of columns, with each included column of degree at least two, or the symmetric alternative. The types are disjoint because neither has both shores fully occupied.

**3. Enumerate the trees.** Choose the \(c\) occupied columns in \(\binom nc\) ways. The bipartite Prüfer encoding of trees on \(m\) labeled row vertices and \(c\) labeled column vertices consists of a word of length \(c-1\) in row labels and a word of length \(m-1\) in column labels. In this encoding the degree of each column is one plus its multiplicity in the second word; this is also immediate from the multivariate bipartite Cayley identity
\[
\sum_{T}\prod_{i=1}^m x_i^{\deg_T(i)-1}\prod_{j=1}^c y_j^{\deg_T(j)-1}
=(\sum_i x_i)^{c-1}(\sum_j y_j)^{m-1}.
\]
The row word is arbitrary, giving \(m^{c-1}\) possibilities. Every chosen column must appear at least once in the second word, giving exactly \(c!\bigl\{{m-1\atop c}\bigr\}\) surjections. The tree has \(m+c-1\) edges, hence the first sum. Transposing the construction gives the second sum.

**4. Extremal coefficients and the support gap.** In either sum every allowed Stirling number is positive; hence the two support intervals follow. For \(m\le n\), their first exponents are \(m\) and \(n\), and their final exponents are \(2m-2\) and \(m+n-2\). The gap criterion and extrema follow. Minimum terms use \(c=1\), giving one full-row-shore star for each column, with the transposed stars tying only when \(m=n\). For \(m<n\), the maximum term comes only from the transposed sum with \(r=m-1\); its coefficient simplifies to \(m n^{m-2}(m-1)!\bigl\{{n-1\atop m-1}\bigr\}\). When \(m=n\), both maximum terms contribute equally, giving \(2m!m^{m-2}\). All claimed cases include \(m=n=2\).

## Verification
The accompanying standalone Python 3 checker, `verify_rook_minimal_connected_domination.py`, constructs each graph directly from row/column adjacency; exhaustively tests domination, induced connectivity, and deletion minimality for all nonempty subsets on 17 tested ordered graph dimensions (up to 20 vertices); independently compares coefficient dictionaries; and checks the Stirling surjection identity by direct word enumeration for lengths at most six. Its completed output includes `VERIFY_OK: 17 graph orders; 1444991 nonempty subsets`. Sample exact polynomials are
\[
M_{3,3}(z)=6z^3+36z^4,\quad
M_{3,4}(z)=4z^3+39z^4+72z^5,\quad
M_{3,6}(z)=6z^3+90z^4+3z^6+540z^7.
\]
These finite computations corroborate, but do not establish, the infinite theorem. The infinite argument is the structural bijection and labeled-tree enumeration above.

## Relationship to prior work
General enumeration and upper bounds for inclusion-minimal connected dominating sets were developed by Lokshtanov, Pilipczuk, and Saurabh (first posted November 2, 2016), and later by Abu-Khzam and coauthors. Their reviewed theorems concern algorithms and bounds for general graphs, rather than a closed all-parameter polynomial for Cartesian products of complete graphs. The connected domination polynomial of Yoosuf and Kuttipulackal, and the algebraic/homological formulation of Caputi, Celoria, and Collari, enumerate **all** connected dominating sets rather than the inclusion-minimal subfamily. A computer-algebra graph library also tabulates the minimal connected domination polynomial of individual named graphs; a finite table does not imply this two-parameter formula and gap classification. Standard bipartite tree counts and the scalar connected domination minimum are not claimed as new.

## Limitations
The theorem does not classify minimal connected dominating sets of arbitrary Cartesian products or count graph-isomorphism orbits. The Prüfer formula is a labeled enumeration and is not a complexity bound for arbitrary input graphs. Literature comparison reduces but cannot eliminate the risk that an equivalent formula appears in unindexed sources or is an unstated corollary of a stronger published theorem. No independent mathematical audit has been performed.

## References
1. D. Lokshtanov, M. Pilipczuk, S. Saurabh, *Below All Subsets for Minimal Connected Dominating Set*, arXiv:1611.00840v1 (first public 2016-11-02), later SIAM J. Discrete Math. 32 (2018), 2332–2345, DOI:10.1137/17M1138753.
2. F. N. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, K. Mann, *Enumerating Minimal Connected Dominating Sets*, ESA 2022, DOI:10.4230/LIPIcs.ESA.2022.1.
3. V. Caputi, C. Celoria, C. Collari, *Categorifying Connected Domination via Graph Überhomology*, arXiv:2201.00721 (2022).
4. E. W. Weisstein, *Minimal Connected Dominating Set*, MathWorld, https://mathworld.wolfram.com/MinimalConnectedDominatingSet.html (accessed 2026-10-29).
5. M. Yoosuf and P. B. Kuttipulackal, *The Connected Domination Polynomial of Some Graph Constructions*, J. Phys.: Conf. Ser. 1850 (2021), 012043, DOI:10.1088/1742-6596/1850/1/012043.
