# Integral homology of the first six king-configuration complexes

## Finding
Let \(G_n=P_n\boxtimes P_n\) be the king-attack graph of the ordinary, nonperiodic \(n\times n\) chessboard, and put \(K_n=\operatorname{Ind}(G_n)\). Its vertices are squares; a finite set of squares is a face exactly when no two are at Chebyshev distance one. For every integer \(1\leq n\leq 6\), all reduced integral homology groups of \(K_n\) are free abelian, and their nonzero ranks are exactly:

| Board | Nonzero reduced integral homology |
| --- | --- |
| \(n=1\) | None (contractible) |
| \(n=2\) | \(\widetilde H_0\cong\mathbb Z^3\) |
| \(n=3\) | \(\widetilde H_0\cong\mathbb Z\), \(\widetilde H_1\cong\mathbb Z^2\) |
| \(n=4\) | \(\widetilde H_3\cong\mathbb Z^2\) |
| \(n=5\) | \(\widetilde H_3\cong\mathbb Z^{45}\), \(\widetilde H_4\cong\mathbb Z^{32}\), \(\widetilde H_5\cong\mathbb Z^2\) |
| \(n=6\) | \(\widetilde H_3\cong\mathbb Z\), \(\widetilde H_4\cong\mathbb Z^{16}\), \(\widetilde H_5\cong\mathbb Z^{64}\), \(\widetilde H_6\cong\mathbb Z^{66}\), \(\widetilde H_7\cong\mathbb Z^2\) |

In particular, **five is the smallest square-board size with nonzero reduced integral homology in at least two strictly positive dimensions**. The six-by-six case has nonzero reduced integral homology in five consecutive positive dimensions. This is a statement about homology, not a claim that any of these complexes is a wedge of spheres.

## Assumptions and scope
The graph has vertex set \(\{(r,c):0\leq r,c<n\}\); distinct vertices are adjacent when \(\max(|r-r'|,|c-c'|)=1\). No periodic boundary identifications are made. Every nonattacking placement, including the empty placement, contributes a simplex of cardinality equal to the number of kings. Homology is reduced singular/simplicial homology with coefficients in \(\mathbb Z\); the dimension of a \(k\)-king face is \(k-1\). This theorem makes claims only for the six explicitly stated values of \(n\).

## Proof
**1. Exhaustive face sets.** Encode square \((r,c)\) by bit position \(nr+c\). For a square \(v\), construct its forbidden-neighbor bit mask using the displayed Chebyshev condition. Starting from the empty face, choose the smallest available square, record the enlarged face, and recurse on later available nonneighbors. This visits each independent set once. A separate row-transfer computation uses row masks with no adjacent bits and forbids vertical and diagonal attacks against the previous row; the two methods produce identical complete cardinality vectors, including the empty face:

| \(n\) | Numbers of faces of cardinality \(0,1,2,\ldots\) |
| --- | --- |
| \(1\) | \((1,1)\) |
| \(2\) | \((1,4)\) |
| \(3\) | \((1,9,16,8,1)\) |
| \(4\) | \((1,16,78,140,79)\) |
| \(5\) | \((1,25,228,964,1987,1974,978,242,27,1)\) |
| \(6\) | \((1,36,520,3920,16834,42368,62266,51504,21792,3600)\) |

**2. An explicit integral Morse reduction.** Order the squares by increasing Chebyshev distance from the geometric board center, then by increasing Manhattan distance from that center, then by row-major label. At each square \(v\), match every still-unmatched face \(F\) not containing \(v\) to \(F\cup\{v\}\) whenever both are still unmatched. These are disjoint pairs. Give each face incidence \(U\supset U\setminus\{v\}\) its downward orientation, reversing precisely those incidences that belong to a pair. For each of the six boards, exhaustive Kahn elimination processes *every* vertex of this directed Hasse graph; thus the matching is acyclic, not merely locally consistent. The empty face participates in the augmented matching when appropriate.

The numbers of matched face pairs for \(n=1,\ldots,6\) are \(1,1,15,141,3170,101331\). Unmatched Morse-cell counts by dimension are respectively \(\varnothing\); \((0:3)\); \((0:1,1:3,2:1)\); \((1:4,2:15,3:13)\); \((2:1,3:49,4:35,5:2)\); and \((3:1,4:16,5:72,6:81,7:9)\). The notation \((d:q)\) means \(q\) critical cells of dimension \(d\).

**3. Signed boundary maps and exact integral invariant factors.** Orient each face by increasing row-major vertex order. Deleting the \(j\)-th vertex contributes \((-1)^{j-1}\) to its simplicial boundary. The Morse boundary is obtained by algebraically cancelling each matched incidence of coefficient \(\pm1\): for a matched lower face \(u\) and upper face \(v\), replace \(u\) in a boundary by \(-\langle\partial v,u\rangle^{-1}\sum_{w\ne u}\langle\partial v,w\rangle w\), recursively along the acyclic matching. Unmatched upper faces project to zero, while unmatched lower faces project to their critical basis elements. This signed gradient-path recurrence constructs the complete Morse differential with integer entries and is implemented in `verify.py`.

The nonzero unit-invariant ranks of the reduced boundary matrices are:

| \(n\) | Integral reduced-boundary ranks; all nonzero Smith factors equal \(1\) |
| --- | --- |
| \(1,2\) | No surviving boundary maps |
| \(3\) | \(\operatorname{rank}\partial_2=1\) |
| \(4\) | \(\operatorname{rank}\partial_2=4\), \(\operatorname{rank}\partial_3=11\) |
| \(5\) | \(\operatorname{rank}\partial_3=1\), \(\operatorname{rank}\partial_4=3\); \(\partial_5=0\) |
| \(6\) | \(\partial_4=\partial_5=0\), \(\operatorname{rank}\partial_6=8\), \(\operatorname{rank}\partial_7=7\) |

Exact row and column swaps and integer multiples of rows/columns reduce each of these matrices to a diagonal block of \(\pm1\) pivots with a zero residual matrix. Every operation has determinant \(\pm1\). Hence all nonzero Smith invariant factors are units, so no homology torsion occurs. Subtracting incoming and outgoing ranks from the critical-cell counts proves the displayed complete reduced integral homology groups. In particular, the three nonzero positive-degree groups at \(n=5\), compared with the complete lower-size list, prove the threshold.

## Verification
The standalone `verify.py` recomputes graph edges, all faces, independent row-transfer face counts, every Morse pair, the full directed Hasse-graph acyclicity test, the signed Morse matrices, all integral unit reductions, and the Morse chain identity \(\partial^2=0\). It additionally computes ranks of the **unreduced original simplicial boundary matrices over \(\mathbb F_2\)** independently for all boards up to size five and verifies the exact rank relation implied by the Morse cancellation. No sampling, convergence assumption, or unproved extrapolation is used. The `certificate.json` file stores counts and cryptographic digests of sorted pairs, critical faces, and complete Morse matrices; `verification_output.txt` records the reproduced run, ending in `VERIFY_OK`.

## Relationship to prior work
Bousquet-Mélou, Linusson and Nevo (first publicly posted January 30, 2007) developed acyclic matchings and homotopy classifications for selected **ordinary square-lattice** independence complexes. Those square grids have only horizontal/vertical edges and are not the king graphs here, which also have diagonal attack edges. Their general Morse methodology is antecedent, not a computation of the present groups.

Carnero Bravo (arXiv first posted May 9, 2025) directly identifies \(P_n\boxtimes P_m\) as the king graph and determines strong-product independence-complex homotopy behavior for widths at most four (Section 5, especially Corollary 27 and Theorem 29). That is close and important prior coverage. The present first five-by-five and six-by-six cases have **minimum width five and six**, respectively, so their exact integral Betti vectors are not supplied by the cited width-at-most-four results. The two small-board checks agree with applicable earlier cases. Searches of both graph aliases and complete homology vectors found no published statement covering these two calculations; absence of a retrieved match does not establish global novelty.

## Limitations
No general formula for arbitrary board size, no assertion concerning the homotopy type or attaching maps beyond what integral homology detects, and no full dihedral-representation classification is claimed. Computations are exhaustive **only for sizes one through six**. Novelty comparison includes the directly relevant 2025 strong-product paper and the 2007 square-grid paper but can miss unindexed equivalent computations, unpublished calculations, or additional consequences derived elsewhere. The scientific result has not undergone independent mathematical audit.

## References
1. M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first public version 2007-01-30. https://arxiv.org/abs/math/0701890 ; readable primary text https://arxiv.org/html/math/0701890v2 .
2. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457, first public version 2025-05-09, Section 5, Corollary 27 and Theorem 29. https://arxiv.org/abs/2505.06457 .
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, for discrete Morse reduction and homotopy equivalence. https://doi.org/10.1006/aima.1997.1650 .
