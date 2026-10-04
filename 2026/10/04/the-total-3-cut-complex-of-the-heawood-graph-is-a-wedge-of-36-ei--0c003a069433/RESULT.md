# The total \(3\)-cut complex of the Heawood graph is a wedge of \(36\) eight-spheres
## Finding
Let \(H\) be the Heawood graph, realized as the Levi graph of the Fano plane with points \(p_i\) and lines \(\ell_i\) for \(i\in\mathbb Z/7\mathbb Z\), where \(p_j\) is incident to \(\ell_i\) exactly when \(j-i\in\{0,1,3\}\). For the total \(3\)-cut complex \(\Delta_3^t(H)\), whose facets are complements of independent three-subsets of \(V(H)\), one has \(\Delta_3^t(H)\simeq\bigvee^{36}S^8\).

## Assumptions and scope
The graph \(H\) has vertices \(p_0,\ldots,p_6,\ell_0,\ldots,\ell_6\). Its edges are precisely \(p_j\ell_i\) with \(j-i\in\{{0,1,3\}}\) modulo \(7\). Thus \(H\) is the standard fourteen-vertex Heawood graph. The total \(3\)-cut complex is the simplicial complex in which a set \(\sigma\subseteq V(H)\) is a face exactly when \(V(H)\setminus\sigma\) contains an independent set of cardinality \(3\).

The statement is an exact finite homotopy computation for this graph and this value of \(k\). It does not assert a formula for larger incidence graphs or for other total \(k\)-cut complexes.

## Proof
There are exactly \(154\) independent three-subsets of \(V(H)\). Exhaustively applying the defining face criterion gives \(15{,}900\) faces including the empty face and the nonempty face vector
\[
(14,91,364,1001,2002,3003,3432,3003,2002,833,154).
\]

Order the vertices as \(p_0,p_1,\ldots,p_6,\ell_0,\ell_1,\ldots,\ell_6\). Starting with the full face poset, perform the standard element matching successively at these fourteen vertices: at stage \(v\), match every currently unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{{v\}}\) whenever the latter is also a currently unmatched face. The resulting matching has exactly \(7{,}932\) pairs. Its unmatched faces are exactly \(36\) faces, all of dimension \(8\); the empty face is matched.

The union of sequential element matchings is acyclic. Independently of that general theorem, the supplied verifier constructs the entire Hasse diagram, reverses precisely the matched cover relations, and topologically sorts the resulting directed graph. All \(15{,}900\) vertices are visited, so no directed cycle exists.

Discrete Morse theory therefore replaces the simplicial complex by a CW complex with one \(0\)-cell and exactly \(36\) cells of dimension \(8\), with no other cells. Hence
\[
\Delta_3^t(H)\simeq\bigvee^{36}S^8.
\]

## Verification
Run `python3 verify.py`. The verifier reconstructs the Heawood graph from the Fano-plane incidence rule, enumerates all independent triples and all faces, recreates the staged matching, checks every matching pair and every Hasse cover relation, and proves acyclicity by a complete topological sort. As an independent chain-level check it computes all augmented boundary ranks over \(\mathbb F_2\), obtaining
\[
(1,13,78,286,715,1287,1716,1716,1287,679,154),
\]
which gives reduced Betti number \(36\) in degree \(8\) and zero in every other degree. The verifier prints `HEAWOOD_TOTAL3_VERIFY_OK` on success.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced total \(k\)-cut complexes and proved exact homotopy results for several graph families. Their paper gives the defining face criterion and the discrete-Morse element-matching machinery used here, but its complete-bipartite theorem does not apply to the Heawood graph, which is bipartite but not complete bipartite. Full-text inspection of arXiv:2209.13503 found no Heawood graph, Fano-plane incidence graph, or projective-plane incidence case.

A later paper, arXiv:2512.04486, studies total \(2\)-cut complexes for powers of cycles and Cartesian products and explicitly limits its main results to those families. It does not subsume this total \(3\)-cut computation.

## Limitations
The originality comparison cannot exclude an unindexed or very recent duplicate. The proof is finite and exact for the stated labeled realization of the Heawood graph; it gives no general theorem for all Levi graphs. The mod-\(2\) homology computation is corroborative only; the homotopy conclusion rests on the explicitly verified acyclic Morse matching.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, “Total Cut Complexes of Graphs,” arXiv:2209.13503v1, first public 2022-09-27.
2. P. Chauhan, S. Shukla, K. Vinayak, “Total \(2\)-cut complexes of powers of cycle graphs and Cartesian products of certain graphs,” arXiv:2512.04486v1, 2025-12-04.
