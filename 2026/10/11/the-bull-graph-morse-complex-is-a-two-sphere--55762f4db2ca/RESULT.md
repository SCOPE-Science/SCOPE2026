# The bull-graph Morse complex is a two-sphere
## Finding
Let \(B\) be the bull graph: start with the triangle \(v_0v_1v_2v_0\), attach a pendant vertex \(v_3\) to \(v_0\), and attach a pendant vertex \(v_4\) to \(v_1\). For the ordinary Morse complex of acyclic discrete vector fields on this graph,
\[
\mathcal M(B)\simeq S^2.
\]

Thus two leaves attached at distinct vertices can produce a noncontractible Morse complex, in contrast with the known strong-collapsibility theorem for two leaves sharing one support vertex.

## Assumptions and scope
The graph is the five-vertex simple graph with edge set
\[
\{v_0v_1,v_1v_2,v_2v_0,v_0v_3,v_1v_4\}.
\]
A vertex of \(\mathcal M(B)\) is a primitive discrete vector field \((v,e)\), where \(v\) is an endpoint of the edge \(e\). A simplex is a collection of primitive fields in which no cell is used twice and there is no nontrivial closed \(V\)-path. For a graph, this is equivalently a partial orientation in which every vertex is the tail of at most one selected edge, no underlying edge is selected twice, and there is no directed cycle.

The claim is only for the ordinary Morse complex of this bull graph. It does not assert a formula for all unicyclic graphs with leaves, generalized Morse complexes, or pure Morse complexes.

## Proof
The five graph edges have two possible primitive fields each, so \(\mathcal M(B)\) has ten vertices. Exhaustively enumerating compatible acyclic partial orientations gives the complete nonempty face vector
\[
(f_0,f_1,f_2,f_3)=(10,33,40,15),
\]
so there are \(98\) nonempty faces.

The enumeration is independently reconstructed by letting each of the five graph vertices choose either no outgoing edge or one incident outgoing edge, then rejecting choices that reuse an underlying edge or create a directed cycle. The two constructions give the same face set and face vector.

Order the ten primitive fields lexicographically by graph edge and chosen tail. On the nonempty face poset, process them in that order and at each stage pair every still-unmatched face \(\sigma\) not containing the current primitive field \(p\) with \(\sigma\cup\{p\}\) whenever that coface is present and still unmatched. This produces \(48\) matched pairs. The complete Hasse diagram has \(246\) cover relations. Reverse the matched covers and direct every unmatched cover downward; exhaustive topological sorting of this directed Hasse graph proves the matching acyclic.

Exactly two cells remain critical: one \(0\)-cell and one \(2\)-cell. Forman's acyclic-matching theorem therefore gives a CW complex homotopy equivalent to \(\mathcal M(B)\) with one point and one \(2\)-cell attached to that point. Its homotopy type is \(S^2\).

## Verification
Run `python3 verify_bull_morse.py`. The standalone script uses only the Python standard library. It reconstructs the bull graph and all primitive fields, exhaustively enumerates the entire Morse complex in two independent ways, verifies all \(246\) Hasse covers, rebuilds the \(48\)-pair matching, and proves acyclicity by a full topological sort.

As an independent homological cross-check, the signed simplicial boundary matrices have ranks
\[
(9,24,15)
\]
over each of \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\). Hence the Betti vector over each of those fields is \((1,0,1,0)\), consistent with the discrete-Morse proof. These finite-field computations are checks, not substitutes for the homotopy proof.

## Relationship to prior work
Donovan, Lin, and Scoville prove that if a simplicial complex has two leaves sharing a common vertex, then its Morse complex is strongly collapsible and therefore contractible. Their exact graph calculations also include the one-leaf cycle family and the construction obtained by attaching a leaf to every vertex of a graph. The bull graph lies immediately outside all three cases: its two leaves have distinct support vertices, it has two rather than one leaf, and one triangle vertex has no attached leaf.

For comparison, their one-leaf cycle formula makes the Morse complex of a triangle with one attached leaf contractible. The present calculation therefore isolates a small structural boundary: placing a second leaf at a different triangle vertex changes the Morse complex to a two-sphere. Scoville and Zaremsky give general connectivity results for Morse complexes of graphs, but those bounds do not determine this exact homotopy type.

## Limitations
This is an exact result for one natural named graph and serves as a boundary example for a published leaf-configuration theorem. No family-wide classification is claimed. Exact and alias searches did not locate a published bull-graph Morse-complex computation, but an obscure equivalent computation under substantially different directed-forest terminology remains a residual bibliographic risk.

## References
1. C. Donovan, M. Lin, and N. A. Scoville, “On the homotopy and strong homotopy type of complexes of discrete Morse functions,” arXiv:1909.11440, first public 2019-09-25; DOI 10.4153/S0008439522000121.
2. N. A. Scoville and M. C. B. Zaremsky, “Higher connectivity of the Morse complex,” arXiv:2004.10481, first public 2020-04-22; DOI 10.1090/bproc/115.
