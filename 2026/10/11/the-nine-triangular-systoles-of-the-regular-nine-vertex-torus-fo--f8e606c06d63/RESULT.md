# The nine triangular systoles of the regular nine-vertex torus form three homology directions
## Finding
Let \(K\) be the regular nine-vertex torus triangulation \({}^{2}9^{18}_{1}\) in the Köhler--Lutz vertex-transitive census. Its face vector is
\[
f(K)=(9,27,18).
\]
An independent integral chain calculation gives
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2.
\]

The one-skeleton contains exactly \(27\) three-vertex cliques. Exactly \(18\) are triangular faces, leaving \(9\) nonfacial triangular cycles. Every one of these nine cycles is integrally homologically nonzero and primitive. Hence the simple integral homology \(1\)-systole has edge length \(3\), with exactly nine minimizers.

There is an explicitly certified basis \(g_1,g_2\) of \(H_1(K;\mathbb Z)\) for which, up to reversing orientation, the nine minimizers have exactly three homology directions:
\[
\{\pm g_1\},\qquad \{\pm g_2\},\qquad \{\pm(g_1-g_2)\},
\]
with exactly three carriers in each direction.

The full simplicial automorphism group has order \(108\) and is transitive on all nine minimizers. Its action on \(H_1(K;\mathbb Z)\) has image of order \(12\) and kernel of order \(9\). The kernel has exactly three orbits on the minimizers, each of size \(3\), and these are precisely the three homology directions above. The order-
\(12\) homology image acts transitively on the three unoriented directions.

## Assumptions and scope
The labelled complex is the regular orientable genus-one entry \({}^{2}9^{18}_{1}\) of the vertex-transitive census. The source gives the facet orbit \(136_{18}\) and the group \(\mathbb Z_3^2:D_6\); `verify.py` reconstructs the resulting eighteen triangular facets from the published group generators and independently enumerates the complete automorphism group.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose integral homology class is nonzero. A class in the free abelian group \(H_1(K;\mathbb Z)\) is primitive when its coordinates have greatest common divisor \(1\).

The displayed basis is computational rather than canonical. The intrinsic statement is the three-by-three decomposition of the minimum carrier layer together with its compatibility with the automorphism action.

## Proof
Contract the deterministic spanning tree used in `verify.py`. Since the one-skeleton has \(27\) edges and \(9\) vertices, the graph-cycle lattice has rank
\[
27-9+1=19.
\]
Each of the \(18\) triangular faces gives an integral relation.

The verifier performs only unimodular integral row and column operations on the resulting \(18\times19\) relation matrix. It isolates \(17\) unit pivots and the entire residual block is zero. Thus the Smith form is
\[
\operatorname{diag}(1^{17},0,0),
\]
which proves
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2.
\]

Two explicit integral cocycles \(y_1,y_2\), stored in `verify.py`, annihilate every facial relation. Two explicit triangular cycles evaluate to \((1,0)\) and \((0,1)\), so the evaluation map is onto \(\mathbb Z^2\). Because the Smith calculation has already proved that the quotient is exactly \(\mathbb Z^2\), these evaluations provide exact homology coordinates.

Exhaustion of all three-vertex cliques gives \(27\) graph triangles. Removing the \(18\) facial triangles leaves exactly nine nonfacial cycles. With the increasing-vertex orientation their coordinates occur with multiplicities
\[
(0,-1):3,\qquad(1,0):3,\qquad(-1,1):3.
\]
Every coordinate is nonzero and primitive. A simple cycle in a simplicial graph has at least three edges, so the existence of these essential triangular cycles proves the systolic length is \(3\).

For symmetry, the verifier first reconstructs the published order-\(108\) group and then independently tests all \(9!\) vertex permutations, proving that this is the full simplicial automorphism group. The full group is transitive on the nine nonfacial triangles. Direct evaluation of the two basis cycles under every automorphism yields exactly \(12\) distinct matrices in \(\operatorname{GL}(2,\mathbb Z)\), with kernel of size \(9\). The kernel orbits on the nine carriers have sizes \(3,3,3\), and each orbit has a single exact homology coordinate up to the chosen orientation. The quotient action permutes the three unoriented directions transitively.

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs the source facet orbit, checks that the result is a closed torus triangulation, proves the integral Smith form, verifies both cocycles against every facial relation, exhausts every graph triangle, enumerates every simplicial automorphism, and computes every induced integral homology action.

Exact successful output:

`VERIFY_OK f=9,27,18 H1_Z=Z^2 graph_triangles=27 facial3=18 empty3=9 all_empty3_nonzero_primitive=yes simple_integral_1_systole=3 unoriented_directions=3 carrier_counts=3,3,3 aut=108 aut_carrier_orbits=9 H1_action_image=12 H1_action_kernel=9 kernel_carrier_orbits=3,3,3 smith=1^17,0,0`

The proof of integral primitivity is not inferred from a finite-field calculation. The automorphism statement is not inferred solely from the published group label: the full permutation group is exhaustively recomputed from the eighteen facets.

## Relationship to prior work
Altshuler gives a complete construction and enumeration framework for regular torus triangulations of type \(\{3,6\}\), including the nine-vertex case. Köhler and Lutz later list the exact regular nine-vertex combinatorial type \({}^{2}9^{18}_{1}\), its face vector, facet orbit, full automorphism group \(\mathbb Z_3^2:D_6\), and explicit generators.

Those sources determine the map and its symmetry, but they do not state the complete integral homology classes of its nonfacial triangular cycles. Focused scientific searches using the exact census label, the regular-map and nine-vertex-torus aliases, shortest-homology terminology, nonfacial-triangle terminology, symmetry-action language, and the numerical nine-carrier fingerprint did not locate the three-by-three homology shell or the kernel-orbit theorem.

## Limitations
The theorem concerns simple edge cycles in this fixed regular nine-vertex triangulation and simplicial edge length. It does not compare other torus triangulations, Euclidean metric geodesics, or stable norms.

The basis \(g_1,g_2\) is explicit but not canonical. The source literature on regular torus maps is extensive, and an unindexed historical calculation could contain the same finite homology census even though the inspected exact-object sources do not state it.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24; Table 3 and Table 13.
2. A. Altshuler, *Construction and Enumeration of Regular Maps on the Torus*, Discrete Mathematics 4 (1973), 201--217, DOI `10.1016/S0012-365X(73)80002-0`.
