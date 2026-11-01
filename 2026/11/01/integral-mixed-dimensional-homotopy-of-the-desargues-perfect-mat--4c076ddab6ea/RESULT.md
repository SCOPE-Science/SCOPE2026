# Integral mixed-dimensional homotopy of the Desargues perfect-matching complex

## Finding

Let \(D=\operatorname{GP}(10,3)\) be the Desargues graph, and let \(\mathcal M_{\mathrm p}(D)\) be the simplicial complex whose faces are precisely the sets of graph edges extendible to a perfect matching. There is an integral homotopy equivalence
\[
\boxed{\mathcal M_{\mathrm p}(D)\simeq\bigvee^{31}S^3\vee S^4.}
\]
Thus the only nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^{31}\) and \(\widetilde H_4\cong\mathbb Z\). The theorem is a homotopy statement, not merely a computation over a field.

## Assumptions and scope

The graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), and edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\), with indices taken modulo ten. In the checker, \(u_i=i\) and \(v_i=10+i\), and the thirty unordered graph edges are indexed from zero after sorting endpoint pairs lexicographically. A simplicial vertex represents one graph edge, not a graph vertex. A face is a subset of some perfect matching of ten disjoint graph edges. All assertions concern this one graph; no uniform generalized-Petersen classification is claimed.

## Proof

**Complete facet enumeration.** Recursively select a vertex of minimum available residual degree, pair it with each available neighbor, and recurse on the uncovered vertices. Every perfect matching is encountered exactly once. The exact result is sixty ten-edge perfect matchings. An independent bipartite partition with ten vertices per class yields a ten-by-ten zero-one adjacency matrix whose permanent, computed by subset dynamic programming, is also sixty. The union of the downward closures of the sixty facets has exactly \(44{,}282\) faces including the empty face, or \(44{,}281\) nonempty simplices. An independent recursion over all \(113{,}192\) graph-edge matchings, combined with exact residual perfect-completion dynamic programming, returns the same extendible face set. The nonempty simplex face numbers in dimensions zero through nine are
\[
(30,375,2320,7320,12096,11700,7080,2700,600,60).
\]
These exhaustive algorithms are both supplied in `verify_desargues_perfect.py`.

**Acyclic face matching.** Encode a simplex by the thirty-bit mask of its indexed graph edges. Starting with the entire downward-closed face set, process the following edge indices in this exact order (literal checker data):

`23,27,18,1,10,9,12,21,6,14,0,11,5,2,15,29,16,26,28,7,13,17,3,8,24,19,4,20,25,22`.

At an index, pair every remaining face without that edge with its one-edge extension when both are still unpaired; remove the two paired faces. Delete the pair containing the empty face so that its upper vertex becomes critical, and exclude the empty face from the ordinary face poset. This leaves exactly \(22{,}124\) codimension-one pairs and the thirty-three critical nonempty simplices: one vertex, thirty-one dimension-three faces, and one dimension-four face. The critical vertex mask is `8388608` and the critical four-simplex mask is `272631820`. The verifier prints the full ordered list of thirty-one critical dimension-three masks.

To verify acyclicity, orient every matched Hasse incidence upward and all other incidences downward. The checker constructs all \(244{,}830\) incidences among the \(44{,}281\) nonempty simplices and performs a complete topological sort of this directed graph. All vertices are visited. Thus the matching is acyclic, and discrete-Morse theory gives a homotopy-equivalent CW complex containing exactly one zero-cell, thirty-one three-cells, and one four-cell.

**Integral attaching map.** Order simplex vertices by increasing indexed graph edge. The oriented simplicial boundary removes the successive vertices with alternating signs. For every matched pair \(\lambda\subset\mu\) with \(\lambda\) the codimension-one lower face, eliminate \(\lambda\) by the unit-coefficient relation from \(\partial\mu\). Acyclicity guarantees that recursively substituting along directed gradient paths terminates. The supplied exact-integer algorithm projects the signed boundary of the sole critical four-cell onto the thirty-one critical three-cells. In their printed increasing-mask order, **all thirty-one coefficients are zero**. The resulting integral cellular boundary map \(\mathbb Z\to\mathbb Z^{31}\) is zero.

**Upgrade from homology to homotopy.** The three-skeleton of this Morse CW model is a wedge of thirty-one three-spheres. The homotopy group \(\pi_3(\bigvee^{31}S^3)\cong\mathbb Z^{31}\) is detected completely by the individual attaching degrees; Whitehead-product contributions occur in higher dimensions. Since the integral degree vector of the four-cell is zero, its attaching map is nullhomotopic. Attaching that cell therefore adds a free four-sphere, establishing the asserted integral homotopy equivalence.

## Verification

Execute `python3 verify_desargues_perfect.py` using Python 3 standard library only. The checker reconstructs the graph, checks the complete perfect-matching enumeration against an independent permanent, independently enumerates all matching faces and tests perfect extendibility, builds and validates every discrete-Morse pair, topologically sorts the full oriented Hasse graph, computes every signed integral Morse boundary coefficient, and independently calculates simplicial homology ranks over \(\mathbb F_2\). It prints `DESARGUES_PMC_INTEGRAL_WEDGE_31_S3_1_S4_VERIFIED` on success. The expected textual output is included as `VERIFY_OUTPUT.txt`. Exact counts are finite certificates, not assertions that experiments alone establish an infinite statement; the claim concerns this fully enumerated finite complex.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega introduced and classified perfect-matching complexes for specified honeycomb families, including a line of hexagons and a particular finite honeycomb; their paper does not classify this incidence graph. Chandrakar and Singh proved perfect-matching results for polygonal line tilings and two-row grids, not this graph. The published ordinary matching-complex classification for the Desargues graph concerns **all** partial edge matchings, including those not extendible to perfect matchings: it has \(113{,}191\) nonempty simplices and homotopy type \(\bigvee^5S^5\vee\bigvee^{45}S^6\), which does not determine the \(44{,}281\)-face subcomplex here. The published Heawood perfect-matching result treats a different incidence graph with fourteen vertices and twenty-one edges and supplies no uniform formula covering the Desargues case. Searches under the aliases bipartite double cover of Petersen and middle-level graph \(H(5,2)\) found no covering theorem.

## Limitations

The result is an exact finite homotopy classification for one canonical bipartite cubic graph. It does not determine equivariant attaching maps, a general formula for perfect-matching complexes of cubic graphs, or the map on homology induced by the inclusion into the ordinary matching complex. The proof depends on the complete enumerated acyclic matching and on exact signed gradient-path reduction; mod-two homology or Euler characteristic alone would not prove the integral homotopy equivalence. Novelty is assessed against accessible primary literature, searchable research records, and checked claims, not guaranteed against unindexed publications. No independent external audit has been performed.

## References

1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first public 2022-09-06, especially Definition 1 and Section 5. https://arxiv.org/abs/2209.02803
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v1, first public 2024-07-08, Theorem 1.1 and Section 6. https://arxiv.org/abs/2407.05809
3. *The Desargues matching complex is a mixed-dimensional wedge of spheres*, published research record `2026/10/11/SCOPE-the-desargues-matching-complex-is-a-mixed-dimensional-wedge-of-s--67ff1e627721`, specifically the ordinary matching-complex theorem. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-desargues-matching-complex-is-a-mixed-dimensional-wedge-of-s--67ff1e627721
4. *Perfect Morse reduction of the Heawood perfect-matching complex*, published research record `2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d`. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
