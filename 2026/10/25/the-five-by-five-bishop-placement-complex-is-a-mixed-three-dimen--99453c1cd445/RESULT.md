# The five-by-five bishop-placement complex is a mixed three-dimension sphere wedge

## Finding

Let \(B_5\) consist of every subset of the \(5\times5\) board whose bishop pieces do not attack each other. Its integral homotopy type is

\[
 B_5\simeq \left(\bigvee^{2}S^{3}\right)\vee\left(\bigvee^{13}S^{4}\right)\vee\left(\bigvee^{15}S^{5}\right).
\]

In particular, \(\widetilde H_3(B_5;\mathbb Z)=\mathbb Z^2\), \(\widetilde H_4(B_5;\mathbb Z)=\mathbb Z^{13}\), and \(\widetilde H_5(B_5;\mathbb Z)=\mathbb Z^{15}\); all other reduced integral homology groups vanish. This is a homotopy classification, not only a field-homology calculation.

## Assumptions and scope

The board is ordinary, with no identified boundaries or wraparound. Number the squares \((r,c)\), where \(r,c\in\{0,1,2,3,4\}\), by \(5r+c\). Two distinct squares attack one another exactly when \(|r-r'|=|c-c'|\). A face is any set of squares with no attacking pair. The empty set is included; homotopy type refers to the geometric realization.

Color \((r,c)\) by the parity of \(r+c\). There are thirteen even squares and twelve odd squares. Let \(X_0\) and \(X_1\) denote the restrictions of \(B_5\) to these two color classes. Each bishop preserves square color, so there are no graph edges between classes and therefore \(B_5=X_0*X_1\), an ordinary simplicial join. Equivalently, on each class use two coordinates \((r+c,r-c)\): a placement is independent exactly when neither diagonal coordinate repeats. The corresponding diagonal-incidence Ferrers rook boards have sorted row lengths \((5,3,3,1,1)\) and \((4,4,2,2)\). Neither is a complete rectangular rook board.

## Proof

**First component.** Exhaustive face enumeration gives the face-count vector by cardinality \((1,13,46,46,8)\), from empty face through four-vertex faces. Every one of its eight tetrahedra admits a free triangular face. Remove the eight pairs in lexicographic tetrahedron order, each time choosing the lexicographically first triangle contained in only that remaining tetrahedron. This is a sequence of elementary simplicial collapses to a two-dimensional complex with thirteen vertices, forty-six edges, and thirty-eight triangles.

Choose the breadth-first spanning tree rooted at the least-numbered vertex, visiting neighbors in increasing order. Contract the tree. The result is a CW complex with one vertex, thirty-four oriented one-cell generators (non-tree edges oriented from the smaller to the larger square number), and thirty-eight triangular two-cell relators. The signed boundary word of a triangle \((a,b,c)\), with \(a<b<c\), follows edges \((a,b),(b,c),(c,a)\); tree edges contribute the empty word. Repeatedly choose the shortest remaining freely reduced relator with a generator occurring exactly once, then the lowest relator index and lowest generator ID to break ties. If the word is \(u z v\), solve \(z=u^{-1}v^{-1}\), or invert this substitution if the unique letter is \(z^{-1}\); substitute into every other relator and freely reduce. Each step is an elementary two-cell/one-cell CW cancellation, preserving homotopy type. Exactly thirty-three generators are eliminated. All five remaining relators are freely trivial, and precisely one one-cell generator survives. Hence

\[
X_0\simeq S^1\vee\bigvee^5S^2.
\]

**Second component.** The corresponding face vector is \((1,12,38,32,4)\). Four free triangle–tetrahedron collapses leave twelve vertices, thirty-eight edges, and twenty-eight triangles. Tree contraction produces twenty-seven generators. The same deterministic exact-word procedure eliminates twenty-five generators, leaving two generators and three trivial attaching words. Thus

\[
X_1\simeq\bigvee^2S^1\vee\bigvee^3S^2.
\]

**Join.** For based connected CW complexes, the join satisfies \(X*Y\simeq\Sigma(X\wedge Y)\). Distributing smash products over these finite sphere wedges yields two copies of \(S^3\) from \(1\cdot2\) circle–circle pairs, thirteen copies of \(S^4\) from \(1\cdot3+5\cdot2\) circle–two-sphere pairs, and fifteen copies of \(S^5\) from \(5\cdot3\) two-sphere pairs. There are no other summands. This proves the stated integral homotopy type.

## Verification

The supplied standalone `verify_bishops5.py` constructs every face directly from bishop attacks rather than importing a precomputed face table. It checks both factors and the full complex. On the full board, the face-count vector by cardinality, including the empty face, is \((1,25,240,1124,2728,3368,1960,440,32)\). It checks every elementary free-face collapse, every tree and cellular relator, the exact generator substitutions, all remaining trivial words, and the final join arithmetic. It also independently constructs the signed simplicial boundary matrices and calculates their Smith forms over the integers. The nonzero Smith entries are all units; ranks for the even factor in degrees one through three are \((12,33,8)\), and for the odd factor \((11,25,4)\). This independent calculation corroborates the integral homology while the explicit CW cancellations establish the stronger homotopy claim. Run `python verify_bishops5.py` with Python 3 and `sympy==1.14.0`.

## Relationship to prior work

Ziegler's *Shellability of Chessboard Complexes* (1992 preprint) establishes sufficient diamond-configuration criteria for vertex decomposability of rook-board complexes or their skeleta; it does not furnish the two particular mixed-dimensional homotopy decompositions computed here. Shareshian–Wachs (arXiv:math/0409054, first public version 2004-09-03) concern torsion and connectivity of complete matching/chessboard complexes. Clark–Zeckner (arXiv:1008.4525, first public version 2010-08-26) analyze triangular Ferrers boards having a positive number of rows of *every* permitted length. Neither of the two diagonal-incidence boards has that pattern, and the inspected theorems do not supply these exact CW-equivalence classes. Harris–Perkins–Roach–Jones (2013) determine bishop independence numbers on several board topologies, not the homotopy type of all nonattacking placements. The present statement concerns a specific finite board and makes no claim of a general bishop-board classification.

## Limitations

The explicit reduction proves only the ordinary \(5\times5\) board, not an entire family of board sizes or other boundary identifications. The computational certificates are exhaustive because they enumerate *every* face in the fixed finite complexes, and every homotopy cancellation is justified by a free face or by a generator occurring once in an attaching word. Smith forms alone would not prove a homotopy wedge; the word-level cancellations supply the needed information. An equivalent result in unindexed literature cannot be excluded solely by unsuccessful searches. No independent review has been performed.

## References

1. G. M. Ziegler, *Shellability of Chessboard Complexes* (preprint dated 22 September 1992), https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/033PREPRINT.pdf.
2. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054v1 (3 September 2004), https://arxiv.org/abs/math/0409054.
3. E. Clark and M. Zeckner, *Simplicial Complexes of Triangular Ferrers Boards*, arXiv:1008.4525v1 (26 August 2010), https://arxiv.org/abs/1008.4525.
4. L. H. Harris, S. Perkins, P. A. Roach and S.-K. Jones, *Bishop Independence*, Journal of Advances in Mathematics and Computer Science 3 (2013), 835–843, https://doi.org/10.9734/BJMCS/2013/5760.
