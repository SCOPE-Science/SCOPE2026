# The Morse complex of \(K_{3,4}\): a 432-sphere wedge and its full bipartition-symmetry character

## Finding

For the complete bipartite graph \(K_{3,4}\), the simplicial Morse complex of acyclic discrete vector fields has integral homotopy type
\[
\mathcal M(K_{3,4})\simeq\bigvee^{432} S^5.
\]
The natural action of \(S_3\times S_4\), permuting vertices within the two bipartition classes, on its unique nonzero reduced rational homology \(\widetilde H_5\) has the **complete character** in the following table. Rows are \(S_3\) conjugacy classes \((1,1,1),(2,1),(3)\), and columns are \(S_4\) classes \((1,1,1,1),(2,1,1),(2,2),(3,1),(4)\), in that order:

| Class of \(S_3\) | \((1,1,1,1)\) | \((2,1,1)\) | \((2,2)\) | \((3,1)\) | \((4)\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \((1,1,1)\) | 432 | -16 | 4 | 0 | -2 |
| \((2,1)\) | 0 | 0 | 4 | 0 | -2 |
| \((3)\) | -3 | -1 | 1 | -3 | 1 |

The complete decomposition into rational irreducible outer products \(\operatorname{Sp}^{\lambda}\boxtimes\operatorname{Sp}^{\mu}\) has multiplicity matrix, with rows indexed by \(\lambda=(3),(2,1),(1,1,1)\) and columns by \(\mu=(4),(3,1),(2,2),(2,1,1),(1,1,1,1)\):
\[
\begin{pmatrix}
2&8&7&9&4\\
5&17&12&19&8\\
2&8&6&10&3
\end{pmatrix}.
\]
These coefficients are nonnegative integers and their dimension-weighted sum is 432. The result is a statement about the representation on rational homology, **not** an equivariant wedge decomposition.

## Assumptions and scope

View \(K_{3,4}\) as a one-dimensional simplicial complex with labeled vertices \(A=\{0,1,2\}\), \(B=\{3,4,5,6\}\), and all 12 edges between the two classes. Its Morse complex \(\mathcal M(K_{3,4})\) has 24 vertices, one for each incidence \((u,\{u,v\})\), encoded as an oriented arc \(u\to v\). A face is a set of incidences with pairwise distinct source vertices and pairwise distinct underlying graph edges, containing **no directed cycle**. This is precisely the acyclic Forman-vector-field condition for a graph, with all quantifiers over the 24 finite oriented incidences. The empty face is included for enumeration, but not as a cell of the geometric realization.

The claim concerns the *ordinary Morse complex of discrete gradient vector fields*, not the generalized Morse complex, the graph's ordinary matching complex, its two-matching complex, or the algebraic Morse chain complex associated to one fixed vector field.

## Proof

**1. Exhaustive finite face enumeration with an independent count.** An oriented face determines a rooted directed forest: every graph vertex has at most one outgoing arc and a directed cycle is forbidden. The two standalone programs enumerate faces independently, one by iterating admissible subsets of the 24 incidences and the other by choosing one outgoing neighbor or none at every graph vertex and rejecting cycles. In both computations the numbers of faces of cardinality \(k=0,1,2,3,4,5,6\) are
\[
(1,24,234,1192,3357,4968,3024),
\]
for a total of 12,800 faces. As a separate enumerative certificate, the complete bipartite Laplacian has nonzero eigenvalues \(7,4,4,3,3,3\), and the matrix-forest identity gives
\[
\frac{\det(tI+L)}{t}=(t+7)(t+4)^2(t+3)^3
=t^6+24t^5+234t^4+1192t^3+3357t^2+4968t+3024.
\]
Here the coefficient of \(t^{7-k-1}\) counts rooted spanning forests with \(k\) arcs. Both algorithms agree with every coefficient, not merely the Euler characteristic.

**2. A complete acyclic simplicial matching.** Order the oriented incidences by first listing underlying edges \((i,j)\) lexicographically for \(i\in A,j\in B\), then the two orientations \((i,j),(j,i)\). Regard each face as a 24-bit mask. Start with all 12,799 nonempty faces unmatched. At stage \(k=0,1,\ldots,23\), scan faces in their recursively defined order and match each currently unmatched face \(F\) lacking incidence \(k\) with \(F\cup\{k\}\) whenever both are currently unmatched. This definition completely determines 6,181 disjoint pairs, with critical cells: one vertex, two four-simplices, 434 five-simplices. To verify acyclicity, orient each nonempty Hasse covering edge down except matched edges, which are oriented up. The exact topological-sort routine visits all 12,799 vertices of this directed Hasse graph and its 60,456 arrows; thus the matching is acyclic.

**3. Integral attaching maps.** The acyclic matching yields a Morse CW complex with exactly one zero-cell, two four-cells, and 434 five-cells. To compute its degree map from five-cells to the four-cell wedge, use simplicial incidence signs \(\langle\partial F,F\setminus\{k\}\rangle=(-1)^{\#\{i\in F:i<k\}}\), and recursively eliminate matched four-faces against their matched five-faces. This is the exact integral gradient-path boundary, implemented in `verify_morse.py`. The complete resulting integer \(2\times434\) matrix has entries only in \(\{-1,0,1\}\) and 22 nonzero entries. Its four-dimensional critical cells have masks 1198084 and 4331524; columns indexed by critical five-cells 1198240 and 4331680 are respectively \((-1,0)^T\) and \((0,1)^T\). This is a unit minor of determinant \(-1\); hence its Smith invariants are \(1,1\) and the map is a split surjection over the integers. Because \(\pi_4(S^4\vee S^4)\cong\mathbb Z^2\), the five-cell attaching maps are completely determined by those degree vectors. Integral changes of four- and five-cell bases cancel the two independent degree-one attachments, leaving 432 unattached five-cells, proving
\[
\mathcal M(K_{3,4})\simeq\bigvee^{432}S^5.
\]
There are no unaccounted cells in dimensions one, two, three, or above five. Independently, the mod-two top simplicial boundary has rank 2592 among 3024 top-dimensional faces, yielding a 432-dimensional kernel, consistent with the integral classification.

**4. Full rational automorphism character.** A permutation pair \((\sigma,\tau)\in S_3\times S_4\) acts by permuting the labels of the 24 incidences. On each simplex setwise fixed by it, the induced simplicial-chain trace is the parity of the permutation of that simplex's ordered vertices. Sum these signed fixed-face contributions with their alternating degree signs, including the empty-face reduced correction. The only nonzero reduced homology lies in odd degree five, so its trace is the negative of the reduced Lefschetz number. `verify_character.py` checks **all 144 group elements** using integer arithmetic and verifies conjugacy-class invariance, yielding the displayed \(3\times5\) matrix. Taking the standard weighted inner products with the irreducible characters of \(S_3\) and \(S_4\), with exact centralizer orders, yields the displayed multiplicity matrix. Thus all 15 class values and all 15 multiplicities are proved by a complete finite calculation.

## Verification

The self-contained Python 3 standard-library scripts `verify_morse.py` and `verify_character.py` are included alongside this file. From a directory containing both, run `python3 verify_morse.py` and `python3 verify_character.py`. Both assert all numerical claims and print `VERIFY_OK` on success. `verify_morse.py` independently constructs the face poset, checks the entire oriented Hasse graph for directed cycles, and computes the full integer Morse boundary; `verify_character.py` constructs faces by a different algorithm, checks the matrix-forest polynomial and top mod-two boundary rank, and exhaustively computes the character and Specht multiplicities. No external data, floating-point arithmetic, remote service, or unaudited saved cache is needed. These are exhaustive finite certificates for this single graph; they are not evidence for any unstated infinite graph family.

## Relationship to prior work

Scoville and Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481 (first public 22 April 2020), define exactly this Morse complex in their Section 1. Their Theorem 4.3 gives connectivity bounds and Example 4.6 explicitly discusses complete bipartite graphs while leaving their homotopy type open at that time. Donovan, Lin and Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions* (arXiv:1909.11440), examine other graph families and do not present this computation. Jojić, *Shellability of complexes of directed trees* (2013), studies related directed-forest complexes, but the inspected shellability criteria do not apply directly to the bidirected four-cycle-containing graph \(K_{3,4}\). Scoville's *The complex of discrete Morse matchings of the \(n\)-simplex* (arXiv:2604.18172) instead treats simplices and their boundaries.

Published computations of the Morse complexes of \(K_{3,3}\) and the family \(K_{2,n}\) do not logically determine that of \(K_{3,4}\). The reported two-matching complex of \(K_{3,4}\) is a different simplicial complex: it consists of sets of original graph edges subject to degree caps, whereas the present complex consists of compatible, acyclic **incidence pairs**. Neither equality of graph labels nor nearby parameter values gives an implication between these homotopy classifications.

## Limitations

This theorem is for the single, naturally motivated graph \(K_{3,4}\), and determines its ordinary homotopy type and rational \(S_3\times S_4\) homology character only. It does not claim a natural equivariant homotopy equivalence, integral representation-theoretic splitting, or a formula for arbitrary \(K_{p,q}\). No independent external audit has been carried out. There is residual bibliographic risk that an equivalent \(K_{3,4}\) result exists under an unindexed directed-forest formulation, despite the documented comparisons; a negative search alone cannot eliminate that risk.

## References

1. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, version 1 dated 2020-04-22, https://arxiv.org/abs/2004.10481 (particularly §1, Theorem 4.3 and Example 4.6).
2. A. Donovan, M. Lin and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440, https://arxiv.org/abs/1909.11440.
3. D. Jojić, *Shellability of complexes of directed trees*, 2013, https://arxiv.org/abs/1109.4475.
4. N. A. Scoville, *The complex of discrete Morse matchings of the \(n\)-simplex: homotopy types and structural results*, arXiv:2604.18172, https://arxiv.org/abs/2604.18172.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.

