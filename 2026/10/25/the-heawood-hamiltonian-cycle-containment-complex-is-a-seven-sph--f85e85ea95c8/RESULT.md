# The Heawood Hamiltonian-cycle containment complex is a seven-sphere

## Finding
Let \(H\) be the 14-vertex Heawood graph, regarded as the incidence graph of the seven-point Fano plane. Define the **Hamiltonian-cycle containment complex** \(\mathcal H(H)\) to have one simplicial vertex per graph edge of \(H\). A finite edge set \(\sigma\subseteq E(H)\) is a simplex exactly if a spanning 14-cycle contains every edge in \(\sigma\). Then
\[
\mathcal H(H)\simeq S^7.
\]
In particular, the only nonzero reduced integral homology is \(\widetilde H_7(\mathcal H(H);\mathbb Z)\cong\mathbb Z\). The complex is pure of dimension 13, so its homotopy dimension is six less than its combinatorial dimension.

## Assumptions and scope
Label the points of the Fano plane by \(0,\ldots,6\) and its lines by \(7,\ldots,13\). For each \(j\in\{0,\ldots,6\}\), the line indexed by \(7+j\) contains the points \(j\), \(j+1\), and \(j+3\), taken modulo seven. Let \(H\) have one edge between a point and each line containing it. It is a simple cubic bipartite graph with 14 vertices and 21 edges. Number its edges from zero to twenty, ordered first by line index and then by point index, so that each subset has a unique 21-bit mask. Hamiltonian cycles are un-oriented 14-edge subsets.

The complex \(\mathcal H(H)\) consists of all subsets of all Hamiltonian-cycle edge sets. This is **not** the ordinary matching complex, whose faces are pairwise disjoint edges, nor the perfect-matching complex, whose facets are the seven-edge perfect matchings.

## Proof
**Exact finite description.** A depth-first Hamiltonian-cycle enumeration starts at point zero and traverses each other graph vertex exactly once. Keeping only tours whose second vertex precedes their last vertex counts each undirected Hamiltonian cycle once. The verifier finds exactly 24 distinct cycles. Separately, independent enumeration of all bijective point-to-line incidence choices gives 24 perfect matchings; complements of those matchings agree exactly with the set of 24 Hamiltonian cycles. Every facet of \(\mathcal H(H)\) therefore has fourteen edges. Generating all subsets of these 24 facets gives exactly 252,902 nonempty faces, with face vector in dimensions zero through thirteen
\[
(21,210,1316,5691,17346,37072,55380,58170,43400,23100,8652,2184,336,24).
\]
This generation is exhaustive because a face is *by definition* contained in at least one enumerated Hamiltonian cycle.

**Explicit discrete-Morse matching.** Represent each face by the bit mask of its graph-edge subset. Reserve mask zero (the empty face) and mask one (a vertex) from all pairings. Initially mark every face active. For edge-bit positions \(e=0,\ldots,20\) in ascending order, pair simultaneously every active nonreserved face \(f\) missing bit \(e\) to the active face \(f\cup\{e\}\), if both are active, then remove every paired face. Each pair is a covering relation in the face poset, and no simplex occurs in two pairs. Exhaustively executing these precisely specified operations leaves the empty face, a single critical vertex (mask one), and a single critical eight-element face (mask 674086). The remaining eight-element face is a critical seven-simplex. There are exactly 126,450 matched pairs, accounting for all 252,902 nonempty faces except the two critical faces.

**Acyclicity certificate.** For each incidence \(\tau\subset\sigma\) with dimensions differing by one and both nonempty, orient \(\tau\to\sigma\) when the pair is matched, and \(\sigma\to\tau\) otherwise. The verifier enumerates all 1,936,998 such incidences, constructs their directed in-degrees, and exhaustively performs Kahn's topological sort. It visits all 252,902 nonempty simplices and exhausts all directed edges. Consequently this orientation is acyclic; this is an exact finite certificate, not evidence merely from random sampling.

By the standard acyclic-matching theorem of discrete Morse theory, the complex is homotopy equivalent to a CW complex with one cell of dimension zero and one cell of dimension seven and no other cells. Because the attaching map of the sole seven-cell lands in a point, this CW complex is \(S^7\). This proves the assertion.

## Verification
Run the included standalone Python 3.9+ script `heawood_hamilton_verify.py` with the standard library only. It reconstructs graph incidences, independently enumerates all perfect matchings and Hamiltonian cycles, generates every face, recomputes the entire matching, and certifies acyclicity by complete topological sorting. The included `verification_output.txt` is the result of an actual execution. The final marker is `VERIFY_OK`.

## Relationship to prior work
Lawrence and Wilson's *The Structure of the Heawood Graph* enumerates its 24 Hamiltonian cycles and classifies cycle orbits (arXiv:1907.11978). Funk, Jackson, Labbate, and Sheehan study the 2-factor-Hamiltonian property of related cubic bipartite graphs. These graph-theoretic facts motivate the **family of Hamiltonian facets**, but do not themselves determine the homotopy type of their down-closure.

The separately published Heawood **perfect-matching complex** is homotopy equivalent to a wedge of sixteen two-spheres, while the ordinary **matching complex** is a wedge of sixteen four-spheres. Our 14-edge facets are the **complements of the seven-edge matching facets**. Taking complements of facets is not a homotopy equivalence or the standard simplicial Alexander dual, so neither prior homotopy theorem implies this seven-sphere result. The Hamiltonian-cycle containment condition and the full acyclic-matching proof constitute the new statement.

## Limitations
This proves the particular Heawood case, not a general assertion for all cubic bipartite or 2-factor-Hamiltonian graphs. The computation is exhaustive only because the graph and all its 24 Hamiltonian cycles are finite and explicitly enumerated. No claim of external or independent certification is made. Searches did not find a prior homotopy theorem for this exact containment complex, but unindexed or differently named equivalents may exist. Several relevant source comparisons were restricted to abstracts or indexed summaries rather than complete texts.

## References
1. K.-i. Kawarabayashi, K. Ota, A. Saito, *Hamiltonian cycles in n-extendable graphs*, Journal of Graph Theory **40** (2002), 75–82; first published 16 April 2002, doi:10.1002/jgt.10050. Background on the relationship between extension conditions and Hamiltonian cycles.
2. E. D. Lawrence, R. T. Wilson, *The Structure of the Heawood Graph*, arXiv:1907.11978 (first posted 27 July 2019), especially the Hamiltonian-cycle count and automorphism transitivity.
3. M. Funk, B. Jackson, D. Labbate, J. Sheehan, *2-Factor hamiltonian graphs* (2003), archival research record at https://iris.unibas.it/handle/11563/417.
4. M. Bayer, N. Jelić Milutinović, A. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics (2023), doi:10.37236/11525. A different matching-facet complex.
5. *Perfect Morse reduction of the Heawood perfect-matching complex*, indexed mathematical record https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d; comparison based on accessible indexed summary.
6. *The Heawood matching complex is a wedge of sixteen 4-spheres*, indexed mathematical record https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-heawood-matching-complex-is-a-wedge-of-sixteen-4-spheres--7150930ba12a; comparison based on accessible indexed summary.
7. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145. Standard acyclic-matching principle.
