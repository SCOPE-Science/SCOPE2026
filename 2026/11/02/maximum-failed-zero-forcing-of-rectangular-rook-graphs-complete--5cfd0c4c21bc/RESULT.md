# Maximum failed zero forcing of rectangular rook graphs: complete extremizer classification and counts

## Finding

For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\), with cells \((i,j)\) adjacent when they share a row or a column. In standard zero forcing, a blue vertex with exactly one white neighbor forces that neighbor blue. A failed zero forcing set is an initial blue set from which not every vertex can be forced; a *maximum* failed set has largest possible cardinality among such sets. Write \(M_{m,n}\) for the number of labeled maximum failed sets and \(\phi_{m,n}\) for the size of their white complements.

**Theorem.** For every integer pair \(2\le m\le n\), the minimum size of a nonempty fort is
\[
\phi_{m,n}=\begin{cases}
2,&(m,n)=(2,2),\\
3,&(m,n)\in\{(2,3),(3,3)\},\\
4,&\text{otherwise}.
\end{cases}
\]
The largest failed zero forcing set therefore has \(mn-\phi_{m,n}\) vertices. The exact number of maximum failed sets is
\[
M_{m,n}=\begin{cases}
2,&(m,n)=(2,2),\\
6,&(m,n)\in\{(2,3),(3,3)\},\\
44,&(m,n)=(2,4),\\
\bigl(\binom{n}{2}\bigr)^2,&m=2,\ n\ge5,\\
54,&(m,n)=(3,4),\\
60,&(m,n)=(4,4),\\
\binom{m}{2}\binom{n}{2},&3\le m\le n\text{ and none of the preceding cases}.
\end{cases}
\]
Every maximum failed set is stalled before any forcing move, and its white complement is one of the following shapes (up to independently permuting rows and columns, and transposing for square boards):

- \((2,2)\): one white cell in each row and column (two labeled possibilities).
- \((2,3)\) and \((3,3)\): one white cell in every column and at least one white cell in each row; for \((3,3)\) this is a permutation pattern.
- \(m=2,n\ge4\): two arbitrary white cells in each row; additionally for \(n=4\), a white column transversal having row counts \(3,1\) is possible.
- \((3,4)\): either a filled \(2\times2\) rectangle, or one white cell in every column with row counts \(2,1,1\).
- \((4,4)\): either a filled \(2\times2\) rectangle, or a four-cell permutation pattern.
- \(m\ge3,n\ge5\): precisely the filled \(2\times2\) rectangles.

In the thin-board regime \(m=2,n\ge5\), let \(t\) be the intersection size of the two row-wise two-element column sets. The three symmetry types \(t=0,1,2\) have, respectively,
\[
\binom{n}{2}\binom{n-2}{2},\qquad 2\binom{n}{2}(n-2),\qquad \binom{n}{2}
\]
labeled realizations. For \((2,4)\), the same three types account for \(36\) patterns and the additional \((3,1)\) transversal type accounts for \(8\). This separates the thin-board family from the eventually single-orbit family \(m\ge3,n\ge5\).

## Assumptions and scope

All graphs are finite, simple, undirected and labeled by their coordinate cells. The theorem assumes exactly \(2\le m\le n\); swapping the two dimensions gives the result for all \(m,n\ge2\). A *fort* is a nonempty white set \(W\) such that every vertex outside \(W\) has either zero or at least two neighbors in \(W\). A *minimum fort* has smallest size, not merely inclusion-minimality. The counted objects are distinct labeled vertex subsets; quotienting by automorphisms gives the orbit descriptions but not the displayed \(M_{m,n}\). No claim concerns generalized or positive-semidefinite zero forcing.

## Proof

**1. Reduction to minimum forts.** If a failed blue set \(S\) admits a forcing move, run all possible forcing moves until no more are possible. Its final blue closure \(T\) is strictly larger than \(S\) but is still failed, because the original process cannot force the entire graph. Therefore every maximum failed set is stalled. For a stalled blue set, its nonempty white complement \(W\) is a fort, by the zero-forcing rule. Conversely the complement of any fort is stalled and failed. Consequently the maximum size equals \(mn\) minus the minimum fort size, and complementing gives a bijection between maximum failed sets and minimum forts.

**2. Row-column criterion.** For any nonempty \(W\subseteq[m]\times[n]\), let \(r_i\) be the number of its cells in row \(i\), and \(c_j\) the number in column \(j\). At a blue cell \((i,j)\notin W\), the white neighbors occupy its row or its column, with no overlap (because the cell is blue), so their number is exactly \(r_i+c_j\). Thus \(W\) is a fort if and only if
\[
\forall (i,j)\notin W:\quad r_i+c_j\ne1.
\]
This criterion yields an exhaustive four-way classification according to empty rows or columns:

(a) If every row and every column meets \(W\), the set is automatically a fort.

(b) If every row meets \(W\) but some column is empty, the set is a fort precisely when each row contains at least two white cells: any row containing just one gives an external blue cell in an empty column with exactly one white neighbor. Hence \(|W|\ge2m\).

(c) If every column meets \(W\) but some row is empty, the corresponding condition is at least two white cells in each column, implying \(|W|\ge2n\).

(d) If some row and some column are empty, the set is a fort precisely when every occupied row and every occupied column contains at least two white cells. Hence \(|W|\ge4\), and equality forces exactly two occupied rows and two occupied columns with all four intersections white, a filled \(2\times2\) rectangle.

Case (a) has \(|W|\ge\max(m,n)=n\). In every dimension a filled \(2\times2\) rectangle is a fort, so \(\phi_{m,n}\le4\). For \(|W|<4\), only case (a) can occur for \(m,n\ge2\), except that case (b) with \(|W|=2m\ge4\), case (c) with \(|W|=2n\ge4\), and case (d) with \(|W|\ge4\) cannot contribute. Thus the only smaller forts are (i) the two bijective two-cell transversals of \((2,2)\); (ii) the six three-cell column transversals of \((2,3)\) that use both rows; and (iii) the six permutation patterns of \((3,3)\). This proves the fort-size formula and classifies those cases.

**3. Enumerating the four-cell cases.** When the minimum fort has size four and \(m\ge3\), case (d) contributes exactly \(\binom{m}{2}\binom{n}{2}\) filled rectangles: choosing two occupied rows and columns necessarily leaves both an empty row and an empty column. When \(m=2\), the same rectangular patterns do **not** belong to case (d), because no row is empty. Instead, across cases (a) and (b), four whites with two occupied rows each containing exactly two whites are chosen independently in \(\bigl(\binom{n}{2}\bigr)^2\) ways. Some such patterns have no empty column when \(n=4\) and therefore belong to case (a), while the others belong to case (b); this unified row-wise count includes each exactly once. In case (c), four whites require \(n=2\), which, under \(2\le m\le n\), occurs only in the previously settled \((2,2)\) case.

Case (a) with four whites requires \(n\le4\). At \((2,4)\), the four occupied columns each contain one white cell; the row distribution must be \((2,2)\) or \((3,1)\). The former is already counted among the \(\binom{4}{2}^2=36\) two-plus-two row patterns; the latter gives \(2\binom41=8\) additional forts. At \((3,4)\), every column has one white and all three rows are occupied, forcing row counts \((2,1,1)\). Choosing the repeated row, its two columns, and arranging the remaining two columns on the other rows gives \(3\binom{4}{2}\,2!=36\) extra forts, on top of \(\binom{3}{2}\binom{4}{2}=18\) rectangles. At \((4,4)\), every row and column has exactly one white, giving \(4!=24\) permutation patterns in addition to \(\binom{4}{2}^2=36\) rectangles. These exhaust the case (a) possibilities; for \(n\ge5\) none are possible. Adding the disjoint families proves the claimed multiplicity formula.

**4. Orbit refinement.** In a \(2\times n\) board with two whites in each row, the row-wise two-element column sets \(A,B\) are related under row exchange and simultaneous column permutation. Their intersection size \(t=|A\cap B|\in\{0,1,2\}\) completely determines the orbit. For each ordered \(A\), the numbers of choices for \(B\) with \(t=0,1,2\) are \(\binom{n-2}{2}\), \(2(n-2)\), and \(1\). Multiplication by \(\binom{n}{2}\) proves the orbit counts. The other shapes each form one orbit under row/column permutations; when both shapes occur, they are distinct by their occupancy degree sequences. This completes the classification.

## Verification

The accompanying standalone `verify.py` constructs rook-graph adjacency directly from coordinate equality and enumerates white subsets, testing the defining fort condition without using the row-column proof criterion. It verifies the minimum sizes and exact counts for all \(2\le m\le n\le7\) with \(mn\le48\): 20 dimension pairs and 360,898 tested candidate subsets. It separately simulates the standard blue-to-white forcing rule for eight small graph dimensions and checks that every minimum-fort complement stalls and gives exactly the predicted maximum count. The execution output includes `FORT_COUNTS_OK` and eight `ZERO_FORCING_OK` lines. The finite tests are corroboration, not the justification of the infinite classification.

Run `python3 verify.py` with Python 3 and only its standard library. Its source is included with this result.

## Relationship to prior work

Fetcie, Jacob, and Saavedra (2015, Theorem 4.3) determined the **number of vertices** in a maximum failed zero forcing set of \(K_m\square K_n\) for dimensions with one factor at least four, and exhibited one \(2\times2\) rectangle obstruction. Their theorem does not enumerate **all** maximum sets. Abara and Pelayo (2022, Section 3.1, Theorem 3.7) recall that scalar theorem in a paper about constructions of maximal failed sets for graph products; that does not count rook extremizers. Cameron et al. (2023) give general fort-hypergraph and product bounds, not this classification. Becker et al. (2024) count minimal forts of other graph families and develop general graph-operation constructions, without this specific all-maximum rook enumeration. The distinction between minimum cardinality and inclusion-minimal forts is important: this result counts only minimum forts, not all inclusion-minimal forts.

## Limitations

This is a self-review, not an independent audit or an established publication-priority claim. Searches of published literature and mathematical research records did not identify an equivalent complete enumeration, but an unindexed account of the minimum-fort multiplicities or an indirect stronger graph-product classification could exist. In particular, the previously known scalar failed zero forcing number is not claimed as new. The theorem is specific to rook graphs and the *standard* zero-forcing rule; it makes no assertion about arbitrary products, stronger forcing variants, or the count of all inclusion-minimal forts of every cardinality.

## References

1. K. Fetcie, B. Jacob, and D. Saavedra, *The failed zero forcing number of a graph*, Involve 8 (2015), 99–117, Theorem 4.3. DOI: https://doi.org/10.2140/involve.2015.8.99 . Full text: https://msp.org/involve/2015/8-1/involve-v8-n1-p09-s.pdf .
2. M. N. M. Abara and P. A. B. Pelayo, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997v1, first publicly posted 2022-02-10, Section 3.1. https://arxiv.org/abs/2202.04997 .
3. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1, first posted 2023-10-27. https://arxiv.org/abs/2310.17904 .
4. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1, first posted 2024-04-09, Sections 2 and 5. https://arxiv.org/pdf/2404.05963 .
