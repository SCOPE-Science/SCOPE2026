# Two symmetry orbits exhaust the mod-two one-systoles of the 15-vertex quaternionic space
## Finding
Let \(K\) be the 15-vertex vertex-transitive triangulation of the quaternionic spherical space \(S^3/Q=P(2)\) with face vector \(f(K)=(15,90,150,75)\). A **missing triangle** is a three-vertex set whose three edges belong to \(K\) but whose two-simplex does not.

Exactly \(120\) triples are missing triangles, and the boundary of every one represents a nonzero element of \(H_1(K;\mathbf F_2)\cong\mathbf F_2^2\). Consequently the simple mod-two combinatorial homology \(1\)-systole has edge length \(3\), with exactly \(120\) unoriented minimizers. The three nonzero homology classes each occur on exactly \(40\) minimizers.

The full simplicial automorphism group is \(\mathrm{GL}(2,4)\). Its action on the \(120\) systolic triangles has exactly two orbits, of sizes \(90\) and \(30\), represented by \({1,2,10}\) and \({1,2,12}\). Each orbit is homologically balanced: the size-
\(90\) orbit contains \(30\) representatives of each nonzero class, and the size-
\(30\) orbit contains \(10\) representatives of each nonzero class.

## Assumptions and scope
The labeled complex is reconstructed from the published 75-tetrahedron data record for the 15-vertex triangulation of \(S^3/Q\). Homology is simplicial homology with coefficients in \(\mathbf F_2\). A simple combinatorial \(1\)-cycle is a simple cycle in the one-skeleton, and its length is its number of edges. The automorphism action is the full simplicial automorphism group identified in the vertex-transitive classification; the published generators for action type \(15^{15}\) are used directly.

The claim concerns only shortest simple mod-two homology representatives. It does not classify longer representatives, integral \(1\)-cycles, embedded geodesics in a metric realization, or minimal-area surfaces.

## Proof
The reconstructed complex has \(15\) vertices, \(90\) edges, \(150\) triangles, and \(75\) tetrahedra. Over \(\mathbf F_2\), the edge-to-vertex boundary map has rank \(14\), while the span of the \(150\) triangular boundaries has rank \(74\). Therefore
\[
\dim H_1(K;\mathbf F_2)=90-14-74=2.
\]

Among all \(\binom{15}{3}=455\) triples, exactly \(150\) are faces, exactly \(120\) are missing triangles, and the remaining \(185\) fail to contain all three edges. Reducing the boundary vector of each of the \(120\) missing triangles modulo the triangular-boundary span gives no zero remainder and exactly three distinct nonzero remainders, each occurring \(40\) times. Since \(H_1(K;\mathbf F_2)\) is two-dimensional, these are precisely its three nonzero elements.

Any simple graph cycle has at least three edges. A three-edge cycle in the one-skeleton is the boundary of a vertex triple. If the triple is a two-simplex then its boundary is null-homologous; otherwise it is a missing triangle, and the exhaustive reduction above shows that it is nonzero. Thus the simple mod-two combinatorial homology \(1\)-systole is exactly \(3\), and the \(120\) missing triangles are exactly all systolic representatives.

For symmetry, the three published generators of the action labeled \(15^{15}=[3]A_5=\mathrm{GL}(2,4)\) generate \(180\) distinct vertex permutations, all preserving the 75 tetrahedra. Their action partitions the missing triangles into exactly two orbits. The lexicographically least representatives are \({1,2,10}\) and \({1,2,12}\), with orbit sizes \(90\) and \(30\). Direct homology reduction inside the two orbits gives class multiplicities \(30,30,30\) and \(10,10,10\).

## Verification
The accompanying `verify.py` is standalone Python and contains the complete 75-facet list and the three published permutation generators. It reconstructs every face, performs exact bit-vector Gaussian elimination over \(\mathbf F_2\), exhausts all 455 vertex triples, generates the 180-element permutation group, checks that every generated permutation preserves the facet set, computes the two missing-triangle orbits, and recomputes the homology class of every orbit member.

Its recorded output is:

`VERIFY_OK f=15,90,150,75 ranks_d1_d2=14,74 H1_F2=2 missing3=120 essential3=120 class_counts=40,40,40 systole=3 aut_group=180 orbit_sizes=90,30 orbit_reps=1-2-10,1-2-12 orbit_class_counts=30x3,10x3`

The finite computation proves the stated facts for this labeled complex; it is not used to infer an infinite-family theorem.

## Relationship to prior work
Brehm and Kühnel's 1986 article introduces the 15-vertex polyhedral model of Cartan's hypersurface, an eightfold quotient of the three-sphere, and records a transitive icosahedral Euclidean symmetry in the accessible abstract. Lutz's 2003 full text identifies \(P(2)=S^3/Q\), records the face vector \((15,90,150,75)\), and gives \(H_1(P(2);\mathbb Z)\cong\mathbb Z/2\oplus\mathbb Z/2\). Köhler and Lutz's 2005 full text identifies the vertex-transitive complex with group \([3]A_5=\mathrm{GL}(2,4)\), gives its tetrahedral orbit data, and prints generators for the group action. The public manifold data record supplies the complete 75-facet labeled complex used in the verification.

Those sources establish the object, topology, homology, and symmetry, but the inspected material does not state the complete shortest-cycle classification, the \(40+40+40\) homology split, or the two \(90+30\) symmetry orbits with their class balance. The 1986 full article was not available in readable full text during this check, so an unindexed observation there remains a residual originality risk.

## Limitations
The result is specific to the published labeled 15-vertex triangulation. It classifies simple edge cycles of minimum length over \(\mathbf F_2\); it does not claim that analogous orbit counts hold for other triangulations of \(S^3/Q\), nor does it address metric systoles. The 1986 source is earlier than the day-resolved sources used for the metadata date, but the inspected bibliographic record resolves it only to June 1986, so no artificial day is assigned.

## References
U. Brehm and W. Kühnel, *A polyhedral model for Cartan's hypersurface in* \(S^4\), Mathematika 33 (1986), 55–61, DOI 10.1112/S0025579300013863.

F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:math/0311116, first arXiv version 7 November 2003.

E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:math/0506520v1, 24 June 2005.

F. H. Lutz, public `3_manifolds.txt` data record, entry `manifold_3_15_15_1`.
