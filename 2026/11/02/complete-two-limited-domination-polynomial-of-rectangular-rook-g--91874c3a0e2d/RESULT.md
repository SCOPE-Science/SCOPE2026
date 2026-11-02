# Complete two-limited domination polynomial of rectangular rook graphs

## Finding
For every pair of integers \(m,n\ge4\), let \(R_{m,n}=K_m\square K_n\) be the rook graph, whose vertices are squares of an \(m\times n\) grid, with two squares adjacent precisely when they share a row or column. A set \(D\) is *two-limited dominating* if every vertex outside \(D\) has a neighbor in \(D\), and each vertex in \(D\) has at most two neighbors outside \(D\).

Let \(F_{m,n}(u)=\sum_{D}u^{mn-|D|}\), summed over all two-limited dominating sets. Then
\[
\begin{aligned}
F_{m,n}(u)={}&\sum_{t=0}^{\min(m,n)}\binom mt\binom nt t!u^t
 +\left(m\binom n2+n\binom m2\right)u^2\\
&+4\binom m2\binom n2u^3+\binom m2\binom n2u^4\\
&+m u^n+n u^m+mn(m-1)u^{n+1}+mn(n-1)u^{m+1}\\
&+\binom m2u^{2n}+\binom n2u^{2m}.
\end{aligned}
\]
Terms whose exponents coincide are to be **added**, not identified as overlapping set families. The polynomial by selected-set size is \(L_{m,n}^{(2)}(z)=z^{mn}F_{m,n}(z^{-1})\).

In particular,
\[
\gamma_2^{\mathrm L}(R_{m,n})=mn-2\max\{m,n\}.
\]
The number of minimum two-limited dominating sets is \(\binom m2\) when \(m<n\), \(\binom n2\) when \(n<m\), and \(2\binom m2\) when \(m=n\).

## Assumptions and scope
All graphs are finite, simple, and undirected; \(m,n\ge4\) throughout. Rows have \(n\) vertices and columns have \(m\) vertices. For a candidate selected set \(D\), let \(H=V(R_{m,n})\setminus D\) be its set of *omitted squares*. Put \(r_i=|H\cap\text{row }i|\) and \(c_j=|H\cap\text{column }j|\). Equivalently, view each omitted square \((i,j)\) as an edge of the bipartite incidence graph with row and column vertices.

Every feasible \(H\) is in precisely one of the following disjoint types: (A) a bipartite matching (including the empty matching); (B) a two-edge star, a three-edge path supported on a \(2\times2\) subgrid, or all four cells of a \(2\times2\) subgrid; (C) one complete row plus zero or one omitted square outside that row, or exactly two complete rows; (D) the column analog of (C). Within (B), the three-edge path consists of three of four cells of a \(2\times2\) subgrid. The types are disjoint as configurations, though they can give monomials of the same degree.

## Proof
**Equivalence to occupancy inequalities.** An unselected square \((i,j)\in H\) is undominated exactly when its entire row and its entire column are omitted. Thus \(D\) dominates if and only if no completely omitted row and completely omitted column coexist. For a selected square \((i,j)\notin H\), its omitted neighbors consist of the \(r_i\) omitted squares in its row and the \(c_j\) omitted squares in its column. These sets do not intersect because \((i,j)\notin H\). Therefore the two-limited condition is exactly
\[
r_i+c_j\le2\quad\text{for every }(i,j)\notin H.
\tag{1}
\]
These two tests are necessary and sufficient.

**Case I: no complete row or column.** Every row and column has at least one selected square. Its omitted degree must be at most two, since a selected square in a row containing at least three omitted squares would violate (1). Hence all incidence degrees are at most two. If all degrees are at most one, \(H\) is a matching, giving (A). Otherwise, by interchanging row and column if needed, take an omitted row of degree two, in columns \(a,b\). Any omitted square in a third column \(c\) would leave selected square \((i,c)\) with \(r_i=2,c_c\ge1\), contradicting (1). Therefore \(H\) uses only columns \(a,b\). If three distinct rows were incident to omissions, the two other rows would each have exactly one omission (column degrees are at most two); their omissions would lie in different columns. Then a selected cross square would have row degree one and column degree two, violating (1). Thus at most two rows are incident. With at most two rows and columns, maximum degree two, and some degree two, the only bipartite edge patterns are the two-edge star, three-edge path, or four-edge cycle \(K_{2,2}\). This gives (B). Each pattern satisfies (1), as can be checked on its at most four support squares and on the outside; no row/column is complete because \(m,n\ge4\).

**Case II: a complete omitted row.** Domination excludes any complete omitted column. If at least three rows were complete, every selected square in a remaining row would see at least three omitted neighbors in its column, violating (1); thus there are one or two complete omitted rows. Every noncomplete row has at most one omitted square: if it had two, any selected square in it would see those two plus at least one omission in its column from the complete row. If there are exactly two complete rows, a further omitted square in a third row would create a selected square in that row with row degree one and column degree at least two, contradicting (1). So two complete rows admit no additional omissions.

If there is exactly one complete row, suppose there were two more omissions. They must be in different rows, because each noncomplete row has at most one omission. If their columns differ, the selected cross square in the row of one and column of the other has \(r_i=1,c_j\ge2\), contradicting (1). If their columns agree, that column has at least three omitted squares. Since \(m\ge4\) and the column is not complete, it contains a selected square, which violates (1). Thus at most one additional omission is possible. Conversely, a complete row plus at most one further omission, and exactly two complete rows, meet both tests. This gives (C); exchanging rows and columns gives (D). The case of simultaneous full row and column is excluded by domination. The classification is exhaustive.

**Enumeration.** A size-\(t\) matching chooses \(t\) rows, \(t\) columns, and a bijection: \(\binom mt\binom nt t!\) choices. Two-edge stars number \(m\binom n2+n\binom m2\). A three-edge path occupies a uniquely determined \(2\times2\) subgrid and omits exactly one of its four cells, yielding \(4\binom m2\binom n2\); full blocks number \(\binom m2\binom n2\). There are \(m\) ways to omit one complete row, \(mn(m-1)\) ways to omit one complete row plus an outside square, and \(\binom m2\) ways to omit two complete rows. The corresponding column counts are \(n\), \(mn(n-1)\), and \(\binom n2\). The disjoint classification gives the displayed polynomial.

**Minimum size and its multiplicity.** The largest possible omitted-set size among the types is \(2\max(m,n)\), attained by two complete rows if \(n\ge m\), or two complete columns if \(m\ge n\). Indeed, matchings omit at most \(\min(m,n)\) squares, small blocks at most four, and a single full row or column with one extra square at most \(\max(m,n)+1<2\max(m,n)\) because \(m,n\ge4\). The maximizers therefore are exactly the pairs of complete rows in the first case and pairs of complete columns in the second; both families occur when \(m=n\). This proves the minimum and the stated counts. \(\square\)

## Verification
The standalone \(\texttt{verify.cpp}\) (C++17) independently tests the **original graph definition**: it visits every selected/omitted subset, explicitly traverses rook neighbors, checks domination and the number of omitted neighbors at every selected vertex, and compares the full cardinality histogram with the formula. It separately tests whether each omitted subset has a type from the classification and verifies the minimum and number of minimizers. Entire vertex-set spaces were enumerated for \((m,n)=(4,4),(4,5),(5,4),(5,5)\), respectively \(65,536\), \(1,048,576\), \(1,048,576\), and \(33,554,432\) subsets. The observed numbers of feasible sets were \(553\), \(1,036\), \(1,036\), and \(2,376\), respectively. Every test passed. These finite checks corroborate, rather than replace, the proof for all \(m,n\ge4\).

## Relationship to prior work
Božović, Radić, Kovijanić-Vukićević, and Tepeh introduced \(k\)-limited domination and its regular-graph correspondence to \((1,t)\)-domination. Tepeh's Cartesian-product paper (first publicly posted June 21, 2026) proves the **already known** special value \(\gamma_k^{\mathrm L}(K_{k+2}\square K_{k+2})=2(k+2)\); its \(k=2\) instance is the \(4\times4\) minimum. That minimum is not claimed as new. The present classification supplies all two-limited dominating sets, their cardinality enumerator, the complete rectangular minimum formula, and exact minimizer counts, none derived from that special minimum statement.

Mertens computes the ordinary rook-graph domination polynomial without the capacity/two-limited restriction; its coefficients do not determine the constrained enumerator by themselves. The same rook graphs are also line graphs of complete bipartite graphs, or two-coordinate Hamming graphs. These equivalent graph descriptions were considered in the priority comparison. An identical result in unindexed literature cannot be excluded.

## Limitations
The theorem requires \(m,n\ge4\) and exactly the two-limited condition; it makes no claim for smaller dimensions, general \(k\), or arbitrary Cartesian products. Originality has been compared against identified available sources, not independently certified as historically unique. All proof and computational review reported here is internal/self-review; independent mathematical audit has not occurred.

## References
1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, and A. Tepeh, *On \(k\)-limited domination in graphs*, arXiv:2606.22422 (first posted 2026-06-21). https://arxiv.org/abs/2606.22422
2. A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (first posted 2026-06-21), Section 4, Proposition 6. https://arxiv.org/abs/2606.22428
3. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (2024). https://arxiv.org/abs/2401.00716
