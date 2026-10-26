# The three-geodesic position number of every rectangular grid

## Finding
For every pair of integers \(m,n\ge2\), the general three-position number of the rectangular path grid is
\[
\operatorname{gp}_3(P_m\square P_n)=\left\lceil\frac{mn}{2}\right\rceil.
\]
In addition, when \(m=3\) and \(n\ge2\), the maximum sets are exactly the maximum-cardinality bipartition classes. With labeled grid vertices, their number is \(1\) when \(n\) is odd and \(2\) when \(n\) is even. The equalities for even-by-even grids were already implied by earlier bounds for general two-position sets; the new part of the numerical theorem includes the mixed- and odd-parity grids and the unified construction.

## Assumptions and scope
Here \(P_m\) is the path on \(m\) vertices, and \(P_m\square P_n\) is the grid on coordinates \((i,j)\) with \(1\le i\le m\), \(1\le j\le n\), edges joining pairs of Manhattan distance one. For a graph \(H\), the number \(\operatorname{gp}_3(H)\) is the maximum size of a subset \(S\subseteq V(H)\) such that every geodesic of length at most three meets \(S\) in at most two vertices. In this statement both side lengths are at least two. A rectangular subgrid is isometric in its ambient rectangular grid.

## Proof
**Local tile bounds.** A \(2\times2\) tile contains at most two vertices of any general three-position set: each of its four three-vertex subsets contains a length-two geodesic. A \(3\times2\) tile contains at most three selected vertices. Indeed, if four were chosen, each of its two \(2\times2\) subtile intersections would contain at most two; but, independently, any three vertices containing two in one three-vertex column and one in the other are forbidden except when the two occupy the top and bottom positions and the third occupies the middle. To establish this exhaustive assertion: three in one column are forbidden; two adjacent vertical vertices together with any vertex of the other column lie on a geodesic of length at most three; and top and bottom vertices in one column together with a top or bottom vertex in the other column lie on such a geodesic. Exactly two triples survive, represented as column masks \((101,010)\) and \((010,101)\). In particular any feasible set in a \(3\times2\) tile with three vertices is one of these two triples, and four vertices are impossible because all its three-subsets would have to be allowed. By symmetry the \(2\times3\) bound is also three.

In a \(3\times3\) tile, denote the numbers selected in its successive columns by \(a,b,c\). No whole three-vertex column is selected, hence \(a,b,c\le2\). The adjacent \(3\times2\) inequalities give \(a+b\le3\) and \(b+c\le3\). If \(b=0\), then \(a+b+c\le4\). Otherwise \(a+b+c\le6-b\le5\). Thus the four fundamental tile bounds, in the order \(2\times2\), \(2\times3\), \(3\times2\), \(3\times3\), are \(2,3,3,5\).

**Tiling argument.** Every integer \(m\ge2\) has a decomposition \(m=2a+3\varepsilon\), where \(a\ge0\), \(\varepsilon\in\{0,1\}\), and \(\varepsilon=1\) exactly when \(m\) is odd; similarly \(n=2b+3\delta\). Partition the rows into \(a\) adjacent two-row strips and, when \(\varepsilon=1\), one three-row strip; independently partition the columns into \(b\) two-column strips and, when \(\delta=1\), one three-column strip. The resulting disjoint isometric tiles and the four local bounds imply
\[
|S|\le 2ab+3a\delta+3b\varepsilon+5\varepsilon\delta
=\frac{mn+\varepsilon\delta}{2}
=\left\lceil\frac{mn}{2}\right\rceil.
\]
The two parts of the bipartition by coordinate-sum parity each meet every length-at-most-three path in at most two vertices (the path alternates parity). The larger part has exactly \(\lceil mn/2\rceil\) vertices, attaining the upper bound.

**Three-row rigidity.** For \(n=2k\), partition \(P_3\square P_n\) into \(k\) consecutive \(3\times2\) tiles. Equality in the upper bound forces each tile to use one of the two local triples \((101,010)\) or \((010,101)\). A change from the first to the second across consecutive tiles produces four consecutive column masks \((101,010,010,101)\), where the top vertex of the first column and the middle vertices of the next two columns lie on a length-three geodesic. A change in the opposite direction gives \((010,101,101,010)\), whose two middle columns contain four vertices in a \(3\times2\) tile. Therefore all tiles have the same phase, giving exactly two checkerboards. For \(n=2k+1\), equality forces the first \(k\) two-column tiles to attain three selected vertices each and the final column to contain two vertices. The last two columns must then have exactly the local pattern \((010,101)\); the phase-change obstruction propagates this pattern across every preceding tile. Thus exactly one checkerboard attains the optimum. Both are direct infinite classifications, not experimental extrapolations.

## Verification
The accompanying `verify.py` generates forbidden triples in two independent ways: by enumerating actual shortest paths of length at most three in the grid, and by testing Manhattan interval betweenness. It checks agreement of the two forbidden-triple families, exhaustive maxima for 17 small rectangles (429200 examined subsets), the four tile optima, and the exact maximizing-set counts for three-row strips through length six. Its recorded standard output is `verification_output.txt`, ending with `VERIFICATION_OK`. The all-order proof above is independent of these finite computations.

## Relationship to prior work
Klavžar, Rall, and Yero [1, §6.1] explicitly asked for general \(d\)-position numbers of rectangular grids for \(d\ge3\). They also showed that the general two-position number agrees with dissociation and recorded the even-by-even grid case where that number already equals half the grid order [1, §5]. Cody and Moore [2, §6, Open Problems 7.1] give formulas for two-row grids for general \(k,d\), and explicitly leave width greater than two open. This result gives the full two-dimensional rectangular-grid answer for the natural fixed pair \((k,d)=(3,3)\). Unlike the previously known general two-position bound, the present formula can be strictly smaller: on the \(3\times4\) grid, \(\operatorname{gp}_2=7\) but \(\operatorname{gp}_3=6\), as directly checked by the supplied verifier.

## Limitations
The theorem does not determine \(\operatorname{gp}_d\) for \(d\ge4\), the numbers for \(k\ne3\), or a full classification of equality sets when neither dimension is three. The enumeration of optimum sets is restricted to three-row grids. The bibliographic comparison includes the two directly relevant foundational primary papers and targeted searches; it cannot guarantee the nonexistence of an unindexed equivalent formulation. Independent validation has not been performed.

## References
[1] S. Klavžar, D. F. Rall, and I. G. Yero, *General d-position sets*, arXiv:2005.08095v1, publicly submitted 16 May 2020. https://arxiv.org/pdf/2005.08095

[2] B. Cody and G. Moore, *The k-general d-position problem for graphs*, arXiv:2409.05644v1, publicly submitted 9 September 2024. https://arxiv.org/pdf/2409.05644
