# Every empty triangle is essential in the sixteen-vertex \(\mathcal G_2\) flat manifold
## Finding
Let \(K\) be the published sixteen-vertex triangulation of the orientable flat three-manifold \(\mathcal G_2\). It has
\[
f(K)=(16,116,200,100).
\]

Its integral first homology is
\[
H_1(K;\mathbb Z)\cong \mathbb Z\oplus(\mathbb Z/2)^2.
\]

The one-skeleton contains exactly \(507\) three-vertex cliques. Of these, \(200\) are triangular faces and \(307\) are nonfacial triangular cycles. Every one of the \(307\) nonfacial triangles represents a nonzero integral homology class.

Therefore the simple integral homology \(1\)-systole has edge length \(3\), with exactly \(307\) minimizers.

The minimum layer splits naturally according to the free and torsion parts of \(H_1\). Exactly \(157\) systoles have zero free coordinate and hence are nonzero order-two classes. The three nonzero elements of the torsion subgroup occur with multiplicities
\[
55,\qquad53,\qquad49.
\]

The other \(150\) systoles have free coordinate \(\pm1\), so they are primitive infinite-order classes. Up to reversing orientation, the four torsion lifts of a chosen free generator occur with multiplicities
\[
38,\qquad38,\qquad37,\qquad37.
\]

Thus every empty triangle is homologically essential, and the complete shortest integral loop layer simultaneously realizes all three nonzero torsion classes and all four torsion decorations of a primitive free direction.

## Assumptions and scope
The complex is the labelled \(\mathcal G_2\) entry of the public flat-three-manifold facet table. Vertices are \(1,\ldots,16\), and the complete list of \(100\) tetrahedra is embedded in `verify.py`.

A simple integral homology \(1\)-systole means a simple simplicial edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero.

Every increasing triple \(a<b<c\) is oriented as
\[
a\to b\to c\to a.
\]
For the infinite-order classes, reversing this orientation negates the free coordinate and leaves the order-two coordinates unchanged. Consequently the four multiplicities \(38,38,37,37\) are stated up to orientation.

The displayed torsion coordinates in the verifier depend on a chosen algebraic basis, but the distinction between the three nonzero torsion classes, the multiset \(\{55,53,49\}\), and the multiset \(\{38,38,37,37\}\) are basis-independent.

## Proof
Use the spanning tree consisting of the fifteen edges from vertex \(1\) to every other vertex. Contracting it identifies the integral graph-cycle lattice with
\[
\mathbb Z^{116-15}=\mathbb Z^{101}.
\]
Each of the \(200\) triangular faces gives one integral relation.

Let \(R\) be the resulting \(200\times101\) relation matrix. The verifier exhibits a fixed \(100\times100\) minor of determinant
\[
-4.
\]
Thus \(\operatorname{rank}_{\mathbb Q}R\ge100\).

An explicit primitive integral cocycle \(y\in\mathbb Z^{101}\) annihilates every row of \(R\). Hence \(\operatorname{rank}_{\mathbb Q}R\le100\), so the rank is exactly \(100\) and \(H_1\) has free rank one.

Modulo \(2\), exact row reduction gives
\[
\operatorname{rank}_{\mathbf F_2}R=98.
\]
Write the nonzero Smith factors of \(R\) as
\[
d_1\mid d_2\mid\cdots\mid d_{100}.
\]
Exactly two of these factors are even, because the mod-two rank is \(98\). Their product, together with the odd factors, is the determinantal divisor given by the greatest common divisor of the \(100\times100\) minors. The displayed minor of absolute value \(4\) shows this product divides \(4\), while two even factors force it to be divisible by \(4\). Therefore
\[
d_1=\cdots=d_{98}=1,\qquad d_{99}=d_{100}=2,
\]
and hence
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus(\mathbb Z/2)^2.
\]

The cocycle \(y\) has relatively prime coordinates, so its evaluation map onto \(\mathbb Z\) is primitive and gives the free coordinate.

For the torsion coordinates, reduced row elimination over \(\mathbf F_2\) leaves three quotient coordinates supported on the non-tree edges
\[
(2,7),\qquad(2,9),\qquad(2,16).
\]
Call these coordinates \(c_0,c_1,c_2\). Reduction of the integral cocycle modulo \(2\) is the functional
\[
c_0+c_2.
\]
Thus for a cycle with integer free coordinate \(n\),
\[
n\equiv c_0+c_2\pmod2.
\]
At fixed \(n\), the pair \((c_1,c_2)\) therefore gives exact coordinates on the order-four torsion fiber.

The verifier then exhausts every three-vertex clique in the one-skeleton. There are \(507\) in total, and exactly \(307\) are nonfaces. None has coordinate \((0,0,0)\).

For the \(157\) cycles with free coordinate \(0\), the three nonzero torsion coordinates occur \(55\), \(53\), and \(49\) times.

For the remaining \(150\), the free coordinate is always \(+1\) or \(-1\). After identifying a class with its negative, the four torsion decorations occur \(38\), \(38\), \(37\), and \(37\) times.

Every simple cycle in a simplicial graph has at least three edges. Since essential triangular cycles exist, edge length \(3\) is the simple integral homology systole, and the exhaustive clique enumeration proves that the \(307\) empty triangles are exactly all minimizers.

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds all \(100\) tetrahedra, reconstructs the face vector, forms the integral facial relation matrix, checks the primitive integral cocycle, evaluates the fixed determinant certificate by fraction-free Bareiss elimination, computes the full mod-two quotient, and exhausts all three-vertex cliques.

Its exact successful output is:

`VERIFY_OK f=16,116,200,100 H1_Z=Z+Z2+Z2 maximal_minor_det=-4 rank_mod2=98 graph_triangles=507 facial3=200 empty3=307 all_empty3_nonzero=yes torsion_systoles=157 torsion_counts=55,53,49 primitive_infinite_systoles=150 lift_counts=38,38,37,37`

The integral group structure is proved from the determinant certificate, mod-two rank, and primitive cocycle; it is not inferred from the published homology table.

## Relationship to prior work
Lutz's 2003 geometric-three-manifold survey classifies \(\mathcal G_2\) among the six orientable flat three-manifolds and records
\[
H_1(\mathcal G_2;\mathbb Z)\cong\mathbb Z\oplus(\mathbb Z/2)^2.
\]
At that stage the listed triangulation had \(17\) vertices.

Lutz, Sulanke, and Swartz later recorded the improved sixteen-vertex face vector
\[
(16,116,200,100)
\]
together with the same homology group. The companion public data table gives the exact \(100\)-tetrahedron presentation used here.

Those sources specify the manifold, homology, face vector, and facets, but they do not state the complete homology classification of the \(307\) nonfacial triangles. Focused publication searches using \(\mathcal G_2\), half-turn-space terminology, empty triangles, shortest homology loops, primitive triangular cycles, and the numerical fingerprint \(307\) did not locate a covering statement.

## Limitations
The result concerns simplicial edge length in this fixed sixteen-vertex triangulation. It does not compare other triangulations of \(\mathcal G_2\) or a Euclidean metric systole.

The chosen algebraic torsion coordinates are not canonical; only the class multiplicities up to automorphism of \((\mathbb Z/2)^2\) and orientation are intrinsic.

The exact public facet table is not itself day-stamped. The source-date field uses the earliest inspected day-resolved public source that explicitly reports a sixteen-vertex \(\mathcal G_2\) triangulation with this face vector, the 2008-05-08 arXiv submission.

An unindexed historical computation could contain the same finite triangular-class census.

## References
1. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; Table 7.
2. F. H. Lutz, *The Manifold Page: 3-Manifolds*, companion data file `flat_3manifolds.txt`, entry \(\mathcal G_2\).
3. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5 and Table 9.
