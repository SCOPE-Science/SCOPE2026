# Six fifth-dimensional spheres and irreducible symmetry in the Petersen induced-forest complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph on the ten two-element subsets of \([5]\), with two vertices adjacent exactly when disjoint. Let
\[
\mathcal F(P)=\{A\subseteq V(P):P[A]\text{ has no cycle}\}
\]
be its **induced-forest complex**, also known as the acyclic vertex-subset complex or the terminal forest-filtration complex. Then there is an integral homotopy equivalence
\[
\boxed{\mathcal F(P)\simeq\bigvee^{6}S^{5}.}
\]
For the natural action of \(\operatorname{Aut}(P)\cong\mathfrak S_5\), let \(V\) denote the four-dimensional rational standard representation (the augmentation subrepresentation of the five-point permutation module). There is an isomorphism of rational representations
\[
\boxed{\widetilde H_5(\mathcal F(P);\mathbb Q)\cong
\bigwedge^{2}V\cong S^{(3,1,1)}.}
\]
All other reduced integral homology groups vanish. In particular the fifth-homology representation is irreducible over \(\mathbb Q\), and the full automorphism group has no nonzero invariant rational homology class.

## Assumptions and scope
All graphs are finite, simple and undirected; forest means an undirected graph with no cycles. The complex has one vertex for each of the ten graph vertices, **not** for each graph edge. Thus it is distinct from the independence complex of the Petersen graphic matroid. All homotopy and integral homology statements concern the geometric realization of the full simplicial complex, including all induced forest vertex sets. The representation statement concerns rational fifth homology under the natural permutation of the five labels.

Ordering the ten graph vertices lexicographically by their two-subsets of \([5]\), encode a face as a ten-bit integer. Exhaustively testing all \(2^{10}=1024\) subsets yields \(786\) faces including the empty face, with nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(10,45,120,210,240,140,20).
\]
There are \(15\) maximal five-simplices and \(20\) maximal six-simplices, so the complex is nonpure. Its minimal nonfaces are exactly the vertex sets of the \(12\) chordless five-cycles and \(10\) chordless six-cycles of \(P\). Equivalently, forestness is tested by excluding those \(22\) subsets; no other minimal nonfaces occur.

## Proof
**Step 1: Complete face enumeration.** The graph vertices are the unordered pairs in \([5]\); an edge joins disjoint pairs. The executable `VERIFY.py` checks the forest predicate in two independent ways. First, it adds all induced graph edges with union-find and rejects an edge closing a cycle. Second, it computes the number of connected components by graph traversal and checks \(|E(P[A])|=|A|-c(P[A])\). They agree for every one of the \(1024\) subsets. The face and facet counts above follow.

**Step 2: An explicit acyclic Morse matching.** Start with all faces (temporarily including the empty face). For pivots \(i=0,\ldots,9\) in order, scan unmatched faces in increasing cardinality and then integer order. Whenever \(i\notin A\) and both \(A\) and \(A\cup\{i\}\) are still unmatched faces, pair and remove them. This produces \(390\) pairs with six remaining faces, all of cardinality six. The unique pair containing the empty face is \((\varnothing,\{0\})\). Discard that pair; on the ordinary nonempty face poset this leaves exactly \(389\) matched pairs and exactly one critical vertex and six critical five-faces.

For every codimension-one relation \(B\subset A\) of nonempty faces, direct the Hasse edge from \(A\) to \(B\), except that a matched edge is directed from \(B\) to \(A\). The verifier enumerates all \(3470\) such edges, constructs this entire directed graph on \(785\) nonempty faces, and performs topological sorting. All \(785\) vertices are removed, proving the matching acyclic. Forman's discrete Morse theorem therefore gives a CW model with one zero-cell and precisely six five-cells, with no cells in dimensions one through four or six. Every attaching map of a five-cell lands in the zero-cell, so this CW model is a wedge of six five-spheres. This proves the claimed **integral homotopy type**, not merely its Euler characteristic.

**Step 3: Equivariant character.** Every permutation \(g\in\mathfrak S_5\) induces a graph automorphism on the two-element subsets and hence a simplicial automorphism of \(\mathcal F(P)\). The classical five largest independent sets of \(P\) are the five stars of two-subsets containing a prescribed label; each graph vertex is the intersection of two stars. Thus every graph automorphism permutes the five stars and is determined by that permutation, proving \(\operatorname{Aut}(P)\cong\mathfrak S_5\).

For a face \(A\) fixed setwise by \(g\), the induced action on its oriented simplex has sign \(\epsilon(g,A)\). With the empty face contributing \(-1\), the reduced simplicial Lefschetz formula and the already-proved homotopy type give
\[
\operatorname{tr}\big(g\mid\widetilde H_5(\mathcal F(P);\mathbb Q)\big)
=-\sum_{\substack{A\in\mathcal F(P)\\gA=A}}
(-1)^{|A|-1}\epsilon(g,A).
\]
The verifier evaluates this expression for **all \(120\) permutations**. In cycle-type order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), the character is
\[
(6,0,-2,0,0,0,1).
\]
For the standard module \(V\), \(\chi_V(g)=\#\operatorname{Fix}_{[5]}(g)-1\). The exterior-square character satisfies
\[
\chi_{\wedge^2V}(g)=\tfrac12\big(\chi_V(g)^2-\chi_V(g^2)\big),
\]
and this agrees element by element with the computed fifth-homology trace. Rational representations of finite groups are semisimple and their characters determine their isomorphism classes, establishing the stated module identification. The squared character norm is exactly one, so this module is irreducible; it is the Specht module \(S^{(3,1,1)}\). Averaging its character gives zero invariant multiplicity.

## Verification
Run `python3 VERIFY.py` with Python 3 and no external packages. The output in `VERIFY_OUTPUT.txt` was generated by executing that exact program. It checks the two forest predicates, the complete face vector and minimal nonfaces, every matched Hasse edge and directed-cycle absence, all mod-two boundary ranks, all \(120\) signed Lefschetz calculations, equality with the exterior-square character, and character irreducibility. The boundary ranks in dimensions one through six over \(\mathbb F_2\) are \((9,36,84,126,114,20)\), independently giving reduced Betti number six in degree five and zero otherwise. This modular calculation is only corroboration; the integral homotopy proof is the explicit acyclic Morse matching.

## Relationship to prior work
Taylan's 2015 publicly available preprint introduces general matching-tree techniques for devoid complexes and studies, among others, forbidden paths in path and cycle graphs. It does **not** state the Petersen induced-forest classification. Barton, Brown and Pike (first arXiv version 2020) define the acyclic polynomial whose coefficients count exactly the faces here, but do not give this homotopy type or representation. Carnero Bravo's forest-filtration study (first arXiv version 2023) treats paths, cycles, double stars, cacti and graph operations; its displayed classifications do not specialize to this Petersen graph.

A different Petersen **three-cut** complex has already been found to carry the same irreducible \(S^{(3,1,1)}\) in sixth homology, and an **edge-set graphic-matroid forest** complex of the Petersen graph has also been studied. Neither is the induced vertex-subset forest complex: their faces, dimensions and allowable obstructions differ. The coincidence of representation type does not by itself imply a homotopy equivalence or determine the present homology. Targeted comparison found no existing statement implying both results asserted here.

## Limitations
The calculation is specific to \(P=\operatorname{KG}(5,2)\), not an assertion for all cubic, vertex-transitive or girth-five graphs. It does not determine an integral decomposition of the \(\mathbb Z[\mathfrak S_5]\)-lattice or any equivariant homotopy equivalence. The representation equivalence is rational. Mathematical novelty is assessed against accessible published sources and searchable research records; unindexed work could contain an equivalent answer. No independent mathematical audit is represented as completed.

## References
1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754 (public version 27 January 2015), https://arxiv.org/abs/1501.06754 .
2. C. Barton, J. I. Brown and D. A. Pike, *Acyclic polynomials of graphs*, arXiv:2011.01735 (first public version 2020), https://arxiv.org/abs/2011.01735 .
3. A. Carnero Bravo, *The forest filtration of a graph*, arXiv:2307.13271 (first public version 2023), https://arxiv.org/abs/2307.13271 .
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
5. Standard representation theory of symmetric groups: \(\bigwedge^2 S^{(4,1)}\cong S^{(3,1,1)}\).
