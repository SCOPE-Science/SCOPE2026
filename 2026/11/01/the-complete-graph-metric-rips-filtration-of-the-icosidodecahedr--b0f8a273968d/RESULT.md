# The complete graph-metric Rips filtration of the icosidodecahedral graph

## Finding
Let \(G\) be the \(30\)-vertex, \(60\)-edge icosidodecahedral graph, the rectification of the ordinary icosahedral graph. Equip \(V(G)\) with shortest-path **graph distance**, and write \(\operatorname{VR}_{\le r}(G)\) for the inclusive clique Vietoris–Rips complex of subsets whose pairwise graph distances are at most \(r\). Its complete integral homotopy filtration is
\[
\operatorname{VR}_{\le r}(G)\simeq
\begin{cases}
\bigvee^{29}S^0,&0\le r<1,\\
\bigvee^{11}S^1,&1\le r<2,\\
S^2,&2\le r<4,\\
S^{14},&4\le r<5,\\
\ast,&r\ge5.
\end{cases}
\]
In particular, the *actual inclusion* from scale \(2\) to scale \(3\) is a simple-homotopy equivalence, certified by exactly \(7472\) explicit elementary simplicial collapses
\[
\operatorname{VR}_{\le3}(G)\searrow\operatorname{VR}_{\le2}(G).
\]
There are a further \(426\) certified elementary collapses from the scale-two complex onto a canonical \(30\)-vertex triangulated icosidodecahedral boundary \(K\cong S^2\). Thus this sphere is an embedded common deformation retract of both intermediate complexes.

Equivalently, the full reduced integral persistence barcode has eleven degree-one intervals \([1,2)\), one degree-two interval \([2,4)\), and one degree-fourteen interval \([4,5)\). Ordinary degree-zero persistence has twenty-nine finite intervals \([0,1)\) and one unbounded component interval. These multiplicities hold over every field.

## Assumptions and scope
Construct the icosahedron combinatorially with vertex set \(\{0,\ldots,11\}\). Its north and south poles are \(0\) and \(11\); its two five-cycles are \(1,\ldots,5\) and \(6,\ldots,10\). With subscripts modulo \(5\), write \(a_i=1+i\) and \(b_i=6+i\). The thirty icosahedral edges are all of the following: \(\{0,a_i\}\), \(\{11,b_i\}\), \(\{a_i,a_{i+1}\}\), \(\{b_i,b_{i+1}\}\), \(\{a_i,b_i\}\), and \(\{a_i,b_{i-1}\}\), for \(0\le i<5\).

The vertices of \(G\) are these thirty edges, indexed in lexicographic order. Two distinct vertices of \(G\) are adjacent exactly when their two corresponding icosahedral edges occur together in an icosahedral triangular face. The resulting graph has degree four and is the standard icosidodecahedral edge graph, with twenty triangular faces and twelve pentagonal faces. Distances are shortest-path lengths in \(G\), **not** Euclidean chord lengths between polyhedral vertices, geometric intrinsic distances on its surface, or distances between the underlying icosahedron's twelve vertices.

Let \(K\) contain the twenty triangular faces of \(G\), and triangulate each of its twelve pentagonal faces by a fan from that face's lowest indexed vertex. The resulting simplicial complex has face vector \((30,84,56)\) and triangulates the polyhedral boundary. The explicit construction of \(K\) is fixed, rather than chosen up to homotopy.

## Proof
**Polyhedral boundary.** An icosahedral triangular face yields one triangle in its rectification; the five original edges around each icosahedral vertex yield one pentagon. These are precisely the twenty triangular and twelve pentagonal faces of an icosidodecahedron. After choosing the twelve diagonal fans, the resulting \(K\) has \(30\) vertices, \(84\) edges and \(56\) triangles. The independent verifier also checks every edge lies in exactly two triangles, every vertex link is a connected simple cycle, and the full surface is connected. Hence \(K\) is a closed connected triangulated surface of Euler characteristic \(30-84+56=2\). Classification of compact surfaces shows \(|K|\cong S^2\).

**Scale one.** The graph \(G\) has \(30\) vertices and \(60\) edges. Its only graph cliques of size at least three are twenty triangles, with every triangle edge in exactly one such triangle. Removing a free edge along with its unique triangle for each of the twenty triangles collapses the Rips complex onto a connected graph with \(30\) vertices and \(40\) edges. The cycle rank is \(40-30+1=11\), giving \(\bigvee^{11}S^1\).

**Scale two and scale three.** Complete lexicographically increasing clique enumeration of each graph power produces the following face vectors, from vertices upward:
\[
\begin{aligned}
 r=2:&\quad(30,180,380,330,102),\\
 r=3:&\quad(30,300,1340,3150,4374,3800,2100,720,140,12).
\end{aligned}
\]
The certified face sets are nested \(K\subseteq\operatorname{VR}_{\le2}(G)\subseteq\operatorname{VR}_{\le3}(G)\). The included `collapse_certificate.json` contains \(7472\) ordered pairs for the upper collapse, and \(426\) for the lower one, using nonzero thirty-bit masks to encode faces. The standalone `verify_icosidodecahedron.py` **reconstructs both full face sets** from graph distances; at every removal pair \((\sigma,\tau)\), it verifies: both are still present and outside the target, \(\sigma\) is a codimension-one face of \(\tau\), \(\tau\) is the *only* remaining immediate coface of \(\sigma\), and \(\tau\) is a maximal remaining simplex. Deleting both is therefore an elementary simplicial collapse. It finally compares the exact surviving face set, not just its number of faces, with the prescribed target. Since each step is a valid elementary collapse, this independently checkable finite certificate proves the two claimed strong deformation retractions. In particular, the scale-two to scale-three inclusion induces an isomorphism on every integral homology group.

**Scale four and scale five.** Breadth-first search gives the same distance-shell sizes from each vertex: one at distance zero, four at distance one, eight each at distances two, three and four, and one at distance five. Thus the graph diameter is \(5\), and the thirty vertices form fifteen disjoint antipodal distance-five pairs. At radius four the only missing edges join antipodes, so the Rips complex is the join of fifteen copies of \(S^0\), hence \(S^{14}\). At radius five every pair is an edge and the complex is the full simplex, hence contractible.

**Persistence.** Graph distances are integers, so there are no changes between these thresholds. The explicit relative collapse from radius three onto radius two certifies the unique two-dimensional integral class survives the radius-three inclusion. Every other positive-dimensional birth and death follows from the adjacent sphere-wedge stages, whose nonzero homology lies in different degrees. This determines the full barcode stated above without inferring persistence merely from equal Betti numbers.

## Verification
Place `verify_icosidodecahedron.py` beside `collapse_certificate.json` and execute `python3 verify_icosidodecahedron.py collapse_certificate.json` (Python standard library only). It reconstructs the thirty-vertex rectified graph from its twelve-vertex icosahedral definition, checks all thirty breadth-first distance profiles, exhaustively enumerates all cliques of the graph powers at radii one, two and three, checks the target surface and its vertex links, and replays every elementary free-face pair with complete current coface sets. All \(7472+426=7898\) recorded pairs are checked. It also verifies all fifteen distance-five antipodal pairs and the scale-one free triangular edges. The bundled `verification_output.txt` records actual execution and ends with `ICOSIDODECAHEDRON_RIPS_COLLAPSE_CERTIFICATE_VERIFIED`. Full finite enumeration is used only in this specified thirty-vertex graph; no extrapolation to a family is made.

## Relationship to prior work
Saleh, Titz Mite and Witzel (arXiv:2302.14388, first posted 2023-02-28) classify graph-metric Rips complexes of the five *Platonic* solids, and explicitly identify Archimedean solids as a possible extension. The icosidodecahedron is Archimedean, not Platonic; their results on the regular icosahedron do not concern the thirty vertices of its rectification, and neither determine the two relative collapses nor the complete barcode here. Saleh's 2023 dissertation was additionally checked at its full contents, introduction, and relevant polyhedral and sphere-point-cloud portions; its Archimedean example concerns a different polyhedron with a spherical point-cloud metric, rather than this graph metric.

Adamaszek (arXiv:1104.0433) identifies graph-metric Rips complexes with clique complexes of graph powers and proves a high-girth collapse criterion. This graph has triangles, so the high-girth hypothesis is false. The graph is also **not** the ordinary line graph of the icosahedron: the latter has degree eight, while this rectification graph has degree four. Hence generic results on line graphs do not immediately cover it.

The closest fully inspected published mathematical records concern the \(24\)-vertex rhombicuboctahedron graph at radius two, the \(24\)-vertex truncated octahedron's complete graph-metric filtration, and the \(12\)-point Euclidean cuboctahedron. These use different finite metric spaces, and even their sphere-stage conclusions do not imply this exact embedded-boundary collapse or the radius-three persistence isomorphism. Targeted searches for “icosidodecahedron,” “rectified icosahedron,” “graph power clique complex,” “radius-three simplicial collapse,” and the exact homotopy fingerprint found no indexed theorem covering this claim. Search absence is not proof of universal novelty.

## Limitations
This is an exact theorem for one prescribed \(30\)-vertex graph with shortest-path distance. No result is asserted for Euclidean chordal metrics, other Archimedean graphs, perturbations, or a generic medial-graph classification. The two collapse counts describe the supplied explicit witnesses, not a minimum number of elementary collapses. Independent scientific audit has not been performed. A differently phrased or unindexed equivalent computation remains a bibliographic risk.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public 2023-02-28; *Innovations in Incidence Geometry* 21 (2024), DOI 10.2140/iig.2024.21.17.
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, *Israel Journal of Mathematics* 196 (2013), 295–319, DOI 10.1007/s11856-012-0166-1.
3. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, doctoral thesis, Justus Liebig University Giessen, 2023-09, DOI 10.22029/jlupub-17950.
4. Published mathematical record, *An explicit scale-two Rips collapse onto the rhombicuboctahedral sphere*, `2026/10/11/SCOPE-an-explicit-scale-two-rips-collapse-onto-the-rhombicuboctahedral--333648c8216c`.
5. Published mathematical record, *Complete graph-metric Vietoris--Rips filtration of the truncated octahedral graph*, `2026/10/11/SCOPE-complete-graph-metric-vietoris-rips-filtration-of-the-truncated--3b8391bcadb8`.
6. Published mathematical record, *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, `2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e`.
