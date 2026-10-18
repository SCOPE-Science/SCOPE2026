# Independent-coalition partitions of three-row rook graphs

## Finding

Let \(R_{3,n}=K_3\square K_n\) be the rook graph on the labeled array \(\{0,1,2\}\times\{0,\ldots,n-1\}\), adjacent when cells share a row or a column. An *independent-coalition partition* is a partition of the vertices into nonempty sets such that each set is either a singleton dominating set or has a distinct partner whose union with it is independent and dominating, while neither partner dominates individually. Write \(\operatorname{IC}(G)\) for the greatest number of blocks, and \(c_{\max}(G)\) for the number of unordered, labeled-vertex partitions attaining that number.

**Theorem.** For every integer \(n\ge3\),
\[
\operatorname{IC}(R_{3,n})=3n-3,
\qquad
c_{\max}(R_{3,n})=
\begin{cases}
54,&n=3,\\
n(n-1)^2,&n\ge4.
\end{cases}
\]

For \(n\ge4\), all maximizing partitions consist of three two-cell blocks and \(3n-6\) singleton blocks. With row labels \(0,1,2\), the three two-cell blocks are, up to the *displayed choices of column labels*, exactly one of the following two families:

* **Two-column family:** for distinct columns \(a,b\),
\[
\bigl\{\{(1,a),(2,b)\},\ \{(0,b),(2,a)\},\ \{(0,a),(1,b)\}\bigr\}.
\]
* **Three-column family:** for pairwise distinct columns \(a,b,d\),
\[
\bigl\{\{(1,a),(2,b)\},\ \{(0,a),(2,d)\},\ \{(0,b),(1,d)\}\bigr\}.
\]

Every other cell is a singleton block. There are respectively \(n(n-1)\) and \(n(n-1)(n-2)\) partitions of the two types, with no overlap. At \(n=3\), the 54 maximizers instead split into 12, 36 and 6 partitions according as the sorted numbers of two-cell blocks omitting each of the three rows are \((1,1,1)\), \((0,1,2)\), and \((0,0,3)\).

## Assumptions and scope

All graphs are finite, undirected and simple. A dominating set uses closed neighborhoods. All partitions have nonempty, *unlabeled* blocks, while the graph cells retain their displayed row and column labels; no quotient by graph automorphisms is taken in the count. The statements concern \(n\ge3\) and use the independent-coalition definition of Samadzadeh and Mojdeh [1]. In this range the graph has no universal vertex.

The graph is also the line graph \(L(K_{3,n})\). Its independent sets correspond to matchings in \(K_{3,n}\), and its independent dominating sets correspond to maximal matchings. Because \(n\ge3\), a matching in \(K_{3,n}\) is maximal exactly when it saturates all three vertices in the three-element part: a matching leaving an unmatched vertex there leaves an unmatched vertex on the other side and can be extended. Thus every independent dominating set of \(R_{3,n}\) contains precisely three cells, one in each row and in three distinct columns. In particular, no block of an independent-coalition partition may contain three or more cells.

## Proof

**1. Sharp upper bound.** In any independent-coalition partition, each block has one or two cells: three independent cells would already be independent dominating and would be forbidden as a nonsingleton block. Let \(t\) be the number of two-cell blocks. Since all remaining blocks are singletons, the number of blocks is \(3n-t\).

Suppose \(t\le2\). Every row contains a singleton, because at most two of its \(n\ge3\) cells can lie in two-cell blocks. A singleton in row \(r\) can acquire an independent dominating partner only from a two-cell block occupying both other rows. Consequently there must be a distinct two-cell block missing each of the three rows, contradicting \(t\le2\). Thus \(t\ge3\) and \(\operatorname{IC}(R_{3,n})\le3n-3\).

**2. Attainment.** For any distinct columns \(a,b\), take the three two-cell blocks of the two-column family above and leave all other cells singleton. Each two-cell block misses one row and two columns. Every singleton in that row lies outside these two columns (the two column positions are already used in other two-cell blocks). Adding that singleton gives three nonattacking rooks, hence an independent dominating set. Every two-cell block has a singleton partner because \(n\ge3\), and every singleton is partnered. Neither member alone dominates. This attains \(3n-3\).

**3. Classification when \(n\ge4\).** Any maximum partition has exactly three two-cell blocks. Each row contains at least \(n-3\ge1\) singleton cells, so the three two-cell blocks must miss the three distinct rows, one each. Denote them
\[
B_0=\{(1,a),(2,b)\},\quad B_1=\{(0,c),(2,d)\},\quad B_2=\{(0,e),(1,f)\}.
\]
Here \(a\ne b\), \(c\ne d\), \(e\ne f\), and cells in distinct blocks do not repeat. In row zero, the singleton columns are exactly the columns outside \(\{c,e\}\). They can have only \(B_0\) as a partner. Every such singleton must avoid the two columns of \(B_0\), giving \(\{a,b\}=\{c,e\}\). The analogous argument in rows one and two gives
\[
\{c,d\}=\{a,f\},\qquad\{e,f\}=\{b,d\}.
\]
These equalities also suffice: every singleton in row \(r\) avoids the two columns of the unique block missing row \(r\), and every block has at least \(n-2\) singleton partners.

There are only two solutions. If \(c=b,e=a\), the remaining two equalities force \(d=a,f=b\), giving the two-column family. If \(c=a,e=b\), they force \(d=f\), with \(d\notin\{a,b\}\), giving the three-column family. Since \(B_0\) uniquely identifies \((a,b)\), and \(B_1\) identifies \(d\) in the latter case, there is no overcount from the fact that blocks are unlabeled. Their counts are \(n(n-1)\) and \(n(n-1)(n-2)\), totaling \(n(n-1)^2\).

**4. The square boundary \(n=3\).** A maximum partition still has exactly three two-cell blocks. Let \(m_r\) be the number of these blocks missing row \(r\). Since \(\sum_r m_r=3\), and row \(r\) then contains exactly \(m_r\) singleton cells, the sorted profile is one of \((1,1,1)\), \((0,1,2)\), \((0,0,3)\).

The \((1,1,1)\) case obeys the column equalities in step 3 (each row has one singleton). The two-column and three-column families give \(3\cdot2+3\cdot2\cdot1=12\) configurations.

For profile \((0,0,3)\), choose which row contains all three singleton cells in three ways. The three pairs then give a column-deranged bijection between the other two rows. Exactly two derangements of three symbols exist, and each permits every singleton to acquire a partner, giving \(3\cdot2=6\).

For profile \((0,1,2)\), choose the assignment of the three distinct profile numbers to the rows in six ways. Rename the rows so that the numbers are \(0,1,2\). The sole block missing row one selects \((0,c)\) and \((2,d)\) with \(c\ne d\); there are six ordered choices \((c,d)\). Let \(z\) be the third column. The unique singleton in row one must be \((1,z)\). Its two paired cells have columns \(c,d\). The two remaining blocks, which miss row two, must pair \((0,d)\) with \((1,c)\), and \((0,z)\) with \((1,d)\), since sharing a column is prohibited. Both singleton cells in row two have partners: \((2,z)\) completes the first block and \((2,c)\) completes the second. There is therefore exactly one partition per ordered \((c,d)\), or \(6\cdot6=36\) configurations across row assignments. Summing gives \(12+6+36=54\). This completes the proof.

## Verification

The standalone file `verify.py` enumerates all 21,147 set partitions of the nine labeled cells for \(n=3\) and checks each partition against the graph-theoretic definitions; it finds exactly 54 valid partitions, all of size six. For \(4\le n\le8\), it exhaustively tests near-maximum partitions (zero, one, two, or three two-cell blocks) and independently checks the closed classification, finding 36, 80, 150, 252 and 392 maximizers respectively. Re-run with `python3 verify.py`; expected text is in `verification_output.txt`. These finite computations are consistency checks; the preceding proof establishes the result for all \(n\ge3\).

## Relationship to prior work

Samadzadeh and Mojdeh [1] introduced and studied independent-coalition partitions, including a general lower bound from idomatic partitions and exact values for complete multipartite graphs, paths and cycles. Alikhani, Bakhshesh, Golmohammadi and Klavžar [2] examined extremal independent-coalition numbers and associated coalition graphs, not this Cartesian-product family. Asadzadeh and Alikhani [3] enumerated optimal partitions for several basic graph classes and explicitly listed Cartesian products as a direction for further research. Their general bound \(\operatorname{IC}(G)\le |V(G)|-i(G)+2\) gives only \(3n-1\) here because \(i(R_{3,n})=3\); the general idomatic lower bound \(2\operatorname{id}(G)\) gives only \(2n\). Neither implies the exact value \(3n-3\) or the maximizing count. This work is a leading-coefficient classification for a natural Cartesian product, not a computation of the full independent-coalition polynomial.

## Limitations

The count distinguishes vertex-labeled configurations and does not classify them up to automorphisms. Nothing is asserted here about the full coalition-partition polynomial, general \(K_m\square K_n\) with \(m\ge4\), or a putative exact transfer law for all graph products. The literature comparison does not exclude equivalent results in unidentified or unindexed sources. Independent validation has not been performed.

## References

[1] M. R. Samadzadeh and D. A. Mojdeh, *Independent coalition in graphs: existence and characterization*, arXiv:2306.02079 (first public version 2023-06-03); Ars Mathematica Contemporanea 24 (2024), #P3.09. https://arxiv.org/abs/2306.02079

[2] S. Alikhani, D. Bakhshesh, H. Golmohammadi and S. Klavžar, *On independent coalition in graphs and independent coalition graphs*, Discussiones Mathematicae Graph Theory 45 (2025), 533–544, DOI:10.7151/dmgt.2543. https://users.fmf.uni-lj.si/klavzar/preprints/DMGT-2543.pdf

[3] P. Asadzadeh and S. Alikhani, *Counting the Number of Independent Coalition Partitions*, public preprint posted 2026-06-12. https://www.researchgate.net/publication/406982240_Counting_the_Number_of_Independent_Coalition_Partitions
