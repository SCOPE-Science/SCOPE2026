# Complete minimum total \(3\)-domination census for three-row rook graphs

## Finding

For every integer \(n\ge2\), let \(R_n=K_3\square K_n\). A total \(3\)-dominating set is a subset \(S\subseteq V(R_n)\) for which every vertex has at least three **distinct open neighbors** in \(S\). Write \(\gamma_{3t}(R_n)\) for its minimum size and \(M_n\) for the number of minimum sets, with rows and columns labeled. Then

\[
\gamma_{3t}(R_n)=\begin{cases}
6,&n=2,\\
8,&n=3,4,\\
9,&n\ge5,
\end{cases}
\qquad
M_n=\begin{cases}
1,&n=2,\\
9,&n=3,\\
18,&n=4,\\
160,&n=5,\\
\displaystyle\binom n3+n(n-1)(n-2)(n-3),&n\ge6.
\end{cases}
\]

Moreover, the following descriptions are **if and only if** classifications of the minimum sets (a *full column* has three selected cells, and a *double column* has two):

1. At \(n=2\), select every cell.
2. At \(n=3\), select two full columns and a double third column.
3. At \(n=4\), select two full columns and a single cell in each of the other two columns, both in the same row.
4. At every \(n\ge5\), two families occur: (A) select precisely three full columns, or (B) select precisely one full column and three double columns, with each row omitted once from those three double columns. All other columns are empty.
5. Only at \(n=5\), there is an additional family (C): select two full columns and one cell in each other column, all three singleton cells in the same row.

The numerical minimum for \(n\ge5\) follows from previously published general bounds; the all-minimum-set classification and the exact multiplicities are the enumerative claim here.

## Assumptions and scope

The graphs are finite, simple, undirected and are the usual **Cartesian**, not tensor, products. Vertex coordinates are \((i,j)\) for \(i\in\{1,2,3\}\) and \(j\in\{1,\ldots,n\}\); two distinct vertices are adjacent precisely when they share a row or a column. Different labeled subsets count separately, and the empty set is never valid. We use *total \(3\)-domination* in the set-valued (not weighted-function) sense: membership in \(S\) does not itself count toward a vertex's three neighbors.

## Proof

Set \(x_{ij}=1\) if \((i,j)\in S\) and \(0\) otherwise; write \(r_i=\sum_j x_{ij}\) and \(c_j=\sum_i x_{ij}\). The open neighbors of \((i,j)\) in \(S\) number exactly

\[
 r_i+c_j-2x_{ij}.
\]

Thus feasibility is **equivalent** to

\[
 r_i+c_j-2x_{ij}\ge3\qquad\text{for all }i,j.\tag{1}
\]

**Low-row rigidity.** Every row contains at least two selected cells. A row of size zero cannot supply three neighbors to any of its own cells (a column has at most two other-row cells); a row of size one fails (1) at its selected cell, which has at most two same-column neighbors. If a row has exactly two selected cells, (1) at either selected cell forces its column to be full: it has just one selected same-row neighbor and must have two more in its column. Hence any two-row forces two distinct full columns and six selected cells altogether. Furthermore, **every other column must be nonempty**: an empty column would give the two-row cells only two selected neighbors.

**The lower bounds.** At \(n=2\), every vertex has degree three; the only total \(3\)-dominating set is the entire graph, of size six. For \(n\ge3\), a set with at most seven cells must have a two-row (because all three row sums are at least two). Its two full columns already use six cells. If the seventh cell is absent, an empty third column violates (1); if a seventh cell is present in a singleton column, its row sum is three and its selected vertex has only two neighbors in \(S\). Thus \(|S|\ge8\). If \(|S|=8\), a two-row again forces two full columns and leaves at most two selected cells outside them. Because all other columns must be nonempty, this is impossible for \(n\ge5\). Therefore \(|S|\ge9\) for \(n\ge5\).

**Eight-cell equality.** For \(|S|=8\), the two remaining cells lie outside the two full columns. If they share a third column, they occupy different rows, making that column double; a fourth or subsequent column would be empty, so \(n=3\). Conversely every such three-column configuration satisfies (1). If the two remaining cells occupy two different singleton columns, each occupied row must have row sum at least four by (1) at that singleton; this forces the two singletons into the same row. All columns must be nonempty, so \(n=4\), and again (1) is satisfied. These give exactly \(3\binom32=9\) sets at \(n=3\) and \(3\binom42=18\) at \(n=4\). Both sizes are attained.

**Nine-cell equality.** Three full columns satisfy (1) for every \(n\ge3\), so nine cells suffice for \(n\ge5\). Let \(|S|=9\), \(n\ge5\). If a row has size two, two full columns use six cells, leaving three selected cells; since every other column must be nonempty, \(n\le5\). In the only relevant case \(n=5\), the three remaining columns are singleton. At a selected singleton cell, (1) forces its row sum to be at least four. With only three cells distributed between the other two rows, this is possible only when all three singleton cells are in one row. This is family (C), and it satisfies (1).

Otherwise all rows have size at least three, and their total is nine, so each row has size exactly three. At any selected cell (1) now requires \(c_j\ge2\); there can be no singleton column. Since the column sizes are zero, two, or three and sum to nine, the positive sizes are necessarily either \((3,3,3)\) or \((3,2,2,2)\). In the second case each row is present in the full column and exactly two double columns; hence each row is omitted from exactly one of the three double columns. Conversely every configuration of these forms satisfies (1): a selected vertex has \((3-1)+(c_j-1)\ge3\) neighbors, and an unselected vertex has \(3+c_j\ge3\). This proves the complete classification.

**Counting.** Family (A) has \(\binom n3\) members. For family (B), choose the full column in \(n\) ways, choose the three double columns in \(\binom{n-1}{3}\) ways, then biject the three omitted rows to those columns in \(3!\) ways. This is \(6n\binom{n-1}{3}=n(n-1)(n-2)(n-3)\). Family (C) exists only at \(n=5\), with \(3\binom52=30\) choices. Consequently the count is \(10+120+30=160\) at \(n=5\) and is the asserted polynomial for \(n\ge6\). Together with the eight-cell cases and \(n=2\), the theorem follows. \(\square\)

## Verification

The accompanying dependency-free `verify.py` builds the Cartesian rook graphs and tests their open neighborhoods directly for every subset of size at most the claimed minimum for \(2\le n\le7\). This is exhaustive over those bounded vertex sets; the observed pairs \((\gamma_{3t},M_n)\) are \((6,1),(8,9),(8,18),(9,160),(9,380),(9,875)\). A second algorithm enumerates unordered column-type multisets for \(8\le n\le12\), weighting each by the exact multinomial multiplicity; it independently reproduces the claimed minimum counts. The infinite claim follows from proof (1) and its case distinction, not from numerical testing.

Run using `python3 verify.py` with Python 3.9 or later. It prints `VERIFY_OK` when all checks pass.

## Relationship to prior work

Bermudo, Sánchez and Sigarreta (2017), Proposition 3.2, already imply \(\gamma_{3t}(K_3\square K_n)=9\) for \(n\ge5\) from their general exact-range theorem. Their Theorem 3.1 supplies the associated lower-bound mechanism, but neither statement classifies or counts optimal sets. Carballosa and Wisby (arXiv version first posted 2020-01-22), Section 4 and Proposition 4.1, investigate total \(3\)-domination of rook graphs and establish general lower bounds and selected square cases; they do not state the three-row minimum-set enumerator. Thus the numerical stabilization is **not** asserted to be new. The classification, two structural pattern families and exceptional \(n=5\) third family, and exact count are the claims evaluated here.

The graph \(K_3\square K_n\) is also the line graph of \(K_{3,n}\), so the result counts minimum collections of edges in that bipartite graph such that each edge is incident (at either endpoint) to at least three **other** selected edges. Exact multiplicities are also the leading coefficients of the total-three-domination reliability polynomial under rare independent vertex activation.

## Limitations

The theorem does not count nonminimum total \(3\)-dominating sets, classify optimums under unlabeled graph symmetries, or extend to clique widths other than three or to domination thresholds other than three. Originality is evaluated relative to the specifically inspected literature and database records; an unindexed equivalent earlier enumeration cannot be ruled out. No independent mathematical audit has occurred.

## References

1. S. Bermudo, J. L. Sánchez and J. M. Sigarreta, *Total k-domination in Cartesian product graphs*, Periodica Mathematica Hungarica **75** (2017), 255–267, DOI `10.1007/s10998-017-0191-2`. Public online date 2017-07-21. See Theorem 3.1, Proposition 3.2.
2. W. Carballosa and J. Wisby, *Total k-domination in Cartesian product of complete graphs*, `arXiv:2001.07850`, originally posted 2020-01-22, version 4 dated 2022-05-10. See the introduction and Section 4 (notably Proposition 4.1 and the stated odd-threshold open problem).
