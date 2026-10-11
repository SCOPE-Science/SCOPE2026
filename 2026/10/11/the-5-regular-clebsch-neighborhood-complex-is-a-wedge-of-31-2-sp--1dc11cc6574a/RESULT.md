# The \(5\)-regular Clebsch neighborhood complex is a wedge of \(31\) \(2\)-spheres
## Finding
Let \(C\) be the \(5\)-regular Clebsch graph in the explicit Cayley model
\[
C=\operatorname{Cay}(\mathbb F_2^4,\{e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}).
\]
For a finite graph \(G\), its Lovász neighborhood complex \(\mathcal N(G)\) has vertex set \(V(G)\); a nonempty set \(\sigma\subseteq V(G)\) is a face exactly when all vertices of \(\sigma\) have a common neighbor in \(G\). For this Clebsch graph,
\[
\mathcal N(C)\simeq\bigvee^{31}S^2.
\]

## Assumptions and scope
The graph is the standard \(5\)-regular Clebsch graph, not its \(10\)-regular complement. Vertices are the \(16\) vectors of \(\mathbb F_2^4\), encoded by integers \(0,\ldots,15\), with adjacency given by XOR with one of \(1,2,4,8,15\). The verifier independently checks the strongly regular parameters \((16,5,0,2)\), so the graph presentation is fixed internally. The finding concerns the ordinary Lovász neighborhood complex and ordinary homotopy type.

## Proof
The \(16\) open neighborhoods are \(5\)-element subsets of the vertex set. Exhaustive union of all nonempty subfaces of these neighborhoods gives exactly \(352\) nonempty faces, with face vector
\[
(16,80,160,80,16).
\]

On the nonempty face poset, apply sequential vertex toggles in the order
\[
(9,11,0,5,4,14,3,2,12,8,13,6,15,7,10,1).
\]
At each stage, pair every still-unmatched face not containing the current vertex with the face obtained by adjoining that vertex whenever both faces are present and still unmatched. The resulting matching contains exactly \(160\) Hasse pairs. Direct orientation of all \(1040\) Hasse covers, reversing exactly the matched covers, is acyclic. Hence Forman's discrete Morse theorem gives a CW complex with one cell for each unmatched face.

Exactly one unmatched face has dimension \(0\), exactly \(31\) unmatched faces have dimension \(2\), and there are no other unmatched faces. Thus the Morse CW complex has one \(0\)-cell, no \(1\)-cells, and \(31\) \(2\)-cells. Every \(2\)-cell therefore attaches to the unique \(0\)-cell, proving
\[
\mathcal N(C)\simeq\bigvee^{31}S^2.
\]

## Verification
Run `python verify.py certificate.json` using only the Python standard library. The verifier rebuilds the Cayley graph and all \(352\) neighborhood-complex faces, checks the parameters \((16,5,0,2)\), reconstructs the \(160\)-pair matching, checks every one of the \(1040\) Hasse covers, and topologically sorts the oriented Hasse graph to certify acyclicity.

As independent finite cross-checks of the same chain complex, the verifier computes boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). In each characteristic the Betti vector is
\[
(1,0,31,0,0).
\]
It also verifies Euler characteristic \(32\), proves by exhaustive backtracking that no \(3\)-coloring exists, and exhibits a \(4\)-coloring.

## Relationship to prior work
Robinson's Dowker-complex framework applies directly: taking the symmetric adjacency relation of \(C\), a set of row vertices is a Dowker simplex exactly when it has a common adjacent column vertex, so the resulting Dowker complex is \(\mathcal N(C)\). That source supplies the relation-complex setting but does not compute this Clebsch graph.

Shukla determines neighborhood-complex homotopy types for graphs of maximum degree at most \(3\) and for \(4\)-regular circulant graphs. The present graph is \(5\)-regular, so those classification theorems do not imply the claim. Searches under the aliases “Clebsch graph,” “folded \(5\)-cube,” “Greenwood–Gleason graph,” and the equivalent \(\operatorname{Hom}(K_2,C)\) formulation found no statement implying the \(31\)-sphere wedge. Exact database comparisons likewise found only neighborhood-complex calculations for different graphs and Clebsch calculations for different simplicial-complex functors.

The result is especially natural because the verifier also finds \(\chi(C)=4\). Since the displayed wedge is simply connected but not \(2\)-connected, the Lovász connectivity bound gives the sharp lower bound \(\chi(C)\ge4\).

## Limitations
This is an exact finite computation and discrete-Morse proof for this one canonical graph; it does not classify neighborhood complexes of all folded cubes or all strongly regular graphs. The literature search cannot exclude an equivalent computation hidden in poorly indexed or unpublished material. No claim about simple-homotopy uniqueness, equivariant homotopy type, or the \(10\)-regular complement is made.

## References
1. M. Robinson, “Cosheaf Representations of Relations and Dowker Complexes,” arXiv:2005.12348, first public 2020-05-25; Journal of Applied and Computational Topology; DOI: 10.1007/s41468-021-00078-y. Mathematics Subject Classification: 55U10.
2. S. Shukla, “Homotopy Type of the Neighborhood Complexes of Graphs of Maximal Degree at most \(3\) and \(4\)-Regular Circulant Graphs,” arXiv:1802.04526; Electronic Journal of Combinatorics 26(2) (2019), P2.4; DOI: 10.37236/7549.
3. R. Forman, “Morse Theory for Cell Complexes,” Advances in Mathematics 134 (1998), 90–145; DOI: 10.1006/aima.1997.1650.
