# The three-sun graph has a 27-sphere discrete-Morse complex

## Finding
Let \(S_3\) be the **three-sun graph**: start with the triangle on vertices \(0,1,2\); add mutually nonadjacent vertices \(3,4,5\), joining \(3\) to \(0,1\), \(4\) to \(1,2\), and \(5\) to \(0,2\). Let \(\mathfrak M(S_3)\) be the ordinary discrete-Morse matching complex of this one-dimensional simplicial graph. Then
\[
\mathfrak M(S_3)\simeq \bigvee^{27}S^4.
\]
This is an integral homotopy equivalence. In particular, \(\widetilde H_4(\mathfrak M(S_3);\mathbb Z)\cong\mathbb Z^{27}\), and all other reduced integral homology groups vanish.

## Assumptions and scope
All graphs are finite, simple and undirected before bidirecting their edges. The graph has six vertices and nine edges. A vertex of \(\mathfrak M(S_3)\) is a vertex–edge incidence \((u,\{u,v\})\) of \(S_3\); this corresponds to an arrow from \(u\) to \(v\). A nonempty set of incidences is a simplex exactly when no graph vertex or edge participates in more than one incidence and these arrows are cycle-free. The choice of pointing toward or away from roots is immaterial for this bidirected graph, since reversing all arrows is an isomorphism. This is the rooted-forest definition of the discrete-Morse complex for graphs, not the ordinary graph-edge matching complex.

## Proof
Number the 18 incidence vertices by listing the nine graph edges in ascending lexicographic order, and listing the two endpoints of each edge in ascending order. The exact order of those incidence labels is determined by the standalone verifier. Two exhaustive face generators are used: (a) choose for each graph vertex either no outgoing arrow or one arrow to a neighbor, rejecting a directed cycle; (b) choose for each graph edge either no arrow or one of its two orientations, rejecting repeated arrow sources and directed cycles. They produce identical sets of 1,444 nonempty faces, whose counts in dimensions zero through four are respectively
\[
(18,123,394,585,324).
\]

On this complete face set, perform the following greedy element-matching procedure, using the 18 incidence indices
\[
(13,0,9,17,5,3,4,15,6,2,14,16,12,8,1,11,10,7).
\]
For each index \(j\) in this order, pair every still-unmatched face \(\sigma\) not containing vertex \(j\) with \(\sigma\cup\{j\}\), whenever both faces are still unmatched. Remove both from further matching stages. This gives precisely 708 disjoint codimension-one pairs. The remaining critical faces consist of one zero-simplex and 27 four-simplices, with no others.

For acyclicity, take **every** codimension-one incidence in the Hasse diagram of the complete face poset. Direct unmatched incidences from higher-dimensional to lower-dimensional face and reverse every matched incidence. The verifier constructs all 5,388 such directed incidences and deletes vertices by a zero-indegree queue. All 1,444 face-vertices are deleted, proving that the directed Hasse graph has no directed cycle. The pairs therefore form an acyclic discrete-Morse matching in Forman's sense. The resulting CW model has exactly one zero-cell and 27 four-cells, with no cells in dimensions one through three; each four-cell attaches to the zero-skeleton via a constant map. Thus the CW model, and hence the original complex, is a wedge of 27 four-spheres.

## Verification
The attached standalone Python 3 script `verify_three_sun_morse.py` uses no external packages. It independently generates the simplices in two ways, checks the entire Hasse directed graph for acyclicity, and computes the binary ranks of the simplicial boundaries. In degrees one through four these ranks are
\[
(17,106,288,297),
\]
which give mod-two fourth Betti number 27 and all other reduced mod-two Betti numbers zero. The Euler characteristic is 28; the independent integral determinant calculation of \(I-L(S_3)\) gives \(-27\), consistent with the matrix–forest identity \(\chi=1-\det(I-L)\). Neither field ranks nor Euler characteristic are used to infer the integral homotopy type; the acyclic matching proves it.

## Relationship to prior work
Chari and Joswig (2000, Section 3) identify the discrete-Morse complex of a graph with its rooted-forest complex and relate its face numbers to the graph Laplacian. Celoria and Yerolemou (first public version 2020, Section 2 and Table 2) compute filtered complexes for complete graphs, including the complete graph on five vertices, but not the three-sun graph. Donovan and Scoville (2022) treat paths, extended stars, cycles and related complexes, not this sun graph. Jojić (2012, Theorem 2.1 and Section 3) proves a shellability theorem for directed graphs with a dominant pair and an exact result for complete multipartite graphs. The bidirected three-sun has neither a complete source nor a dominant pair and is not complete multipartite, as checked exhaustively by the verifier. These results therefore do not imply its homotopy type. Calculations for other specifically named graph Morse complexes concern different input graphs; equal sphere dimensions or counts do not imply isomorphic constructions.

## Limitations
The homotopy equivalence concerns exactly the six-vertex three-sun, not the full family of \(k\)-sun graphs or arbitrary chordal graphs. The independent matrix–forest identity already fixes the Euler characteristic, so only the integral homotopy concentration is new. Literature indexing is incomplete; an equivalent unindexed computation is possible. No shellability, equivariant homology, or persistence statement is claimed.

## References
- M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234, https://arxiv.org/abs/math/0011234 (first public 2000-11-28; Section 3).
- D. Celoria and N. Yerolemou, *Filtered matchings and simplicial complexes*, arXiv:2011.02015, https://arxiv.org/abs/2011.02015 (first public 2020-11-03; Sections 1–2, Table 2).
- C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, https://arxiv.org/abs/2207.13780 (first public 2022-07-27; Sections 1–3).
- D. Jojić, *Complexes of directed trees of complete multipartite graphs*, *Publ. Inst. Math.* 92 (2012), 43–51, https://doi.org/10.2298/PIM1206043J (Section 2, Theorem 2.1, and multipartite result).
