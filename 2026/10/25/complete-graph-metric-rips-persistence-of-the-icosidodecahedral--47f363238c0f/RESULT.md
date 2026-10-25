# Complete graph-metric Rips persistence of the icosidodecahedral graph

## Finding
Let \(G\) be the graph of the convex icosidodecahedron, equivalently the rectification graph of the icosahedron or the line graph of the dodecahedral graph. Give each edge length one, let \(d_G\) be shortest-path distance, and for real \(r\ge0\) let \(K_r=\operatorname{VR}_{\le r}(G)\) contain exactly the nonempty vertex subsets of pairwise distance at most \(r\).

The **complete integral homotopy filtration** is
\[
K_r\simeq
\begin{cases}
\bigvee^{29}S^0,&0\le r<1,\\
\bigvee^{11}S^1,&1\le r<2,\\
S^2,&2\le r<4,\\
S^{14},&4\le r<5,\\
\ast,&r\ge5.
\end{cases}
\]
More strongly, the **actual inclusion** \(K_2\hookrightarrow K_3\) is a homotopy equivalence. Consequently reduced persistent homology with integral coefficients has precisely 29 degree-zero bars \([0,1)\), 11 degree-one bars \([1,2)\), one degree-two bar \([2,4)\), and one degree-fourteen bar \([4,5)\). The same interval statement holds over every field.

## Assumptions and scope
The graph is fixed combinatorially. Start with the icosahedral graph on labels \(0,\ldots,11\) whose thirty edges are specified explicitly in `verify.py`. Make these thirty edges the vertices of \(G\); two are adjacent when they lie together in a triangular face of the icosahedron. This is the standard rectification, with thirty vertices, sixty edges, twenty triangular faces, twelve pentagonal faces, and diameter five. It is also abstractly isomorphic to the line graph of the dodecahedron. The Rips filtration uses **graph distance**, not Euclidean chord or spherical distance. All thresholds are inclusive; since all distances are integers, the displayed intervals cover every real \(r\ge0\).

## Proof
**Combinatorial construction.** The explicit icosahedral edge list in `verify.py` has twelve vertices of degree five and twenty triangular faces. Taking its edge midpoints and joining those in a common triangular face gives the rectified graph. Exact breadth-first search gives diameter five. Enumerating every clique in the distance-power graphs gives the following nonempty face vectors in increasing dimension:
\[
\begin{aligned}
f(K_1)&=(30,60,20),\\
f(K_2)&=(30,180,380,330,102),\\
f(K_3)&=(30,300,1340,3150,4374,3800,2100,720,140,12).
\end{aligned}
\]
These counts are reproducible from the full algorithm, rather than inferred from Euler characteristics.

**Scales zero and one.** Before the first positive threshold the complex is thirty isolated points. At threshold one, the only two-dimensional faces are twenty triangles, and each of the sixty edges is in exactly one such triangle. Collapse each triangle along one of its free edges. The result is a connected graph with thirty vertices and forty edges, hence a wedge of \(40-30+1=11\) circles. This scale-one fact also follows from the general line-graph clique-complex theorem of Adamaszek [2], since \(G\) is the line graph of the dodecahedral graph; its inclusion here records the filtration, not a new discovery of this elementary stage.

**Scale two.** Enumerate all 1,022 nonempty simplices. Starting from the complete face set, for \(v=0,1,\ldots,29\) successively pair every currently unpaired face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), if both are still present, processing lower-face integer bitmasks in increasing order. This produces 510 pairs and exactly two critical faces: one vertex and one triangle. A topological sort of the entire Hasse graph, oriented upward on matched covers and downward otherwise, visits all 1,022 faces; thus the matching is acyclic. Discrete Morse theory supplies a CW model with exactly one zero-cell and one two-cell, hence \(K_2\simeq S^2\).

**Scale three.** The same fully specified matching on all 15,966 nonempty faces produces 7,981 pairs. The remaining critical cells consist of one vertex, two triangles and one tetrahedron. The oriented Hasse graph again passes an exhaustive directed-acyclicity test. In the oriented critical triangle basis ordered by increasing face bitmask, the exact signed Morse boundary from the unique critical three-cell is
\[
\partial^{\mathrm M}_3=\begin{pmatrix}1\\-1\end{pmatrix}.
\]
The signed coefficient is obtained from the usual gradient-path elimination: for a matched lower triangle \(\sigma\) and upper tetrahedron \(\tau\), with incidence \(\epsilon=[\tau:\sigma]\in\{-1,1\}\), substitute
\[
[\sigma]=-\epsilon^{-1}\sum_{\substack{\eta\prec\tau\\\eta\ne\sigma}}[\tau:\eta][\eta],
\]
recursively until only critical triangles remain; triangles matched downward project to zero. Exhaustive directed acyclicity makes this recursion terminate. `verify.py` evaluates the complete signed expression, not a field-rank approximation. The critical CW two-skeleton is \(S^2\vee S^2\). Its three-cell has primitive attaching vector \((1,-1)\) in \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\), so cancelling one sphere with the three-cell leaves \(K_3\simeq S^2\). In particular its integral homology is torsion-free.

**The inclusion from scale two to three.** Triangulate the polyhedral two-sphere by its twenty original triangles and a fan of three triangles inside each of its twelve pentagons. The resulting oriented fundamental cycle \(z\) contains 56 triangles on 84 edges; the checker constructs its coherent orientations and verifies every edge cancels in \(\partial z\). Define integral cochains on all two-simplices of \(K_2\) and \(K_3\) by signed Morse projection to critical triangles (sum of the two critical coordinates at scale three). Rather than assume they are cocycles, the checker verifies their coboundaries vanish on **every** original three-simplex: 330 at scale two and 3,150 at scale three. The cochain evaluations on \(z\) are, respectively, \(+1\) and \(-1\); the unreduced scale-three Morse coordinates of \(z\) are \((-1,0)\), while the relation is \((1,-1)\). Therefore \([z]\) is a primitive generator of both rank-one integral degree-two homology groups. The inclusion induces multiplication by \(\pm1\); as both spaces are homotopy equivalent to \(S^2\), it is a homotopy equivalence.

**Scales four and five.** The only unordered vertex pairs at graph distance five form exactly fifteen disjoint pairs covering all thirty vertices; `verify.py` checks each pair and its uniqueness. Thus \(K_4\) is the join of fifteen copies of \(S^0\), the boundary of the fifteen-dimensional cross-polytope, and is \(S^{14}\). At scale five all vertex pairs are present, so \(K_5\) is a full simplex. Together with the previously established inclusion, these observations determine every reduced integral persistence map and every interval.

## Verification
Run `python3 verify.py` using only the Python standard library. The program reconstructs the graph from the thirty given icosahedral edges, computes the complete thirty-by-thirty distance matrix, enumerates every face at scales one, two and three, executes both fully deterministic matchings, and checks acyclicity on the entire oriented Hasse graphs. It also computes the signed integral Morse boundary at scale three and an explicitly orientable surface cycle. For the persistence map it constructs integer cocycles and checks vanishing against **all** original three-simplex boundaries, then evaluates them on the sphere cycle. Finally it enumerates all fifteen distance-five antipodal pairs. No floating-point algebra, sample-only inference, or external data are used. A complete successful replay prints all finite totals and exits without an assertion failure.

## Relationship to prior work
Saleh, Titz Mite and Witzel [1] classified Vietoris–Rips complexes of the five Platonic solids and identified Archimedean solids as a possible extension. They did not classify this 30-vertex rectification or its persistence maps. Adamaszek [2] treats graph powers, including ordinary clique complexes of line graphs, which accounts for the known radius-one homotopy type; its line-graph theorem is **not** a theorem about powers of those line graphs and does not imply the radius-two or radius-three calculation. Adams and Virk [3] establish a different persistence behavior for hypercube graphs, where inclusion maps across strictly increasing integer scales are null-homotopic. The long-surviving \(S^2\) of this rectified polyhedral graph shows that this nullity is not a general feature of graph-metric Rips filtrations.

Published computations for other Archimedean polyhedra and for the scale-two graph Čech nerve of line graphs concern different graphs or a different filtration functor. No inspected source determines the simultaneous \(K_2\), \(K_3\) and **nonzero inclusion-map** classification here. This is a comparison of the mathematical implications, not a claim that search results establish global novelty.

## Limitations
The result is a finite, exact classification of this particular canonical graph. It is not a uniform theorem for all Archimedean solids, line graphs, or arbitrary rectifications. It uses shortest-path distance rather than ambient Euclidean distance, and makes no claim about equivariant homotopy or integral group actions. Computer-assisted verification exhausts a precisely specified finite complex and relies on standard discrete-Morse and CW attachment theorems. Equivalent results absent from accessible indexing remain a possible originality risk; no independent audit has been performed.

## References
[1] N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public 2023-02-28. https://arxiv.org/abs/2302.14388

[2] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v3, Section 5, especially Theorem 5.2. https://arxiv.org/html/1104.0433v3

[3] H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, arXiv:2309.06222v1. https://arxiv.org/abs/2309.06222

[4] E. W. Weisstein, *Icosidodecahedral Graph*, MathWorld; graph order, size, diameter and line-graph identification. https://mathworld.wolfram.com/IcosidodecahedralGraph.html
