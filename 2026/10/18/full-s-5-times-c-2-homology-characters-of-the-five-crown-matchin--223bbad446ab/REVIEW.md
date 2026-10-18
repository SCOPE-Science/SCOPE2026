# Review of the five-crown homology-character theorem

## Correctness — PASS

The graph and the 20 vertex labels of its matching complex are defined without ambiguity. Enumerating the legal partial matchings gives chain dimensions \((20,130,320,265,44)\). Exact elimination in prime characteristic supplies rational rank lower bounds \((19,111,208,44)\). The first two rational rank upper bounds follow from column-sum zero and boundary composition; the top one follows from its 44 columns. The explicit eight-triangle integer two-cycle and 120-entry integer two-cocycle pair to \(2\), yielding the last required upper bound on the third boundary rank. Thus the rational Betti numbers are proved independently of numerical extrapolation or the older homology table.

The signed fixed-simplex trace is checked for all 240 automorphisms and satisfies the class-function property. The reduced Lefschetz identity determines the virtual character. Since rational second homology is one-dimensional, checking its four possible group characters and decomposing the resulting degree-three characters against all 14 irreducibles singles out the unique nonnegative decomposition stated in the theorem. All finite claims are replayed from `verify.py` and `cocycle.json`.

## Originality — PASS, with uncertainty

The most relevant same-object source is Shareshian--Wachs, arXiv:math/0409054v1, Section 8. It gives the diagonal-deleted chessboard definition, sharp connectivity, and Table 8.1 with \(\widetilde H_2\cong\mathbb Z\) at board size five; the older non-equivariant calculation is expressly credited. Its representation discussion in Section 6, following Friedman--Hanlon, applies to **complete** rectangular chessboard complexes, which have different faces and larger symmetry. Neither provides the stated simultaneous-permutation plus transpose character on the diagonal-deleted board. The mathematical implication distinction is that homology ranks and the full-board character do not determine the action on homology of a strict subcomplex.

Searches under the aliases crown graph, derangement board, deleted diagonal, and diagonal-free rook complex, including semantic searches of published mathematical findings, did not identify a covering character formula. Their closest records concern full rook boards, other matching complexes or graph-cut/domination complexes. Björner--Welker's original same-object paper is known through its abstract and Shareshian--Wachs' explicit citation and was not inspected in full. Equivalent results under other terminology or in less-indexed literature remain possible. This qualified novelty judgment is not an absolute priority claim.

## Mathematical value — PASS

Deleting a diagonal is a classical, independently motivated deformation of the chessboard complex. At side length five, it has nontrivial rational homology in **two different dimensions**, making Betti-number knowledge insufficient to understand its natural symmetries. The full \(S_5\times C_2\) character distinguishes a degree-two class that is permutation-invariant but transpose-odd from a degree-three space with nine transpose-even and four transpose-odd dimensions. It also establishes that every positive-degree class loses invariance under the full graph automorphism group. This is structural equivariant information for the first small mixed-degree case, not an arbitrary selection of coefficients.

The result is limited to rational representations at board size five. It does not assert integral equivariant decomposition or a uniform theorem over all board sizes.

Self-review: passed. Independent audit: not yet performed.
