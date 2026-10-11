# The three-rung ladder Morse complex is a mixed-dimensional sphere wedge
## Finding
Let \(L_3=P_3\mathbin{\square}K_2\) be the three-rung ladder graph. For its ordinary Morse complex \(\mathcal M(L_3)\) of acyclic discrete vector fields, \[\mathcal M(L_3)\simeq \bigvee^{2}S^{3}\vee\bigvee^{2}S^{4}.\]

The graph \(L_3\) has six vertices and seven edges. In the standard ladder labeling used by the verifier, the top path is \(0-1-2\), the bottom path is \(3-4-5\), and the rungs are \(0-3\), \(1-4\), and \(2-5\).

## Assumptions and scope
For a finite graph \(G\), a primitive discrete vector field is a pair \((v,e)\) in which the vertex \(v\) is incident to the edge \(e\). A discrete vector field is a compatible set of such pairs, meaning that no graph cell occurs in two pairs. Orienting a paired edge away from its paired vertex identifies a compatible field with a directed subforest exactly when it has no closed \(V\)-path. The ordinary Morse complex \(\mathcal M(G)\) is the simplicial complex whose vertices are primitive discrete vector fields and whose simplices are the nonempty acyclic compatible fields.

The claim is only for the graph \(L_3=P_3\mathbin{\square}K_2\). No uniform assertion for all ladder graphs is made.

## Proof
There are \(14\) primitive vector fields, two orientations for each of the seven graph edges. Exhaustive enumeration of all compatible acyclic fields gives \(575\) nonempty simplices with face vector
\[
(14,74,184,213,90).
\]
The package reconstructs this set twice: once by scanning all subsets of the \(14\) primitive vector fields, and independently by scanning the \(3^7\) states in which each graph edge is unused or assigned one of its two orientations. The two enumerations agree exactly.

On the complete face poset, apply the deterministic repeated-toggle matching in primitive-index order
\[
12,10,3,5,13,4,1,11,6,0,2,9,7,8.
\]
Whenever both are still unmatched, a face not containing the current primitive is paired with the face obtained by adjoining it. This produces \(285\) matched Hasse covers. The verifier reconstructs all \(2002\) Hasse covers, reverses precisely the matched covers, and topologically sorts the resulting directed graph, proving that the matching is acyclic.

Exactly five critical simplices remain: one in dimension \(0\), two in dimension \(3\), and two in dimension \(4\). Therefore Forman's theorem yields a CW complex with one \(0\)-cell, two \(3\)-cells, and two \(4\)-cells. Its \(3\)-skeleton is \(S^3\vee S^3\).

The verifier then computes the signed integral Morse differential from the two critical \(4\)-cells to the two critical \(3\)-cells by exact gradient-path elimination. In the displayed critical-cell bases it is
\[
\partial_4=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
\]
Because \(S^3\vee S^3\) is \(2\)-connected, Hurewicz identifies \(\pi_3(S^3\vee S^3)\) with \(H_3(S^3\vee S^3;\mathbb Z)\cong\mathbb Z^2\). Thus the two attaching maps of the critical \(4\)-cells are determined by the two degree vectors recorded by \(\partial_4\). Both vectors vanish, so both attaching maps are null-homotopic. This proves
\[
\mathcal M(L_3)\simeq S^3\vee S^3\vee S^4\vee S^4.
\]

## Verification
`verify.py` reconstructs the graph and the full Morse complex without external packages. It checks the two independent simplex enumerations, the face vector, every Hasse cover, matching uniqueness, global acyclicity, the critical-cell profile, and the exact signed Morse differential. As cross-checks, direct simplicial boundary elimination over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) gives the same Betti vector
\[
(1,0,0,2,2)
\]
for all three fields. The machine-readable certificate records the primitive indexing, all matching pairs, critical faces, the zero integral Morse differential, and the matching digest.

## Relationship to prior work
Scoville and Zaremsky define the same Morse complex and emphasize that exact homotopy types are known only in a limited set of cases; their graph theorem supplies general connectivity bounds rather than this ladder computation. Their first public arXiv version is dated 2020-04-22 and lists primary MSC \(55U05\).

Kozlov's earlier computations cover paths, cycles, and complete graphs, as summarized in the current literature. Donovan, Lin, and Scoville treat leaf-based and tree families, while Donovan and Scoville later treat extended stars and paths. The ladder \(L_3\) has minimum degree \(2\), contains two cycles, and is neither a path, cycle, complete graph, nor tree.

A separate shellability theorem of Jojić applies to directed-forest complexes with a dominant pair of vertices. Under the standard identification of a graph Morse complex with the directed-forest complex of its double orientation, the verifier checks directly that the double-oriented \(L_3\) has no dominant pair, so that theorem does not imply the present wedge decomposition. Exact searches under the aliases “three-rung ladder,” “domino graph,” and \(P_3\mathbin{\square}K_2\) located no statement of this Morse-complex homotopy type.

## Limitations
The result is an exact finite statement for the first ladder beyond the four-cycle, not a recurrence or closed formula for \(P_n\mathbin{\square}K_2\). The originality assessment is relative to the inspected primary literature and scientific-index searches; a differently indexed or unpublished computation remains a residual risk. The mod-prime homology calculations are cross-checks only; the homotopy conclusion uses the globally verified acyclic matching and the exact integral Morse differential.

## References
1. N. A. Scoville and M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481, first public version 2020-04-22.
2. C. Donovan, M. Lin, and N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440, 2019.
3. C. Donovan and N. A. Scoville, *Star clusters in the Matching, Morse, and Generalized Morse complex*, arXiv:2207.13780, 2022.
4. D. Jojić, *Complexes of directed trees of complete multipartite graphs*, Publ. Inst. Math. 92(106) (2012), 43–51, DOI 10.2298/PIM1206043J.
5. N. A. Scoville, *The complex of discrete Morse matchings of the \(n\)-simplex: homotopy types and structural results*, arXiv:2604.18172, 2026.
6. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
