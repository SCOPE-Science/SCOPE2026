# A 21-sphere wedge in the radius-two Rips complex of the truncated icosahedron

## Finding
Let \(F\) be the 60-vertex truncated-icosahedral (soccer-ball) graph, equipped with shortest-path distance \(d_F\). Its inclusive graph-metric Vietoris–Rips complex at radius two satisfies
\[
\operatorname{VR}_{\le 2}(V(F),d_F)\simeq\bigvee^{21}S^2.
\]
In particular, its integral reduced homology is \(\widetilde H_2\cong\mathbb Z^{21}\) and vanishes in every other degree, and its fundamental group is trivial. This is a homotopy statement, not merely a rational Betti-number computation.

## Assumptions and scope
Construct the icosahedral graph \(I\) from two pentagonal rings \(u_i,v_i\) (indices in \(\mathbb Z/5\mathbb Z\)), together with poles \(N,S\). Its edges are \(Nu_i\), \(Sv_i\), \(u_iu_{i+1}\), \(v_iv_{i+1}\), \(u_iv_i\), and \(u_iv_{i-1}\). Its twenty triangles form the facial triangles in the standard sphere embedding. The vertices of \(F\) are oriented edges \((a,b)\) of \(I\). Two are adjacent in \(F\) exactly if they are \((a,b),(b,a)\), or if they are \((a,b),(a,c)\) and \(\{a,b,c\}\) is a facial triangle of \(I\). This is the ordinary truncation construction and fixes the graph unambiguously.

For a finite graph \(H\), \(\operatorname{VR}_{\le2}(H)\) denotes the simplicial complex on \(V(H)\) in which a nonempty set is a simplex precisely when every two vertices are at graph distance at most two. No Euclidean chord distance, open-threshold convention, or weighted edge metric is used. The assertion concerns this single exact radius, not the complete filtration and not arbitrary fullerenes.

## Proof
**1. Facial structure.** The construction has sixty vertices and ninety edges, every vertex has degree three, and the embedded surface has twelve pentagonal faces (one per vertex of \(I\)) and twenty hexagonal faces (one per triangular face of \(I\)). Every edge belongs to two face boundaries. The graph has no triangles or quadrilaterals. These statements follow directly from the oriented-edge construction and are exhaustively rechecked by `check.py`.

**2. Simple connectivity.** Every radius-two edge not already belonging to \(F\) joins endpoints of a length-two path in \(F\); the path and its shortcut bound a two-simplex of the Rips complex. Hence every loop in the Rips one-skeleton is homotopic to a loop in the original graph \(F\). In a connected planar graph, the boundary walks of its faces normally generate the kernel of the map from the graph's fundamental group to that of the sphere. Here every such facial walk is null-homotopic already in the Rips complex: the vertices of a pentagonal face are pairwise within distance two and hence span a four-simplex; for each hexagonal face with successive vertices \(x_0,\ldots,x_5\), the four Rips triangles \((x_0,x_1,x_2)\), \((x_2,x_3,x_4)\), \((x_4,x_5,x_0)\), and \((x_0,x_2,x_4)\) fill its perimeter. All four triangles satisfy the distance-two constraint, including the central triangle of alternating vertices. Thus \(\pi_1(\operatorname{VR}_{\le2}(F))=1\).

**3. Dimension-two collapse.** The clique complex of the square of \(F\) has exactly the following counts of nonempty simplices in dimensions zero through four:
\[
(f_0,f_1,f_2,f_3,f_4)=(60,270,340,120,12).
\]
An exact deterministic elementary-collapse enumeration removes 120 free-face/coface pairs, always choosing a pair with highest-dimensional coface and breaking ties lexicographically, until no simplex of dimension greater than two remains. Its resulting two-dimensional subcomplex has face vector \((60,270,232)\). The standalone `check.py` reconstructs the graph directly from its twelve-vertex definition, independently enumerates every clique, verifies each free-face condition immediately before the corresponding deletion, verifies downward closure, and checks the final face vector. Thus this is a genuine simplicial deformation retraction onto a two-complex, rather than an inference from rational homology or a partial census.

**4. Homotopy type.** Elementary collapses preserve homotopy and Euler characteristic. The original complex therefore has
\[
\chi=60-270+340-120+12=22.
\]
Its two-dimensional simply connected deformation retract has \(H_1=0\), \(H_i=0\) for \(i>2\), and free integral \(H_2\) (as a subgroup of a free integral chain group), necessarily of rank \(\chi-1=21\). The Hurewicz theorem represents a basis of \(H_2\) by maps of two-spheres. The resulting map from \(\bigvee^{21}S^2\) is an integral homology equivalence between simply connected CW complexes and is therefore a homotopy equivalence by the homological Whitehead theorem. This proves the claim.

## Verification
Run `python3 check.py` from the same directory. The checker uses only the Python standard library, defines all graph vertices and edges explicitly, computes exact graph distances, checks pentagonal and hexagonal null-homotopies, enumerates all cliques, and verifies an actual sequence of 120 elementary collapses. It prints `PASS` for each finite certificate and the stated result. All enumerations and comparisons are integral and exact; no floating-point, truncated search, or random sampling enters the proof. The simple-connectivity and Whitehead deductions are mathematical arguments in the preceding section, not claims made by the program's assertions.

## Relationship to prior work
Saleh, Titz Mite, and Witzel (first public version 2023-02-28) classify the vertex-set Rips homotopy types of the five Platonic solids and explicitly suggest Archimedean solids as another direction. The truncated icosahedron is Archimedean rather than Platonic, and their classifications neither include this sixty-vertex graph nor imply the wedge rank here. Their inclusive-versus-open Rips distinction agrees with the convention fixed above. Adamaszek's 2011 graph-powers manuscript (subsequently published in 2013) proves a scale-two collapse to the original graph when the girth is at least seven, or when every clique of the graph square lies inside a closed neighborhood. Neither condition holds here: the graph has pentagonal cycles and associated five-vertex Rips cliques, larger than the four-vertex closed neighborhoods. Related published computations cover other polyhedral graphs, while published girth-at-least-six hexagon-packing formulas do not apply to this girth-five graph, whose hexagonal faces share edges. Goričan and Virk's theory of critical Rips edges addresses general persistence and does not give this specific higher-dimensional homotopy classification.

## Limitations
The proof concerns exactly one radius and the shortest-path metric on the graph vertices. It does not determine subsequent persistent maps or the action of the icosahedral symmetry group on the rank-21 integral homology. The computational component certifies the finite high-dimensional collapse, not a universal theorem about all fullerene graphs. The literature comparison cannot exclude unindexed or inaccessible equivalent computations; independent mathematical validation has not been performed.

## References
- Michał Adamaszek, *Clique complexes and graph powers*, *Israel Journal of Mathematics* **196** (2013), 295–319, arXiv:1104.0433, https://arxiv.org/abs/1104.0433.
- Nada Saleh, Thomas Titz Mite, Stefan Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public version 2023-02-28), https://arxiv.org/abs/2302.14388. Primary classification 55N31.
- Peter Goričan and Žiga Virk, *Critical Edges in Rips Complexes and Persistence*, *Mediterranean Journal of Mathematics* **20** (2023), article 326, https://doi.org/10.1007/s00009-023-02533-9.
- Dmitry Kozlov, *Organized Collapse: An Introduction to Discrete Morse Theory*, AMS, 2020, for elementary simplicial collapses and their homotopy invariance.
