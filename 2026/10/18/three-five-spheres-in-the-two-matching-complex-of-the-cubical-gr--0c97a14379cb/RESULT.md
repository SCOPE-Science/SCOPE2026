# Three five-spheres in the two-matching complex of the cubical graph

## Finding
Let \(Q_3\) be the graph of the three-dimensional cube, with its eight vertices represented by binary triples and its twelve edges joining triples that differ in exactly one coordinate. Its two-matching complex \(M_2(Q_3)\) has one simplicial vertex for every cube edge; a collection of such vertices is a face when no cube vertex is incident to more than two selected edges. There is an integral homotopy equivalence
\[
M_2(Q_3)\simeq S^5\vee S^5\vee S^5.
\]
Equivalently, because the cube is triangle-free, the three-clique-free complex of the cuboctahedral line graph \(L(Q_3)\) has this same homotopy type: \(\mathsf{CF}_3(L(Q_3))=M_2(Q_3)\) as simplicial complexes. This is a complete finite homotopy classification, not a claim of a theorem for other cubical graphs or higher-dimensional cubes.

## Assumptions and scope
The underlying graph is the ordinary, simple, undirected eight-vertex cube; faces of its two-matching complex are sets of edges with maximum selected degree at most two, including the empty face. Integer labels \(0,\ldots,7\) are binary encodings of cube vertices. The twelve graph edges are placed in the following fixed order:
\[
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
\]
The edge-subsets are encoded by twelve-bit nonnegative integers, with bit \(i\) representing the \(i\)-th edge. All homotopy assertions concern the geometric realizations of finite complexes and integral (not only rational or mod-two) topology. The result is assigned topology classification 55U10 because its main assertion is an explicit CW homotopy type.

## Proof
**Exact face model.** Each cube vertex has degree three. Therefore a subset of edges belongs to \(M_2(Q_3)\) exactly when it does not contain all three edges incident to any one cube vertex. In the fixed ordering, the eight forbidden three-edge bitmasks are \(7,25,98,168,772,1296,2624,3200\). Exhaustively testing the \(2^{12}-1\) nonempty masks produces exactly \(1698\) nonempty faces and dimension-wise face numbers
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)=(12,66,212,423,516,352,108,9).
\]
The \(49\) facets occur in dimensions five, six and seven, with counts four, 36 and nine respectively; consequently homology alone would not make the following wedge conclusion automatic.

**Explicit acyclic matching.** Work on the ordinary face poset of all **nonempty** simplices. Starting with the complete set of faces, for successive pivot indices \(i=11,10,\ldots,0\), pair each still-unpaired face whose bit \(i\) is absent with the still-unpaired face obtained by adding bit \(i\), whenever both are present. Remove both paired faces before passing to the next pivot. The numbers of pairs at the twelve stages, in descending pivot order, are
\[
665,94,51,18,8,0,7,0,2,1,1,0.
\]
There are exactly \(847\) disjoint cover-relation pairs. Four nonempty faces remain unmatched: bitmasks \(888\), \(1235\), \(1421\), \(2048\), of dimensions five, five, five, and zero respectively.

To prove acyclicity, direct each matched face-poset cover relation from its lower face to its upper face, and direct each unmatched cover relation from its upper face to its lower face. A certificate provides all \(1698\) faces, all \(847\) pairings, and an explicit topological ordering of the resulting directed Hasse graph. The standalone checker recomputes every cover relation and verifies all \(7980\) directed arrows and the complete acyclic topological order. This establishes an acyclic discrete-Morse matching, rather than merely counting candidate critical faces.

**Topological conclusion.** The acyclic matching theorem for finite simplicial complexes gives a CW complex homotopy equivalent to \(M_2(Q_3)\) with one zero-cell, exactly three five-cells, and no other cells. Since each five-cell must attach along a map from a four-sphere to the single zero-cell, its attaching map is constant. The resulting CW complex is precisely the wedge of three five-spheres. In particular,
\[
\widetilde H_j(M_2(Q_3);\mathbb Z)\cong
\begin{cases}
\mathbb Z^3,& j=5,\\
0,& j\ne5,
\end{cases}
\]
and all its reduced integral homology is torsion-free.

**Equivalent clique-free formulation.** The vertices of \(L(Q_3)\) are the twelve cube edges, with adjacency when edges share an endpoint. Any three cube edges that are pairwise incident either share one endpoint or form a triangle in the original graph. The latter is impossible because the cube is bipartite. Hence the forbidden three-cliques of \(L(Q_3)\) are precisely the eight vertex-stars already excluded from the two-matching complex. The two simplicial complexes are therefore identical, not merely homotopy equivalent by a reduction.

## Verification
Run `python verify.py --check-certificate certificate.json` using standard Python 3; no third-party packages are required. The program enumerates all \(4095\) nonempty edge-subsets, recognizes exactly \(1698\) faces, recomputes the \(847\) matching pairs and \(4\) critical cells, checks cover-incidence and checks directed acyclicity via topological sorting. It compares the reconstructed lists, pairings and directed topological order to the complete serialized certificate. The recorded execution is `verification_output.txt`. As a separate, nonessential check, it evaluates mod-two chain ranks and recovers unreduced Betti vector \((1,0,0,0,0,3,0,0)\) and Euler characteristic \(-2\). These finite computations are exhaustive for the fixed twelve-edge object; no inference about infinitely many graphs is made.

## Relationship to prior work
Vega, *2-Matching Complexes* (arXiv:1909.10406), defines the bounded-degree two-matching complex and applies discrete Morse methods to clawed graph constructions, wheels and caterpillar graphs, but does not give this cube computation. The primary 2026 reference, Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (arXiv:2602.09623v1, publicly available February 10, 2026), studies higher clique-free complexes and shellability for classes including diamond-free chordal graphs and graph modifications. Its sufficient theorem does not apply to the cuboctahedral line graph, which contains induced four-cycles; neither its results nor its proof provide this explicit nonpure homotopy classification. Previously published computations of the **ordinary** matching complex of the cube, of matching complexes of the line graph, and of the cube's discrete-Morse complex concern different simplicial complexes and do not determine \(M_2(Q_3)\).

## Limitations
The statement concerns only the three-dimensional cube and the degree cap two. No homotopy type is asserted for other regular graphs, higher cubes, or the entire clique-free filtration. The proof certificate establishes acyclicity by finite integer enumeration; its completeness is justified by the exact twelve-edge list and the exhaustive face test. The literature search cannot exclude an unindexed equivalent theorem. Independent mathematical audit has not been performed.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, February 10, 2026. https://arxiv.org/abs/2602.09623
2. J. Vega, *2-Matching Complexes*, arXiv:1909.10406, first circulated September 23, 2019. https://arxiv.org/abs/1909.10406
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145 (standard discrete-Morse theorem).
