# The Heawood matching complex is a wedge of sixteen 4-spheres
## Finding
Let \(H\) be the Heawood graph in its Fano-plane incidence presentation: the point vertices are \(p_0,\ldots,p_6\), the line vertices are \(\ell_0,\ldots,\ell_6\), and \(p_j\) is adjacent to \(\ell_i\) precisely when \(j\in\{i,i+1,i+3\}\) modulo \(7\). Then its ordinary matching complex satisfies
\[
\mathcal M(H)\simeq\bigvee^{16} S^4.
\]
Here \(\mathcal M(H)\) is the simplicial complex whose vertices are the 21 edges of \(H\) and whose simplices are pairwise vertex-disjoint edge sets.

## Assumptions and scope
The statement concerns the ordinary matching complex of the 14-vertex, 21-edge Heawood graph, not the perfect-matching complex. The graph is fixed intrinsically by the Fano incidence rule above. No equivariant homotopy type, torus embedding statement, or extension to a family of incidence graphs is claimed.

## Proof
Index the 21 incidences by listing, for \(i=0,\ldots,6\), the three edges from \(\ell_i\) to \(p_i,p_{i+1},p_{i+3}\) in that order. Exhaustive enumeration gives 3,461 nonempty faces. The face numbers in dimensions \(0\) through \(6\) are
\[
(21,168,644,1218,1050,336,24).
\]
The last entry is consistent with the classical count of 24 perfect matchings of the Heawood graph.

On the nonempty face poset, start with every face unmatched and process the edge indices in the order
\[
0,20,11,18,3,15,1,7,19,17,16,5,9,10,8,4,13,12,6,2,14.
\]
At an index \(x\), pair every still-unmatched face \(\sigma\) not containing \(x\) with \(\sigma\cup\{x\}\) whenever the latter is also still unmatched. This gives 1,722 matched cover pairs and leaves exactly 17 critical faces: one vertex and sixteen 4-simplices. The packaged certificate records all 17 critical faces.

The verifier constructs every one of the 14,574 cover relations in the nonempty face-poset Hasse diagram, reverses exactly the matched cover relations, and topologically sorts the resulting directed graph. All 3,461 faces are exhausted, so the matching is acyclic. By discrete Morse theory, \(\mathcal M(H)\) is homotopy equivalent to a CW complex with one 0-cell, sixteen 4-cells, and no cells in other dimensions. Every 4-cell therefore attaches to the 0-skeleton by the constant map, giving \(\bigvee^{16}S^4\).

## Verification
Run `python3 verify_heawood_matching.py` beside `morse_certificate.json`. The script reconstructs the Fano plane and its incidence graph, checks 3-regularity and the projective-plane pair condition, enumerates every matching, rebuilds the deterministic discrete-Morse matching, verifies every matched cover, checks the complete directed Hasse graph for acyclicity, and independently computes mod-2 simplicial boundary ranks. The latter are \(20,148,496,722,312,24\) in degrees \(1\) through \(6\), yielding reduced Betti number \(\widetilde\beta_4=16\) and zero in every other degree. A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Matsushita's 2019 preprint, later published in 2022, studies matching complexes as topological objects and has primary MSC 55P10. It determines wedge decompositions recursively for polygonal line tilings, a planar chain-of-polygons family. Its full text does not mention the Heawood graph, Fano plane, or toroidal incidence graphs. Bayer, Jelić Milutinović, and Vega later extended the polygonal-line-tiling family, again for graphs built as strings of intersecting cycles. The Heawood graph is instead the nonplanar Levi graph of the Fano plane, so those family theorems do not specialize to this object. Targeted searches for the Heawood graph, its line graph, Fano-incidence terminology, and matching-complex homotopy returned no equivalent or stronger statement. This search evidence supports originality but cannot prove absolute novelty.

## Limitations
The proof is finite and graph-specific. It does not classify matching complexes of all cubic symmetric graphs, Levi graphs, or generalized Heawood graphs. Acyclicity is exhaustively verified rather than replaced by a short symbolic description of every gradient path. Literature indexing is incomplete, so an unindexed or differently phrased prior computation remains a residual originality risk.

## References
1. T. Matsushita, *Matching complexes of polygonal line tilings*, arXiv:1910.00186, first submitted 2019-10-01; Hokkaido Math. J. 51 (2022), 339--359. Primary MSC 55P10.
2. M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, Discrete Math. 346 (2023), 113428.
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90--145.
