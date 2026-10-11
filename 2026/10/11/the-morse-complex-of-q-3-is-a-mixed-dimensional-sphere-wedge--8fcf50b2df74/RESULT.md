# The Morse complex of \(Q_3\) is a mixed-dimensional sphere wedge
## Finding
Let \(Q_3\) be the graph on \(\{0,1\}^3\), with two vertices adjacent exactly when they differ in one coordinate. Let \(\mathcal M(Q_3)\) denote the ordinary Morse complex whose vertices are primitive discrete vector fields and whose simplices are acyclic compatible collections. Then
\[
\mathcal M(Q_3)\simeq \bigvee^{4}S^{5}\vee\bigvee^{139}S^{6}.
\]
In particular,
\[
\widetilde H_5(\mathcal M(Q_3);\mathbb Z)\cong\mathbb Z^4,
\qquad
\widetilde H_6(\mathcal M(Q_3);\mathbb Z)\cong\mathbb Z^{139},
\]
and all other reduced integral homology groups vanish.

## Assumptions and scope
A primitive vector field on a graph pairs a vertex with an incident edge. Encode such a pair as a directed edge from the paired vertex toward the other endpoint. Compatibility means that no graph vertex is used as a tail twice and no undirected graph edge is used twice. For graphs, a nontrivial closed \(V\)-path is exactly a directed cycle, so a simplex of \(\mathcal M(Q_3)\) is exactly an acyclic partial orientation satisfying those compatibility conditions.

The statement concerns the ordinary Morse complex of the three-dimensional cube graph only. It does not assert a formula for \(Q_n\) for \(n>3\).

## Proof
The cube has eight graph vertices, twelve graph edges, and twenty-four primitive discrete vector fields. Exhausting the three states of each graph edge—absent or oriented in either direction—and retaining precisely the compatible acyclic states gives \(23{,}624\) nonempty simplices with face vector
\[
(24,240,1296,4080,7488,7424,3072).
\]
An independent rooted-forest count gives the same numbers: a forest with component sizes \(s_1,\ldots,s_r\) contributes \(s_1\cdots s_r\) orientations toward chosen roots.

Now process the twenty-four primitive vector fields in a fixed order. At each stage, match every still-unmatched face \(F\) not containing the current primitive \(p\) with \(F\cup\{p\}\) whenever the latter is a face and is still unmatched. The resulting matching has \(11{,}700\) pairs. Direct orientation of every Hasse cover relation, reversing exactly the matched covers, is acyclic. Its critical cells consist of one \(0\)-cell, forty-four \(5\)-cells, and one hundred seventy-nine \(6\)-cells, with no critical cells in dimensions \(1\) through \(4\).

Forman's theorem therefore gives a CW complex homotopy equivalent to \(\mathcal M(Q_3)\) with exactly those cells. The signed gradient-path boundary from the critical \(6\)-cells to the critical \(5\)-cells is an integer \(44\times179\) matrix with \(195\) nonzero entries, every one equal to \(1\) or \(-1\). Exact rational elimination gives rank \(40\). A specified \(40\times40\) minor has determinant \(1\), so every nonzero Smith invariant factor is a unit. Thus, after integral basis changes, the attaching matrix is
\[
\operatorname{diag}(I_{40},0).
\]

The \(5\)-skeleton of the Morse CW complex is \(\bigvee^{44}S^5\). It is \(4\)-connected, so the Hurewicz isomorphism identifies \(\pi_5\) with \(H_5\); consequently each \(6\)-cell attaching map is completely classified by its integer degree vector. Row and column basis changes correspond to homotopy self-equivalences and cell slides. Forty unit attachments cancel forty \(5\)-/\(6\)-cell pairs, while the remaining one hundred thirty-nine \(6\)-cells attach trivially. Four \(5\)-spheres remain, proving the displayed wedge decomposition.

## Verification
Run `python3 artifacts/verify_cube_morse_wedge.py`. The standard-library verifier reconstructs \(Q_3\), exhausts all \(3^{12}\) edge states, independently checks the rooted-forest face count, constructs the full toggle matching, and checks acyclicity of the complete matched Hasse orientation. It then reconstructs the signed algebraic-Morse boundary, verifies its exact rational rank \(40\), verifies rank \(40\) modulo \(2\) and \(3\), and checks a \(40\times40\) determinant-one minor. Success ends with `CUBE_MORSE_WEDGE_VERIFY_OK`.

As an external cross-check, the previously published exact mod-\(2\) computation for this same Morse complex reports the same face vector and reduced Betti ranks \(4\) and \(139\). The present argument adds integral Smith information and the attaching-map analysis needed for the full homotopy type.

## Relationship to prior work
Donovan, Lin, and Scoville compute exact Morse-complex homotopy types for several graph families. Their searchable full text has no occurrence of “cube.” Scoville and Zaremsky explicitly discuss the hypercube family \(Q_n\): their Example 4.8 gives a connectivity bound, while the paper states that precise Morse-complex homotopy types are known only in a small number of examples. For \(Q_3\), that connectivity result does not determine the two nonzero top-dimensional groups or the attaching maps.

A published exact computation for this same object establishes only reduced mod-\(2\) homology, with ranks \(4\) in degree \(5\) and \(139\) in degree \(6\), and explicitly leaves integral homology and full homotopy type unresolved. The wedge decomposition here strictly strengthens that statement. Contreras and Tawfeek's Laplacian generating-function theorem explains the rooted-forest face count but does not determine the Morse differential or homotopy type.

Courtney's thesis on directed forest complexes of Cayley graphs is a plausible terminology-adjacent source because \(Q_3\) is a Cayley graph. Its public abstract was inspected; the linked full text was not accessible during comparison, so possible additional overlap remains a bibliographic risk rather than being asserted away.

## Limitations
The result is a complete homotopy-type calculation only for \(Q_3\). It does not provide a recurrence or stable pattern for higher hypercubes. The proof relies on a finite exact matching and its signed Morse boundary; the included verifier replays both from definitions, but the result is not presented as a classification theorem for all graphs. Literature searches cannot prove global novelty, and the inaccessible full text of the directed-forest thesis remains the principal source-coverage risk.

## References
1. C. Donovan, M. Lin, N. A. Scoville, *On the homotopy and strong homotopy type of complexes of discrete Morse functions*, arXiv:1909.11440v1, first public 2019-09-25.
2. N. A. Scoville, M. C. B. Zaremsky, *Higher connectivity of the Morse complex*, arXiv:2004.10481v1, first public 2020-04-22; primary classification 55U05.
3. I. Contreras, A. R. Tawfeek, *On discrete gradient vector fields and Laplacians of simplicial complexes*, arXiv:2105.05388v1, first public 2021-05-12.
4. published-finding corpus record `2026/10/4/SCOPE-mod-2-homology-of-the-cube-graph-morse-complex-is-concentrated-i--3861de13b7e0`, *Mod-\(2\) homology of the cube-graph Morse complex is concentrated in degrees \(5\) and \(6\)*.
5. K. Courtney, *The Directed Forest Complex of Cayley Graphs*, DOI:10.18122/td/1684/boisestate, 2020.
