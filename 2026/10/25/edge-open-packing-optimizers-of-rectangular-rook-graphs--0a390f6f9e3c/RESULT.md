# Edge-open-packing optimizers of rectangular rook graphs

## Finding

Let \(R_{p,q}=K_p\square K_q\) be the rook graph on a labeled \(p\)-by-\(q\) board, with integers \(2\le p\le q\). Two distinct edges have a **common edge** if a third edge joins an endpoint of the first to an endpoint of the second. An *edge open packing* (EOP) is a set of edges no two of which have a common edge. Let \(\rho_e^o(R_{p,q})\) be its maximum size, and let \(N_{p,q}\) count EOPs attaining that size, with all board cells distinguished.

**Theorem.** For all \(2\le p\le q\),
\[
\rho_e^o(R_{p,q})=p-\mathbf1_{\{p=q\text{ and }p\text{ odd}\}}.
\]
When \(p<q\), or when \(p=q\) is even, the exact number of maximum EOPs is
\[
N_{p,q}=\sum_{\substack{0\le h\le\min\{p,q-p\}\\ h\equiv p\pmod 2}}
\frac{p!\,q!}{2^h\,((p-h)/2)!\,h!\,(q-p-h)!}.
\]
When \(p=q\) is odd, it is
\[
N_{p,p}=(p!)^2\left[\frac{1}{((p-1)/2)!}
+\frac{1}{4((p-3)/2)!}\right].
\]
The proof also classifies each maximizing edge set, not merely its cardinality. In particular \(N_{2,3}=12\), \(N_{3,3}=45\), \(N_{4,4}=288\), and \(N_{5,5}=10800\).

For any fixed integer \(p\ge2\), as \(q\) increases without bound,
\[
N_{p,q}\sim\frac{q^{2p}}{2^p}.
\]

## Assumptions and scope

All graphs are finite, undirected, and simple. Cells are ordered pairs \((i,j)\), with row index \(1\le i\le p\) and column index \(1\le j\le q\); two distinct cells are adjacent when they share a row or column. EOPs are unordered subsets of the edge set, counted with row and column labels fixed. The theorem addresses the parameter in its edge-based, *not* vertex-open-packing, sense. Board sizes below two rows are excluded; the one-row graph is a clique and has EOP number one whenever it has an edge.

## Proof

**1. Canonical components.** Let \(B\) be an arbitrary EOP. Its selected-edge support has connected components that are induced stars. Indeed, an edge outside the selected pair joining endpoints of two selected edges would contradict the EOP definition. In a rook graph, two selected edges sharing a cell cannot both be horizontal: their other endpoints lie in the same row and are adjacent, giving a forbidden common edge. Similarly, two selected edges at a cell cannot both be vertical. Thus no cell is incident to three selected edges; a two-edge component is necessarily a bend formed by one horizontal and one vertical edge. Every component is consequently one of three types: \(H\), a single horizontal edge using one row and two columns; \(V\), a single vertical edge using two rows and one column; or \(L\), a two-edge bend using two rows and two columns, with one of four cells as its center.

Different components use **disjoint row sets and disjoint column sets**. Otherwise an endpoint in one component and an endpoint in the other share a row or column, hence are adjacent, contradicting the EOP condition. Conversely, any collection of \(H\), \(V\), and \(L\) components with pairwise disjoint row and column supports is an EOP, since the two leaves of each \(L\) are diagonal rather than adjacent and no edges cross between different supports. This proves a bijective decomposition of all EOPs.

**2. Size and parity.** Suppose an EOP has \(\ell\) bends, \(h\) horizontal single edges, and \(v\) vertical single edges. Its cardinality and row/column occupancies are respectively
\[
k=2\ell+h+v,\qquad r=2\ell+h+2v=k+v,\qquad c=2\ell+2h+v=k+h.
\]
Since \(r\le p\) and \(c\le q\), we have \(k\le p\). If \(p=q\) is odd and \(k=p\), then \(v=h=0\); this would require \(p=2\ell\), impossible. Hence \(k\le p-1\) in that case. If \(p\) is even, choose \(p/2\) disjoint \(L\) blocks, using \(p\) rows and \(p\) columns and giving \(p\) edges. If \(p\) is odd and \(q>p\), choose \((p-1)/2\) disjoint bends and one horizontal edge, using \(p\) rows and \(p+1\) columns and giving \(p\) edges. If \(p=q\) is odd, \((p-1)/2\) bends give \(p-1\) edges. Thus the claimed optimum is attained in all cases.

**3. Classification when \(k=p\).** The row identity \(r=k+v\le p\) forces \(v=0\). Thus \(2\ell+h=p\), every row is used, and the columns used number \(p+h\). Exactly the configurations with
\[
2\ell+h=p,\quad 0\le h\le q-p
\]
are possible: \(\ell\) two-row bends and \(h\) one-row horizontal components, with disjoint row and column supports. To count a fixed \((\ell,h)\), partition the \(p\) rows into \(\ell\) unordered pairs and \(h\) singleton blocks in
\[
\frac{p!}{2^\ell\ell!h!}
\]
ways. Assign a distinct unordered pair of columns to each of the \(\ell+h\) identified row blocks in
\[
\frac{q!}{2^{\ell+h}(q-2\ell-2h)!}
\]
ways. Each bend has four possible central cells, producing \(4^\ell\) choices; horizontal edges are then forced. Multiplication, using \(2\ell+h=p\), yields
\[
\frac{p!q!}{2^h\ell!h!(q-p-h)!}.
\]
Summing over admissible \(h\), necessarily congruent to \(p\) modulo two, proves the first enumeration.

**4. Classification when \(p=q\) is odd and \(k=p-1\).** Then \(v\le1\) and \(h\le1\) by the occupancy equations. Because \(p-1\) is even, \(h+v\) must be even. There are exactly two cases:

* \(h=v=0\): there are \(\ell=(p-1)/2\) bends, leaving one unused row and one unused column. Choose those in \(p^2\) ways and pair/match the remaining rows and columns, choosing four bend centers per pair. The number is \((p!)^2/\ell!\).
* \(h=v=1\): there are \(\ell=(p-3)/2\) bends and one component of each singleton orientation, using all rows and columns. Choose the horizontal singleton's row, the vertical singleton's two-row block, and pair the remaining rows; dually choose the vertical singleton's column and the horizontal singleton's two-column block, then assign disjoint pairs of columns to the remaining row pairs. Four bend centers per pair give a total of \((p!)^2/(4\ell!)\).

These cases are disjoint and exhaustive, proving the second enumeration. Finally, for fixed \(p\), the term \(h=p\) in the first sum exists for \(q\ge2p\) and has polynomial degree \(2p\) in \(q\), with leading coefficient \(1/2^p\); all other terms have lower degree. This proves the asymptotic.

## Verification

A standalone Python 3 verifier (`verify_eop.py`) constructs each rook graph from cell adjacencies, tests every candidate pair of selected edges against the original third-edge definition, and enumerates the resulting compatible edge subsets by increasing edge index using integer bitsets. It never uses the \(H/V/L\) decomposition. The independent enumeration agrees with both formulas on 12 boards (from \(2\times2\) through \(5\times5\)), discovering 30,977 nonempty EOPs in those test instances. Reproduce with `python3 verify_eop.py`. The exhaustive checks support the proof but do not substitute for its universal argument.

## Relationship to prior work

Chelladurai, Kalimuthu, and Soundararajan introduced edge open packings and basic bounds (2022). Brešar and Samadi (arXiv:2403.00750, 1 March 2024) provided complexity results and general bounds. Brešar, Dravec, Hedžet, and Samadi (arXiv:2406.04020, first public 6 June 2024), in Section 5, proved the generic Cartesian-product lower bound
\[
\rho_e^o(G\square H)\ge\max\{\rho_e^o(G)\alpha(H),\alpha(G)\rho_e^o(H)\}.
\]
For two nontrivial cliques, that bound equals one, whereas the theorem above grows like the smaller clique size, with a single odd-square exception. The inspected sections of the product paper present bounds and hypercube results, not the stated rook-graph classification or enumeration. Pandey and Santra (arXiv:2508.01935, 2025) provide general tests for an EOP number, rather than labeled optimizer counts for rook graphs. A bibliographic search did not identify equivalent exact rook-board formulas. This is a best-knowledge statement, not a proof of priority.

## Limitations

The count is for **maximum** EOPs, not all inclusion-maximal EOPs or an injective edge-coloring decomposition. The theorem does not cover arbitrary Cartesian products, Hamming graphs of three or more factors, or higher-dimensional rook boards. A future or unindexed equivalent enumeration may exist. No independent mathematical audit has been performed.

## References

1. C. Gayathri, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776. DOI: 10.1051/ro/2022171. https://www.numdam.org/articles/10.1051/ro/2022171/
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (2024). https://arxiv.org/abs/2403.00750
3. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (2024), especially Section 5. https://arxiv.org/abs/2406.04020
4. A. Pandey and K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935 (2025), especially Section 2. https://arxiv.org/abs/2508.01935
