# The Frucht-graph independence complex is a wedge of three 2-spheres
## Finding
Let \(F\) be the graph on vertex set \(\{0,1,\ldots,11\}\) with edge set
\[
\{01,06,07,12,17,23,28,34,39,45,49,56,5\!10,6\!10,7\!11,89,8\!11,10\!11\}.
\]
This labeled graph is isomorphic to the standard Frucht graph. Its independence complex satisfies
\[
\operatorname{Ind}(F)\simeq\bigvee^3 S^2.
\]

## Assumptions and scope
Graphs are finite and simple. A face of \(\operatorname{Ind}(F)\) is a vertex subset containing no edge of \(F\). The displayed edge set fixes the object independently of naming conventions. The accompanying verifier also checks an explicit isomorphism from this labeling to the order-one LCF realization
\[
[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]
\]
listed for the Frucht graph.

The claim is only about this independence complex. It does not assert a family theorem for asymmetric cubic graphs, Halin graphs, or identity graphs.

## Proof
Exhaustive enumeration of all \(2^{12}-1\) nonempty vertex subsets finds exactly \(168\) independent faces. Their face vector by simplicial dimension is
\[
(12,48,73,34,1).
\]

On the nonempty face poset, apply staged element matching in the vertex order
\[
(8,11,4,6,3,5,7,10,0,9,1,2).
\]
At each stage, pair every still-unmatched face \(\sigma\) not containing the current vertex \(v\) with \(\sigma\cup\{v\}\) whenever the latter is also a still-unmatched face.

This produces \(82\) disjoint matched cover relations. The only critical faces are
\[
\{8\},\qquad
\{5,7,9\},\qquad
\{1,9,10\},\qquad
\{0,3,11\}.
\]
Thus there is one critical \(0\)-cell and three critical \(2\)-cells.

For acyclicity, the verifier constructs all \(456\) Hasse cover relations of the nonempty face poset, reverses the matched covers relative to the ordinary face-poset orientation, and performs a complete topological sort. All \(168\) faces are visited, so the directed graph is acyclic. Forman's discrete-Morse theorem therefore gives a CW complex with one \(0\)-cell and three \(2\)-cells and no cells in any other positive dimension. Each \(2\)-cell is attached to the unique \(0\)-cell, hence
\[
\operatorname{Ind}(F)\simeq\bigvee^3S^2.
\]

## Verification
`verify.py` uses only the Python standard library. It checks the explicit Frucht LCF identification, connectedness, cubicity, and trivial automorphism group; exhaustively enumerates all independent faces; reconstructs the complete Hasse diagram; reproduces the staged matching; and verifies acyclicity.

As an independent chain-level check, it constructs the simplicial boundary matrices with signs. Over each of \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), the boundary ranks are
\[
(11,37,33,1),
\]
which gives Betti vector
\[
(1,0,3,0,0).
\]
The Euler characteristic is \(4\), consistent with the wedge decomposition. Running `python3 verify.py` ends with `VERIFY_OK`.

## Relationship to prior work
Matsushita and Wakatsuki study the same independence-complex construction under primary MSC \(55P10\). Their 2022 paper emphasizes that exact homotopy types can be difficult even for easily described graphs and gives a complete result for the square-grid family \(\Gamma_{n,6}\); its theorem does not cover the Frucht graph.

Goyal, Shukla, and Singh give explicit homotopy calculations for categorical products of complete graphs, generalized Mycielskians of complete graphs, and a specified local perturbation construction. Those inspected families likewise do not contain the Frucht graph.

The closest checked named-graph records concern independence complexes of the Heawood and dodecahedral graphs. A separate checked result treats graph-metric Vietoris--Rips complexes of asymmetric cubic Hamiltonian graphs on twelve vertices, which is a different simplicial-complex functor and does not imply the present claim.

## Limitations
The result is a single exact named-graph computation, not a classification of independence complexes of cubic or asymmetric graphs. The literature comparison does not prove universal bibliographic uniqueness: an obscure or non-indexed equivalent computation may exist. The homotopy conclusion itself does not rely on search completeness; it is certified by the explicit finite Morse matching and independently checked homology.

## References
1. Takahiro Matsushita and Shun Wakatsuki, “Independence complexes of \((n\times 6)\)-grid graphs,” arXiv:2207.10363v1, first posted 2022-07-21.
2. Shuchita Goyal, Samir Shukla, and Anurag Singh, “Homotopy Type of Independence Complexes of Certain Families of Graphs,” arXiv:1905.06926v1, first posted 2019-05-16.
3. Eric W. Weisstein, “Frucht Graph,” MathWorld, object reference and LCF data.
