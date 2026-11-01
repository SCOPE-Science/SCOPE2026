# A mixed-dimensional homotopy transition in even-board bishop complexes

## Finding
For an ordinary, nonperiodic \(n\times n\) chessboard, let \(\mathcal B_n\) be the simplicial complex whose vertices are squares and whose faces are sets of pairwise nonattacking bishops. For the first three positive even board sizes, the integral homotopy types are
\[
\mathcal B_2\simeq S^1,\qquad
\mathcal B_4\simeq\bigvee^{9} S^3,\qquad
\mathcal B_6\simeq
\bigvee^{196} S^5\vee\bigvee^{84} S^6\vee\bigvee^{9} S^7.
\]
Consequently \(6\) is the first positive even square-board size for which the reduced integral homology of the nonattacking-bishop complex is nonzero in more than one dimension. In particular \(\widetilde H_5(\mathcal B_6;\mathbb Z)\cong\mathbb Z^{196}\), \(\widetilde H_6(\mathcal B_6;\mathbb Z)\cong\mathbb Z^{84}\), and \(\widetilde H_7(\mathcal B_6;\mathbb Z)\cong\mathbb Z^9\), with every other reduced integral homology group zero.

## Assumptions and scope
Squares have coordinates \((r,c)\), where \(0\le r,c<n\). Two different bishops attack precisely when their squares satisfy \(|r-r'|=|c-c'|\). Attacks are evaluated on an otherwise empty board; occupying another square does not shield a bishop. The simplicial complex includes the empty face. No claims are made about periodic or higher-dimensional chessboards or any even \(n>6\).

For each even \(n\), the two colors \((r+c)\bmod 2\) are preserved by bishop attacks. Write \(X_n\) for the complex on even-color squares. The map \((r,c)\mapsto(r,n-1-c)\) identifies the two color complexes, so \(\mathcal B_n\cong X_n*X_n\) as abstract simplicial complexes (with disjoint copies of \(X_n\)). The star denotes simplicial join.

For \(n=6\), one color corresponds to nonattacking rooks on the Ferrers bipartite graph with row lengths \((6,4,4,2,2)\). Indeed, its diagonal labels are \(r-c\in\{-4,-2,0,2,4\}\); the allowed antidiagonal labels are \(r+c\in\{0,2,4,6,8,10\}\). The resulting row neighborhoods have sizes \(2,4,6,4,2\) and are nested after sorting the antidiagonal labels in the order \((4,6,2,8,0,10)\).

## Proof
**Finite Morse certificates.** The accompanying `verify_bishops.py` constructs each \(X_n\) for \(n\in\{2,4,6\}\), enumerating every face twice by distinct exhaustive methods. Vertices are indexed by increasing lexicographic square coordinate, starting at zero. In order \(n=2,4,6\), the explicit pivot-index orders are

- \(n=2\): `(0,1)`;
- \(n=4\): `(0,1,2,3,4,5,6,7)`;
- \(n=6\): `(3,9,16,17,7,11,4,5,15,13,1,0,12,14,8,6,2,10)`.

For each pivot \(v\), traverse the currently unpaired faces by increasing vertex bitmask and pair every available face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), when both are present and still unpaired. This completely specifies a partial matching of the face poset, including the empty face. Orient matched covering relations from lower to upper face, and every other covering relation from upper to lower face. Exhaustive topological sorting of the oriented Hasse graph proves acyclicity.

The face counts by cardinality (starting with the empty face) are, respectively, \((1,2)\), \((1,8,14,4)\), and \((1,18,98,184,100,8)\). The respective directed Hasse graphs have \(2\), \(48\), and \(1206\) covering incidences. The matchings have \(1\), \(12\), and \(196\) pairs. Their complete reduced critical-cell multiplicities are one dimension-zero cell for \(n=2\), three dimension-one cells for \(n=4\), and fourteen dimension-two plus three dimension-three cells for \(n=6\); the empty face is paired in every case.

**Integral attaching maps.** For each enumerated face, the program forms the actual oriented augmented simplicial boundary over \(\mathbb Z\), ordered by increasing vertex index, and independently checks that its square is zero. It eliminates every matched lower/higher pair by an exact unit-pivot chain contraction: if the coefficient of a lower cell \(a\) in the boundary of its matched higher cell \(b\) is \(u\in\{\pm1\}\), each other same-dimensional column \(x\) is replaced by \(\partial x-(\partial x)_a u^{-1}\partial b\) before deleting \(a\) and \(b\). Every required pivot is checked to be a unit. No critical-to-critical boundary survives in any of the three resulting integer Morse chain complexes.

Reduced discrete Morse theory supplies a CW model with an additional basepoint and exactly the indicated critical cells. Hence \(X_2\simeq S^0\) and \(X_4\simeq\bigvee^3 S^1\). For \(X_6\), its Morse CW model has one vertex, no one-cells, fourteen two-cells, and three three-cells. Its two-skeleton is \(\bigvee^{14}S^2\). By the Hurewicz isomorphism for this simply connected two-skeleton, each three-cell attaching map is determined by its integral cellular boundary coordinates. All such coordinates vanish in the exact Morse differential, so each attaching map is nullhomotopic. Thus
\[
X_6\simeq\bigvee^{14}S^2\vee\bigvee^3 S^3.
\]

**Join calculation.** For the above based CW homotopy types, \(X_n*X_n\simeq\Sigma(X_n\wedge X_n)\). The smash product distributes over finite wedges. Therefore \(X_2*X_2\simeq S^1\), \(X_4*X_4\simeq\bigvee^{3\cdot3} S^3\), and \(X_6*X_6\) has \(14^2=196\) summands in dimension \(5\), \(2\cdot14\cdot3=84\) in dimension \(6\), and \(3^2=9\) in dimension \(7\), exactly as claimed.

## Verification
Run `python3 verify_bishops.py` with a standard Python 3 interpreter. No nonstandard packages, external files, downloads, or randomness are required. The script checks two independent full-face enumerations, the complete partial-matching definition, every directed face incidence, acyclicity, the original oriented boundary-square identities, every exact unit pivot, all resulting critical-cell counts, and the zero integer Morse boundary. The accompanying `verification_output.txt` is a captured complete run and ends with `VERIFY_OK`.

## Relationship to prior work
Clark and Zeckner, *Simplicial Complexes of Triangular Ferrers Boards* (arXiv:1008.4525, first posted 2010-08-26), study matching complexes for a different subfamily of Ferrers shapes, particularly sufficiently wide triangular Ferrers boards and the Stirling complex. Their triangular family requires rows of every length up to the maximum. The bishop-color Ferrers partition \((6,4,4,2,2)\) lacks rows of lengths \(1,3,5\); their vertex-decomposability criterion and Stirling-complex statements do not imply the present mixed-dimensional homotopy type.

Harris, Perkins, Roach, and Jones, *Bishop Independence* (2013), address maximum cardinalities of bishop placements on several board topologies, not the homotopy type of the full simplicial complex of configurations. Exact face counts or independence numbers alone do not imply attaching maps or the stated wedge decomposition. Discrete Morse theory itself is standard (Forman, 1998); the finite matching certificate and the resulting particular classification are the mathematical contribution here.

## Limitations
This is an exact finite-board computation supported by an explicit, reproducible topological certificate, not an infinite-board classification or a homotopy statement for \(n\ge8\). The smaller sizes establish the **first even** mixed-dimensional occurrence; odd sizes are not covered by that threshold. Independent mathematical audit has not been performed. While the closest inspected Ferrers and bishop literature does not cover the statement, an equivalent calculation in unindexed literature remains possible. A related source PDF concerning bishop independence could not be retrieved in full; its public abstract and metadata were compared, but no inference about its uninspected pages is made.

## References
1. E. Clark and M. Zeckner, *Simplicial Complexes of Triangular Ferrers Boards*, arXiv:1008.4525 (first public version 2010-08-26), https://arxiv.org/abs/1008.4525.
2. L. Harris, S. Perkins, P. Roach and S.-K. Jones, *Bishop Independence*, British Journal of Mathematics and Computer Science 3(4) (2013), 835–843, https://doi.org/10.9734/BJMCS/2013/5760.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
4. D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008, for reduced discrete Morse methods and elementary CW arguments.
