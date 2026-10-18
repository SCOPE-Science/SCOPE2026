# Complete edge-open-packing polynomial and odd-square rigidity of rook graphs

## Finding

Let \(R_{m,n}=K_m\square K_n\), with integers \(m,n\ge2\), be the rook graph whose vertices are the cells of a labeled \(m\)-by-\(n\) board; two cells are adjacent precisely when they share a row or column. An edge-open-packing set is a subset \(B\) of graph edges for which no two distinct members admit a *third* graph edge joining an endpoint of one to an endpoint of the other. Define the size-generating polynomial \(P_{m,n}(z)=\sum_B z^{|B|}\), where the sum includes the empty set.

**Complete polynomial.** For any \(m,n\ge2\),
\[
P_{m,n}(z)=\sum_{\substack{h,v,e\ge0\\h+2v+2e\le m\\2h+v+2e\le n}}
\frac{(m)_{\underline{h+2v+2e}}(n)_{\underline{2h+v+2e}}}{2^{h+v}h!v!e!}\,z^{h+v+2e},
\]
where \((a)_{\underline b}=a!/(a-b)!\) is the falling factorial, and all summation variables are integers. Equivalently, including degenerate board sizes in the generating series as an algebraic convention,
\[
\sum_{m,n\ge0}P_{m,n}(z)\frac{u^m w^n}{m!n!}
=\exp\!\left(u+w+\frac z2(uw^2+u^2w)+z^2u^2w^2\right).
\]

**Maximum and optimizer count.** If \(2\le m\le n\), then the edge-open-packing number is
\[
\rho_e^o(R_{m,n})=\begin{cases}m-1,&m=n\text{ and }m\text{ odd},\\m,&\text{otherwise}.\end{cases}
\]
Let \(N_{m,n}\) count maximum-cardinality edge-open-packing sets on the labeled board. When \(m<n\),
\[
N_{m,n}=\sum_{\substack{0\le h\le\min(m,n-m)\\h\equiv m\pmod 2}}
\frac{m!\,(n)_{\underline{m+h}}}{2^h h!\,((m-h)/2)!}.
\]
When \(m=n\) is even,
\[
N_{m,m}=\frac{(m!)^2}{(m/2)!}.
\]
When \(m=n\) is odd,
\[
N_{m,m}=\frac{(m+7)(m!)^2}{8\,((m-1)/2)!}.
\]
The formulas classify every optimal set by its horizontal-single-edge, vertical-single-edge, and perpendicular-elbow components.

## Assumptions and scope

All graphs are finite, simple, and undirected. The rook graph's two coordinates index labeled rows and columns, so the counting formulas do not divide by graph automorphisms. In the polynomial, \(h\) denotes the number of isolated horizontal chosen edges, \(v\) the isolated vertical chosen edges, and \(e\) the number of chosen induced two-edge perpendicular elbows. Every chosen edge is counted once, while an elbow contributes two chosen edges. The empty edge subset contributes the constant coefficient one. The same polynomial formula is symmetric after interchanging \(m\) with \(n\) and \(h\) with \(v\), so ordering the sides is needed only for the closed extremal formulas.

## Proof

**Step 1: complete component classification.** A general fact about an edge-open-packing set \(B\) is that the graph induced by endpoints of its selected edges is a disjoint union of induced stars, and those stars have exactly the selected edges. Indeed, an extra edge between endpoints of any two different selected edges would be a forbidden third edge; a nonstar selected-edge component would likewise produce two selected edges with a third edge joining their endpoints. This statement can also be checked directly: if selected edges form a cycle, a path of three edges, or any branching pattern with an extra leaf–leaf edge, two selected edges are joined by a distinct edge, contradicting the definition.

For each vertex \((i,j)\) in a rook graph, its neighborhood is the disjoint union of the clique on its other row cells and the clique on its other column cells. Thus an induced star has at most two leaves, and if it has two, one leaf lies in the row and the other in the column. Consequently each component of a nonempty packing is one of precisely three tiles: \(H\), a horizontal single edge using one row and two columns; \(V\), a vertical single edge using two rows and one column; or \(E\), a two-edge perpendicular elbow using two rows and two columns. If two distinct components reused any row or column, one vertex from each would be adjacent, providing a forbidden third edge. Hence components use pairwise disjoint row sets and pairwise disjoint column sets. Conversely, any family of the three permitted tile types on mutually disjoint row and column sets is a valid edge-open-packing set. This proves a bijective classification without additional assumptions.

**Step 2: enumeration.** For \(h\) horizontal tiles, \(v\) vertical tiles, and \(e\) elbow tiles, the total numbers of occupied rows and columns are respectively
\[
r=h+2v+2e,\qquad s=2h+v+2e,
\]
and the selected-edge count is \(k=h+v+2e\). Select and order the \(r\) distinct row labels and \(s\) distinct column labels, giving \((m)_{\underline r}(n)_{\underline s}\). Divide by \(h!v!e!\) to forget the order of components of each type and by \(2^h\) for the two unordered columns of each horizontal edge and \(2^v\) for the two unordered rows of each vertical edge. For each elbow there are four choices of center in its designated two-by-two rectangle. These four choices exactly cancel the two unordered-row and two unordered-column symmetries of that elbow, so there is no further elbow denominator. Hence the number of specified tile families is \((m)_{\underline r}(n)_{\underline s}/(2^{h+v}h!v!e!)\), proving the polynomial formula by summation. The labeled exponential formula with one unused row or column, horizontal and vertical single-edge tiles, and elbows gives the stated exponential generating series.

**Step 3: the maximum.** Assume \(2\le m\le n\). The row count gives \(k+v\le m\), so \(k\le m\). If \(k=m\), then necessarily \(v=0\); if also \(n=m\), the column bound \(k+h\le n=m\) forces \(h=0\). Thus on a square board, \(k=m\) would imply \(m=2e\), impossible for odd \(m\). When \(m=n\) is even, \(m/2\) disjoint elbows attain \(k=m\). When \(m<n\) and \(m\) is even, the same construction attains \(k=m\). When \(m<n\) and \(m\) is odd, one horizontal edge and \((m-1)/2\) elbows use \(m\) rows and \(m+1\le n\) columns and attain \(k=m\). Finally, on an odd square, \((m-1)/2\) elbows attain \(k=m-1\). This proves the maximum for all allowed integer parameters, including the smallest \(2\)-by-\(2\) and \(3\)-by-\(3\) boards.

**Step 4: all extremizers.** For \(m<n\), equality \(k=m\) requires \(v=0\), so \(m=h+2e\), and the column bound becomes \(m+h\le n\). The possible nonnegative integer values of \(h\) therefore have the range and parity in the displayed sum. Substituting \(v=0\), \(e=(m-h)/2\), and \(r=m\) into the polynomial coefficient proves the rectangular optimizer formula and enumerates every equality case. For an even square, \(k=m\) forces \(h=v=0\) and \(e=m/2\), giving \((m!)^2/(m/2)!\). For an odd square put \(m=2t+1\). Equality \(k=m-1=2t\) implies \(v,h\le1\), and parity of \(k=h+v+2e\) forces either \((h,v,e)=(0,0,t)\) or \((1,1,t-1)\). These contribute respectively \((m!)^2/t!\) and \((m!)^2/(4(t-1)!)\), whose sum simplifies to \((m+7)(m!)^2/(8t!)\). No other extremizers exist because the component classification is exhaustive.

## Verification

The package includes standalone `verify.py` and `verification_output.txt`. Run `python3 verify.py` in the directory containing the extracted files. The program independently builds rook-graph edges and tests the *third-edge* definition for all pairs of selected edges, without using the tile classification for its direct enumeration. Its complete coefficient vectors coincide with the proposed polynomial on thirteen labeled boards from \(2\)-by-\(2\) through \(5\)-by-\(5\) (including rectangular examples), totaling \(46{,}476\) enumerated edge-open-packing sets. It separately checks the maximum and its coefficient against the explicit extremal expressions for all \(190\) pairs \(2\le m\le n\le20\). The final output is `VERIFICATION_OK`. The proof, not these finite computations, establishes all infinite-domain claims.

## Relationship to prior work

Chelladurai, Kalimuthu, and Soundararajan (2022) introduced edge-open-packing sets and observed their induced-star structure. They determined the parameter for paths, cycles, complete multipartite graphs, wheels, and the Petersen graph; the present rook-graph polynomial and extremizer counts are not among their reported results. Brešar and Samadi (2024) studied computational complexity, algorithms on trees, and general upper bounds, not a complete two-parameter rook-graph counting polynomial. Brešar, Dravec, Hedžet, and Samadi (2024) gave general bounds for graph products, including a Cartesian-product lower bound. Their direct-product theorems refer to a different graph product, and their Cartesian bound by itself does not determine the present polynomial, sharp odd-square obstruction, or numbers of extremizers. The novelty claim is confined to the exact distribution, its tile classification in rook graphs, the generating function, and extremal counts; it does not claim priority for the general induced-star observation or the definition of edge-open packing.

## Limitations

The theorem concerns the rook-graph Cartesian products of complete graphs and does not assert formulas for arbitrary Cartesian products or general line graphs. Verification covers finite examples only. The literature comparison involved accessible full texts and mathematical-record searches, so equivalent results in unindexed or undiscovered literature remain possible. No independent review or external validation of this finding has been performed.

## References

1. G. Chelladurai, K. Kalimuthu, and S. Soundararajan, “Edge open packing sets in graphs,” *RAIRO Operations Research* **56** (2022), 3765–3776. DOI: `10.1051/ro/2022171`. Public full text: https://www.numdam.org/item/10.1051/ro/2022171.pdf (first publicly available journal posting verified 2022-11-01).
2. B. Brešar and B. Samadi, “Edge open packing: complexity, algorithmic aspects, and bounds,” arXiv:`2403.00750` (2024). https://arxiv.org/abs/2403.00750.
3. B. Brešar, T. Dravec, J. Hedžet, and B. Samadi, “Induced matching vs edge open packing: trees and product graphs,” arXiv:`2406.04020` (2024). https://arxiv.org/abs/2406.04020.
