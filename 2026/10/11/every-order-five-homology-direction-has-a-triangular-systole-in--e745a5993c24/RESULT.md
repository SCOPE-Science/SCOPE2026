# Every order-five homology direction has a triangular systole in the Weber–Seifert space
## Finding
Let \(K\) be the twenty-one-vertex triangulation of the Weber–Seifert hyperbolic dodecahedral space listed in the public manifold data. Its face vector is
\[
f(K)=(21,190,338,169).
\]
An independent integral computation gives
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/5)^3.
\]

The one-skeleton contains exactly \(984\) three-vertex cliques. Of these, \(338\) are triangular faces and \(646\) are nonfacial triangular cycles. Every one of the \(646\) nonfacial triangles represents a nonzero integral homology class. Hence the simple integral homology \(1\)-systole has edge length \(3\) and exactly \(646\) minimizers.

Because every nonzero element has order \(5\), the one-dimensional subgroups of \(H_1\) are the \(31\) points of
\[
\mathbb P(H_1)\cong\operatorname{PG}(2,5).
\]
Every one of these \(31\) homology directions contains a triangular systolic class.

For a fixed projective direction there are two unoriented nonzero class types, represented by
\[
\{\pm x\}\quad\text{and}\quad\{\pm2x\}.
\]
Across all \(31\) directions, exactly \(40\) of the \(62\) possible unoriented nonzero class types occur. Nine directions contain both types, while the other twenty-two contain exactly one.

There is an explicit simplicial automorphism of order \(3\). Its induced action on \(\operatorname{PG}(2,5)\) has one fixed direction and ten orbits of size \(3\). The fixed direction contains \(16\) triangular carriers. For the ten nonfixed direction-orbits, the total numbers of triangular carriers per direction are
\[
2,\ 7,\ 8,\ 19,\ 21,\ 25,\ 26,\ 28,\ 35,\ 39,
\]
with each total constant on the corresponding three-cycle.

## Assumptions and scope
The labelled complex is the public `hyperbolic_dodecahedral_space` entry. Vertices are \(1,\ldots,21\), and all \(169\) tetrahedra are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero.

A projective homology direction means a one-dimensional \(\mathbf F_5\)-subspace of
\[
H_1(K;\mathbb Z)\cong\mathbf F_5^3.
\]
Orientation reversal identifies \(x\) with \(-x\), but does not identify \(x\) with \(2x\).

## Proof
Contract a spanning tree of the one-skeleton. Since \(K\) has \(190\) edges and \(21\) vertices, the resulting graph-cycle lattice has rank
\[
190-21+1=170.
\]
Each of the \(338\) triangular faces gives an integral relation in this lattice.

A deterministic set of \(170\) facial relations has determinant
\[
-125.
\]
Therefore the integral quotient is finite and its order divides \(125\). Reduction of the full relation matrix modulo \(5\) has rank \(167\), so the quotient has mod-\(5\) dimension \(3\). In Smith-normal-form language, at least three invariant factors are divisible by \(5\), so the quotient order is divisible by
\[
5^3=125.
\]
Consequently the quotient has order exactly \(125\), with exactly three nontrivial invariant factors, all equal to \(5\). Thus
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/5)^3.
\]

The verifier computes a basis of the three-dimensional nullspace of the facial relation matrix over \(\mathbf F_5\). Since the integral homology has already been proved to be \((\mathbb Z/5)^3\), evaluation against these three cocycles gives exact homology coordinates.

Exhaustion of every three-vertex clique gives \(984\) graph triangles. The \(338\) facial triangles are boundaries. Every one of the other \(646\) triangles has a nonzero coordinate in \(\mathbf F_5^3\). Hence all \(646\) are homologically essential. Since a simple graph cycle has at least three edges, the simple integral homology systole is exactly \(3\).

Projectivizing the \(646\) coordinates yields all \(31\) one-dimensional subspaces of \(\mathbf F_5^3\). Identifying each coordinate with its negative yields \(40\) distinct unoriented nonzero class types. A projective line has exactly two such types, and exact counting gives nine lines with both types and twenty-two with one.

Finally, the verifier checks that the permutation
\[
(1,2,\ldots,21)\longmapsto(14,9,11,1,5,15,16,17,19,3,10,7,13,4,20,12,21,18,2,6,8)
\]
preserves the complete tetrahedron set and has order \(3\). Its induced linear map on \(H_1\) is derived from the certified cocycle coordinates and checked on every graph triangle. The induced projective action has one fixed direction and ten three-cycles, and the stated carrier totals follow by exact enumeration.

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs every face from all \(169\) tetrahedra, builds the contracted integral cycle presentation, computes the determinant certificate and mod-\(5\) rank, constructs exact homology coordinates, exhausts every graph triangle, enumerates all projective directions, and verifies the order-three simplicial symmetry and its induced homology action.

Exact successful output:

`VERIFY_OK f=21,190,338,169 H1_Z=Z5^3 graph_triangles=984 facial3=338 empty3=646 all_empty3_nonzero=yes projective_directions=31 all_directions_hit=yes unoriented_class_pairs_hit=40of62 direction_pair_profile=double9+single22 order3_symmetry=yes projective_orbits=1+10x3 fixed_direction_carriers=16 triple_direction_totals=2,7,8,19,21,25,26,28,35,39 maximal_minor_det=-125 rank_mod5=167`

The finite homology structure is proved integrally before mod-\(5\) cocycles are used to classify individual triangles.

## Relationship to prior work
Lutz, Sulanke, and Swartz list the Weber–Seifert hyperbolic dodecahedral space with homology
\[
(\mathbb Z,(\mathbb Z/5)^3,0,\mathbb Z)
\]
and the face vector
\[
(21,190,338,169)
\]
in their hyperbolic-manifold table. The public Manifold Page supplies the exact \(169\)-tetrahedron simplicial complex.

The earlier geometric-three-manifold survey identifies the Weber–Seifert space as a classical closed hyperbolic \(3\)-manifold and records an older, larger triangulation. Later work of Burton, Rubinstein, and Tillmann proves that the Weber–Seifert space is non-Haken using a distinct \(23\)-tetrahedron singular triangulation and normal-surface enumeration.

These sources determine the manifold, its ambient homology, and several triangulations, but they do not state the \(646\)-triangle systolic census, the fact that every projective order-five homology direction is represented at length \(3\), or the order-three projective orbit structure found here. Focused searches under the Weber–Seifert and hyperbolic-dodecahedral aliases, shortest-homology terminology, empty-triangle terminology, projective-homology terminology, and the numerical fingerprints did not locate a covering statement.

## Limitations
The theorem concerns simple simplicial cycles in this fixed twenty-one-vertex triangulation. It does not compare other triangulations of the Weber–Seifert space, hyperbolic geodesic length, stable norms, or normal-surface complexity.

The cocycle basis is computational and not canonical. The projective-direction assertions and carrier counts are basis-independent, while the displayed matrix coordinates used internally by the verifier depend on the chosen basis.

An unindexed historical finite computation could contain part or all of the same triangular census.

## References
1. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; Section 6 and Table 11.
2. F. H. Lutz, *The Manifold Page*, `hyperbolic_dodecahedral_space.txt`, `hyperbolic_dodecahedral_space_hom.txt`, and `hyperbolic_dodecahedral_space_f_vec.txt`.
3. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 10.
4. B. A. Burton, J. H. Rubinstein, and S. Tillmann, *The Weber-Seifert dodecahedral space is non-Haken*, arXiv:`0909.4625v1`, submitted 2009-09-25.
