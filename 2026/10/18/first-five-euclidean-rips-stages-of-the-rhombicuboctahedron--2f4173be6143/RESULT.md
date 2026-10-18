# First five Euclidean Rips stages of the rhombicuboctahedron

## Finding
Let \(P\subset\mathbb R^3\) be the 24 vertices obtained by permuting the coordinates of \((\pm(1+\sqrt2),\pm1,\pm1)\), with independent signs. For every real \(r\ge0\), write \(K_r=\operatorname{VR}_{\le r}(P)\) for the **inclusive Euclidean**, not graph-distance, Vietoris–Rips complex. Then
\[
K_r\simeq
\begin{cases}
\bigsqcup^{24}\{\mathrm{pt}\},&0\le r<2,\\
\bigvee^{17}S^1,&2\le r<2\sqrt2,\\
S^2,&2\sqrt2\le r<\sqrt{12+8\sqrt2},\\
\bigvee^{7}S^3,&\sqrt{12+8\sqrt2}\le r<\sqrt{16+8\sqrt2}.
\end{cases}
\]
At squared radii \(8+4\sqrt2\) and \(12+4\sqrt2\), which lie strictly within the \(S^2\)-range, the inclusions from the squared-radius-eight complex are **simple-homotopy equivalences**: explicit relative elementary collapses retract each larger complex onto that same included smaller complex. The unique integral degree-two class consequently persists across both intermediate critical scales, then dies at squared radius \(12+8\sqrt2\), where seven integral degree-three generators appear. The latter homotopy equivalence to a wedge of seven three-spheres is an integral statement, not an inference from field Betti numbers alone.

## Assumptions and scope
The point set is not rescaled. The 24 points are indexed by sorting their triples of coordinates in increasing real lexicographic order, with the coordinate order \(-(1+\sqrt2)<-1<1<1+\sqrt2\). For a nonempty finite subset \(\sigma\subseteq P\), the simplex \(\sigma\in K_r\) occurs exactly when every two vertices in \(\sigma\) have Euclidean distance at most \(r\). There are precisely seven nonzero squared pairwise distances, in strictly increasing order:
\[
4,\quad8,\quad8+4\sqrt2,\quad12+4\sqrt2,\quad12+8\sqrt2,\quad16+8\sqrt2,\quad20+8\sqrt2.
\]
Their pair multiplicities are respectively \(48,36,48,48,36,48,12\). The finding concerns only the five stages at the first five values and the open intervals until the sixth. No assertion is made at the sixth or seventh distance thresholds.

## Proof
**Exact metric and first nonzero stage.** Write every coordinate as an ordered integer pair \((a,b)\), representing \(a+b\sqrt2\), and compute squared differences using \((a+b\sqrt2)^2=a^2+2b^2+2ab\sqrt2\). This gives the seven values and multiplicities above without any floating-point comparisons. At squared radius four the clique complex has \(24\) vertices, \(48\) edges, and exactly \(8\) triangular faces; no higher faces occur. A listed sequence of \(8\) elementary free-edge/triangle collapses leaves a connected graph with \(24\) vertices and \(40\) edges, hence a wedge of \(40-24+1=17\) circles.

**Geometric two-sphere and its persistence.** At squared radius eight the complex has face vector \((24,84,80,18)\). Its eight old triangle facets remain, and the vertices of each of the \(18\) square facets of the convex rhombicuboctahedron form a tetrahedron. Choose the lexicographically smaller of each square's two diagonals; the eight triangular faces plus the resulting \(36\) triangles make a connected triangulated surface \(T\) with face vector \((24,66,44)\). An exact finite check verifies that every edge of \(T\) lies in two triangles, each vertex link is one cycle, and its Euler characteristic equals two. Thus \(T\cong S^2\). A listed sequence of \(36\) elementary collapses removes all non-surface simplices and leaves exactly \(T\).

At squared radius \(8+4\sqrt2\), the clique complex has face vector \((24,132,248,186,48)\) and exactly \(638\) nonempty simplices. A separate, explicit sequence of \(216\) elementary free-face collapses leaves **exactly the included squared-radius-eight complex**, which has \(206\) nonempty simplices. At squared radius \(12+4\sqrt2\), the face vector is \((24,180,576,906,744,304,48)\), comprising \(2782\) simplices. A sequence of \(1288\) elementary collapses again leaves exactly that same included squared-radius-eight complex. Every intermediate deletion is verified against the current face poset. Thus each inclusion is a simple-homotopy equivalence and acts isomorphically on integral homology.

**Change to seven three-spheres.** At squared radius \(12+8\sqrt2\) the complex has face vector
\[
(24,216,944,2202,2904,2236,960,192,8),
\]
comprising \(9686\) nonempty simplices. Exactly \(36\) new edges are introduced relative to the immediately preceding stage. For **every** such edge \(\{u,v\}\), the exact checker produces an old vertex \(w\) with old edges \(\{u,w\},\{w,v\}\) and a new triangle \(\{u,v,w\}\). Consequently every loop is homotopic into the previously simply connected complex, so this stage also has trivial fundamental group.

A further certificate of \(3872\) elementary free-face collapses reduces the 9686-simplex complex to a three-dimensional complex \(Y\) with face vector \((24,216,944,758)\). Form the third simplicial boundary homomorphism \(\partial_3:\mathbb Z^{758}\to\mathbb Z^{944}\) using the standard ascending-vertex orientation. The attached integer certificate gives \(751\) successive unit pivots, all \(\pm1\), using only integer-unimodular row and column operations; on replay the remaining matrix is identically zero. Hence the Smith normal form of \(\partial_3\) has \(751\) unit entries and no other nonzero entries, so \(\ker\partial_3\cong\mathbb Z^7\), and \(\operatorname{coker}\partial_3\cong\mathbb Z^{193}\) is torsion-free.

Because \(Y\) is connected and simply connected, \(\operatorname{im}\partial_2=\ker\partial_1\) has rank \(216-24+1=193\). The induced map \(\mathbb Z^{944}/\operatorname{im}\partial_3\to\operatorname{im}\partial_2\) is a surjection between free abelian groups of equal rank, so its kernel \(H_2(Y;\mathbb Z)\) is zero. Thus \(Y\) is two-connected, has \(H_3(Y;\mathbb Z)\cong\mathbb Z^7\), and has no homology above dimension three. The Hurewicz and homological Whitehead theorems give \(Y\simeq\bigvee^7S^3\); the elementary collapses transfer this equivalence to the Rips complex.

## Verification
The attachments `rhombicuboctahedron_certificates.json` and `verify_rhombicuboctahedral_euclidean.py` are self-contained and use only Python 3 standard-library facilities. Place them together and run `python3 verify_rhombicuboctahedral_euclidean.py`. The program reconstructs exact \(\mathbb Z[\sqrt2]\) distances and all \(5\) complexes from the coordinates; verifies every simplex count and boundary-surface link; checks all \(8+36+216+1288+3872=5420\) elementary collapses one by one against current unique cofaces; checks all \(36\) new-edge triangular nullhomotopies; and replays the \(751\) integer unit-pivot operations on the signed third boundary matrix. The expected terminal string is `VERIFY_OK`. The certificates apply to the entire finite configuration, not to a random sample or inferred asymptotic family.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* (arXiv:1104.0433, first posted 2011-04-03) supplies general graph-power topology and a surjectivity principle for the fundamental group under graph powers; its cycle-specific homotopy calculations do not determine this finite Euclidean filtration. Saleh, Titz Mite and Witzel's *Vietoris–Rips complexes of platonic solids* (arXiv:2302.14388) classifies the five Platonic solids and explicitly identifies Archimedean solids as another direction; the present solid is Archimedean, not Platonic.

A closely related published finite result, *An explicit scale-two Rips collapse onto the rhombicuboctahedral sphere* (public published-finding corpus record, 2026), establishes the graph-metric **scale-two** collapse to the rhombicuboctahedral boundary. Its 638-simplex complex coincides here with the Euclidean stage at squared radius \(8+4\sqrt2\). It does **not** determine the earlier 206-simplex Euclidean sphere stage or the 9686-simplex Euclidean (equivalently graph-metric scale-three) stage with seven integral three-spheres. Its earlier graph-metric scale-one circle computation is credited and is not claimed as an independent new theorem. Another public finite result studies the **12-vertex cuboctahedron**, not this 24-vertex rhombicuboctahedron.

## Limitations
No claim is made for squared radii at or above \(16+8\sqrt2\), for other Archimedean solids, or for integral symmetry representations. The matching and integer certificates establish homotopy and integral homology, but not a canonical geometric decomposition or a symmetry-equivariant collapse. Published and indexed searches do not guarantee uniqueness against unindexed equivalent calculations; independent mathematical review has not occurred.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first submitted 2011-04-03), https://arxiv.org/html/1104.0433v3.
2. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of platonic solids*, arXiv:2302.14388 (first submitted 2023-02-28), https://arxiv.org/abs/2302.14388.
3. *An explicit scale-two Rips collapse onto the rhombicuboctahedral sphere*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-explicit-scale-two-rips-collapse-onto-the-rhombicuboctahedral--333648c8216c.
4. *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e.
