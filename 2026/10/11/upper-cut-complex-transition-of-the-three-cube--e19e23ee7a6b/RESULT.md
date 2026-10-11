# Upper cut-complex transition of the three-cube
## Finding
Let \(Q_3\) be the graph on \(\{0,1\}^3\) with edges joining vertices that differ in one coordinate. For the ordinary cut-complex filtration,
\[
\Delta_4(Q_3)\simeq \bigvee^{3}S^2,
\qquad
\Delta_5(Q_3)\cong S^2\sqcup S^2.
\]
More precisely, \(\Delta_5(Q_3)\) is simplicially the disjoint union of the boundaries of the tetrahedra on the two parity classes. The inclusion \(\Delta_5(Q_3)\hookrightarrow\Delta_4(Q_3)\) is null-homotopic.

## Assumptions and scope
The vertex set is encoded by \(0,\ldots,7\), interpreted as binary triples. Two vertices are adjacent exactly when their Hamming distance is one. The even-parity class is \(E=\{0,3,5,6\}\) and the odd-parity class is \(O=\{1,2,4,7\}\).

For a graph \(G\) on vertex set \(V\), the ordinary \(k\)-cut complex \(\Delta_k(G)\) has as facets the complements \(V\setminus D\) of the \(k\)-subsets \(D\subseteq V\) for which the induced graph \(G[D]\) is disconnected. This is the convention of Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue.

The claim concerns only \(Q_3\) and the adjacent filtration levels \(k=4,5\). No statement for higher-dimensional hypercubes is asserted.

## Proof
There are exactly \(32\) disconnected four-vertex subsets of \(Q_3\). Classified by the numbers of even- and odd-parity vertices, their profile is
\[
1,12,6,12,1
\]
for parity splits \((4,0),(3,1),(2,2),(1,3),(0,4)\), respectively. Their complements are the \(32\) tetrahedral facets of \(\Delta_4(Q_3)\).

Every three-vertex subset is a face of \(\Delta_4(Q_3)\). Equivalently, the complete two-skeleton on eight vertices occurs. One direct reason is that every five-vertex set contains a disconnected four-vertex set: a parity split \((4,1)\) already contains four vertices from one independent parity class, while for a split \((3,2)\), one of the two minority vertices has its unique non-neighbor in the opposite parity class among the selected three, producing a disconnected \((3,1)\) subset. Hence \(\Delta_4(Q_3)\) is simply connected.

Its face vector is
\[
(f_0,f_1,f_2,f_3)=(8,28,56,32).
\]
With the standard orientations on sorted simplices, the integral simplicial boundary maps have rational ranks
\[
\operatorname{rank}(\partial_1)=7,
\qquad
\operatorname{rank}(\partial_2)=21,
\qquad
\operatorname{rank}(\partial_3)=32.
\]
Thus the rational Betti vector is \((1,0,3,0)\). The verifier also exhibits a \(32\times32\) minor of \(\partial_3\) with determinant \(-1\). Therefore \(\operatorname{im}(\partial_3)\) is primitive in \(C_2\), so \(H_2(\Delta_4(Q_3);\mathbb Z)\) is torsion-free. Since the complex is simply connected, \(H_1=0\); since \(H_3\) is a free group of rational rank zero, \(H_3=0\). Consequently
\[
\widetilde H_i(\Delta_4(Q_3);\mathbb Z)=
\begin{cases}
\mathbb Z^3,&i=2,\\
0,&i\ne2.
\end{cases}
\]
Hurewicz identifies \(\pi_2\) with \(H_2\). Choosing three sphere maps representing a basis gives a homology equivalence \(\bigvee^3S^2\to\Delta_4(Q_3)\); the homological Whitehead theorem for simply connected CW complexes makes this a homotopy equivalence.

For \(k=5\), the eight disconnected five-vertex subsets have complements
\[
\binom{E}{3}\ \cup\ \binom{O}{3}.
\]
Hence the facets of \(\Delta_5(Q_3)\) are exactly the four triangular faces of the tetrahedron on \(E\) together with the four triangular faces of the tetrahedron on \(O\). The two vertex sets are disjoint, so
\[
\Delta_5(Q_3)=\partial\Delta(E)\sqcup\partial\Delta(O)\cong S^2\sqcup S^2.
\]
Finally, both full tetrahedra \(E\) and \(O\) occur as three-simplices of \(\Delta_4(Q_3)\). Therefore the restriction of the filtration inclusion to each sphere component extends across a three-ball. The target \(\Delta_4(Q_3)\) is connected, so the two resulting constant maps can be joined to one basepoint. Thus the entire inclusion \(\Delta_5(Q_3)\hookrightarrow\Delta_4(Q_3)\) is null-homotopic.

## Verification
The standalone verifier exhaustively enumerates all vertex subsets rather than sampling them. It checks that there are \(32\) disconnected four-sets and \(8\) disconnected five-sets; reconstructs the complete face sets; obtains face vectors \((8,28,56,32)\) and \((8,12,8)\); verifies the complete two-skeleton of \(\Delta_4(Q_3)\); computes exact rational boundary ranks \((7,21,32)\); and evaluates an explicit maximal boundary minor to determinant \(-1\). It also checks that the \(k=5\) facets are precisely the two tetrahedral boundaries and that both filling tetrahedra are faces of \(\Delta_4(Q_3)\).

The proof of the homotopy type uses standard Hurewicz and Whitehead theorems after these exact finite checks. The null-homotopy uses the explicit filling tetrahedra, not only vanishing induced homology maps.

## Relationship to prior work
Bayer et al. introduced ordinary cut complexes and studied their topology for several graph families in arXiv:2304.13675. Their follow-up arXiv:2407.08158 records the filtration inclusion \(\Delta_{k+1}(G)\subseteq\Delta_k(G)\) and proves that a simplicial complex with complete two-skeleton is simply connected. The accessible full texts of both papers were inspected for the cube and hypercube, and no cube-specific statement was found. Chandrakar, Hazra, Rout and Singh study rectangular \(2\times n\) and \(3\times n\) grid graphs in arXiv:2408.07646; that coverage does not include the three-dimensional cube \(P_2\square P_2\square P_2\).

A published database record gives the distinct neighboring fact \(\Delta_3(Q_3)\simeq S^3\vee\bigvee^4S^4\). That result concerns a different filtration level and does not determine either \(\Delta_4(Q_3)\), \(\Delta_5(Q_3)\), or the inclusion map between them. Focused searches for the exact \(k=4\), \(k=5\), parity-boundary and null-homotopy formulations did not surface a covering statement.

## Limitations
This is an exact finite result for one canonical graph, not a general hypercube theorem. The literature search cannot rule out every unindexed source, and the strongest residual originality risk is an undiscovered small-graph computation containing the same two filtration levels.

## References
1. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, Lei Xue, “Topology of Cut Complexes of Graphs,” arXiv:2304.13675; first public version 2023-04-26.
2. Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Sheila Sundaram, Lei Xue, “Topology of Cut Complexes II,” arXiv:2407.08158; first public version 2024-07-11.
3. Himanshu Chandrakar, Nisith Ranjan Hazra, Debotosh Rout, Anurag Singh, “Topology of total cut and cut complexes of grid graphs,” arXiv:2408.07646; first public version 2024-08-14.
