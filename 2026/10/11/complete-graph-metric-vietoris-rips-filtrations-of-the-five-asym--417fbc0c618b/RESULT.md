# Complete graph-metric Vietoris–Rips filtrations of the five asymmetric cubic Hamiltonian graphs on twelve vertices
## Finding
Let \(G_1,\ldots,G_5\) be the graphs encoded by the graph6 strings

``K?ABE`Ke@WEO``, ``K?ABCfCU@WF?``, ``K?ABAdgi?wQ_``, ``K?AB?tos@WP_``, and ``K?`@EaKX?sEO``,

respectively. Equip each graph with its unweighted shortest-path metric, and let \(\operatorname{VR}_{\le r}(G_i)\) be the inclusive Vietoris--Rips complex: a nonempty set of vertices is a simplex exactly when its diameter is at most \(r\). These five graphs are pairwise nonisomorphic, cubic, Hamiltonian, and asymmetric. Since Brewer--Gregory--Jones--Florez--Narayan prove that there are exactly five asymmetric cubic Hamiltonian graphs on twelve vertices, they exhaust that class.

Their complete filtrations are
\[
\operatorname{VR}_{\le r}(G_i)\simeq \bigvee^{11}S^0\qquad(0\le r<1)
\]
for every \(i\), while for \(1\le r<2\) the five homotopy types are
\[
\bigvee^6S^1,\quad \bigvee^6S^1,\quad \bigvee^5S^1,\quad \bigvee^6S^1,\quad \bigvee^4S^1,
\]
and for \(2\le r<3\) they are
\[
\bigvee^2S^2,\quad S^2,\quad S^2,\quad S^2,\quad S^2.
\]
For every \(i\), \(\operatorname{VR}_{\le r}(G_i)\) is contractible for \(r\ge3\).

## Assumptions and scope
Graphs are finite, simple, and unweighted. Distances are shortest-path distances with every edge of length one. The Rips convention is inclusive. The graph6 strings fix the labeled representatives; the theorem itself is invariant under graph isomorphism.

The completeness statement is specifically for asymmetric cubic Hamiltonian graphs on twelve vertices. It uses the published count of exactly five such isomorphism classes together with an independent exact check that the five listed representatives are pairwise nonisomorphic and have the required properties.

## Proof
The graph6 strings decode to connected graphs on twelve vertices with eighteen edges and degree three at every vertex. Exact backtracking finds a Hamiltonian cycle in each graph. A full graph-isomorphism backtracking computation finds exactly one automorphism of each graph and no isomorphism between any two of the five representatives. Thus the five representatives are pairwise nonisomorphic asymmetric cubic Hamiltonian graphs. The published count of five such isomorphism classes proves exhaustion of the class.

For each graph, breadth-first search computes the complete integer distance matrix. Therefore the Rips filtration can change only at integer thresholds. Every one of the \(2^{12}-1=4095\) nonempty vertex subsets is tested directly for diameter at most \(1\), \(2\), and \(3\).

At each nontrivial threshold, a staged vertex-toggle matching is formed on the nonempty face poset. For a chosen vertex \(v\), whenever both an unmatched face \(\sigma\) not containing \(v\) and \(\sigma\cup\{v\}\) are present, those two faces are paired; the process is repeated through the fixed vertex order. Every asserted matching is then verified on the complete Hasse diagram: every pair is a cover relation, no face occurs twice, matched cover relations are oriented upward, unmatched covers downward, and a complete topological sort confirms that the oriented Hasse graph is acyclic.

The critical-cell counts are as follows. At radius \(1\), the five matchings leave one critical \(0\)-cell and respectively \(6,6,5,6,4\) critical \(1\)-cells. At radius \(2\), the first graph leaves one critical \(0\)-cell and two critical \(2\)-cells, while each of the other four leaves one critical \(0\)-cell and one critical \(2\)-cell. At radius \(3\), every graph has a matching leaving only one critical \(0\)-cell. Forman's discrete-Morse theorem therefore gives exactly the sphere wedges stated above; with only a critical \(0\)-cell the complex is contractible.

The first graph has diameter \(3\), so its radius-3 complex is already the full simplex. The other four graphs have diameter \(4\); their radius-3 complexes are contractible and remain unchanged for \(3\le r<4\), while radius \(4\) is the full simplex. Hence all five filtrations are contractible from radius \(3\) onward.

## Verification
`verify.py` uses only the Python standard library. It decodes all five graph6 strings, verifies connectedness, cubicity, Hamiltonicity, trivial automorphism groups, and pairwise nonisomorphism; computes all-pairs distances; exhaustively reconstructs every Rips face at radii \(1,2,3\); verifies the stated face vectors and Hasse-cover counts; builds the staged matchings; and topologically sorts each complete oriented Hasse diagram.

The radius-1 face counts are \(31,31,32,31,33\), the radius-2 face counts are \(189,186,142,186,150\), and the radius-3 face counts are \(4095,3071,1535,3071,2303\). Running `python3 verify.py` ends with `VERIFY_OK`.

## Relationship to prior work
Saleh, Titz Mite, and Witzel define the same inclusive Vietoris--Rips convention and determine complete filtrations for the vertex sets of the five Platonic solids. Their paper emphasizes the value of complete calculations in highly structured finite metric spaces and explicitly points to broader polyhedral generalizations, but its theorem does not cover these asymmetric cubic graph metrics.

Brewer, Gregory, Jones, Florez, and Narayan study asymmetric graphs and state that among the eighty cubic Hamiltonian graphs on twelve vertices exactly five are asymmetric. That result supplies the natural finite class exhausted here, but it does not compute Vietoris--Rips complexes.

Exact searches under the terms “Frucht graph”, “asymmetric cubic Hamiltonian”, “graph-metric Rips”, the five graph6 encodings, and equivalent clique-complex/graph-power language found no checked source stating this five-graph filtration. The closest inspected results concern Platonic-solid Rips complexes, a truncated-tetrahedron graph metric, a truncated-cube scale, projective-plane incidence graphs, and hypercube Rips complexes; none implies the present class-wide statement.

## Limitations
The theorem concerns graph shortest-path distance, not a Euclidean embedding of any drawing of these graphs. It does not classify Rips filtrations of all cubic graphs on twelve vertices, all asymmetric cubic graphs, or larger asymmetric Hamiltonian graphs. The class-exhaustion step relies on the published exact count of five asymmetric cubic Hamiltonian graphs on twelve vertices; the accompanying verifier independently checks that the five listed representatives realize five distinct classes but does not regenerate all eighty cubic Hamiltonian graphs. As with any literature search, an unindexed or differently phrased prior computation remains possible.

## References
1. A. Brewer, A. Gregory, Q. Jones, R. Florez, D. A. Narayan, *Infinite Families of Asymmetric Graphs*, arXiv:1811.11655v1, 2018-11-28.
2. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris--Rips complexes of Platonic solids*, arXiv:2302.14388v1, 2023-02-28; *Innovations in Incidence Geometry* 21 (2024), 17--31, DOI 10.2140/iig.2024.21.17.
