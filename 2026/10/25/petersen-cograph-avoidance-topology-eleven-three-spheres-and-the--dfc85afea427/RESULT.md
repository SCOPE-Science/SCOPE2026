# Petersen cograph-avoidance topology: eleven three-spheres and the full \(S_5\)-character

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph: its ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), and two are adjacent if they are disjoint. Let \(K\) be the simplicial complex of subsets \(U\subseteq V(P)\) such that the induced graph \(P[U]\) has no induced four-vertex path \(P_4\). Equivalently, \(K\) is the *cograph-inducing* (four-vertex-path-devoid) complex of \(P\). Then
\[
K\simeq\bigvee^{11} S^3,
\qquad
\widetilde H_i(K;\mathbb Z)\cong
\begin{cases}\mathbb Z^{11},&i=3,\\0,&i\ne3.\end{cases}
\]
For the natural action of \(\operatorname{Aut}(P)\cong S_5\), the rational reduced homology has the complete character and irreducible decomposition
\[
\widetilde H_3(K;\mathbb Q)
\cong S^{(3,1,1)}\oplus S^{(2,1,1,1)}\oplus S^{(1,1,1,1,1)},
\]
where \(S^\lambda\) denotes the rational Specht module indexed by partition \(\lambda\). The character values on cycle types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), in that order, are \((11,-3,-1,2,0,-1,1)\). In particular, the full symmetric group fixes no nonzero rational reduced-homology class, while its sign character occurs exactly once.

## Assumptions and scope
The graph is exactly the ten-vertex Petersen graph, not the triangular graph (its complement). All complexes and homotopy statements are ordinary, non-equivariant simplicial complexes with their geometric realizations; the homology representation is over \(\mathbb Q\). The complex is defined by *induced* forbidden four-vertex paths. Because the Petersen graph has girth five, a path on four vertices has no chord in the Petersen graph, so induced-path avoidance agrees with ordinary four-vertex-path avoidance here. The permitted induced subgraphs are exactly disjoint unions of stars (isolated vertices count as trivial stars): a connected triangle-free cograph is complete bipartite, and the absence of four-cycles makes it a star.

This construction is motivated by the forbidden-path topology introduced for devoid complexes: forbidding \(P_4\) imposes cograph structure rather than the more restrictive matching/independence conditions. The Petersen graph is a canonical smallest highly symmetric cubic graph of girth five and is neither a path nor a cycle; both its full integral homotopy type and its automorphism representation therefore probe a case outside the earlier path/cycle classifications.

## Proof
**Exact face model.** Order the ten vertices lexicographically as \((01),(02),(03),(04),(12),(13),(14),(23),(24),(34)\), with indices \(0,\ldots,9\). Represent a vertex set by its ten-bit mask. Among the fifteen graph edges, exactly sixty distinct four-vertex masks induce a path: each such quadruple has three graph edges and induced degree multiset \((1,1,2,2)\). A mask is a face if and only if it contains none of these sixty masks. Testing all \(2^{10}=1024\) masks gives \(391\) faces including the empty face, hence \(390\) nonempty faces, with dimensional face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(10,45,120,150,60,5).
\]
There are ten three-dimensional facets, thirty four-dimensional facets, and five five-dimensional facets. A second verifier enumerates induced paths directly from graph adjacency, giving the same face predicate for all \(1024\) masks.

**Explicit acyclic matching.** Start with the nonempty face set unmatched. For pivots \(v=0,1,\ldots,9\), pair every still-unmatched face \(A\) not containing \(v\) with \(A\cup\{v\}\) if the latter is still unmatched; process candidates in increasing mask order and remove both faces immediately. This creates exactly \(187\) disjoint codimension-one pairs. The remaining critical cells comprise one vertex, thirteen three-cells, and two four-cells. Orient each of the \(1380\) nonempty codimension-one incidences downward, reversing each matched incidence. An exhaustive indegree-zero topological sort visits all \(390\) face-nodes. The resulting gradient digraph is therefore acyclic, as required by Forman's discrete Morse theory.

**Integral attaching degrees.** Use increasing-label simplex orientations. For each paired lower/upper cell, eliminate the corresponding integral incidence by a chain-level elementary cancellation, including its effects on all other current boundary columns. All \(187\) pivots are \(\pm1\); therefore the resulting Morse chain complex is integrally chain-equivalent to the simplicial chains. With critical three-cells ordered by increasing masks and critical four-cells likewise, its sole possible nontrivial boundary is
\[
\partial_4=\begin{pmatrix}
0&0\\0&1\\0&0\\1&0\\-1&0\\0&-1\\1&1\\0&0\\1&1\\0&1\\-1&-1\\1&0\\0&0
\end{pmatrix}.
\]
Rows two and four of this matrix form a \(2\times2\) minor with determinant \(-1\); hence the two attaching vectors span a primitive rank-two summand of \(\mathbb Z^{13}\). The Morse CW complex has a point as its zero-skeleton, no one- or two-cells, thirteen three-cells, and two four-cells. Its three-skeleton is \(\bigvee^{13}S^3\), whose \(\pi_3\) is exactly its third integral homology. The primitive rank-two attaching matrix can therefore be reduced by integral basis changes (realizable by homotopy equivalences of the three-skeleton and cell slides) to two standard generators. The resulting cancelling three/four-cell pairs leave \(\bigvee^{11}S^3\). This proves the integral *homotopy* assertion, not merely its homology ranks.

**Full symmetry character.** Each permutation of the five labels permutes the ten graph vertices and hence the oriented simplices of \(K\). For each of all \(120\) permutations, enumerate the invariant simplices; one fixed oriented simplex contributes the sign of its induced vertex permutation. The alternating signed trace over nonempty simplices is the ordinary Lefschetz number \(L(g)\). As the only unreduced homology is \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^{11}\), we have \(L(g)=1-\chi_3(g)\). The seven class traces stated in the finding result. Exact Murnaghan–Nakayama calculations and the \(S_5\) character inner product give multiplicity one for the three stated partitions and zero for the others.

## Verification
The complete standard-library verifier `evidence/verify_petersen_cograph.py` reconstructs the graph, verifies the forbidden-path test in two independent ways, checks every simplex and facet, exhaustively checks the matching's acyclicity across all \(1380\) face incidences, performs all integer Morse cancellations, checks the displayed boundary and unit minor, recomputes the simplicial boundary ranks directly over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_{13}\), and verifies the character on all \(120\) permutations and its irreducible decomposition. In every tested characteristic the direct simplicial boundary ranks from degrees one through five are \((9,36,84,55,5)\). Run `python3 evidence/verify_petersen_cograph.py`; its checked output is provided in `evidence/verification_output.txt` and ends `VERIFY_OK`.

The finite enumeration is exhaustive because there are exactly \(1024\) vertex subsets, not a partial sampling. The homotopy theorem uses the acyclic matching and actual attaching-degree matrix, not field homology alone.

## Relationship to prior work
Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs* (arXiv:1501.06754, first submitted 27 January 2015), defines these forbidden-subgraph complexes and calculates their homotopy types for paths and cycles (Theorems 3.10 and 5.2) and for three-vertex-path avoidance in forests (Theorem 3.14). None of those graph-family assumptions includes the Petersen graph; nor do these theorems give its \(P_4\)-devoid \(S_5\)-module. The earlier theory of cographs and \(P_4\)-sparse graphs supplies structural motivation, not this homotopy classification.

There are two particularly close but mathematically distinct publicly recorded calculations. The Petersen **two-independence** complex allows only components of size at most two: it has \(260\) nonempty faces and is homotopy equivalent to \(S^3\). It embeds properly in the present \(390\)-face cograph complex, but its one-dimensional top homology does not determine the latter's eleven-dimensional homology. The **four-cut complex** of the complementary triangular graph \(J(5,2)\) also has homotopy type \(\bigvee^{11}S^3\), but it is pure five-dimensional with ten facets and its \(S_5\) character is \((11,-1,3,-1,-1,-1,1)\), not the character \((11,-3,-1,2,0,-1,1)\) here. Its disconnected-quadruple definition is not the present forbidden-path definition, and the published implication does not cover this different complex. Related Petersen matching, Morse and cut complexes likewise have different ground sets or face predicates.

## Limitations
This is a complete classification for this specific graph and induced forbidden pattern, not a formula for other Kneser graphs or forbidden paths. The representation statement is rational: no integral \(\mathbb Z[S_5]\)-lattice decomposition or equivariant homotopy equivalence is asserted. The original published literature comparison and indexed-record comparison do not rule out unindexed equivalent prior work. The provided executable supplies a finite exact proof for the specified graph; it does not provide a general theory of arbitrary cograph-devoid complexes.

## References
- Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1 (first public 27 January 2015), Sections 3 and 5.
- Andreas Brandstädt and Raffaele Mosca, *On Variations of \(P_4\)-Sparse Graphs*, Discrete Applied Mathematics 129 (2003), 521–532, DOI:10.1016/S0166-218X(03)00180-X.
- Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
- *The Petersen Two-Independence Complex Is a Three-Sphere* (public mathematical result, 2026; direct full-result comparison).
- *Eleven Three-Spheres and the Symmetric-Group Character of a Four-Cut Complex* (public mathematical result, 2026; direct full-result comparison).
