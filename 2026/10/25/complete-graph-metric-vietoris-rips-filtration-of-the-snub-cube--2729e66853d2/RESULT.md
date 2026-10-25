# Complete graph-metric Vietoris–Rips filtration of the snub cube

## Finding
Let \(G\) be the skeleton of the chiral snub cube, equipped with the unweighted shortest-path metric. Its complete **inclusive graph-distance** Vietoris–Rips filtration is
\[
\operatorname{VR}_{\le r}(V(G),d_G)\simeq
\begin{cases}
\bigvee^{23}S^0,&0\le r<1,\\
\bigvee^5 S^1,&1\le r<2,\\
S^2,&2\le r<3,\\
\bigvee^5 S^5,&3\le r<4,\\
\ast,&r\ge4.
\end{cases}
\]
In particular, the nontrivial reduced integral homology occurs in three distinct positive dimensions at three consecutive graph-distance scales. This is a homotopy-type determination, not only a field-dependent Betti-number calculation.

## Assumptions and scope
The snub cube is the Archimedean solid with 24 vertices, 60 edges, 32 triangular faces and six square faces. To fix a reproducible labeling, let \(t\) be the unique root in \((0,1)\) of \(t^3+t^2+t=1\), and consider the 24 signed coordinate permutations of \((1,t,t^{-1})\) for which even coordinate permutations have an even number of positive signs and odd coordinate permutations have an odd number. Join points with squared Euclidean separation less than \(7/2\). This is precisely its nearest-neighbor graph: the first squared-distance shell is approximately \(2.591\), and the second is approximately \(5.182\). The attached checker uses rational interval inequalities to certify the strict separating threshold without relying on floating-point edge tests.

For any real \(r\ge0\), \(\operatorname{VR}_{\le r}\) contains a face exactly when each pair of its vertices has graph distance at most \(r\). The coordinate model identifies one handedness; both chiral copies have isomorphic graphs. All homotopy equivalences are ordinary nonequivariant integral homotopy equivalences.

## Proof
**Metric thresholds.** Exact signed-permutation enumeration constructs a connected five-regular 24-vertex, 60-edge graph of diameter four. Since all graph distances are integers, the filtration changes only at \(r=1,2,3,4\). For \(0\le r<1\), there are 24 isolated vertices. At \(r\ge4\), every pair is adjacent in the Rips graph, giving a 23-simplex.

**Scale one.** The clique complex of \(G\) has exactly 24 vertices, 60 edges and 32 triangles, with no higher simplices. A deterministic sequence of 40 elementary free-face collapses leaves a connected graph with 16 vertices and 20 edges. Its first Betti number is \(20-16+1=5\), so its homotopy type is \(\bigvee^5S^1\). Each collapse is certified as a free codimension-one face of a maximal coface at the moment of removal.

**Scale two.** The face counts in dimensions zero through five are \((24,156,400,474,264,56)\). A deterministic sequence of 662 elementary collapses leaves a two-dimensional simplicial subcomplex with ten vertices, 24 edges and 16 triangles. It is connected; every edge lies in precisely two triangles; and each vertex link is a connected cycle. Hence it is a closed connected triangulated surface. Its Euler characteristic is \(10-24+16=2\), so by the classification of closed surfaces it is \(S^2\). This proves the asserted homotopy equivalence.

**Scale three.** Face counts in dimensions zero through nine are \((24,240,1304,4218,8400,10352,7800,3498,872,96)\), totaling 36,804 nonempty faces. Pair nonempty faces by toggling the first available vertex in the explicit fixed order \((14,0,17,7,6,11,22,21,10,4,2,20,3,19,5,18,9,23,15,16,8,1,13,12)\), processing remaining faces in each stage by increasing dimension. Exactly 18,399 pairs are formed; the critical cells consist of one vertex and five dimension-five simplices.

A complete directed-gradient-path test establishes acyclicity: make a directed graph whose vertices are matched lower faces \(\sigma\), putting an arrow from \(\sigma\) to a different matched lower face \(\sigma'\) whenever \(\sigma'\) is a facet of the upper partner of \(\sigma\). All 18,399 vertices are removed by topological sorting. Any closed Forman gradient path would give a directed cycle in this graph (necessarily within adjacent dimensions). Therefore the matching is acyclic. Discrete Morse theory yields a CW model with one zero-cell and five five-cells, necessarily \(\bigvee^5S^5\): the attaching maps land in the point because no cells occur in dimensions one through four.

## Verification
The included standalone `snub_certificate.py` uses only Python's standard library. Execute `python3 snub_certificate.py` from the extracted package. It reconstructs signed-permutation vertices, certifies the algebraic-root interval and all adjacency decisions by exact rational inequalities, enumerates every Rips face through radius three, checks all elementary collapses and all surface links, constructs the full scale-three matching, and performs a global acyclicity topological sort. The script prints `PASS` only after all assertions pass. It has been executed successfully from the packaged source path. Its output includes the precise counts stated in the proof.

## Relationship to prior work
Saleh, Titz Mite and Witzel's *Vietoris–Rips complexes of Platonic solids* (public preprint 28 February 2023) gives a complete filtration for the five Platonic solids and explicitly suggests Archimedean solids as a further direction. The snub cube is Archimedean but not Platonic, and is absent from that theorem and its detailed case analysis. Published calculations for the truncated octahedron and the cuboctahedron treat different graphs or Euclidean metrics; they do not imply this graph-metric snub-cube classification. A published result on the ordinary independence complex of the **snub-cubical graph** concerns \(\operatorname{Ind}(G)\), whereas the present radius-three Rips complex is the independence complex of the graph joining *distance-four pairs*, which is a different, cubic 24-vertex graph. These are different complexes with distinct homology, not alternative names for the same invariant.

## Limitations
The theorem determines nonequivariant homotopy types, not a full symmetry representation or explicit maps between stages beyond the implied homology-degree vanishings. The computer-assisted proof is a finite exhaustive combinatorial certificate, not a claim about all Archimedean solids. Novelty was evaluated against the inspected primary paper and indexed records; equivalent unindexed or inaccessible prior work cannot be ruled out categorically. An independent audit has not been performed.

## References
- N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (public 2023-02-28), https://arxiv.org/pdf/2302.14388.
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
- D. N. Kozlov, *Organized Collapse: An Introduction to Discrete Morse Theory*, American Mathematical Society, 2020.
- *Snub cube*, standard signed-permutation coordinate realization, https://en.wikipedia.org/wiki/Snub_cube.
