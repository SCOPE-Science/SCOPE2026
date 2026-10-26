# Complete minimum-fort classification for rectangular rook graphs

## Finding

For integers \(1\le p\le q\), write \(R_{p,q}=K_p\square K_q\). Its vertices are cells \((i,j)\), with distinct cells adjacent exactly when they share a row or column. A **fort** is a nonempty vertex set \(F\) such that every cell outside \(F\) has either zero or at least two neighbors in \(F\). Let \(\phi(p,q)\) be the minimum fort cardinality, and \(A(p,q)\) the number of minimum forts, with rows and columns distinguished.

**Theorem.** The complete parameter-dependent values are
\[
\phi(p,q)=\begin{cases}
1,&(p,q)=(1,1),\\
2,&p=1,\ q\ge2,\text{ or }(p,q)=(2,2),\\
3,&(p,q)\in\{(2,3),(3,3)\},\\
4,&\text{otherwise},
\end{cases}
\]
\[
A(p,q)=\begin{cases}
1,&(p,q)=(1,1),\\
\binom q2,&p=1,\ q\ge2,\\
2,&(p,q)=(2,2),\\
6,&(p,q)=(2,3)\text{ or }(3,3),\\
\binom q2^2+8\mathbf1_{q=4},&p=2,\ q\ge4,\\
\binom p2\binom q2+36\mathbf1_{(p,q)=(3,4)}+24\mathbf1_{(p,q)=(4,4)},&3\le p\le q,\ q\ge4.
\end{cases}
\]
Here \(\mathbf1\) is an indicator. The proof below classifies **every** minimum fort; the count is not an orbit count. In particular, for each fixed \(p\ge3\), \(A(p,q)\sim \binom p2 q^2/2\) as \(q\to\infty\), while \(A(2,q)\sim q^4/4\). The distinction is a sharp change in the degree of growth of the minimum-obstruction hypergraph under addition of a third row.

## Assumptions and scope

The graphs are finite, undirected, simple, and include the one-vertex case. Vertices (cells) are distinguished, and each minimum fort is counted once as a subset of those cells. The theorem concerns the **smallest fort size and every fort of that size**, not the total number of inclusion-minimal forts. In any graph a minimum-cardinality fort is inclusion-minimal, but inclusion-minimal forts can be larger.

## Proof

**Exact occupancy criterion.** For \(F\subseteq [p]\times[q]\), let \(r_i\) be its selected-cell count in row \(i\), and \(c_j\) its selected-cell count in column \(j\). An unselected cell \((i,j)\) has exactly \(r_i+c_j\) selected neighbors; there is no double counting because \((i,j)\notin F\). Hence \(F\ne\varnothing\) is a fort if and only if:

* if at least one column is empty, no row has selected degree exactly one;
* if at least one row is empty, no column has selected degree exactly one.

Indeed, \(r_i+c_j=1\) can occur only as \((r_i,c_j)=(1,0)\) or \((0,1)\), and in either case the cell is absent. This proves both necessity and sufficiency of the conditions.

**Lower bounds by support.** If all rows and columns are occupied, then \(|F|\ge\max\{p,q\}=q\). If all rows are occupied but some column is empty, the occupancy criterion forces at least two cells in each of the \(p\) rows, hence \(|F|\ge2p\). If all columns are occupied but some row is empty, similarly \(|F|\ge2q\). If some row and some column are both empty, all occupied rows and columns have at least two cells; this forces \(|F|\ge4\), and equality requires exactly two occupied rows and two occupied columns, with all four intersections selected. Such \(2\)-by-\(2\) rectangles are always forts when \(p,q\ge3\). When a dimension is two, the same four selected corners form the whole grid on their row or column supports and are forts by direct application of the criterion.

When \(p=1\), the graph is \(K_q\): a singleton is a fort only for \(q=1\), and all pairs are the minimum forts for \(q\ge2\). If \(2\le p\le q\le3\), the preceding bounds show that any fort of size \(q\) must use every row and column; thus it consists of exactly one selected cell in each column, using every row. This yields \(2\) permutation matrices on \(2\)-by-\(2\), \(6\) onto assignments of three columns to two rows on \(2\)-by-\(3\), and \(6\) permutation matrices on \(3\)-by-\(3\). No smaller fort is possible. For \(q\ge4\) and \(p\ge2\), every support pattern has at least four cells, and a \(2\)-by-\(2\) rectangle (or two occupied rows each carrying two cells when \(p=2\)) attains four. This establishes \(\phi\) throughout.

**Exhaustive equality classification for \(p=2,q\ge4\).** When any column is empty, both rows must have degree at least two; equality \(|F|=4\) forces each row to contain two cells. Choosing each row's two-column set independently gives \(\binom q2^2\) distinct forts, including the case in which all four columns are occupied. The only other equality case occurs when all columns are occupied; necessarily \(q=4\), with exactly one selected cell per column. Every assignment of the four columns to the two rows is a fort provided both rows are occupied. The assignments of row degrees \((2,2)\) are already included in the preceding \(\binom42^2\) term. The remaining possibilities \((1,3)\) and \((3,1)\) contribute \(2\binom41=8\) additional forts. These are all cases.

**Exhaustive equality classification for \(3\le p\le q,\ q\ge4\).** If an entire row and column are empty, every four-cell fort is exactly a full \(2\)-by-\(2\) rectangle. The same rectangles are forts when their two occupied rows or columns exhaust a dimension. They contribute \(\binom p2\binom q2\) distinct configurations. If all rows are occupied but a column is empty, equality would require at least \(2p\ge6\) cells. If all columns are occupied but a row is empty, it would require at least \(2q\ge8\). Thus any four-cell fort not already a rectangle must occupy every column, forcing \(q=4\) and exactly one selected cell per column. All rows must also be occupied, hence \(p\in\{3,4\}\). For \((p,q)=(3,4)\), there are \(3! S(4,3)=36\) surjections from the four columns onto three labeled rows. For \((p,q)=(4,4)\), there are \(4!=24\) permutations. These cannot be rectangles and are disjoint from the preceding class. All cases of the formula follow.

## Verification

The accompanying dependency-free \(\texttt{verify.py}\) checks the original neighbor-count definition independently of the support lemma; it exhaustively enumerates all candidate sets up to the proved minimum for \(1\le p\le4\), \(p\le q\le8\), and compares them with the constructive classification, covering 26 boards and 120168 tested subsets. It separately verifies equivalence of the support lemma and original definition on all subsets of each of the tested boards of area at most 12, covering 10190 subsets. These finite checks corroborate, but do not replace, the preceding unrestricted combinatorial proof. Output is provided as \(\texttt{verification_output.txt}\).

## Relationship to prior work

Forts are standard obstructions to graph zero forcing. Cameron, Hogben, Kenter, Mojallal and Schuerger investigate fort hypergraphs and Cartesian products of graphs (arXiv:2310.17904, initial public version 27 October 2023). Becker, Cameron, Hanely, Ong and Previte count inclusion-minimal forts for several graph families and give methods for graph products (arXiv:2404.05963, first posted 9 April 2024). Brimkov, Cameron and Grubbs classify minimum forts of hypercubes and develop Cartesian-product constructions (arXiv:2507.10826, posted 14 July 2025). The inspected source passages do not provide the all-parameter exact minimum-fort classification or multiplicity formula for \(K_p\square K_q\). In particular, formulas for the **base graph** \(K_{p,q}\) do not determine the fort hypergraph of its **line graph** \(L(K_{p,q})\cong K_p\square K_q\). A possible unindexed equivalent treatment remains a bibliographic uncertainty.

## Limitations

The count concerns minimum-size forts only. It does not count all forts or all inclusion-minimal forts, calculate the zero forcing number, or claim a new general Cartesian-product theorem. The finite verifier cannot establish an infinite classification without the proof above. Bibliographic priority and the proof have not been independently validated.

## References

1. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (initial public version 27 October 2023).
2. P. Becker, T. R. Cameron, D. Hanely, B. Ong and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (initial public version 9 April 2024).
3. B. Brimkov, T. R. Cameron and O. Grubbs, *On the forts and related parameters of the hypercube graph*, arXiv:2507.10826 (initial public version 14 July 2025).
