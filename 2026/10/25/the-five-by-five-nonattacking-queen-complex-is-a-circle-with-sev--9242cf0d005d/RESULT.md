# The five-by-five nonattacking-queen complex is a circle with seventeen two-spheres

## Finding

Let \(Q_5\) be the graph whose \(25\) vertices are the squares of an ordinary \(5\times5\) chessboard, with two squares adjacent exactly when queens on those squares attack each other horizontally, vertically, or along a diagonal. Let \(K=\operatorname{Ind}(Q_5)\), the simplicial complex of all sets of mutually nonattacking queens. Then the **integral homotopy type**, not merely its Betti numbers, is

\[
K\simeq S^1\vee\bigvee^{17}S^2.
\]

In particular, \(\pi_1(K)\cong\mathbb Z\), \(H_1(K;\mathbb Z)\cong\mathbb Z\), \(H_2(K;\mathbb Z)\cong\mathbb Z^{17}\), and all other positive-degree integral homology groups vanish. The complex has an explicit perfect reduced discrete-Morse matching, with one critical \(1\)-simplex and seventeen critical \(2\)-simplices.

## Assumptions and scope

The board is ordinary, finite, and nonperiodic, with row and column indices \(r,c\in\{0,1,2,3,4\}\). A vertex has label \(5r+c\). A finite set of vertices is a simplex precisely if each pair of its squares lies in different rows, different columns, and different diagonals; diagonals mean equality of \(r-c\) or \(r+c\). No further restriction, such as requiring a maximal placement, is imposed. Homotopy refers to the geometric realization of this abstract simplicial complex. Empty faces are included in the reduced face poset.

## Proof

**Face enumeration.** Generate all partial placements row by row, giving the option of using no square in a row or one legal square in that row. The procedure enumerates every simplex exactly once. The counts, by number of vertices per simplex, are

\[
(1,25,140,204,82,10).
\]

Thus there are \(462\) faces including the empty one, and no simplex has more than five vertices. The resulting Euler characteristic is \(25-140+204-82+10=17\).

**A finite integral discrete-Morse reduction.** Start with every face unmatched. For pivot vertices \(v=0,1,\ldots,24\), in that order, visit the currently unmatched faces not containing \(v\), sorted first by cardinality and then lexicographically. Whenever both \(\sigma\) and \(\sigma\cup\{v\}\) are present and unmatched, match them and remove them from further consideration. This gives \(222\) matched pairs. There remain exactly \(18\) unmatched faces: one edge and seventeen triangles; the empty face is matched. This is a *reduced* matching, so its unreduced CW model includes a base vertex.

Reverse the orientation of each matched cover relation in the usual downward-oriented Hasse diagram. The resulting directed graph has all \(462\) faces and all \(1295\) codimension-one incidences. A complete topological sort visits every vertex, so there is no directed cycle. Consequently the matching is acyclic, and the discrete-Morse theorem gives a CW model with one zero-cell, one one-cell, and seventeen two-cells, and no higher cells.

**Integral attaching degrees.** For any ordered oriented face \(\tau\), the signed boundary is \(\partial\tau=\sum_j(-1)^j(\tau\setminus\{\tau_j\})\). Whenever an edge \(e\) is paired upward with a triangle \(t\), its coefficient in \(\partial t\) is \(\pm1\), allowing integral elimination of \(e\). Edges paired downward with vertices contribute zero after contraction. Recursively applying these eliminations along the acyclic matching gives the boundary coefficient of each of the seventeen critical triangles on the unique critical edge. The resulting signed integral row is

\[
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0).
\]

These are *integer* equalities, not finite-field computations. As an independent check, exact rational elimination on the original \(140\times204\) signed triangle-to-edge boundary matrix gives rank \(115\), while the vertex-to-edge incidence matrix has rank \(24\). Hence \(\dim_{\mathbb Q}H_1(K;\mathbb Q)=140-115-24=1\). Since the one-cell Morse complex has only one one-cell, this rational rank also forces its integral two-cell attaching-degree matrix to vanish.

The one-skeleton of the reduced CW model is a circle. Every attaching map from the boundary of a two-cell to that circle has degree zero and therefore is null-homotopic. Attaching the seventeen two-cells consequently yields precisely a circle wedged with seventeen two-spheres.

## Verification

The accompanying standard-library Python script `verify_queens5.py` exhaustively reconstructs all \(462\) simplices, all \(222\) matched pairs, the \(1295\) oriented Hasse incidences, and the exact signed integral Morse boundary. It also independently computes ranks \(24\) and \(115\) for the original simplicial boundary maps over \(\mathbb Q\). Run `python3 verify_queens5.py` from a directory containing the script. A successful run ends with `VERIFY_OK_QUEENS5_INTEGRAL_HOMOTOPY`. The output supplied in `verification_output.txt` is reproducible from the script.

## Relationship to prior work

Ehrenborg–Hetyei (2005/2006) study a general class of independence complexes and obtain homotopy classifications for forests and related special block systems. The queen's graph is not a forest, and their corresponding results do not give this complex's homotopy type. Chaiken–Hanusa–Zaslavsky (2013/2014), including their square-board treatment, derive counting and quasipolynomial formulas for nonattacking placements, not the topology of the complex whose faces are those placements. The present result supplies an additional homotopy-level invariant that cannot be inferred from the placement counts alone. Bell–Stevens survey the classical combinatorial problem, but their full text could not be independently inspected in this comparison.

## Limitations

This is a complete result only for the ordinary \(5\times5\) board. It does not establish a uniform formula as board size varies or an equivariant splitting under board symmetries. The topological calculation is finite, with exhaustive certificate rather than a short symbolic family proof. Bibliographic indexing may miss equivalent work; the cited comparison does not establish absolute uniqueness or historical priority.

## References

1. Richard Ehrenborg and Gábor Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, DOI:10.1016/j.ejc.2005.04.010. Author-hosted text: https://www.ms.uky.edu/~jrge/Papers/Independence.pdf (available online 2005-11-28).
2. Seth Chaiken, Christopher R. H. Hanusa and Thomas Zaslavsky, *A q-Queens Problem. I. General Theory*, Electronic Journal of Combinatorics 21 (2014), P3.33, DOI:10.37236/4093, arXiv:1303.1879 (first public version 2013-03-08).
3. Seth Chaiken, Christopher R. H. Hanusa and Thomas Zaslavsky, *A q-Queens Problem. II. The Square Board*, arXiv:1402.4880 (first public version 2014-02-20).
4. Jordan Bell and Brett Stevens, *A survey of known results and research areas for n-queens*, Discrete Mathematics 309 (2009), 1–31, DOI:10.1016/j.disc.2007.12.043.
