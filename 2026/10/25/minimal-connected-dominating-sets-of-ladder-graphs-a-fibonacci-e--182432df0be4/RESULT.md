# Minimal connected dominating sets of ladder graphs: a Fibonacci enumeration and full size profile

## Finding

Let \(L_n=P_n\square K_2\) be the two-row ladder on \(n\ge2\) columns, with both row vertices in each column distinguished. A connected dominating set is **inclusion-minimal** if no proper subset is a connected dominating set. Let \(q_{n,k}\) be the number of inclusion-minimal connected dominating sets having \(k\) vertices, and put \(a_n=\sum_k q_{n,k}\).

All such sets have the exact column-word characterization described below. Their full bivariate enumerator is rational. Write
\[
 U=\frac{xy}{1-xy},\qquad V=\frac{x^2y^2}{1-xy},\qquad B=xy^2.
\]
Then
\[
\boxed{\sum_{n\ge2}\sum_k q_{n,k}x^ny^k
 =2V+\frac{2BV^2+4xBV+2x^2B^2U}{1-BU}
   +x^2B+x^2B^2+2x^2y^2.}
\]
In particular, with \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\),
\[
\boxed{a_2=4,\quad a_3=3,\quad a_4=7,\quad a_n=2F_n\ (n\ge5).}
\]
Equivalently,
\[
\boxed{\sum_{n\ge2}a_nx^n=\frac{4x^2-x^3-x^6}{1-x-x^2}.}
\]

## Assumptions and scope

All graphs are finite, simple, undirected. Label the vertices of \(L_n\) by \((i,r)\) with \(1\le i\le n\) and \(r\in\{0,1\}\). Vertices are adjacent if they are in the same column but different rows, or in consecutive columns and the same row. The closed neighborhood of a set contains its vertices and their neighbors. A set \(S\) is connected dominating if its closed neighborhood is all of \(V(L_n)\) and the induced subgraph \(L_n[S]\) is connected.

Encode \(S\) as a word \(w_1\cdots w_n\) over the alphabet `.` (no vertex), `T` (row zero only), `D` (row one only), and `B` (both rows). For \(n\ge3\), the complete language of minimal connected dominating sets is given by these simultaneous rules:

1. The nonempty columns occupy one interval \([a,b]\), with \(a\in\{1,2\}\) and \(b\in\{n-1,n\}\), with no internal `.` columns.
2. If \(a=1\), the word begins `TT` or `DD`; if \(a=2\), the word begins `.B`. If \(b=n\), it ends `TT` or `DD`; if \(b=n-1\), it ends `B.`.
3. Each `B` strictly between the first and last occupied columns occurs in a block `TBD` or `DBT`. Consecutive non-`B` occupied letters belong to the same row. Thus every nonempty monochromatic run has constant row, and rows alternate when separated by internal `B` letters.

For the short case \(n=3\), the word `.B.` satisfies these rules; for \(n=4\), `.BB.` satisfies them. At \(n=2\), the exact four words are `TT`, `DD`, `B.`, and `.B`.

## Proof

**Occupied interval and boundary.** The selected columns of any connected vertex set must be consecutive, since edges cannot jump a column. If its first occupied column were at least the third, no selected vertex could dominate a vertex of the first column, and similarly at the right. This forces \(a\le2\) and \(b\ge n-1\). A missing boundary column is dominated only when the adjacent selected column is `B`. When the first selected column is at the first end, its letter cannot be `B`: at least one of the two vertices in that `B` can be deleted while retaining the rung partner, connectedness and domination, since the endpoint has no earlier selected neighbor. Its letter must be a singleton `T` or `D`. To be connected to the next occupied column, the next must meet the same row. If the next were `B`, the first singleton could be deleted: `B` dominates both end vertices and connects to the remaining selected set. Hence the next letter equals the first singleton. The right-hand argument is symmetric. These facts prove rules 1 and 2. The one-column and two-column exceptional cases are checked directly under the same boundary argument.

**Internal letters.** For consecutive occupied columns, connectedness requires a common selected row, since the only edges crossing their cut are same-row horizontal edges. Thus adjacent singleton letters cannot be in different rows. Every internal singleton vertex is indispensable: deleting it creates a completely empty interior column, leaving selected vertices in nonempty columns to its left and right and disconnecting the induced subgraph. If an interior column is `B`, each of its vertices could be deleted without compromising domination because the other selected vertex of that column dominates its rung partner. Such a deletion also preserves connectedness unless the singleton row used by the preceding column and the singleton row used by the next column are opposite. Accordingly, minimality forces the neighbors of any interior `B` to be opposite-row singletons; equivalently, it is part of `TBD` or `DBT`. This proves the necessity of rule 3.

**Sufficiency and minimality.** Each word satisfying the rules is connected: every occupied column is linked to the next in a common row, and both vertices in any `B` column are linked by the rung. Its occupied interval covers all columns except possibly one at either endpoint, where an adjacent `B` dominates the missing column. Every vertex is essential. An internal singleton separates the selected interval when removed. Both vertices in an interior `B` are individually essential for linking the rows on its two sides. An endpoint singleton is essential for dominating the vertex in the other row of the outermost column; the same argument applies to the last endpoint. In a `B` adjacent to an unoccupied outermost column, its two vertices are both essential for dominating the two vertices of that unoccupied column, except in the tiny exceptional configurations already listed, where direct removal also fails. The only other possible two-column words were explicitly checked. A connected dominating superset of a connected dominating set is again connected dominating: every added vertex has a neighbor in the dominating subset. Therefore, failure of every single-vertex deletion is equivalent to inclusion-minimality. The classification follows.

**Enumeration.** A maximal singleton-row run of length at least one contributes \(U=xy/(1-xy)\); one of length at least two contributes \(V=x^2y^2/(1-xy)\). Each `B` has weight \(B=xy^2\). Every internal `B` separates monochromatic runs of opposite rows, so the initial run has two row choices and all later rows are forced. If neither endpoint is omitted, either there is one run (weight \(2V\)) or there are two or more runs (weight \(2BV^2/(1-BU)\)). If exactly one endpoint is omitted, there are two choices of which endpoint, two choices of row, a `B` next to the omitted endpoint, and an outer run of length at least two; intermediate switching steps form a geometric series. This gives \(4xBV/(1-BU)\). If both endpoints are omitted but at least one singleton-row run occurs, the corresponding weight is \(2x^2B^2U/(1-BU)\). The remaining words with both endpoints omitted are `.B.` and `.BB.`, contributing \(x^2B+x^2B^2\). Finally the two words `B.` and `.B` when \(n=2\), not covered by the preceding families, contribute \(2x^2y^2\). These mutually disjoint families exhaust the classification and give the displayed bivariate generating function.

Setting \(y=1\) and reducing rational expressions gives \((4x^2-x^3-x^6)/(1-x-x^2)\). Comparing coefficients gives \(a_2=4\), \(a_3=3\), \(a_4=7\), \(a_5=10\), \(a_6=16\), and the Fibonacci recurrence \(a_n=a_{n-1}+a_{n-2}\) for \(n\ge7\), yielding \(a_n=2F_n\) for \(n\ge5\).

## Verification

The self-contained standard-library script `verify_ladder.py` enumerates **every nonempty vertex subset** of \(L_n\) for \(2\le n\le10\) from the original graph-adjacency definition. It tests domination, connectedness, and deletion minimality independently of the column-word rules, and checks equality of the resulting **sets**, not merely counts. It covers 1,398,087 nonempty vertex subsets. It also evaluates the univariate rational generating function recurrence against the Fibonacci formula through degree fifty. The exact output is `verification_output.txt`. The exhaustive tests corroborate the proof but do not replace its infinite quantifiers.

## Relationship to prior work

Abu-Khzam, Fernau, Gras, Liedloff and Mann, *Enumerating Minimal Connected Dominating Sets* (arXiv:2205.00086, 29 April 2022; ESA 2022), formulate the general enumeration problem and prove subexponential-over-\(2^n\) algorithms and exponential extremal lower bounds. Their inspected conference article develops general branching algorithms, bounds, and hardness, but contains no ladder-family enumerator. Golovach and collaborators' *Enumerating Minimal Connected Dominating Sets in Graphs of Bounded Chordality* (IPEC 2015) also concerns general enumeration algorithms. The inspected preprint of *Enumerating Minimal Vertex Covers and Dominating Sets with Capacity and/or Connectivity Constraints* (arXiv:2308.16426, 2023) studies algorithmic constraints, not this explicit ladder enumeration.

The OEIS entry A291706 counts **all** connected dominating sets of ladders; that is a different quantity from inclusion-minimal sets. Wolfram GraphData documents the `MinimalConnectedDominationPolynomial` invariant on particular finite graphs, but the documentation alone is not an infinite ladder classification or rational bivariate series. The present result isolates the full minimal-set antichain and its cardinality distribution. A newer journal edition or unindexed work might independently contain the same formula; see limitations.

## Limitations

The theorem is restricted to two-row ladders with \(n\ge2\). No analogous classification for wider rectangular grids is asserted. The proof is elementary and independent of finite computational confirmation. This report does not claim mathematical or bibliographic independent validation. Primary-literature inspection covered the accessible conference paper and preprints; the complete 2025 journal version of the same algorithmic study was not accessed, so priority risk remains. The published GraphData repository may contain finite examples that were not individually exhaustively compared.

## References

1. F. N. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff and K. Mann, *Enumerating Minimal Connected Dominating Sets*, arXiv:2205.00086 (first public 2022-04-29), and *ESA 2022*, LIPIcs 244, Article 1, DOI: 10.4230/LIPIcs.ESA.2022.1.
2. P. A. Golovach et al., *Enumerating Minimal Connected Dominating Sets in Graphs of Bounded Chordality*, *IPEC 2015*, DOI: 10.4230/LIPIcs.IPEC.2015.307.
3. *Enumerating Minimal Vertex Covers and Dominating Sets with Capacity and/or Connectivity Constraints*, arXiv:2308.16426 (2023).
4. OEIS A291706, *Number of connected dominating sets in the n-ladder graph*, https://oeis.org/A291706.
5. Wolfram Research, *GraphData* property list (including `MinimalConnectedDominationPolynomial`), https://reference.wolfram.com/language/ref/GraphData.html.
