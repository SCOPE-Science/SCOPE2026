# A six-face homology module in the scale-three Rips complex of the subdivided cube

## Finding
Let \(Q_3\) denote the one-skeleton of the standard three-dimensional cube and let \(S(Q_3)\) be its once-edge-subdivided graph, with 20 vertices. Equip its vertices with unit-edge shortest-path distance and write \(X=\operatorname{VR}_{\le3}(S(Q_3))\), the flag complex whose edges join points at distance at most three. Then
\[
X\simeq S^2\vee\bigvee^6S^3.
\]
The full 48-element cubical symmetry group \(B_3=\operatorname{Aut}(Q_3)\) acts on its integral homology as
\[
H_2(X;\mathbb Z)\cong\mathbb Z_{\det},\qquad H_3(X;\mathbb Z)\cong\mathbb Z[\mathcal F],
\]
where \(\mathcal F\) is the set of six square faces of the cube, \(\mathbb Z[\mathcal F]\) is its *unsigned* permutation lattice, and \(\det\) is the geometric orientation character of the cube. Thus the rational quotient by all cubical symmetries has Betti numbers \((b_0,b_2,b_3)=(1,0,1)\); for the orientation-preserving subgroup they are \((1,1,1)\).

## Assumptions and scope
The original graph has vertices \(0,\ldots,7\), encoded in binary, with an edge exactly when the binary labels differ in one bit. Its 12 edges are ordered lexicographically, and the midpoint of edge number \(j\) has label \(8+j\). Distances refer to the **20 graph vertices only**, not all points on metric edges. All inclusions at threshold three are non-strict. The homotopy assertion concerns the single scale three; no entire-filtration assertion is made.

## Proof
**Finite simplicial model and perfect discrete-Morse matching.** Compute shortest paths by breadth-first search on the twenty vertices. Enumerate every clique of the resulting distance-at-most-three graph. This gives face vector \((20,108,212,152,24)\) in dimensions zero through four, hence 516 nonempty simplices. Use the exact fixed vertex order

`[5,6,18,1,7,11,2,13,16,3,15,0,17,4,12,19,8,9,10,14]`.

Process its vertices \(v\) consecutively: among still-unmatched simplices, pair each simplex \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), when both exist, removing both from subsequent consideration. There are exactly 254 disjoint matched pairs, and the remaining cells comprise one zero-cell, one two-cell, and six three-cells. The oriented Hasse graph (every covering edge directed downward, with matched edges reversed) has all 516 vertices in a complete topological sorting, proving global acyclicity rather than relying on the heuristic selection alone. Discrete Morse theory therefore gives a CW model with those eight cells, no one-cells or cells in dimensions above three.

**Six primitive independent three-dimensional classes.** Each original cube face has four corner vertices and the four corresponding edge-midpoints, an isometric eight-cycle inside the subdivision. At threshold three, the eight vertices of this cycle have precisely four nonedges, the four antipodal pairs. Their induced flag complex is the boundary of a four-dimensional cross-polytope \(S^3\), with 16 three-simplices. For every such sphere, a three-simplex exists which lies in *no* four-simplex of the entire 516-face complex. Its coefficient functional is an integral three-cocycle. The six chosen free tetrahedra are absent from the spheres associated with the other five cube faces. Therefore these six spherical fundamental cycles pair with six integer cocycles in a diagonal matrix with entries \(\pm1\). They give a primitive rank-six subgroup of \(H_3(X;\mathbb Z)\).

The Morse CW complex has only six three-cells. The above six independent non-boundary three-cycles force its entire differential \(C_3\to C_2\) to vanish over \(\mathbb Z\). It follows that \(H_3(X;\mathbb Z)\cong\mathbb Z^6\), \(H_2(X;\mathbb Z)\cong\mathbb Z\), with no other reduced integral homology. The one two-cell is attached to a point. Each three-cell attaches to that \(S^2\) with degree zero, and \(\pi_2(S^2)\cong\mathbb Z\); hence every attaching map is nullhomotopic. This proves the displayed wedge, not merely its Betti numbers.

**Full cubical symmetry.** A cube automorphism permutes the six face-induced three-spheres. Any face stabilizer acts on the eight-cycle as an element of its dihedral group. The induced action on the four antipodal vertex pairs of the cross-polytope has orientation degree equal to the sign of the pair permutation times \((-1)\) to the number of interchanges within pairs. Exact evaluation for all 48 cube symmetries shows that this degree is always \(+1\) when a face is stabilized. As the six primitive cycles form a basis, \(H_3(X;\mathbb Z)\) is *unsigned* face permutation, despite some symmetries reversing the original square's planar orientation.

For each cube symmetry, the signed simplicial Lefschetz number is computed from fixed oriented simplices in all five chain degrees. Since the space is connected and rational homology occurs only in degrees two and three, one obtains
\[\operatorname{tr}(g\mid H_2)=\sum_{k=0}^4(-1)^k\operatorname{tr}(g\mid C_k)-1+\#\operatorname{Fix}_{\mathcal F}(g).\]
Direct enumeration of all 48 signed coordinate permutations gives exactly the geometric determinant character, so the rank-one integral module is \(\mathbb Z_{\det}\). Rational transfer for a finite group identifies rational quotient homology with invariants. There is one invariant three-class (the sum of face classes), and the determinant character has no full-group invariant. For the index-two rotation subgroup, both positive-degree invariant dimensions equal one.

## Verification
Run `python3 verify_subdiv_cube.py` with Python 3.9 or newer. The program uses only the standard library. It reconstructs the graph and metric, enumerates all 516 faces and every Hasse covering relation, confirms the 254-pair matching acyclic, checks the six octahedral subcomplexes and their primitive integer cocycle witnesses, and checks signed Lefschetz and local orientation degrees for all 48 automorphisms. Expected terminal marker: `SUBDIVIDED_CUBE_RIPS3_PERFECT_MORSE_SIX_FACE_SPHERES_48_SYMMETRIES_OK`.

## Relationship to prior work
The 2017 preprint / 2018 conference paper *Vietoris–Rips and Čech Complexes of Metric Gluings* provides a general gluing theorem, but Section 4.2 explicitly identifies cubical graphs as an obstruction to its path-gluing hypotheses. Its discussion concerns the original eight-vertex cube, not this 20-vertex edge-subdivision at radius three. Adamaszek's earlier *Clique complexes and graph powers*, Theorem 5.1, treats a subdivision at radius two, not this radius-three homology and 48-symmetry action. The indexed result *A mixed-dimensional Rips wedge for the truncated cube* has the same abstract wedge type but concerns a **different**, 24-vertex cubic graph; equality of Betti numbers or homotopy types does not determine the present geometric face basis or group action. The indexed complete-graph-subdivision result also concerns a different original graph family and does not imply this assertion.

## Limitations
This is a finite, exact homotopy classification of one canonical metric graph at one threshold, with a full symmetry action. It is not a classification of all subdivided cube graphs in higher dimensions or a theorem about metric-edge-point Vietoris–Rips complexes. The 2026 indexed comparisons were available by descriptive records; their full hosted source packages were not accessible at inspection time, leaving a residual risk of an unindexed reduction. No independent audit has been performed.

## References
1. M. Adamaszek, H. Adams, E. Gasparovic, M. Gommel, E. Purvine, R. Sazdanovic, B. Wang, Y. Wang, L. Ziegelmeier, *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224 (first posted 2017-12-18); conference version *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI 10.4230/LIPIcs.SoCG.2018.3. Section 4.2 describes the cubical obstruction.
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011), Theorem 5.1 on subdivided graphs at radius two.
3. *A mixed-dimensional Rips wedge for the truncated cube*, published research record, 2026-10-04, identifier `2026/10/4/SCOPE-a-mixed-dimensional-rips-wedge-for-the-truncated-cube--4fae71a21a80`.
4. *The Rips filtration of the complete-graph subdivision has two consecutive sphere wedges*, published research record, 2026-10-11, identifier `2026/10/11/SCOPE-the-rips-filtration-of-the-complete-graph-subdivision-has-two-co--fb5f0359b702`.
