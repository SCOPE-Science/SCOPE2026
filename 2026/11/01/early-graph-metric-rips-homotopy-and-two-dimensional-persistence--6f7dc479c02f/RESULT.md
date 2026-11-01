# Early graph-metric Rips homotopy and two-dimensional persistence of the truncated icosahedron

## Finding
Let \(G\) be the edge graph of the truncated icosahedron (the buckminsterfullerene graph): it has \(60\) vertices, \(90\) edges, twelve pentagonal and twenty hexagonal faces. Give its vertices the shortest-path graph metric, in which every edge has length one. Write \(K_r=\operatorname{VR}_{\le r}(V(G),d_G)\) for the *inclusive* Vietoris--Rips complex: every finite vertex set of graph diameter at most \(r\) forms a simplex. The first nontrivial stages have integral homotopy types
\[
K_1\simeq\bigvee^{31}S^1,\qquad
K_2\simeq\bigvee^{21}S^2,\qquad
K_3\simeq S^2.
\]
Over \(\mathbb F_2\), restrict the degree-two persistence module of this filtration to integer thresholds \(0\) through \(6\). Its complete barcode consists of **twenty intervals \([2,3)\)** and **one interval \([2,6)\)**. A specific cycle triangulating the polyhedral boundary is nontrivial in degree-two homology at every scale from \(2\) through \(5\), and becomes a boundary at scale \(6\). The second-homology ranks at scales \(2,3,4,5,6\) are respectively \(21,1,1,1,0\).

## Assumptions and scope
All distances in this result are **graph shortest-path distances**, not Euclidean chord distances between the geometric polyhedron vertices. All complexes use the \(60\) graph vertices, not points in the edge interiors. Since graph distances are integers, the inclusive integer thresholds determine the filtration at real radii. The term *barcode through scale six* means restriction to the interval \(0\le r\le6\), so the claim does not rule out new classes at larger thresholds.

For an exact labeled construction, start with the icosahedral graph on twelve vertices: outer poles \(10,11\), two cyclic five-rings \(0,\ldots,4\) and \(5,\ldots,9\), and edges \(10-i\), \(11-(i+5)\), \(i-(i+1)\), \((i+5)-(i+6)\), \(i-(i+5)\), and \(i-((i-1)\bmod5+5)\), taking ring indices modulo five. The sixty vertices of \(G\) are the oriented edges \((u,v)\) of this icosahedron. Two darts are adjacent exactly if they are reversals \((u,v),(v,u)\), or share their tail \(u\) and their heads are adjacent in the icosahedron. This is the usual vertex truncation of the icosahedron. The executable verifier reconstructs the graph from these rules and finds diameter \(9\).

## Proof
**Scale one.** The truncated icosahedral graph is triangle-free and connected, so \(K_1\) is precisely its one-dimensional graph. Its first Betti number is \(90-60+1=31\); a spanning tree collapse proves \(K_1\simeq\bigvee^{31}S^1\).

**Exhaustive complexes at scales two and three.** Enumerate all subsets in increasing vertex order, retaining each one exactly when every pair lies at graph distance at most the scale. The face vectors, indexed by dimensions from zero, are
\[
 f(K_2)=(60,270,340,120,12),\qquad
 f(K_3)=(60,510,1540,2190,1572,530,60).
\]
A deterministic finite acyclic face-poset matching pairs a face \(\sigma\) with \(\sigma\cup\{v\}\) when both remain unmatched, choosing at each round the vertex \(v\) admitting the largest number of such pairs and processing all its pairs together. The complete directed Hasse diagram is then oriented upward along matching pairs and downward along every other incidence; the standalone verifier topologically sorts the entire resulting directed graph. At scale two it verifies \(375\) matched pairs among \(802\) nonempty faces, leaving critical cells in dimensions \(0,1,2\) in counts \(4,15,33\); all \(2100\) nonempty Hasse incidences are checked and acyclicity holds. At scale three it verifies \(3226\) pairs among \(6462\) nonempty faces, leaving \(2,4,4\) critical cells in those dimensions; the entire \(25860\)-incidence directed Hasse graph is acyclic. There are no critical cells of dimension greater than two at either scale. Discrete Morse theory therefore supplies a connected two-dimensional CW model for each complex.

**Simple connectivity, not just homology.** Independently choose a breadth-first spanning tree in each graph-power one-skeleton. Contracting the tree makes its \(59\) edge generators trivial. Every two-simplex forces its third boundary-edge generator to be trivial whenever the other two are trivial. The checker repeats this elementary triangular implication until all generators are trivial: all \(270\) scale-two edges are eliminated after six sweeps, and all \(510\) scale-three edges after four. These are actual finite presentations of their fundamental groups, because the fundamental group depends only on the two-skeleton. Thus both complexes are simply connected.

The Euler characteristics are \(\chi(K_2)=22\) and \(\chi(K_3)=2\), computed from the complete face vectors. Since their two-dimensional CW models are simply connected, each model has free second integral homology with rank \(\chi-1\), and no homology in degrees greater than two. A simply connected two-dimensional CW complex is homotopy equivalent to a wedge of two-spheres: represent an integral second-homology basis by maps of spheres via Hurewicz, obtain a homology equivalence from a wedge of spheres, and apply Whitehead's theorem. This proves the two asserted homotopy types, including the integral statement.

**Exact degree-two persistence through scale six.** For each integer scale \(r\in\{2,3,4,5,6\}\), enumerate all graph-power edges \(E_r\), triangles \(T_r\), and tetrahedra \(Q_r\). The second simplicial homology depends only on the boundaries \(\partial_2:\mathbb F_2^{T_r}\to\mathbb F_2^{E_r}\) and \(\partial_3:\mathbb F_2^{Q_r}\to\mathbb F_2^{T_r}\), irrespective of higher-dimensional simplices. Exact bit-vector elimination gives

| Radius | Edges | Triangles | Tetrahedra | rank \(\partial_2\) | rank \(\partial_3\) | \(\beta_2\) |
|---|---:|---:|---:|---:|---:|---:|
| 2 | 270 | 340 | 120 | 211 | 108 | 21 |
| 3 | 510 | 1540 | 2190 | 451 | 1088 | 1 |
| 4 | 810 | 4460 | 13110 | 751 | 3708 | 1 |
| 5 | 1110 | 9320 | 44250 | 1051 | 8268 | 1 |
| 6 | 1410 | 17300 | 126930 | 1351 | 15949 | 0 |

Here \(\beta_2=|T_r|-\operatorname{rank}\partial_2-\operatorname{rank}\partial_3\). The rank computations are exhaustive finite computations with integer bitsets, not statistical estimates. The other thresholds up to radius one have no two-simplices, hence zero second homology.

The twelve pentagons can each be filled by three fan triangles and the twenty hexagons each by four triangles with graph-distance-two diagonals. This gives an explicit \(116\)-triangle mod-two cycle \(z\in C_2(K_2;\mathbb F_2)\) representing the polyhedral boundary. The checker verifies directly that its boundary is zero, that its constituent triangles occur already at scale two, and that its chain vector is **not** in \(\operatorname{im}\partial_3\) at radii \(2,3,4,5\), but is in that image at radius \(6\). Therefore the inclusion maps preserve a common nonzero class through radius five. Since target \(H_2\) has dimension one at radii \(3,4,5\), each intervening map has rank one. At radius three the degree-two rank drops from \(21\) to \(1\), killing precisely twenty intervals born at radius two. The last nonzero class dies at radius six. This establishes the specified restricted barcode.

## Verification
Run the standalone `verify_buckyball_rips.py` with Python 3, using only the standard library. It rebuilds the graph and distances from the twelve-vertex construction, enumerates all \(802\) and \(6462\) faces at radii two and three, verifies every matching pair and all oriented Hasse covers, performs a complete directed-acyclicity topological sort, and carries out an independent triangular fundamental-group-generator elimination. For radii two to six it enumerates every graph-power edge, triangle, and tetrahedron; performs exact mod-two boundary-rank reduction; verifies a specific \(116\)-triangle surface cycle; and independently tests whether that cycle lies in each three-boundary image. The recorded output in `verification_output.txt` ends with `BUCKYBALL_RIPS_EARLY_TOPOLOGY_AND_PERSISTENCE_VERIFIED`. Running the script regenerates its checks without relying on separately stored face lists, proprietary software, or unverified source data.

## Relationship to prior work
Saleh, Titz Mite, and Witzel study graph-metric Vietoris--Rips complexes of the five Platonic solids and point to Archimedean solids as further objects. The truncated icosahedron is Archimedean and is not among their cases. Saleh's 2023 dissertation studies related Platonic and higher-dimensional examples but does not provide this computation. Adamaszek's graph-power framework expresses Rips complexes as clique complexes and proves high-girth stability. The truncated-icosahedral graph contains pentagons (girth five), so its higher-girth stabilization theorem does not apply. A published result about graphs of girth at least six with edge-disjoint six-cycles also does not apply, because this graph has five-cycles and its hexagons share edges.

Previously published calculations for the truncated tetrahedron, truncated octahedron and rhombicuboctahedron concern different vertex sets and different graphs. Their homotopy statements cannot be specialized or transported to this sixty-vertex graph. Searches of graph-metric, clique-of-graph-power, fullerene, polyhedral, and exact Betti/persistence formulations did not identify a covering theorem; that negative search is not a proof of universal novelty.

## Limitations
The homotopy classifications are proved only at radii one, two and three. The degree-two barcode is computed over \(\mathbb F_2\) **only through radius six**, not for the full diameter-nine filtration; other homology degrees and integral persistence maps at later scales are not determined. The two- and three-dimensional ranks at radii four to six do not imply a homotopy type. The explicit matching is a discrete-Morse matching, not a claimed sequence of elementary collapses onto the geometric boundary. Its matching-pair count is not asserted to be minimal. A bibliography search cannot exclude unindexed equivalent work, and there is no independent audit.

## References
1. Nada Saleh, Thomas Titz Mite, and Stefan Witzel, *Vietoris--Rips complexes of Platonic solids*, arXiv:2302.14388v1, first public 2023-02-28 (primary MSC 55N31).
2. Nada Saleh, *On Vietoris--Rips Complexes of the 2-Sphere*, doctoral dissertation, 2023.
3. Michal Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1, first public 2011-04-03; *Israel Journal of Mathematics* 196 (2013), 295--319.
4. Published mathematical record, *Complete graph-metric Vietoris--Rips filtration of the truncated octahedral graph*, 2026; inspected for different-graph comparison.
5. Published mathematical record, *An explicit scale-two Rips collapse onto the rhombicuboctahedral sphere*, 2026; inspected for different-graph comparison.
6. Published mathematical record, *A hexagon-packing classification of scale-two graph Rips complexes*, 2026; inspected for hypothesis comparison.
