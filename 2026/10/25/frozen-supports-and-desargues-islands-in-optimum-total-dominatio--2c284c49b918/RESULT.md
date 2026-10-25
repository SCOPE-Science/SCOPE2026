# Frozen supports and Desargues islands in optimum total-domination exchanges of rook graphs

## Finding

For integers \(n\ge m\ge3\), let \(R_{n,m}=K_n\square K_m\), with vertices the \(n\times m\) squares, adjacent exactly when they share a row or a column. A **total dominating set** meets the open neighborhood of every square. Let \(\mathcal X_{n,m}\) be the graph of minimum-cardinality total dominating sets, joining two sets exactly when one square is deleted and another square inserted.

Write \(F(x)=e^x-1-x\) and, for \(1\le r\le\lfloor m/2\rfloor\), define
\[
L_{m,r}=m!\,[x^m]F(x)^r,\qquad E_{m,r}=\binom r2\,mL_{m-1,r}.
\]
Here \(L_{k,r}=0\) if \(k<2r\). Define \(H_{m,r}\) on functions \(f:[m]\to[r]\) whose \(r\) fibers all have at least two elements, adjacent when exactly one function value changes. Then the complete, **componentwise** graph decomposition is
\[
\mathcal X_{n,m}\cong \begin{cases}
\displaystyle\bigsqcup_{r=1}^{\lfloor m/2\rfloor}\binom nr H_{m,r},& n>m,\\
\displaystyle 2\bigsqcup_{r=1}^{\lfloor m/2\rfloor}\binom nr H_{m,r},& n=m.
\end{cases}
\]
The outer integer coefficients indicate numbers of disjoint copies. Each \(H_{m,r}\) has \(L_{m,r}\) vertices, \(E_{m,r}\) edges and degree at \(f\)
\[
\deg(f)=(r-1)\sum_{i:\,|f^{-1}(i)|\ge3}|f^{-1}(i)|.
\]
It is connected exactly when \(r=1\) (a single vertex) or \(m\ge2r+1\). If \(m=2r\), it consists of \(m!/2^r\) isolated vertices. In particular, all optimum states are isolated when \(m\in\{3,4\}\); for \(m=5\), every nontrivial component is the twenty-vertex Desargues graph. On the five-by-five board,
\[
\mathcal X_{5,5}\cong 10K_1\sqcup20\operatorname{Des},
\]
where \(\operatorname{Des}\) is the Desargues graph (the bipartite inclusion graph of two- and three-subsets of a five-element set).

## Assumptions and scope

Squares are distinctly labeled by pairs \((i,j)\) with \(1\le i\le n\), \(1\le j\le m\). A move may replace a square by any other square, not necessarily an adjacent square of \(R_{n,m}\); the intermediate set must remain minimum total dominating. No quotient by board symmetries is taken. The assumption \(m\ge3\) avoids the special two-by-two boundary, where row- and column-oriented configurations can be joined. The known minimum cardinality is \(m\), proved again below to make the classification self-contained.

## Proof

**1. All optimum states.** For any chosen set \(S\) with fewer than \(m\) squares, some row and some column are unoccupied (as \(n\ge m\)). Their intersection has no chosen neighbor, so \(S\) cannot totally dominate. On the other hand, choosing all \(m\) squares of one row totally dominates, proving \(\gamma_t(R_{n,m})=m\).

For a total dominating set of size \(m\), there cannot simultaneously be an unoccupied row and unoccupied column. If \(n>m\), at least one row is empty, so every column contains exactly one chosen square. Let \(a_i\) be the number of chosen squares in row \(i\). Each selected square must have a selected neighbor, and it has none in its column, so every positive \(a_i\ge2\). Conversely, any assignment of the \(m\) columns to rows with every used row occurring at least twice totally dominates: every square lies in an occupied column and each selected square has another chosen square in its row. When \(n=m\), the same argument permits also the transposed orientation, with one selected square per row and each used column containing at least two selections. The two orientations cannot coincide: their intersection would be a permutation matrix, in which every selected square is isolated from the others, hence not totally dominated.

**2. The allowable moves.** In the column-oriented case, at least one row is empty and at most \(\lfloor m/2\rfloor\) rows are occupied. A single replacement cannot produce a configuration with all \(m\) rows occupied, since it changes the number of occupied rows by at most one and \(\lfloor m/2\rfloor+1<m\) for \(m\ge3\). Thus the column orientation is preserved, even on square boards. Furthermore, every column must remain occupied, so a replacement must stay within its original column. Moving its square from row \(i\) to row \(j\) is legal precisely when \(a_i\ge3\) and \(a_j\ge2\). In particular, no row can become empty or newly occupied under a legal move. Consequently the precise occupied-row support is an invariant, and within any fixed support of \(r\) rows the state graph is exactly \(H_{m,r}\). The transposed argument handles row-oriented states.

**3. Connectivity for a fixed support.** If \(r=1\), exactly one map exists. If \(m=2r\), each row occurs exactly twice, so no move exists. Suppose \(r\ge2\) and \(m\ge2r+1\). Choose a distinguished row \(b\) in the fixed support. Starting with any state, move chosen squares from every other row into \(b\) until all other rows contain exactly two; the resulting buffer row \(b\) contains at least three squares. All moves are legal.

Two reduced states (all nonbuffer rows of size two) are related by a permutation of the \(m\) column labels. Any swap of column assignments between a nonbuffer row and \(b\) is possible in two legal moves: transfer a buffer column to the nonbuffer row, then transfer the other column back. Swapping assignments of two nonbuffer rows is possible in five legal moves with a temporary buffer column \(z\): transfer \(z\) from \(b\) to the first row, then the first row's chosen column to the second, then the second row's chosen column to \(b\), then that last column from \(b\) to the first, and finally \(z\) back to \(b\). Every nonbuffer row always retains at least two columns and the buffer has at least two. Thus all reduced states are connected by transpositions. Each original state can reach a reduced state, so \(H_{m,r}\) is connected.

**4. Exact enumeration.** For a chosen ordered list of \(r\) occupied rows, the \(m\) distinct columns form a surjection with all fiber sizes at least two. Exponential labeling gives \(L_{m,r}=m![x^m](e^x-1-x)^r\). Fix a column \(p\), its source row \(i\), and a distinct destination row \(j\). A legal directed move at \(p\) is equivalent to an assignment of the other \(m-1\) columns with all \(r\) row fibers of size at least two, of which there are \(L_{m-1,r}\). There are \(m r(r-1)L_{m-1,r}\) directed moves; dividing by two proves \(E_{m,r}=\binom r2 mL_{m-1,r}\). The degree formula counts the eligible chosen columns in rows containing at least three, times the \(r-1\) possible target rows.

**5. The five-column transition.** For \(m=5\), the only possible support sizes are \(r=1,2\). The first gives one isolated state per support. When \(r=2\), label the two occupied rows \(0,1\). A state is a binary word of length five with exactly two or three ones; moves change exactly one bit. Identify a weight-two word with its two-subset of \([5]\), and a weight-three word with its three-subset. A move is precisely subset inclusion. This is the bipartite double cover of the Petersen Kneser graph \(KG(5,2)\), hence the Desargues graph. There are \(\binom n2\) copies in each orientation and \(n\) isolated states, producing \(10K_1\sqcup20\operatorname{Des}\) when \(n=m=5\).

## Verification

Two independent finite checks accompany the proof. `check_direct.py` inspects every \(m\)-element selected set in the full board for six boards of dimensions \((3,3)\), \((4,3)\), \((4,4)\), \((5,4)\), \((5,5)\), and \((6,5)\), and constructs legal replacement edges from total domination tests. `check_structure.py` independently enumerates the bounded-fiber functions \(H_{m,r}\) through \(m=8\), their edges and connected components, and confirms the degree and order/size formula. Both check that the five-column nontrivial component is the Desargues graph. Their exact outputs are included. The all-order statements are proved above; finite tests are not used as infinite proofs.

## Relationship to prior work

Choudhary, Margulies and Hicks (2013) develop general total-domination bounds for Cartesian products. Kazemi, Pahlavsay and Stones (first public arXiv version 2015) give total-domination bounds and matrix methods for rook graphs, including the \(k=1\) optimum cardinality. The later tabulation OEIS A384117 enumerates minimum total dominating sets and describes their row/column support rule. These results are not claimed as new here. The new result is the exact **single-square-exchange graph decomposition**, its connectivity threshold, component order and edge formulas, and its five-column Desargues components. A related earlier classification of all inclusion-minimal total dominating sets of rectangular rook graphs is broader as a classification of feasible sets, but it does not by itself state this exchange-graph decomposition. Studies of paired domination address a smaller feasible class with an additional induced-perfect-matching condition, and do not imply the present odd-fiber transitions. Mynhardt and Nasserasr (2020) survey total-domination reconfiguration under other move models; the inspected survey does not provide this rook-graph classification.

## Limitations

The theorem is about **minimum total domination**, not arbitrary inclusion-minimal total domination, and about one unrestricted square replacement, not a token slide along a board graph edge or temporary extra squares. Its component structure uses labeled boards; symmetry quotients would differ. Its novelty is assessed against accessible literature and records, not certified against every unpublished or unindexed result. No external independent validation has been performed.

## References

1. K. Choudhary, S. Margulies, I. V. Hicks, *A Note on Total and Paired Domination of Cartesian Product Graphs*, Electron. J. Combin. 20(3) (2013), P25, doi:10.37236/2535 (first published 2013-08-23).
2. A. P. Kazemi, B. Pahlavsay, R. J. Stones, *Cartesian product graphs and \(k\)-tuple total domination*, arXiv:1509.08208 (first submission 2015-09-28), doi:10.2298/FIL1819713K.
3. C. M. Mynhardt, S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956 (2020).
4. OEIS A384117, *Number of minimum total dominating sets in rook graphs* (2025; existing counts only).
