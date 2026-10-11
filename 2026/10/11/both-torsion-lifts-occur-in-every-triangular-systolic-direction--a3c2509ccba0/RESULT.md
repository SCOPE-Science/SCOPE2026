# Both torsion lifts occur in every triangular systolic direction of the twelve-vertex nonorientable genus-four surface
## Finding
Let
\[
K={}^2 12^4_2
\]
be the Köhler--Lutz vertex-transitive twelve-vertex triangulation of the nonorientable closed surface of genus \(4\). Its face vector is
\[
f(K)=(12,42,28),
\]
and its published automorphism group is \(A_4\).

An independent integral chain calculation gives
\[
H_1(K;\mathbb Z)\cong\mathbb Z^3\oplus\mathbb Z/2.
\]
The one-skeleton has exactly \(48\) triangular cliques. Exactly \(28\) are faces and exactly \(20\) are nonfacial triangular cycles.

Every one of these \(20\) cycles is integrally homologically nonzero, and every one has primitive image in the free quotient. Therefore the simple integral homology \(1\)-systole has edge length \(3\) and exactly \(20\) minimizers.

There is an explicit splitting
\[
H_1(K;\mathbb Z)=\langle g_1,g_2,g_3\rangle\oplus\langle t\rangle,
\qquad 2t=0,
\]
for which the free projections of the minimizers, up to reversing orientation, are exactly
\[
g_1,\qquad g_2,\qquad g_3,\qquad g_1-g_2-g_3.
\]
For every one of these four primitive directions, both torsion lifts occur. Their two carrier multiplicities are always \(4\) and \(1\).

The published \(A_4\)-action has three orbits on the twenty carriers, of sizes
\[
4,\quad12,\quad4.
\]
On the eight unoriented integral homology classes represented by the carriers, it has exactly two orbits of size \(4\): the four classes of multiplicity \(4\) form one orbit, and the four classes of multiplicity \(1\) form the other.

## Assumptions and scope
The labeled complex is reconstructed from the three orbit representatives
\[
123_{12},\qquad124_{12},\qquad138_{4}
\]
and the two published generators of the permutation group \(12^4\cong A_4\). These data reproduce all \(28\) triangles.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero. A class is called primitive after free projection when its image in
\[
H_1(K;\mathbb Z)/(\text{torsion})\cong\mathbb Z^3
\]
is primitive.

The displayed splitting is explicit and computational, not canonical. Statements about the existence of both torsion lifts in each of four free directions and the multiplicity pattern \(4+1\) are independent of renaming the chosen basis and torsion generator.

## Proof
The published orbit data generate a complex with \(12\) vertices, \(42\) edges, and \(28\) triangles. Every edge is incident to exactly two triangles, every vertex link is a connected cycle, and
\[
12-42+28=-2,
\]
consistent with the published nonorientable genus-four topology.

Contract the deterministic spanning tree used in `verify.py`. The graph-cycle lattice then has rank
\[
42-12+1=31.
\]
The \(28\) triangular faces give \(28\) integral relations. Unimodular row and column operations isolate \(27\) unit pivots; the remaining relation row is unimodularly equivalent to a row of greatest common divisor \(2\). Thus the Smith data are
\[
1^{27},2,
\]
and therefore
\[
H_1(K;\mathbb Z)\cong\mathbb Z^3\oplus\mathbb Z/2.
\]

Three explicit integral cocycles annihilate all facial relations and give free coordinates. A fourth mod-two cocycle also annihilates every facial relation. The triangular cycles
\[
(1,2,12),\qquad(1,3,4),\qquad(1,4,6)
\]
evaluate to the three standard free basis vectors and have zero torsion coordinate. The six-edge cycle
\[
(1,2,5,7,8,11)
\]
has free coordinate zero and nonzero torsion coordinate. Since these evaluations surject onto a group with the already-proved type \(\mathbb Z^3\oplus\mathbb Z/2\), they are exact homology coordinates.

Exhausting all three-vertex cliques gives \(48\) in total and \(20\) nonfaces. Up to reversing orientation, the eight exact homology coordinate classes have multiplicities
\[
4,4,4,4,1,1,1,1.
\]
Their free projections are precisely the four directions
\[
g_1,\quad g_2,\quad g_3,\quad g_1-g_2-g_3,
\]
and in each direction the two order-two torsion lifts occur with multiplicities \(4\) and \(1\). Every free coordinate vector has coordinate gcd \(1\), proving primitivity after free projection.

No simple graph cycle has fewer than three edges. Because homologically nonzero three-edge cycles occur, the simple integral homology \(1\)-systole is exactly \(3\).

Finally, the verifier applies the published \(A_4\)-permutations to the complete carrier set. The carrier orbits have sizes \(4,12,4\). Applying the same permutations while retaining cycle orientation gives two orbits on the eight unoriented homology classes, each of size \(4\), exactly separated by carrier multiplicity \(4\) versus \(1\).

## Verification
The standalone `verify.py` uses only the Python standard library. It rebuilds the group and all facet orbits from the published generators, verifies the surface links, carries out the integral unimodular reduction, checks all four cocycles against every facial relation, verifies explicit free and torsion generators, exhausts every graph triangle, and computes the two symmetry actions.

Exact successful output:

`VERIFY_OK f=12,42,28 surface=N4 H1_Z=Z^3+Z/2 graph_triangles=48 facial3=28 empty3=20 all_empty3_nonzero=yes all_free_projections_primitive=yes simple_integral_1_systole=3 free_directions=4 both_torsion_lifts_each=yes lift_counts_each=4+1 A4_carrier_orbits=4,4,12 A4_class_orbits=4,4 class_orbit_multiplicities=1|4 smith=1^27,2 torsion_witness_len=6`

The proof of \(H_1\) is integral. The mod-two cocycle is used only to identify the order-two coordinate after the Smith type has already been established.

## Relationship to prior work
Köhler and Lutz enumerate vertex-transitive combinatorial manifolds and list this exact nonorientable genus-four surface with face vector \((12,42,28)\), automorphism group \(A_4\), type \({}^2 12^4_2\), and triangle orbits \(123_{12}\), \(124_{12}\), and \(138_4\). Their generator table gives the two permutations used in the reconstruction. The table row has no earlier-literature remark attached to this example.

Sulanke and Lutz later enumerate all triangulated surfaces on \(12\) vertices and all equivelar polyhedral maps on the nonorientable genus-four surface. This broader classification fixes the surrounding finite landscape but does not state the integral shortest-cycle spectrum above.

A nearby computation for the six orientable equivelar twelve-vertex genus-two surfaces establishes only mod-two triangular systole counts for different complexes. It does not imply the present mixed free-plus-torsion integral classification. The six-vertex projective plane is the classical minimal torsion surface, but its \(\mathbb Z/2\) first homology does not imply the four-direction, two-lift shell in this genus-four surface.

## Limitations
The theorem concerns one fixed labeled vertex-transitive triangulation and simplicial edge length. It does not classify longer simple cycles, geodesic lengths for a chosen metric, or other genus-four triangulations.

The splitting of \(H_1\) is not canonical. The invariant content is the existence of four primitive free directions, both torsion lifts in every direction, the \(4+1\) carrier multiplicity in each direction, and the stated \(A_4\)-orbit structure.

An unindexed historical computation of this exact finite complex could contain part or all of the same cycle census.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24; Table 3 and Table 13.
2. T. Sulanke and F. H. Lutz, *Isomorphism-free lexicographic enumeration of triangulated surfaces and 3-manifolds*, arXiv:`math/0610022v1`, submitted 2006-09-30.
