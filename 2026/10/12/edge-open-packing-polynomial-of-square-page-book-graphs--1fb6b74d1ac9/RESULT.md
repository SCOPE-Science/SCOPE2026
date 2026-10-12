# Edge-open-packing polynomial of square-page book graphs
## Finding
For every integer \(m\ge1\), let \(B_m\) be the square-page book graph formed from \(m\) copies of \(C_4\) sharing the edge \(xy\). On page \(i\), write
\[
L_i=xu_i,\qquad M_i=u_iv_i,\qquad R_i=v_i y.
\]
Thus
\[
E(B_m)=\{xy\}\cup\{L_i,M_i,R_i:1\le i\le m\}.
\]

Define the edge-open-packing enumerator, including the empty packing by convention, by
\[
\mathcal E_o(B_m;z)=\sum_D z^{|D|},
\]
where \(D\) ranges over edge open packing sets. Then
\[
\boxed{\mathcal E_o(B_m;z)=3(1+z)^m-2+2mz^2+z\bigl(2(1+z)^m-1\bigr).}
\]

The edge open packing number is therefore
\[
\rho_e^o(B_m)=m+1.
\]
For \(m\ge2\), the two maximum packings are exactly
\[
\{xy,L_1,\ldots,L_m\}
\quad\text{and}\quad
\{xy,R_1,\ldots,R_m\}.
\]
For the boundary graph \(B_1=C_4\), there are four maximum packings of size \(2\).

## Assumptions and scope
Two distinct edges \(e_1,e_2\) have a common edge if there exists a third edge \(e\notin\{e_1,e_2\}\) joining an endpoint of \(e_1\) to an endpoint of \(e_2\). An edge open packing is a set of edges no two of which have a common edge.

The original parameter is defined for nonempty sets. The enumerator above adjoins the empty set with coefficient \(1\), as is standard for subset generating functions; this convention does not affect \(\rho_e^o\) or any nonempty classification.

The graph family here is the square-page book: each page is the cycle
\[
xu_iv_iyx
\]
and all pages share exactly the spine edge \(xy\).

## Proof
Write the spine as
\[
s=xy.
\]
The proof is a complete compatibility analysis of edge types.

First, \(s\) is compatible with every \(L_i\) and every \(R_i\). For example, the only edges incident with both endpoint sets of \(s=xy\) and \(L_i=xu_i\) that could join the two selected edges are \(s\) and \(L_i\) themselves; the edge \(yu_i\) is absent. The same argument holds for \(R_i\). In contrast, \(s\) conflicts with \(M_i\), because \(L_i\) and \(R_i\) are third edges joining endpoints of \(s\) and \(M_i\).

Second, all left edges are pairwise compatible, all right edges are pairwise compatible, and all middle edges are pairwise compatible. Distinct pages have no edges between their internal vertices, while two left edges share only \(x\) and two right edges share only \(y\).

Third, every \(L_i\) conflicts with every \(R_j\), because the spine \(s=xy\) joins endpoint \(x\) of \(L_i\) to endpoint \(y\) of \(R_j\).

Fourth, \(L_i\) is compatible with \(M_i\), but for \(j\ne i\), the edge \(L_j=xu_j\) is a common edge of \(L_i\) and \(M_j\). Symmetrically, \(R_i\) is compatible with \(M_i\), while \(R_i\) conflicts with \(M_j\) for \(j\ne i\).

These relations classify every packing.

If \(s\in D\), then no middle edge may lie in \(D\), and the left and right families cannot be mixed. Hence the spine-containing packings contribute
\[
z\bigl(2(1+z)^m-1\bigr),
\]
where the subtraction removes the duplicate set \(\{s\}\).

Now suppose \(s\notin D\). If \(D\) contains at least two middle edges, then no side edge can occur, because every side edge conflicts with all middle edges except the one on its own page. Thus all such packings are already among arbitrary subsets of the middle family, contributing
\[
(1+z)^m.
\]
If no middle edge is selected, then the packing is a nonempty subset of the left family or a nonempty subset of the right family, contributing
\[
2\bigl((1+z)^m-1\bigr).
\]
Finally, if exactly one middle edge \(M_i\) is selected, then the only possible side additions are \(L_i\) or \(R_i\), and they cannot both be used because every left edge conflicts with every right edge. The new two-edge packings contribute
\[
2mz^2.
\]
The singleton \(\{M_i\}\) is already counted in \((1+z)^m\).

Adding the four disjoint contributions gives
\[
\mathcal E_o(B_m;z)
=(1+z)^m+2\bigl((1+z)^m-1\bigr)+2mz^2
+z\bigl(2(1+z)^m-1\bigr),
\]
which simplifies to the claimed formula.

The highest possible exponent is \(m+1\), coming from the spine together with all left edges or with all right edges. Hence
\[
\rho_e^o(B_m)=m+1.
\]
For \(m\ge2\), these are the only degree-\((m+1)\) contributions, so there are exactly two maxima. When \(m=1\), the extra two same-page pairs \(\{M_1,L_1\}\) and \(\{M_1,R_1\}\) also have size \(2\), yielding four maxima.

## Verification
The included checker constructs \(B_m\) directly and tests the original common-edge definition for every edge subset for
\[
1\le m\le6.
\]
For each subset it independently tests the structural classification above, compares the complete size distribution with the closed polynomial, and checks the edge open packing number and maximum-set count.

## Relationship to prior work
The 2022 foundational paper introduces edge open packing and determines the scalar parameter for paths, cycles, complete multipartite graphs, wheels, and the Petersen graph. Its searchable full text contains no book or theta specialization. The present result concerns a different standard cyclic family and determines every feasible edge subset, not only the maximum size.

A 2024 follow-up establishes complexity results, a linear-time algorithm on trees, sharp general bounds, and extremal characterizations. A second 2024 preprint studies induced matching versus edge open packing on trees and graph products. Neither inspected source contains a book or theta specialization. Later algorithmic work covers several broad hereditary graph classes, but an algorithm for a super-class does not imply the closed all-set enumerator or the exact optimizer classification stated here.

The square-page book family also appears naturally as a generalized theta construction in other graph-parameter literature. The common spine creates a distinctive compatibility split: left edges form one star arm family, right edges form another, while middle edges behave as a mutually compatible transversal family. That structure is what produces the closed polynomial.

## Limitations
The theorem is for square-page books. It does not address triangular books, longer-cycle books, or arbitrary generalized theta graphs.

The polynomial is an explicitly defined enumerator; no claim is made that this notation is standard in the edge-open-packing literature.

The exhaustive computation through six pages is corroborative only. The arbitrary-\(m\) result follows from the complete compatibility proof.

A differently phrased or non-indexed treatment of square-page books may exist despite the targeted searches.

## References
1. G. Chelladurai, K. Kalimuthu, S. Soundararajan, “Edge open packing sets in graphs,” RAIRO Operations Research 56 (2022), 3765–3776, DOI 10.1051/ro/2022171; published online 1 November 2022.
2. B. Brešar, B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:2403.00750v1, 1 March 2024.
3. B. Brešar, T. Dravec, J. Hedžet, B. Samadi, “Induced matching vs edge open packing: trees and product graphs,” arXiv:2406.04020v1, 7 June 2024.
