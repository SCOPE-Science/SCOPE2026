# Fifty-five triangular torsion systoles in the minimal eleven-vertex real projective 3-space
## Finding
Let \(K\) be Walkup's eleven-vertex triangulation of real projective three-space with tetrahedral facets
\[
1237,1479,2348,25810,36710,12311,14710,23411,25910,3689,
1269,1489,2378,26910,36910,12611,14810,24610,3459,4567,
1279,1568,24611,34511,45611,13510,15611,24810,3489,4579,
13511,15810,2578,35910,46710,13710,1689,2579,3678,5678.
\]
Its face vector is
\[
(11,51,80,40),
\]
and
\[
H_1(K;\mathbb Z)\cong\mathbb Z/2.
\]

Define the simple integral homology \(1\)-systole to be the least number of edges in an unoriented simple cycle representing a nonzero integral first-homology class. For \(K\), this systole is \(3\). Exactly \(55\) three-edge simple cycles attain it. They are precisely the three-vertex cliques that are not triangular faces, and every one represents the unique nonzero class in \(H_1(K;\mathbb Z)\).

The full simplicial automorphism group has order \(48\). Its vertex orbits are
\[
\{1,2,3,4,5,6\},\qquad \{7,8,9,10\},\qquad \{11\}.
\]
The \(55\) systolic triangles split into five automorphism orbits of sizes
\[
3,\ 4,\ 12,\ 12,\ 24.
\]
These five orbits are already distinguished by the numbers of vertices a carrier has in the three vertex orbits above:
\[
(2,0,1),\ (0,3,0),\ (3,0,0),\ (1,2,0),\ (2,1,0).
\]
Representatives are, respectively,
\[
\{1,4,11\},\ \{7,8,9\},\ \{1,2,4\},\ \{1,7,8\},\ \{1,2,8\}.
\]

## Assumptions and scope
A three-edge simple cycle means the boundary of a three-vertex clique in the one-skeleton. Facial triangles are integral boundaries and therefore homologically trivial. The result concerns this particular vertex- and facet-minimal Walkup triangulation, not all thirty eleven-vertex triangulations of \(\mathbb{RP}^3\).

Cycle length is purely combinatorial: every edge has unit length. No geometric metric on \(\mathbb{RP}^3\) is used.

## Proof
The facet list reconstructs \(51\) edges and \(80\) triangles. The only missing edges are
\[
\{7,11\},\ \{8,11\},\ \{9,11\},\ \{10,11\}.
\]
Hence exactly \(135\) three-subsets span cliques. Of these, \(80\) are facial triangles, leaving \(55\) nonfacial three-cycles.

Over \(\mathbf F_2\), the graph cycle space has dimension
\[
51-11+1=41,
\]
while the span of the \(80\) facial triangle boundaries has rank \(40\). Thus \(H_1(K;\mathbf F_2)\) is one-dimensional. Exact reduction of all \(55\) nonfacial triangle boundaries modulo the facial-boundary space shows that every one is nonzero.

The verifier also establishes the integral group. Use the star at vertex \(1\) as a spanning tree. Projection of integral graph cycles to the \(41\) cotree-edge coordinates identifies the integral cycle lattice with \(\mathbb Z^{41}\). A fixed set of \(41\) facial triangle boundaries has determinant \(2\), computed by fraction-free Bareiss elimination. Thus the full facial-boundary lattice has index dividing \(2\). Since the mod-two quotient is nonzero, that index is even, hence exactly \(2\). Therefore
\[
H_1(K;\mathbb Z)\cong\mathbb Z/2.
\]
Every nonfacial triangle is therefore the integral torsion generator. No simple cycle has fewer than three edges, proving the minimum.

For symmetry, graph degrees are \(10\) on vertices \(1\) through \(6\), \(9\) on vertices \(7\) through \(10\), and \(6\) at vertex \(11\). Every simplicial automorphism preserves these three blocks. Exhausting the resulting \(6!\,4!=17{,}280\) block-preserving permutations gives exactly \(48\) automorphisms. Acting on the \(55\) systoles gives the five orbit sizes and representatives displayed above.

## Verification
The standalone `verify.py` contains the complete facet presentation and uses only Python's standard library. It independently reconstructs all faces, checks the four missing edges, computes mod-two homology by exact bit-vector elimination, proves the integral first-homology order with a determinant-two lattice certificate, exhausts the block-preserving permutation search for the automorphism group, and computes every systole orbit.

Its exact successful output is:

`VERIFY_OK f=11,51,80,40 missing_edges=4 H1_Z=Z/2 cliques3=135 facial3=80 essential3=55 aut=48 vertex_orbits=6,4,1 systole_orbits=3,4,12,12,24`

Every finite range appearing in the claim is exhausted; no sampled computation is promoted to a universal statement.

## Relationship to prior work
Walkup proved the vertex-minimality of an eleven-vertex triangulation of \(\mathbb{RP}^3\). Lutz's survey gives this exact forty-facet presentation, identifies it with the Brehm--Światkowski lens-space construction, records its face vector, and determines its full automorphism group. Sulanke and Lutz later enumerated all eleven-vertex combinatorial three-manifolds and proved that there are exactly thirty vertex-minimal triangulations of \(\mathbb{RP}^3\), with Walkup's complex the unique one having face vector \((11,51,80,40)\).

The inspected exact-object sources do not state the complete nonfacial-triangle homology census, that all \(55\) such cycles are the torsion generator, or their five symmetry orbits. The automorphism group itself is therefore treated as prior work; the new content is its action on the complete shortest nonzero homology layer.

## Limitations
The theorem is specific to Walkup's vertex- and facet-minimal complex. It does not classify shortest homology cycles in the other twenty-nine eleven-vertex triangulations of \(\mathbb{RP}^3\), longer simple representatives, or geometric systoles for a metric realization. Literature-based originality cannot exclude an unindexed historical computation of the same finite orbit table.

## References
1. D. W. Walkup, *The lower bound conjecture for 3- and 4-manifolds*, Acta Mathematica 125 (1970), 75--107, DOI `10.1007/BF02392331`.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:`math/0506372v1`, submitted 2005-06-18.
3. T. Sulanke and F. H. Lutz, *Isomorphism-free lexicographic enumeration of triangulated surfaces and 3-manifolds*, arXiv:`math/0610022v1`, submitted 2006-09-30.
4. SageMath, `RealProjectiveSpace(3)` in `simplicial_complex_examples.py`, exact standard facet presentation and homology cross-check.
