# Complete integral Vietoris–Rips persistence of the icosidodecahedral graph

## Finding

Let \(D=GP(10,2)\) be the dodecahedral graph, let \(I=L(D)\) be its line graph (the icosidodecahedral graph), and endow the \(30\) vertices of \(I\) with shortest-path distance. Write \(\mathcal R_t\) for the inclusive Vietoris–Rips complex of this metric, so a vertex set is a face precisely when every pair is separated by graph distance at most \(t\). For every real \(t\geq0\), the integral homotopy types are
\[
\mathcal R_t\simeq
\begin{cases}
\bigvee^{29} S^0,&0\leq t<1,\\
\bigvee^{11} S^1,&1\leq t<2,\\
S^2,&2\leq t<4,\\
S^{14},&4\leq t<5,\\
\ast,&5\leq t.
\end{cases}
\]
The inclusion \(\mathcal R_2\hookrightarrow\mathcal R_3\) induces an isomorphism on second integral homology, with multiplier \(+1\) for the displayed reproducible fundamental-cycle orientations (and hence multiplier \(\pm1\) independent of orientation choices). Therefore all positive-dimensional reduced integral persistence intervals are exactly eleven copies of \([1,2)\) in degree one, one copy of \([2,4)\) in degree two, and one copy of \([4,5)\) in degree fourteen. In degree zero there are twenty-nine reduced intervals \([0,1)\). No torsion occurs.

## Assumptions and scope

Vertices of \(D\) are labeled \(u_i,v_i\), where \(i\in\mathbb Z/10\mathbb Z\). Edges are \(u_i u_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), for all \(i\). A vertex of \(I\) is an edge of \(D\); two vertices of \(I\) are joined when the corresponding edges of \(D\) meet. Distances are shortest-path distances in \(I\), **not** Euclidean distances in an embedding and **not** shortest-path distances in \(D\). The scale convention is \(d\leq t\), with equality admitted. All complexes are abstract finite simplicial complexes, all homology assertions use integer coefficients, and interval endpoints have the usual half-open convention. The claim is for this one canonical graph and every scale, not an arbitrary line graph.

## Proof

**Finite model and exact enumeration.** Construct the thirty edges of \(D\) from the three indexed families above, lexicographically order them, join incident pairs to make \(I\), and run breadth-first search from each of its thirty vertices. The resulting connected graph has sixty edges and diameter five. Given integer \(r\), enumerate faces of \(\mathcal R_r\) by extending increasing tuples only with vertices adjacent to every tuple vertex in the distance-\(r\) graph. This generates every clique exactly once. The nonzero face vectors \((f_0,f_1,\ldots)\) at scales one, two and three are respectively
\[
(30,60,20),\qquad (30,180,380,330,102),\qquad
(30,300,1340,3150,4374,3800,2100,720,140,12).
\]
The complete enumerator and all elementary-collapse checks are supplied in `verify_icosidodeca_rips.py` and require only the Python standard library.

**Scale one.** Every one of the twenty triangles corresponds to the three graph edges at one trivalent vertex of \(D\). Each edge of \(I\) is contained in exactly one of these triangles. Remove any one of its edges together with the triangle, for each triangle. These twenty elementary simplicial collapses leave a connected graph with thirty vertices and forty edges; its cycle rank is \(40-30+1=11\). Hence \(\mathcal R_1\simeq\bigvee^{11}S^1\).

**Scales two and three.** At scale two the deterministic verifier repeatedly chooses a codimension-one face \(\sigma\) with **exactly one coface** \(\tau\), where \(\tau\) is maximal among currently remaining simplices, and removes \((\sigma,\tau)\). This is an elementary strong deformation retraction. The complete procedure removes exactly \(468\) pairs and retains a two-dimensional simplicial complex having sixteen vertices, forty-two edges and twenty-eight triangles. Each edge belongs to exactly two triangles, the link of each vertex is a single circle, all triangles are connected through shared edges, and the oriented triangle adjacency relations are globally consistent. Thus the remainder is a connected closed orientable surface of Euler characteristic \(16-42+28=2\), hence \(S^2\).

At scale three the same fully checked procedure removes exactly \(7940\) pairs and leaves another orientable sixteen-vertex, forty-two-edge, twenty-eight-triangle triangulated \(S^2\). The full initial scale-three complex has \(15966\) nonempty faces, so \(15966-2(7940)=86\) residue faces, exactly \(16+42+28\). Every pair is rechecked at removal time for uniqueness of the codimension-one coface and maximality of its partner; the procedure therefore certifies a homotopy equivalence, not only matching Betti numbers.

**Persistent degree.** Orient the triangles of the scale-two remainder so each common edge has opposite induced coefficients, and sum these twenty-eight signed triangles to obtain a primitive integral fundamental cycle \(z_2\) in \(\mathcal R_2\). Regard \(z_2\) as a chain in \(\mathcal R_3\). Reverse neither collapse: instead, project the chain sequentially along the scale-three elementary collapses. For every removed free triangle \(\sigma\) of a tetrahedron \(\tau\), replace \(\sigma\) by the negative of the other three oriented boundary triangles of \(\tau\), divided by the boundary coefficient \(\varepsilon_{\sigma,\tau}\in\{+1,-1\}\). A removed triangle \(\tau\) paired with a free edge has zero coefficient in a two-cycle and maps to zero. These are precisely the integral chain maps of elementary simplicial collapses. The exact computation produces the primitive oriented fundamental cycle of the scale-three remainder with coefficient \(+1\) on every oriented triangle. It proves that the inclusion induces multiplication by \(+1\) on \(H_2\) in these orientations and an isomorphism over \(\mathbb Z\).

**Scale four and completion.** The distance matrix shows that each vertex of \(I\) has exactly one other vertex at distance five, and these form fifteen disjoint unordered pairs. Consequently, the graph of \(\mathcal R_4\) is the complete graph on thirty vertices with just that perfect matching removed. Its clique complex is the join of fifteen zero-spheres, the boundary complex of the fifteen-dimensional crosspolytope, hence \(S^{14}\). At scale five every pair is an edge and \(\mathcal R_5\) is a full simplex. Below scale one there are thirty isolated vertices. By integer-valued graph distances, the stages are constant on the indicated intervals. These facts and the scale-two-to-three integral map determine all reduced integral persistence intervals.

## Verification

Run `python verify_icosidodeca_rips.py` using Python 3.9 or later; its complete output is embedded as `verification_output.txt`. The program independently regenerates the thirty graph vertices, all-pairs shortest-path distances, exact face sets, every elementary-collapse pair and remaining vertex links, fundamental cycles, integer chain transfers, and the fifteen distance-five pairs. Its successful final line is `VERIFIED_OK`. This is exhaustive finite verification of a uniquely specified thirty-vertex complex and its indicated chain map; it is not a Monte Carlo sample, an extrapolation to other graphs, or an independent external review.

## Relationship to prior work

Adamaszek's *Clique complexes and graph powers* (public 2011-04-03; arXiv:1104.0433) studies clique complexes of graph powers. Its cycle-power classification does not cover the icosidodecahedral graph, which is not a cycle; its line-graph statement concerns ordinary line-graph clique complexes, not the second- and third-power stages or the induced integral persistence map. The *Icosidodecahedral Graph* entry in MathWorld identifies this 30-vertex, 60-edge graph as the line graph of the dodecahedron. Existing calculations for dodecahedral, cuboctahedral, truncated-octahedral, rhombicuboctahedral and Dürer graph complexes concern different graphs, metrics, or Čech constructions. None of these statements determines the complete graph-metric filtration and the nontrivial integer inclusion map asserted here. This comparison is a best-knowledge novelty assessment, not a proof of publication priority.

## Limitations

The classification is specific to the shortest-path metric on \(L(GP(10,2))\). It says nothing about the Euclidean metric on an embedded icosidodecahedron, arbitrary graph powers, or naturality under every graph homomorphism. All finite computations and collapse checks are reproducible but have not received independent mathematical validation. An equivalent calculation may exist in unindexed or inaccessible literature.

## References

1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public version April 3, 2011, https://arxiv.org/abs/1104.0433.
2. E. W. Weisstein, *Icosidodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosidodecahedralGraph.html (graph identification and basic parameters).
3. H. Adams and M. Adamaszek, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (context for nontrivial filtration homotopy types; circular metric, not this graph).
