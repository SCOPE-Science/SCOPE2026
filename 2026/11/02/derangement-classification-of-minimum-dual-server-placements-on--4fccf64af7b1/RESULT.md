# Derangement classification of minimum dual-server placements on square rook graphs

## Finding
Let \(R_n=K_n\square K_n\), \(n\ge2\), have vertices identified with the cells \([n]\times[n]\), with adjacency in a common row or a common column. A *singleton two-rainbow dominating function*, equivalently a two-server placement, is a map \(f:[n]\times[n]\to\{0,1,2\}\) such that every zero-labelled cell has a red (label \(1\)) neighbor and a blue (label \(2\)) neighbor. Write \(w(f)=|f^{-1}(\{1,2\})|\). The known optimum is \(\min_f w(f)=2n-2\), and the finding here is a complete classification and enumeration of *every* function attaining it.

Let \(!u\) be the number of fixed-point-free permutations of \(u\) elements, with \(!0=1\), \(!1=0\). The number of minimum-weight functions on the labelled board, with labels \(1\) and \(2\) distinguished, is
\[
M_n=n^2\sum_{u=0}^{n-2}\left(2-\mathbf{1}_{\{u=n-2\}}\right)\binom{n-1}{u}^2u!\,!u.
\]
In particular \(M_2=4\), \(M_3=18\), \(M_4=320\), \(M_5=8450\), \(M_6=295272\). Every minimizer is formed by one of two complementary orientations of monochromatic rectangular bars and a pair of edge-disjoint perfect matchings on their common residual square. The two orientations coincide only in the singleton-bar boundary case.

## Assumptions and scope
The graph is the ordinary Cartesian product of two complete simple graphs, with \(n\ge2\), fixed row and column labels, open neighborhoods (a zero cell cannot serve itself), and exactly one of the states \(0,1,2\) per cell. Colours \(1\) and \(2\) are distinguished in the count. No multi-colour labels or weighted costs are allowed. Define the red-free rows \(A\), red-free columns \(B\), blue-free rows \(C\), and blue-free columns \(D\). Their cardinalities are \(a,b,c,d\), respectively.

## Proof
**1. Minimum-support boundary.** The upper bound \(2n-2\) is realized by placing red on all but one cell of a selected row and blue on all but one cell of a selected column, with their intersection unselected. Each remaining zero cell sees a red vertex in its column or row and a blue vertex in the other direction.

For the lower bound, first suppose red occurs in every row. If blue occurs in every row or in every column, total support is at least \(2n\). Otherwise write \(c\ge1\), \(d\ge1\) for the numbers of blue-free rows and columns. The entire \(c\times d\) intersection is forced red. Red already meets all \(n\) rows, so it has at least \(n+c(d-1)\) vertices. Blue meets the other \(n-c\) rows and the other \(n-d\) columns, so it has at least \(\max(n-c,n-d)\) vertices. If \(d=1\), the sum is at least \(2n-1\); if \(d\ge2\), it is at least \(2n+c(d-2)\). The same reasoning applies if either colour occurs in every row or every column. Thus any solution with weight at most \(2n-2\) has both colours absent from some row and some column; all four of \(A,B,C,D\) are nonempty.

At every cell of \(A\times B\), no red neighbor is possible, so feasibility forces blue there. Analogously all of \(C\times D\) is red. Thus \(A\cap C=B\cap D=\varnothing\). Let \(U\) be the other rows and \(V\) the other columns, with sizes \(u=n-a-c\), \(v=n-b-d\). Since the red set includes all \(cd\) cells of \(C\times D\), and must additionally meet each row of \(U\) and each column of \(V\), it has at least \(cd+\max(u,v)\) cells. Similarly the blue set has at least \(ab+\max(u,v)\) cells. Hence
\[
\begin{aligned}
w(f)&\ge ab+cd+2\max(u,v)\\
&\ge(a+b-1)+(c+d-1)+2\max(u,v)\\
&=2n-2+|u-v|\ge2n-2.
\end{aligned}
\]
This establishes the optimum without assuming any earlier numerical theorem.

**2. Rigidity at equality.** Suppose \(w(f)=2n-2\). Every inequality above is an equality. In particular \(u=v\), \((a-1)(b-1)=0\), \((c-1)(d-1)=0\), and the support is precisely the forced red block \(C\times D\), forced blue block \(A\times B\), plus exactly \(u\) red cells and \(u\) blue cells. Because each of the two colours must meet every row of \(U\) and every column of \(V\), its \(u\) additional cells are a perfect matching between \(U\) and \(V\). The two matchings are edge-disjoint because each cell has a single state. When \(u=1\), disjoint matchings are impossible.

Let \(s=n-u=a+c=b+d\ge2\). The equality conditions yield exactly the two orientations
\[
\begin{array}{c|cccc}
& a&b&c&d\\\hline
\mathrm{I}&1&s-1&s-1&1\\
\mathrm{II}&s-1&1&1&s-1.
\end{array}
\]
For \(s=2\), both orientations describe the same shape, because all four dimensions equal one. For \(s>2\), the orientation is uniquely determined. Conversely every such configuration is feasible: in a zero cell outside both forced bars and interior matchings, each needed colour occurs in its row or column, because a non-forced row or column intersects the corresponding matching or bar. A direct case check for the row groups \(A,C,U\) and column groups \(B,D,V\) verifies this; occupied cells impose no condition. Thus the description is necessary and sufficient.

**3. Enumeration.** Fix \(u\), so \(s=n-u\). In orientation I, choose the single row of \(A\), the remaining \(s-1\) rows of \(C\), the single column of \(D\), and the remaining \(s-1\) columns of \(B\). This gives
\[
\bigl[n\binom{n-1}{s-1}\bigr]^2=n^2\binom{n-1}{u}^2
\]
choices. Choose the red matching by a bijection \(U\to V\) in \(u!\) ways, then the blue matching by a bijection avoiding each red-matched edge, in \(!u\) ways. Orientation II has the same count, except that the two descriptions coincide when \(s=2\), equivalently \(u=n-2\). Summing these disjoint cases proves the stated formula and classification for every \(n\ge2\).

## Verification
The accompanying standalone `verify.cpp` reconstructs the adjacency by shared rows or columns, exhaustively enumerates every placement of weight \(2n-3\) and \(2n-2\) for \(n=2,3,4,5\), checks the feasibility condition directly, reconstructs the four missing-row/column sets of every minimum placement, verifies the two-bar/two-matching characterization, and compares counts by \(u\) with the formula. It reports exactly \(4,18,320,8450\) minima and `VERIFY_OK`. This finite computation checks the proof's smallest boundaries, not the unrestricted quantifier.

## Relationship to prior work
The scalar minimum \(2n-2\) for square rook graphs is part of previously recorded work on singleton two-rainbow domination of rectangular rook graphs. The papers by Rao, Udupa, and Prathviraj on dual-server domination of graph operations and by Lange on rainbow \(k\)-domination of regular graphs supply the motivating invariant and broader algorithms/bounds. The contribution here is specifically the complete structure of *all* minimum placements and their exact derangement enumerator, not the scalar optimum, the general rainbow domination formalism, or the elementary theory of derangements. The complete-multipartite two-rainbow enumerator in adjacent work concerns a different graph product and does not imply this square-rook census.

## Limitations
The result is for a square rook graph, singleton labels, and named colours. It does not determine weighted or multi-colour rainbow domination, does not classify nonminimum placements, and does not extend the count to unequal rectangular boards. Related unindexed or inaccessible publications may contain an equivalent enumeration; historical priority remains provisional. Independent mathematical review has not been performed.

## References
1. S. L. Rao, S. Udupa N. V., and Prathviraj N., *The Dual-Server Domination Number of Some Graph Operations*, arXiv:2608.14690 (first public 2026-08-07).
2. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow k-Domination in Regular Graphs*, arXiv:2610.06906 (first public 2026-10-01).
