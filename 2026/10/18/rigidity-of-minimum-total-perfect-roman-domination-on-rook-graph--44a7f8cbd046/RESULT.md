# Rigidity of minimum total perfect Roman domination on rook graphs

## Finding
For every integer pair \(2\le m\le n\), let \(G_{m,n}=K_m\square K_n\). Its total perfect Roman domination number is
\[
\gamma_{tR}^{p}(G_{m,n})=2m.
\]
Every minimizing function is obtained by assigning \(2\) to every vertex of one column and \(0\) elsewhere, or (only when \(m=n\)) by assigning \(2\) to every vertex of one row and \(0\) elsewhere. The sole exception is \(G_{2,2}\), for which there are nine additional minima: one all-one function and eight functions of weight four that have one vertex labeled \(2\), the opposite vertex labeled \(1\), and exactly one of the two remaining vertices labeled \(1\) (the other \(0\)). Consequently, the number of minimum functions on the labeled vertex set is
\[
N_{m,n}=n+m\mathbf1_{\{m=n\}}+9\mathbf1_{\{m=n=2\}}.
\]
In particular, for nonsquare boards the entire minimum labeling is determined by the choice of one column; there are precisely \(n\) choices.

## Assumptions and scope
Graphs are finite, simple, undirected. Write vertices as cells \((i,j)\), with \(1\le i\le m\), \(1\le j\le n\); two different cells are adjacent precisely when they share a row or column. A total perfect Roman dominating function is a map \(f:V(G_{m,n})\to\{0,1,2\}\) satisfying both conditions: (i) each zero-labeled vertex has **exactly one** neighbor labeled \(2\), and (ii) the subgraph induced by all positively labeled vertices has minimum degree at least one. Its weight is \(w(f)=\sum_{v\in V(G_{m,n})}f(v)\). All formulae concern the labeled vertex set, not orbits under graph automorphisms. No assertion is made for \(m=1\).

## Proof
**Upper bound.** Fix a column and label all its \(m\) vertices by \(2\), all others by \(0\). Every zero sees precisely the label-two vertex in its own row. The positively labeled vertices induce a clique of order \(m\ge2\), hence no isolated vertex. Weight is \(2m\). When \(m=n\), the same construction can use an entire row.

**Counting forced positive labels.** Let \(T=f^{-1}(2)\) have size \(k\). Suppose \(1\le k<m\). Let \(R\) and \(C\) be the sets of rows and columns meeting \(T\), of respective sizes \(r,c\). Necessarily \(1\le r,c\le k<m\). All \((m-r)(n-c)\) cells outside both \(R\) and \(C\) see no label-two vertex and therefore must have label \(1\). Every cell within \(R\times C\) that is not in \(T\) sees at least one label-two neighbor in its row and a distinct label-two neighbor in its column, and therefore also must have label \(1\). These two regions are disjoint. Hence
\[
|f^{-1}(1)|\ge(m-r)(n-c)+rc-k,
\qquad w(f)\ge k+(m-r)(n-c)+rc.\tag{1}
\]
Put \(s=\max\{r,c\}\) and \(t=\min\{r,c\}\). As \(n\ge m\), \(k\ge s\), and \(1\le t\le s\le m-1\), (1) yields
\[
w(f)\ge s+(m-s)(m-t)+st.\tag{2}
\]
For \(m\ge4\), if \(2s\le m\), the coefficient of \(t\) in (2) is nonpositive, giving
\[
w(f)\ge s+(m-s)^2+s^2\ge \frac{m^2}{2}+1\ge2m+1.
\]
If \(2s>m\), the coefficient is positive; setting \(t=1\) gives
\[
w(f)\ge m(m-1)-s(m-3)\ge3(m-1)\ge2m+1.
\]
For \(m=3\), equation (1) is at least \(7\) whenever \(n\ge4\): replacing \(n\) by \(3\) lowers its right side by at least \(n-3\ge1\), while the finitely many possible \((k,r,c)\) for \(n=3\) all give at least \(6\). At \(m=n=3\), the only possible equality patterns of (1) with value \(6\) are \((k,r,c)=(1,1,1),(2,1,2),(2,2,1)\). In the first, equality makes the unique label-two vertex isolated in the positive-induced graph. In the second, the cell in the occupied row and unoccupied column has two label-two neighbors and is forced to label \(1\) *in addition* to the regions counted in (1). The third case is symmetric. Thus no \(k<m\) attains weight \(2m\) when \(m\ge3\).

For \(m=2\), necessarily \(k=1\), \(r=c=1\). Equation (1) becomes \(w(f)\ge n+1\), which exceeds four if \(n\ge4\). If \(n=3\), achieving equality would make all label-one vertices lie in the row-and-column complement of the unique label-two vertex, leaving that vertex isolated in the positive-induced graph. So weight four is impossible. If \(n=2\), each weight-four function with \(k=1\) must label the opposite vertex \(1\) and choose exactly one of the two neighboring vertices to label \(1\); either choice works. There are four choices for the label-two vertex and two choices for the additional label-one vertex, giving eight functions.

**At least \(m\) label-two vertices.** If \(k\ge m\), then \(w(f)\ge2k\ge2m\); equality requires \(k=m\) and no label ones. Thus every cell outside \(T\) has exactly one neighbor in \(T\), and \(G[T]\) has no isolates. If both an unoccupied row and an unoccupied column existed, their intersection would have no neighbor in \(T\); hence either \(T\) meets all \(m\) rows or all \(n\) columns. If it meets all rows, its \(m\) vertices occupy precisely one cell in each row. If two selected cells occurred in distinct columns, either cross-corner between their rows and columns would be unselected and adjacent to both selected cells, impossible. Therefore all label-two cells lie in one column. If it meets all columns, since \(k=m\le n\), necessarily \(n=m\); the symmetric argument forces a whole row. These configurations are valid by the upper-bound construction.

Finally if \(k=0\), zero labels are impossible under condition (i), so the function is identically one and has weight \(mn\). With \(2\le m\le n\), it has weight \(2m\) only for \(m=n=2\); the positive subgraph is then the entire graph and has no isolates. This supplies the ninth exceptional function. The whole-column family has \(n\) members, the square case has \(m\) additional whole-row members, and the exceptional functions add nine, proving the claimed count.

## Verification
A standalone dependency-free program, `verify_tpr_rook.py`, exhaustively evaluates all \(3^{mn}\) labelings for seven boards up to \(3\times4\) and separately enumerates all labelings of weight at most \(2m\) through the possible defender sets on six additional boards up to \(5\times5\). It checks the exact minimizing weight and number against the theorem in thirteen cases, including the exceptional \(2\times2\) count of thirteen. Its recorded output is in `verify_tpr_rook.out`. The computational tests corroborate but do not replace the general proof above.

## Relationship to prior work
Almulhim [1] defined total perfect Roman domination and determined this parameter for complete multipartite graphs (Proposition 2). These are not the rook graphs \(K_m\square K_n\) in general; the sole intersection at \(m=n=2\) is the four-cycle, whose numerical minimum was already covered. Almulhim, Akwu, and Al Subaiei [2] studied *perfect Roman* (without the positive-support condition) on Cartesian grids and cylinders built from paths and cycles, not total perfect Roman domination on Cartesian products of complete graphs. The present result is the exact classification and multiplicity of total perfect Roman minimum labelings for all rook graphs. A search of mathematical research records and indexed literature did not locate a statement entailing this result. Absence from searched records does not establish universal novelty.

## Limitations
The graph factors must both have at least two vertices, and the classification concerns minimum-weight functions only, not the full weight polynomial. Bibliographic searches cannot exclude equivalent results in unpublished or unindexed literature. The proof and computational checks have not undergone independent scientific audit.

## References
[1] A. Almulhim, "Total Perfect Roman Domination," *Symmetry* 15 (2023), 1676. DOI: 10.3390/sym15091676; first publicly dated 2023-08-31. Full-text PDF: https://pdfs.semanticscholar.org/df1f/c7e883486c82017aff34cacb2c5955260645.pdf.

[2] A. Almulhim, A. D. Akwu, and B. Al Subaiei, "The Perfect Roman Domination Number of the Cartesian Product of Some Graphs," *Journal of Mathematics* (2022), Article 1957027. DOI: 10.1155/2022/1957027; https://onlinelibrary.wiley.com/doi/10.1155/2022/1957027.
