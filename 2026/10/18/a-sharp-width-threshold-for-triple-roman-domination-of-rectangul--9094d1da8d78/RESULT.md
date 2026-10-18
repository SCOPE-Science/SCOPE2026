# A sharp width threshold for triple Roman domination of rectangular rook graphs

## Finding

For all integers \(2\le m\le n\), the Cartesian product of complete graphs satisfies
\[
\gamma_{[3R]}(K_m\square K_n)=\min\{4m,\,2m+n\}.
\]
Equivalently, its minimum defense weight is \(2m+n\) for \(m\le n\le2m\) and \(4m\) for \(n\ge2m\). At the square board the value is \(3m\), while increasing the number of columns beyond twice the number of rows does not increase the minimum. This is one theorem, including the explicit constructions and matching lower bound below.

## Assumptions and scope

A rectangular rook graph has vertex set \(\{(i,j):1\le i\le m,\,1\le j\le n\}\). Distinct vertices are adjacent precisely when they share a row or column. A triple Roman dominating function on a finite simple graph is a map \(f:V\to\{0,1,2,3,4\}\) such that for each \(v\) with \(f(v)<3\),
\[
f(v)+\sum_{u\in N(v):\,f(u)>0}(f(u)-1)\ge3.
\]
Its weight is \(\sum_{v\in V}f(v)\), and \(\gamma_{[3R]}(G)\) is the minimum weight. The neighborhood in the displayed definition is open and excludes \(v\). This definition is equivalent to the active-neighborhood formulation in the foundational literature. The theorem concerns every pair of integers in the stated domain and makes no assertion about other Roman-type parameters or noncomplete Cartesian factors.

## Proof

Fix a feasible labeling. Put \(a_{ij}=\max\{f(i,j)-1,0\}\), and let the row surplus \(r_i=\sum_j a_{ij}\), column surplus \(c_j=\sum_i a_{ij}\), total surplus \(B=\sum_i r_i=\sum_j c_j\), and number \(T\) of positive-labeled cells. The weight is exactly \(W=B+T\). At a zero cell the defense inequality says \(r_i+c_j\ge3\); at a cell labeled one it says \(r_i+c_j\ge2\); at a cell labeled two it says \(r_i+c_j\ge3\), because the cell's own surplus appears once in each of the row and column sums. At labels three and four no such condition is needed. These are equivalences, not relaxations.

**Lower bound.** If a column \(j\) has \(c_j=0\), its cells have labels zero or one. Every row then has \(r_i\ge2\): a zero in this column forces surplus at least three, and a one forces at least two. If \(r_i\ge3\), that row has at least one positive cell and therefore weight at least four. If \(r_i=2\), its entry in column \(j\) must be one; at least one additional positive entry supplies its two units of surplus, again giving row weight at least four. Summing the disjoint row weights yields \(W\ge4m\).

Now suppose instead that \(c_j\ge1\) for every column. Then \(T\ge n\). If every row has \(r_i\ge2\), we have \(B\ge2m\) and thus \(W\ge2m+n\).

Otherwise choose a row with \(r_i\le1\). If \(r_i=0\), every column must have \(c_j\ge2\). Indeed, when \(c_j=1\), the entry in this row is zero or one, and in either case its defense inequality fails. Therefore \(B\ge2n\) and \(W\ge3n\ge2m+n\), using \(n\ge m\).

If \(r_i=1\), let \(a\) denote the number of columns with \(c_j=1\). For each such column, its cell in the selected row must have label one: label zero would require a combined surplus at least three, label two would likewise require three, and labels three or four would make the row surplus at least two. Since this label-one cell contributes no surplus, a distinct positive cell supplies the column's unit of surplus. These \(a\) columns each contain at least two positive cells; every remaining column contains at least one. Hence \(T\ge n+a\). Also \(B=\sum_j c_j\ge a+2(n-a)=2n-a\). Therefore \(W\ge3n\ge2m+n\). In every case \(W\ge\min\{4m,2m+n\}\).

**Upper bound.** If \(n\ge2m\), label exactly one cell in every row with four, choosing the same column each time; label all other cells zero. Every zero cell has a four-labeled neighbor in its row, so the total weight is \(4m\).

If \(m\le n\le2m\), put \(k=n-m\). Select \(k\) rows and put label two in two distinct columns of each such row. Put label three in one column of each of the remaining \(m-k\) rows. Use each of the \(n\) columns exactly once for these positive cells; this is possible since the number of occupied cells is \(2k+(m-k)=m+k=n\). All unlisted cells have label zero. Every row has surplus exactly two, and every column has surplus at least one. Thus each zero cell and each label-two cell meets the appropriate inequality; label-three cells need no check. Its weight is \(4k+3(m-k)=3m+k=2m+n\). The constructions meet the lower bound, proving the formula.

## Verification

The accompanying standalone Python source `verify.py` performs 1,485 explicit construction checks for parameters \(2\le m\le34\) and \(m\le n\le3m+8\), testing the defining inequalities and matching weights. It also exhaustively rejects every labeling with weight smaller than the formula on six small boards: \(2\times2\), \(2\times3\), \(2\times4\), \(2\times6\), \(3\times3\), and \(3\times4\). Running `python3 verify.py` produces the attached `verification_output.txt`, ending in `VERIFY_OK`. Finite computation corroborates but does not substitute for the proof for arbitrary dimensions.

## Relationship to prior work

The foundational work of Abdollahzadeh Ahangar and coauthors introduces triple Roman domination, its defense inequality, general bounds, and exact values for selected families. The full openly available text of its preprint was inspected, including definitions and the results on graph classes. The later \([k]\)-Roman study by Valenzuela-Tripodoro and coauthors investigates general degree bounds and selected graph families such as paths and cycles, not the Cartesian product of complete graphs. Those generic inequalities do not imply the matching rectangular-rook formula: for example, the standard lower bound \(\lceil4|V|/(\Delta+1)\rceil\) is only \(\lceil100/9\rceil=12\) on the \(5\times5\) board, whereas the exact value here is \(15\). Hajjari and coauthors study general upper bounds and other classes. A separate 2023 paper on \([k]\)-Roman domination could be accessed at the abstract level, but not in full text; this uncertainty is recorded in the accompanying review. Results concerning ordinary, double, strong, independent, or total Roman domination are not the same invariant. The claims made here are conditional on the comparative source coverage actually inspected; a search does not prove novelty.

## Limitations

The result applies to \(m,n\ge2\), and the proof's orientation assumes \(m\le n\). It does not classify every optimal labeling, determine generating polynomials, or address arbitrary Cartesian-product factors. The claim has a complete unrestricted combinatorial proof but has not undergone independent review. Overlap under alternative terminology or in inaccessible or unindexed publications is a residual scholarly risk.

## References

1. H. Abdollahzadeh Ahangar, M. P. Álvarez, M. Chellali, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, *Triple Roman domination in graphs*, Applied Mathematics and Computation 391 (2021), 125444, DOI `10.1016/j.amc.2020.125444`; openly available manuscript `arXiv:2402.07009v1` (2024-02-10), https://arxiv.org/html/2402.07009v1 .
2. J. C. Valenzuela-Tripodoro and coauthors, *Further Results on the \([k]\)-Roman Domination in Graphs* (2024), DOI `10.1007/s41980-024-00872-1`, https://link.springer.com/article/10.1007/s41980-024-00872-1 .
3. M. Hajjari and coauthors, *New Bounds on the Triple Roman Domination Number of Graphs* (2022), DOI `10.1155/2022/9992618`, https://onlinelibrary.wiley.com/doi/10.1155/2022/9992618 .
4. N. Khalili, J. Amjadi, M. Chellali, S. M. Sheikholeslami, *On \([k]\)-Roman domination in graphs*, AKCE International Journal of Graphs and Combinatorics 20 (2023), 291–299, DOI `10.1080/09728600.2023.2241531`.
