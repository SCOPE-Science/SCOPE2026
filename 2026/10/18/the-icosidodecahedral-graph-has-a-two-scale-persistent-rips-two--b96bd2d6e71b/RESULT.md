# The icosidodecahedral graph has a two-scale persistent Rips two-sphere

## Finding
Let \(D=GP(10,2)\) be the dodecahedral graph, let \(X=L(D)\) be its thirty-vertex line graph (the icosidodecahedral graph), and let \(\operatorname{VR}_{\le r}(X)\) be the Vietoris–Rips complex of its shortest-path metric with inclusive threshold \(r\ge0\). There are homotopy equivalences
\[
\operatorname{VR}_{\le r}(X)\simeq
\begin{cases}
\bigvee^{29}S^0,&0\le r<1,\\
\bigvee^{11}S^1,&1\le r<2,\\
S^2,&2\le r<4,\\
S^{14},&4\le r<5,\\
\ast,&r\ge5.
\end{cases}
\]
The inclusion-induced integral homology map
\[
\widetilde H_2(\operatorname{VR}_{\le2}(X);\mathbb Z)
\longrightarrow\widetilde H_2(\operatorname{VR}_{\le3}(X);\mathbb Z)
\]
is an isomorphism of free rank-one groups. Thus, over **every field**, the complete reduced persistence barcode comprises exactly twenty-nine degree-zero intervals \([0,1)\), eleven degree-one intervals \([1,2)\), one degree-two interval \([2,4)\), and one degree-fourteen interval \([4,5)\). The unique distance-five antipodal involution acts by \(-1\) on the degree-two homology at both integer thresholds \(2\) and \(3\), and by \(-1\) on degree-fourteen homology at threshold \(4\).

## Assumptions and scope
The graph \(D\) has outer vertices \(u_i\) and inner vertices \(v_i\), indexed by \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). The graph \(X=L(D)\) has one vertex for each of the thirty edges of \(D\), two being adjacent exactly when their original edges meet. Distances are intrinsic shortest-path distances in \(X\), **not Euclidean distances between the vertices of an embedded polyhedron**. A nonempty vertex set is a simplex at scale \(r\) precisely when all its pairwise graph distances are at most \(r\); the empty face is included. All stated homotopy types are ordinary, nonequivariant homotopy equivalences, while the specified antipodal actions are on integral homology.

## Proof
**Complete enumeration and free-face collapse.** The reproducible verifier enumerates cliques of all powers of \(X\) through radius \(3\), constructing every nonempty simplex. At radius \(1\) there are \(30,60,20\) faces of cardinalities \(1,2,3\). A supplied list of twenty free-face/coface pairs reduces this complex to a connected graph with thirty vertices and forty edges, hence \(\bigvee^{11}S^1\).

At radius \(2\) the face counts by cardinality are \((30,180,380,330,102)\). An explicit ordered list of \(471\) elementary collapse pairs leaves a two-dimensional complex with \((f_0,f_1,f_2)=(15,39,26)\). At radius \(3\) the cardinality counts are
\[
(30,300,1340,3150,4374,3800,2100,720,140,12).
\]
An ordered list of \(7964\) elementary collapse pairs leaves \((f_0,f_1,f_2)=(8,18,12)\). For each pair the certificate checker verifies that its lower face is contained in exactly one alive higher face, its upper face, which is maximal. Each remaining complex is connected through its triangle-adjacency graph; every edge occurs in precisely two triangles, every vertex link is a single cycle, and the Euler characteristic is \(2\). The classification of compact connected closed surfaces therefore identifies **both** remainders as triangulated two-spheres. Because elementary collapse preserves homotopy type, the two Rips complexes are homotopy equivalent to \(S^2\).

**Persistence degree.** Orient each residual sphere consistently so adjacent triangles induce opposite signs on their common edge. A free-face collapse of \(f\subset F\) induces the integral chain retraction that replaces \(f\) by the negative sum of the other facets of \(F\), divided by its boundary incidence \([F:f]=\pm1\), and sends \(F\) to zero. The certificate supplies the ordered collapses and both oriented fundamental cycles. Apply the radius-three retraction chain map to the radius-two fundamental cycle, viewed inside the radius-three complex. Its image is exactly \(+1\) times the oriented radius-three fundamental cycle (with the deterministic orientation conventions of the certificate). This uses \(62\) nontrivial coefficient substitutions and proves that the inclusion has degree \(+1\), up to the arbitrary choice of orientations. In particular it is an integral isomorphism, not just a nonzero map over selected fields.

**Final scales and symmetry.** Breadth-first graph distances show that \(X\) has diameter five and that each vertex has exactly one vertex at distance five. The fifteen forbidden unordered pairs at radius four form a perfect matching, while every other pair is at distance at most four. Consequently the radius-four complex is the join of fifteen copies of \(S^0\), homeomorphic to \(S^{14}\). The radius-five complex is the full simplex. The map sending each vertex to its unique distance-five partner is an involutory graph automorphism. Applying this permutation to the oriented radius-two and radius-three cycles and projecting through the respective collapse certificates gives degree \(-1\) at both scales. On the radius-four join it swaps all fifteen \(S^0\) factors, giving degree \((-1)^{15}=-1\).

## Verification
All numeric statements are exact and finite, not inferences from samples. Run `python3 verify.py` in the same directory as `collapse_certificate.json`. The Python standard library suffices. The script regenerates the graph and its complete distance table, enumerates all simplices at radii one through three, replays the supplied free-face certificates (twenty, \(471\), and \(7964\) pairs), checks both surface triangulations and integral fundamental cycles, and computes the inclusion degree and antipodal degrees by signed simplicial chain maps. The expected console record is `expected_output.txt`. The calculation concludes with `EXPLICIT_CERTIFICATE_REPLAY_OK` and `VERIFY_OK`.

## Relationship to prior work
Saleh, Mite, and Witzel classified the Vietoris–Rips complexes of **Platonic-solid vertex sets**, including the twenty-vertex dodecahedron, and expressly suggested the Archimedean solids as a further direction. Their dodecahedral graph at radius three is a different metric space and does not determine the radius-two-to-three inclusion for its thirty-vertex rectification. Goyal, Shukla, and Singh classified radius-one clique complexes of line graphs and imply the first positive-scale term here; the radius-one wedge of circles is accordingly not presented as the main new result. Adamaszek's line-graph theorem likewise concerns radius one. The present result is the complete intrinsic graph-metric filtration of a canonical Archimedean rectification, particularly the integer-persistent two-sphere and its exact integral inclusion degree. A search for equivalent formulations and stronger graph-power results did not identify prior coverage; nonindexed equivalent work remains possible.

## Limitations
This finite-graph theorem makes no assertion for Euclidean chordal distances, continuous point clouds on the icosidodecahedral surface, or all Archimedean solids. The supplied code verifies a finite explicit combinatorial certificate; it is not a formal proof assistant development. The full automorphism-group representation of the eleven-dimensional degree-one homology is not determined. The originality assessment remains conditional on the accessible literature and indexed research records.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first posted 2023-02-28), especially the introduction and Sections 2–4.
2. S. Goyal, S. Shukla, and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (first posted 2020-09-25), especially Lemma 3.2 and Corollary 3.3.
3. M. Adamaszek, *Extremal problems related to Betti numbers of flag complexes* (doctoral thesis, 2012), Section 7.5, Theorem 7.17.
