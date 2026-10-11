# Odd torsion splits the triangular systoles of the seventeen-vertex flat manifold \(\mathcal G_3\)
## Finding
Let \(K\) be Lutz's seventeen-vertex triangulation of the orientable flat three-manifold \(\mathcal G_3\). The published complex has
\[
f(K)=(17,117,200,100)
\]
and
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/3.
\]

The one-skeleton contains exactly \(439\) three-vertex cliques. Of these, \(200\) are triangular faces and \(239\) are nonfacial triangular cycles.

Every one of the \(239\) nonfacial triangles represents a nonzero integral homology class. Therefore the simple integral homology \(1\)-systole has edge length \(3\), with exactly \(239\) minimizers.

Choose a primitive free generator \(g\) and an order-three generator \(t\). Up to reversing orientation, the complete minimum-length class distribution is
\[
\{\pm t\}:130,\qquad
\{\pm g\}:41,\qquad
\{\pm(g+t)\}:34,\qquad
\{\pm(g+2t)\}:34.
\]

Thus every infinite-order triangular systole is primitive, and all three torsion decorations of a primitive free direction occur already at the minimum simple-cycle length.

## Assumptions and scope
The complex is the labelled \(\mathcal G_3\) entry of the published `flat_3manifolds.txt` data table. Vertices are \(1,\ldots,17\), and all \(100\) tetrahedra are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose integral homology class is nonzero.

For an increasing triple \(a<b<c\), its triangular cycle is oriented
\[
a\to b\to c\to a.
\]
The coordinate basis is fixed by two explicit cocycles. The cycle on \(\{1,5,7\}\) has coordinate \((1,0)\), defining \(g\), and the cycle on \(\{1,2,9\}\) has coordinate \((0,1)\), defining \(t\). Reversing orientation sends
\[
(n,r)\longmapsto(-n,-r)
\]
with the torsion coordinate taken modulo \(3\).

## Proof
Contract a spanning tree of the one-skeleton. Since the complex has \(117\) edges and \(17\) vertices, the graph-cycle lattice is
\[
\mathbb Z^{101}.
\]
Each of the \(200\) triangular faces gives one integral relation.

The verifier performs only unimodular integral row and column operations on the resulting \(200\times101\) relation matrix. It isolates \(99\) unit pivots with all cross-terms zero. Every entry in the residual two-column block is divisible by \(3\). After dividing that residual block by \(3\), a second unimodular reduction gives one unit pivot and one zero column. Therefore the full Smith form is
\[
\operatorname{diag}(1^{99},3,0),
\]
and hence
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/3.
\]

An explicit integral cocycle \(y\), stored sparsely in `verify.py`, annihilates every facial relation and evaluates to \(1\) on the cycle \((1,5,7)\). It gives the free coordinate.

A second explicit cocycle \(w\) with coefficients in \(\mathbb Z/3\) also annihilates every facial relation. It vanishes on \((1,5,7)\) and evaluates to \(1\) on \((1,2,9)\). Since the quotient has already been proved isomorphic to \(\mathbb Z\oplus\mathbb Z/3\), the pair \((y,w)\) gives exact homology coordinates.

Exhaustion of all three-vertex cliques gives \(439\) graph triangles. Removing the \(200\) facial triangles leaves \(239\) nonfacial cycles. Their oriented coordinate counts are
\[
(0,1):70,\quad(0,2):60,
\]
\[
(1,0):20,\quad(-1,0):21,
\]
\[
(1,1):16,\quad(-1,2):18,
\]
and
\[
(1,2):23,\quad(-1,1):11.
\]
No coordinate is zero. Pairing each class with its negative gives the four unoriented multiplicities
\[
130,\quad41,\quad34,\quad34.
\]

Every infinite-order triangular class has free coordinate \(\pm1\), so it is primitive. A simple cycle in a simplicial graph has at least three edges, and nonzero three-edge cycles exist, proving the systolic length is \(3\).

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds all \(100\) tetrahedra, reconstructs every face, proves the Smith form integrally, verifies both cocycles against every facial relation, exhausts all graph triangles, and checks the complete oriented and unoriented homology distributions.

Exact successful output:

`VERIFY_OK f=17,117,200,100 H1_Z=Z+Z/3 graph_triangles=439 facial3=200 empty3=239 all_empty3_nonzero=yes pure_order3=130 primitive_free_types=41,34,34 unoriented_types=t|g|g+t|g+2t smith=1^99,3,0`

The integral group structure and primitivity are not inferred from finite-field computations alone.

## Relationship to prior work
Lutz's 2003 geometric three-manifold survey proves that the orientable flat space \(\mathcal G_3\) admits a seventeen-vertex triangulation and records
\[
H_1(\mathcal G_3;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/3
\]
together with the face vector \((17,117,200,100)\). The companion Manifold Page supplies the exact \(100\)-tetrahedron data set.

Those sources determine the topology, ambient homology, and triangulation but do not state which nonfacial triangular cycles are pure torsion, primitive free classes, or torsion-shifted primitive classes. Focused scientific searches using the exact manifold label, flat-space descriptions, empty-triangle terminology, shortest-homology terminology, and the numerical fingerprint \(239\) did not locate the four-type \(130/41/34/34\) spectrum.

## Limitations
The theorem concerns simple simplicial cycles in this fixed seventeen-vertex triangulation. It does not compare other triangulations of \(\mathcal G_3\), Euclidean metric lengths, or stable norms.

The chosen splitting
\[
H_1\cong\mathbb Z\oplus\mathbb Z/3
\]
is not canonical. The intrinsic content is the unoriented multiplicity pattern under an explicit certified splitting, together with the facts that every empty triangle is essential and every infinite-order minimum carrier is primitive.

An unindexed historical finite computation could contain the same triangular census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5, Theorem 21 and Table 9.
2. F. H. Lutz, *The Manifold Page*, `flat_3manifolds.txt` and `flat_3manifolds_hom.txt`, entry \(\mathcal G_3\).
