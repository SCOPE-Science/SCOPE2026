# Every missing tetrahedron is a minimum-support mod-two \(2\)-cycle in Lutz's 11-vertex \(S^2\times S^2\)
## Finding
Let \(K\) be the 11-vertex simplicial triangulation of \(S^2\times S^2\) with facets listed by Lutz. Call a four-vertex set \(Q\) a missing tetrahedron when \(Q\) is not a 3-simplex of \(K\) but each of its four triangular faces is a simplex of \(K\). Then \(K\) has exactly 58 missing tetrahedra, and for every such \(Q\), the tetrahedral boundary \(\partial Q\) represents a nonzero class in \(H_2(K;\mathbf F_2)\).

Moreover,
\[
H_2(K;\mathbf F_2)\cong \mathbf F_2^2,
\]
so there are three nonzero mod-two classes. The 58 missing tetrahedra split by the class of their boundary into support multiplicities \(6\), \(24\), and \(28\). These are exactly all minimum-vertex-support representatives of nonzero classes in degree two.

## Assumptions and scope
The labeled complex is exactly the 68-facet complex on vertices \(\{1,2,3,4,5,6,7,8,9,a,b\}\) printed in Theorem 40 of arXiv:math/0506372v1 and again as Example 3.11 of arXiv:math/0701735v1. The source identifies this complex as a combinatorial 4-manifold triangulating \(S^2\times S^2\) and proves that 11 vertices are minimal for such a triangulation. Coefficients in the finding are \(\mathbf F_2\).

A vertex-support size means the number of vertices occurring in a simplicial chain. The claim is about the specific labeled 11-vertex triangulation, not every 11-vertex triangulation of \(S^2\times S^2\).

## Proof
The published facet list reconstructs the face vector
\[
(11,55,150,170,68).
\]
Over \(\mathbf F_2\), the boundary map from triangles to edges has rank \(45\), while the boundary map from tetrahedra to triangles has rank \(103\). Therefore
\[
\dim H_2(K;\mathbf F_2)=150-45-103=2.
\]

Among the \(\binom{11}{4}=330\) four-vertex sets, exactly 228 have all four triangular faces in \(K\). Exactly 170 of those are tetrahedra of \(K\), leaving exactly 58 missing tetrahedra. For each missing tetrahedron \(Q\), its four-face boundary is a 2-cycle. Row reduction against the image of the tetrahedron-to-triangle boundary map shows that each of the 58 cycles is outside that image, so every one is nonzero in \(H_2(K;\mathbf F_2)\).

Two such boundaries represent the same class exactly when their sum lies in the tetrahedral boundary image. This equivalence relation partitions the 58 missing tetrahedra into three classes of sizes \(6\), \(24\), and \(28\). Since degree-two homology is two-dimensional over \(\mathbf F_2\), these three classes exhaust all nonzero homology classes.

No nonzero simplicial 2-cycle can use fewer than four vertices. On exactly four vertices, the only nonzero mod-two 2-cycle is the full boundary of a tetrahedron: every edge must occur an even number of times, which forces all four triangles. Hence the 58 missing tetrahedral boundaries are exactly all minimum-support nonzero degree-two cycles.

## Verification
The accompanying `verify.py` reconstructs all faces from the published 68 4-simplices, verifies the face vector, computes both boundary ranks by exact bit-vector Gaussian elimination, enumerates all four-vertex sets, checks each missing tetrahedral boundary by an independent rank-increase test, and reconstructs the homology-class partition using pairwise differences modulo the tetrahedral boundary image.

A replay of the exact packaged script returns:

`VERIFY_OK f=11,55,150,170,68 ranks_d2_d3=45,103 H2_F2=2 missing_tetrahedra=58 essential_missing=58 class_supports=6,24,28 min_vertex_support=4`

## Relationship to prior work
Lutz's Theorem 40 gives the exact 68-facet triangulation, its face vector, its \(S^2\times S^2\) topology, and vertex minimality. Datta's Example 3.11 republishes the same labeled complex and topology. Neither inspected source states the number 58 of missing tetrahedra, that every missing tetrahedral sphere is homologically essential, or the support multiplicities \(6,24,28\).

The nearby theory of tight triangulations does not imply this statement for the present complex. In particular, Sparla's tight construction concerns a different symmetric 12-vertex triangulation of \(S^2\times S^2\). Semantic searches for the exact object, missing/empty tetrahedra, induced tetrahedral spheres, minimum homology support, and the numbers \(58\), \(6\), \(24\), and \(28\) did not locate a source whose statement implies this finding.

## Limitations
This is an exact finite statement about one specific 11-vertex triangulation and mod-two degree-two homology. It does not classify integral homology classes of the same 58 cycles, nor does it assert that every vertex-minimal triangulation of \(S^2\times S^2\) has the same support spectrum. An unindexed computation or database note could still contain the same finite census.

## References
1. Frank H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1, submitted 18 June 2005; Theorem 40.
2. Basudeb Datta, *Minimal Triangulations of Manifolds*, arXiv:math/0701735v1; Example 3.11.
3. E. Sparla, *An Upper and a Lower Bound Theorem for Combinatorial 4-Manifolds*, Discrete & Computational Geometry 19 (1998), DOI:10.1007/PL00009369.
