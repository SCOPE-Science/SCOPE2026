# Sharp \(3,5\)-geodesic coloring threshold for two-row ladder graphs

## Finding
For a finite ladder \(L_n=P_n\square P_2\) with \(n\ge1\), define \(\chi^3_5\) as the smallest number of colors on vertices such that every shortest path with at most five edges meets each color in at most two vertices. Then
\[
\chi^3_5(L_n)=\begin{cases}
1,&n=1,\\
2,&n=2,3,\\
3,&n=4,\\
4,&n\ge5.
\end{cases}
\]
The same value four applies to the one-sided and two-sided infinite ladder. For all lengths at least five, an optimal coloring has the repeating four-column pattern \((0,1),(1,0),(2,3),(3,2)\), where entries are the top and bottom vertex colors in each column. The lower-bound obstruction is already present on five consecutive columns.

## Assumptions and scope
All graphs are simple and undirected. For finite \(n\ge1\), the ladder has vertices \((i,r)\), \(0\le i<n\), \(r\in\{0,1\}\), with horizontal edges between consecutive columns in the same row and vertical edges joining the two rows in one column. In infinite variants the column indices are nonnegative integers or all integers. A geodesic means a shortest path between its endpoints in the entire graph. A \((3,5)\)-proper coloring is any vertex coloring with no three vertices of the same color on any geodesic with at most five edges, as in Cody and Detore [1, Definition 1.1]. The color labels below are the integers \(0,1,2,3\).

## Proof
**Lower bound for at least five columns.** It is enough to rule out three colors on \(L_5\). Suppose the vertices in column \(j\) have top and bottom colors \(t_j\) and \(b_j\), for \(0\le j\le4\). There are five distinct top-to-bottom geodesics from \((0,0)\) to \((4,1)\), one for each column \(j\) at which the path changes rows. Each has five edges and six vertices. With only three colors, the path condition forces exactly two occurrences of every color on every such geodesic.

Changing the vertical step from column \(j\) to column \(j+1\) removes precisely \((j,1)\) and inserts precisely \((j+1,0)\). Equality of the three color-multiplicity vectors yields \(t_{j+1}=b_j\) for \(j=0,1,2,3\). Similarly, using the five bottom-to-top geodesics from \((0,1)\) to \((4,0)\) gives \(b_{j+1}=t_j\) for the same indices. Hence \(t_{j+2}=t_j\) for \(j=0,1,2\), in particular \(t_0=t_2=t_4\). These three equal-colored vertices belong to the five-vertex geodesic along the top row from column zero to four (four edges), a contradiction. Every finite ladder of at least five columns, and either infinite ladder, contains an isometric five-column subladder. Thus all these graphs require at least four colors.

**Uniform four-color construction.** For every column \(i\), repeat the ordered top/bottom pairs
\[
(c(i,0),c(i,1))=(0,1),(1,0),(2,3),(3,2)
\]
with period four. Every row of this pattern has period four and uses four distinct colors in each consecutive block of four columns; the two vertices in the same column have distinct colors. Every geodesic in a ladder is either a horizontal segment in one row or consists of a horizontal segment, one vertical edge, and another horizontal segment, with horizontal motion in a single direction. A horizontal geodesic of at most five edges has at most six vertices, in which each of the four row colors appears at most twice.

For a geodesic with a vertical edge, write \(h\) for its number of horizontal edges. Because its total length is at most five, \(h\le4\). If \(h\le3\), both row portions have at most four vertices, so every color appears at most once in each portion and at most twice in total. If \(h=4\) and the vertical edge lies strictly inside the horizontal span, both row portions still have at most four vertices, giving the same bound. Finally, if the vertical edge is at one endpoint, one row portion has five consecutive vertices and may contain the same color twice, namely on its two endpoints; the other portion is a singleton in the same column as one of those endpoints and has a different color. No color occurs three times. Thus the pattern is valid for every finite or infinite ladder. Combined with the lower bound, it gives \(\chi^3_5=4\) whenever at least five columns are available.

**Short ladders.** For \(n=1\), the graph is an edge and one color suffices because no geodesic contains three vertices. For \(n=2,3\), a geodesic on three vertices forces at least two colors, while the usual two-coloring of the bipartite graph works: the graph has diameter at most three, and any shortest path has at most four vertices, alternating between its two colors. For \(n=4\), a length-four geodesic on five vertices rules out two colors by pigeonhole. Three suffice using the successive ordered top/bottom pairs \((0,0),(1,2),(2,1),(1,2)\). The latter can be checked directly over all geodesics, or by the complete three-vertex geodesic-hyperedge test in the standalone verifier. This closes every case.

## Verification
Run `python3 verify_ladder.py` using Python 3 standard libraries. The independent finite checker constructs every triple of vertices lying on a geodesic of length at most five by Manhattan-distance equality, backtracks over bounded color palettes on all ladders of one to five columns, and obtains minimum colors \((1,2,2,3,4)\). A separate explicit enumeration of shortest paths tests the three-color four-column witness and the repeating four-color construction on every ladder with one to 32 columns, checking the length/frequency condition directly. It also checks that the ten oriented opposite-corner geodesics used by the obstruction have six vertices each. Recorded output is in `verify_ladder_output.txt`. These finite tests are consistency checks; the preceding proof is the reason that the statement holds without a finite-size restriction.

## Relationship to prior work
Cody and Detore [1] define the two-parameter coloring invariant and explicitly ask for exact values on Cartesian products of paths, singling out the two-row ladder in Question 6.2. Their paper gives formulas for paths and cycles, not this ladder coloring. Cody and Moore [2, Theorem 6.4] determine the largest \((3,d)\)-independent subsets of thin grids; their extremal set-size formulas do not furnish a vertex partition into minimum-size color classes. Chandran S. V. and collaborators [3, Theorem 7.2] previously established the unrestricted general-position chromatic number of the two-row ladder, namely \(\chi_{\mathrm{gp}}(L_n)=2r\), \(2r+1\), \(2r+2\) as \(n=3r\), \(3r+1\), \(3r+2\). This prior theorem *already implies the short cases here where the diameter does not exceed five* (including \(n=3,4,5\)). It does not cover the new fixed-distance result for \(n\ge7\), where the unrestricted parameter grows with \(n\) while the \((3,5)\)-chromatic number remains exactly four. The first divergence occurs at \(n=7\), with five unrestricted colors but four at distance five.

## Limitations
This is an exact result for fixed \((k,d)=(3,5)\) and width two; it is not a formula for arbitrary \((k,d)\), taller rectangular grids, cylinders, or general position colorings with unrestricted geodesic lengths. The finite checks do not certify the infinite theorem independently of the analytic argument. Bibliographic searches cannot exclude unindexed equivalent results, and an independent mathematical audit has not been performed.

## References
[1] B. Cody and R. Detore, *Metric general position extensions of classical graph invariants and perfection*, arXiv:2601.04351 (first public version 7 January 2026), Definition 1.1 and Question 6.2, https://arxiv.org/abs/2601.04351.

[2] B. Cody and G. Moore, *The \(k\)-general \(d\)-position problem for graphs*, arXiv:2409.05644 (2024), Theorem 6.4, https://arxiv.org/abs/2409.05644.

[3] U. Chandran S. V., G. Di Stefano, H. S., and E. Thomas, *Colouring a graph with position sets*, arXiv:2408.13494 (2024), Theorem 7.2, https://arxiv.org/abs/2408.13494.
