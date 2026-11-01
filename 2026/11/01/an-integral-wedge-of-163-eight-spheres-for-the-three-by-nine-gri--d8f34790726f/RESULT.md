# An integral wedge of \(163\) eight-spheres for the three-by-nine grid matching complex

## Finding
Let \(G=P_3\square P_9\) be the nearest-neighbor rectangular grid graph on three rows and nine columns: its vertex set is \(\{(r,c):0\le r<3,\ 0\le c<9\}\), and two vertices are adjacent exactly when their Manhattan distance is one. The ordinary matching complex \(X=\mathcal M(G)\) has the graph edges as its vertices and the pairwise vertex-disjoint edge sets as its simplices. Then its **integral homotopy type** is
\[
\boxed{|X|\simeq\bigvee^{163}S^8.}
\]
In particular \(\widetilde H_8(X;\mathbb Z)\cong\mathbb Z^{163}\), all other reduced integral homology groups vanish, and \(X\) is \(7\)-connected. This statement is for this exact width; no all-width conclusion is claimed.

## Assumptions and scope
The grid is the Cartesian product of two path graphs (not their categorical product or the complete bipartite graph). There are \(27\) graph vertices and \(42\) graph edges. Number the graph edges by first taking each horizontal edge in row-major order (rows \(0,1,2\), then columns \(0\) through \(7\)), followed by each vertical edge in row-major order (rows \(0,1\), then columns \(0\) through \(8\)). A simplicial face is encoded by a \(42\)-bit integer, with bit \(i\) indicating that edge \(i\) is chosen. All computations use exact integers.

## Proof
**1. Exhaustive face definition.** Starting with the empty matching, for each of the \(42\) graph edges in the stated order, add that edge to every previously formed matching that avoids its two endpoints. This uniquely enumerates each matching. The resulting complex has \(7,594,361\) faces including the empty face, with the numbers of faces of dimensions \(0\) through \(12\) equal to
\[
(42,767,8022,53292,235800,708881,1450678,1993990,1786876,991849,313290,48319,2554).
\]

**2. Explicit acyclic Morse matching.** Keep the singleton face encoded by bit zero as a critical vertex; never match the empty face. On the remaining faces, process pivot bits in increasing order \(i=0,\ldots,41\). For each remaining face \(\sigma\) that does not contain bit \(i\), pair \(\sigma\) with \(\sigma\cup\{i\}\) if both are still unpaired, and remove both from further consideration. The standalone checker enumerates and verifies all \(3,797,088\) matched face pairs, whose members differ by precisely one edge. The \(184\) unmatched nonempty faces comprise one vertex, \(173\) faces of dimension eight, and \(10\) faces of dimension nine.

For a complete acyclicity test, orient each cover relation of the nonempty face poset upward when matched and downward otherwise. The program constructs the indegrees from all \(61,837,314\) cover relations and performs a complete topological sort. Exactly all \(7,594,360\) nonempty faces are removed in this sort, hence there is no directed cycle. Forman's discrete Morse theorem therefore gives a CW model with the indicated critical cells.

**3. Integral attaching-degree computation.** Orient each face by its increasing edge indices. A codimension-one boundary incidence obtained by removing index \(j\) is \((-1)^{p}\), where \(p\) is the position of \(j\) in the sorted face. Let \(q(\sigma)\) be its projection onto the critical eight-cells along the acyclic gradient paths. A critical eight-cell projects to its basis vector, an eight-cell matched from below projects to zero, and an eight-cell \(\sigma\) matched upward to a nine-cell \(\tau\) satisfies
\[
q(\sigma)=-[\tau:\sigma]^{-1}\sum_{\substack{\sigma'\subset\tau\\\dim\sigma'=8,\ \sigma'\ne\sigma}}[\tau:\sigma']q(\sigma').
\]
The matching's acyclicity makes this recursion well-founded; every coefficient is computed over \(\mathbb Z\). Applying the signed boundary to each of the ten critical nine-cells gives a \(10\)-by-\(173\) integral matrix, rows indexed by the critical nine-cells and columns by the critical eight-cells, both ordered by increasing bit-mask integers.

Its columns numbered \(2,53,49,72,20,87,148,166,17,16\) (zero-based) form a \(10\)-by-\(10\) submatrix equal to the identity except for entry \((7,7)=-1\) and entry \((8,7)=-1\), where all row/column indices are zero-based. Thus this minor has determinant \(-1\). Every other entry is constructed explicitly by the supplied program; the unimodular minor proves that the attaching-degree matrix is an integral split surjection of rank ten.

**4. Homotopy conclusion.** The eight-skeleton of the Morse CW model is a wedge of \(173\) eight-spheres, since the only lower-dimensional cell is its vertex. By the Hurewicz theorem, the homotopy classes of attaching maps from \(S^8\) to this eight-skeleton are completely determined by their integer degree vectors. Integral elementary changes of bases, realized by homotopy equivalences and cell slides, reduce the ten attaching maps to ten coordinate inclusions because the matrix contains an integral unit minor. Ten nine-cells cancel ten eight-cells up to homotopy. The remaining \(173-10=163\) eight-spheres give the stated integral wedge decomposition.

## Verification
Compile `verify.cpp` with `g++ -std=c++17 -O3 verify.cpp -o verify` and run `./verify`. No external packages, stored face tables, or unpublished data are needed. The program checks the exact face vector, counts and dimensions of all critical cells, exhaustively topologically sorts every reversed-Hasse incidence, constructs the signed gradient-path matrix by exact integer recursion, and checks the stated unit minor. The successful output ends with `UNIT_MINOR_OK`, `MATRIX_OK`, `EULER 164`, and `ALL_VERIFY_OK`. The independent Euler check uses the original face vector, not the Morse matrix. This is a finite, exhaustive proof for the specified graph, not an extrapolation to larger widths.

## Relationship to prior work
Chauhan, Sharma, and Shukla (arXiv:2609.27366, first public 2026-09-23) study homological vanishing and connectivity for exactly the three-row grid matching complexes. Their Conjecture 4.1, as quoted in a separately accessible published mathematical account, posits an all-width single-dimensional sphere wedge. Their numerical table includes widths through nine; the **novel assertion here is the integral homotopy equivalence with a complete discrete-Morse and unimodular attaching-map proof**, not the numerical Betti rank alone. The full recent manuscript could not be accessed during this review, so this comparison carries a documented residual literature risk.

Goyal, Shukla, and Singh (2021) asserted an all-width wedge theorem, but the journal marks that paper retracted. Its 2025 corrigendum explicitly identifies incorrect non-induced-subgraph inclusions and notes that the predicted nine-column higher homology disagrees with direct calculation. No retracted homotopy implication is used here. Matsushita (2019) treats two-row grids. Known symmetry Lefschetz formulas for three-row grids concern alternating rational traces, not an integral homotopy classification.

## Limitations
This result determines the ordinary integral homotopy type for \(P_3\square P_9\) only. It does not prove the all-width conjecture, classify integral symmetry representations, or resolve the homotopy types for larger grids. The recent manuscript's full text was inaccessible, and an equivalent specific-width proof elsewhere remains possible. There has been no independent mathematical audit.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366, first posted 2026-09-23, https://arxiv.org/abs/2609.27366.
2. S. Goyal, S. Shukla, A. Singh, *Matching Complexes of \(3\times n\) Grid Graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), DOI:10.37236/10496. Retracted; corrigendum submitted 2025-03-01.
3. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics 26(3), P3.1 (2019), DOI:10.37236/8480.
