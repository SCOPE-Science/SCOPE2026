# The graph-metric Rips filtration of the truncated tetrahedron
## Finding
Let \(T\) be the truncated tetrahedral graph with its shortest-path metric. Using the inclusive Vietoris--Rips convention, the complete graph-metric filtration is
\[
\mathrm{VR}(T;r)\simeq
\begin{cases}
\text{a discrete 12-point space}, & 0\le r<1,\\
\bigvee^3 S^1, & 1\le r<2,\\
\bigvee^5 S^2, & 2\le r<3,\\
\ast, & r\ge 3.
\end{cases}
\]
Thus the two nontrivial integer scales exhibit a dimension shift from three independent 1-cycles to five 2-spheres before the filtration becomes contractible.

## Assumptions and scope
The graph is defined intrinsically, avoiding any dependence on a Euclidean realization. Its vertices are the ordered pairs \( (i,j)\) with \(i,j\in\{0,1,2,3\}\) and \(i\ne j\). Two vertices \( (i,j)\) and \( (k,\ell)\) are adjacent exactly when either \(i=k\) or \( (k,\ell)=(j,i)\). This is the 12-vertex, 18-edge truncated tetrahedral graph: the three arcs with a fixed first coordinate form one triangular truncation face, while each reversed pair records one edge inherited from the tetrahedron.

The metric is the shortest-path metric on this graph, and \(\mathrm{VR}(T;r)\) contains a finite set precisely when every pair of its vertices has graph distance at most \(r\). Because all graph distances are integers, the filtration changes only at \(r=1,2,3\). The result is about this graph metric, not the Euclidean chordal metric on a geometrically embedded truncated tetrahedron.

## Proof
For \(0\le r<1\), distinct vertices have positive integral distance, so the Rips complex consists of 12 isolated vertices.

At \(r=1\), the Rips complex is the clique complex of \(T\). Its face vector is \( (f_0,f_1,f_2)=(12,18,4)\). The four 2-simplices are exactly the four triangular truncation faces. In each triangle choose an edge that is contained in no other 2-simplex and collapse that edge together with its unique 2-dimensional coface. The four elementary collapses leave a connected graph with 12 vertices and 14 edges. Its first Betti number is therefore \(14-12+1=3\), so the original clique complex is homotopy equivalent to \(\bigvee^3 S^1\).

At \(r=2\), exhaustive clique enumeration in the distance-two graph gives face vector \( (12,42,48,12)\). The attached certificate gives an explicit acyclic Forman matching with 54 matched face--coface pairs and exactly six critical cells: one critical 0-cell and five critical 2-cells, with no critical cells in dimensions 1 or 3. The matching is checked in two independent finite ways: every matched lower face has the listed upper face as its unique active immediate coface at the moment of elimination, and the full directed Hasse graph obtained by reversing matched incidences is acyclic. Forman's theorem therefore produces a CW complex with one 0-cell and five 2-cells and no 1-cells. Every 2-cell then attaches to the single 0-cell, giving \(\bigvee^5 S^2\).

Finally, the graph has diameter 3. Hence for \(r\ge3\) every pair of vertices is joined in the Rips graph, so \(\mathrm{VR}(T;r)\) is the full 11-simplex and is contractible.

## Verification
The standalone verifier reconstructs \(T\) from the ordered-pair definition, computes all-pairs graph distances, checks 12 vertices, 18 edges, cubic degree sequence, and diameter 3, and enumerates every Rips simplex at scales 1 and 2. It then replays the four elementary collapses at scale 1 and the entire discrete-Morse certificate at scale 2. The final verifier output is `VERIFY_OK`.

The exact scale-2 critical-cell count is \(c_0=1\), \(c_1=0\), \(c_2=5\), and \(c_3=0\). No numerical approximation or probabilistic computation enters the proof.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine the Vietoris--Rips homotopy types of the five Platonic solids and explicitly identify Archimedean solids as a natural direction for extending that program. The truncated tetrahedron is an Archimedean solid, so its graph-metric filtration is a direct, finite test case for that extension.

The source paper treats Platonic solids rather than the truncated tetrahedron. A related dissertation also discusses computational barcodes for polyhedra inscribed in the unit sphere, including a general remark about Archimedean solids; that setting uses geometric point-cloud distances and does not state the graph-metric filtration proved here. Targeted literature and semantic-database searches for the truncated tetrahedron, Archimedean solids, Rips complexes, and equivalent clique-complex formulations did not locate a statement implying this four-regime graph-metric classification. This search evidence is not a proof of absolute novelty.

## Limitations
The claim concerns one Archimedean graph and the shortest-path metric only. It does not classify other Archimedean solids, does not identify the Euclidean-chordal Rips filtration of the usual geometric realization, and does not assert that the displayed Morse matching is canonical or symmetry-equivariant. The originality check is necessarily limited by indexing, terminology, and source accessibility.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, “Vietoris--Rips complexes of Platonic solids,” arXiv:2302.14388 (first public version 2023-02-28); later published in *Innovations in Incidence Geometry*.
2. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral dissertation, Justus-Liebig-Universität Gießen, 2023.
