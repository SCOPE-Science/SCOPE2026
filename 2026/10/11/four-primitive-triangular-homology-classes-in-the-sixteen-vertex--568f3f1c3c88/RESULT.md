# Four primitive triangular homology classes in the sixteen-vertex flat space \(\mathcal B_2\)
## Finding
Let \(K\) be Lutz's sixteen-vertex triangulation of the nonorientable flat three-manifold \(\mathcal B_2\). The published complex has face vector
\[
(16,110,188,94)
\]
and
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2.
\]

The one-skeleton of \(K\) contains exactly \(449\) three-vertex cliques. Of these, \(188\) are triangular faces and \(261\) are nonfacial triangular cycles. Exactly \(218\) of the \(261\) nonfacial triangles represent nonzero integral homology classes; the remaining \(43\) are null-homologous.

Every one of the \(218\) nonzero triangular classes is primitive. Therefore the simple integral homology \(1\)-systole of this triangulation has edge length \(3\), with exactly \(218\) unoriented minimizers.

Up to sign, the \(218\) systolic cycles represent exactly four classes. In the integral basis defined by the two cocycles in `verify.py`, these are
\[
(0,1),\qquad (1,1),\qquad (1,0),\qquad (1,2),
\]
with respective numbers of triangular representatives
\[
86,\qquad 66,\qquad 65,\qquad 1.
\]
The unique triangular representative of the singleton class is the cycle on
\[
\{2,4,16\}.
\]

## Assumptions and scope
The complex is the labelled \(94\)-tetrahedron \(\mathcal B_2\) data set published on the Manifold Page accompanying Lutz's geometric three-manifold work. Vertices are \(1,\ldots,16\).

Every edge is oriented from its smaller endpoint to its larger endpoint. For an increasing triple \(a<b<c\), its triangular cycle is oriented
\[
a\to b\to c\to a.
\]
Changing the orientation of a cycle negates its homology coordinate, so the class multiplicities \(86,66,65,1\) are stated up to sign.

The claim concerns simple simplicial cycles measured by edge length. It does not assert that these four primitive classes are the only primitive classes of \(H_1(K;\mathbb Z)\); it classifies only those attained at the minimum possible simple-cycle length.

## Proof
Choose the spanning tree consisting of the edges
\[
12,13,14,15,16,17,18,29,2\,10,2\,11,2\,12,2\,13,2\,14,2\,15,2\,16.
\]
Contracting this tree leaves \(110-15=95\) oriented graph-cycle generators. Each of the \(188\) triangular faces gives one integral relation among these generators.

The verifier performs only unimodular integer row and column operations on the resulting \(188\times95\) relation matrix. A deterministic unit-pivot reduction produces exactly \(93\) unit pivots and then a zero residual block. Consequently the facial relation lattice is a primitive rank-\(93\) direct summand of \(\mathbb Z^{95}\), and therefore
\[
H_1(K;\mathbb Z)\cong\mathbb Z^{95}/\operatorname{im}\partial_2\cong\mathbb Z^2.
\]

Two explicit integral cocycles \(y_1,y_2\), stored sparsely in `verify.py`, annihilate every facial relation. Their pairings with the nonfacial triangles \(\{2,5,9\}\) and \(\{1,4,5\}\) are
\[
(1,0)\quad\text{and}\quad(0,1),
\]
so the induced map
\[
H_1(K;\mathbb Z)\longrightarrow\mathbb Z^2,\qquad
[z]\longmapsto(\langle y_1,z\rangle,\langle y_2,z\rangle)
\]
is surjective. Since the domain has already been proved free of rank two, this map is an isomorphism. The resulting coordinate pair therefore determines the exact integral homology class of every triangular cycle.

Exhaustion of all three-vertex cliques gives \(449\) graph triangles. Removing the \(188\) faces leaves \(261\) nonfacial cycles. Their exact integral coordinates, after identifying a class with its negative, occur with multiplicities
\[
(0,0):43,\quad
(0,1):86,\quad
(1,1):66,\quad
(1,0):65,\quad
(1,2):1.
\]
All four nonzero coordinate vectors have coprime coordinates, hence are primitive. The singleton is exactly \(\{2,4,16\}\).

A simple cycle in a simplicial graph has at least three edges. Since nonzero three-edge cycles exist, length \(3\) is the simple integral homology systole.

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds all \(94\) tetrahedra, reconstructs every edge and triangular face, contracts the fixed spanning tree, performs the unimodular relation reduction, verifies both integral cocycles on all \(188\) faces, and exhausts every three-vertex clique.

Its exact successful output is:

`VERIFY_OK f=16,110,188,94 H1_Z=Z^2 graph_triangles=449 facial3=188 empty3=261 null_empty3=43 primitive_systoles=218 unoriented_class_counts=86,66,65,1 class_vectors=01|11|10|12 singleton=2,4,16`

The proof of freeness and primitivity is integral. No finite-field computation is used to infer the integral claim.

## Relationship to prior work
Lutz's 2003 geometric three-manifold paper classifies the ten flat three-manifolds in this context, identifies \(\mathcal B_2\) as a nonorientable flat space that is both a Klein-bottle bundle and a nonorientable torus bundle over the circle, and records
\[
H_1(\mathcal B_2;\mathbb Z)\cong\mathbb Z^2
\]
together with the face vector \((16,110,188,94)\). The companion Manifold Page supplies the exact \(94\)-tetrahedron data set.

Those sources determine the ambient topology and the triangulation but do not state the complete shortest integral homology-loop spectrum. Focused searches using the exact manifold label, flat-space aliases, empty-triangle language, homology-systole terminology, and the numerical fingerprints \(261\) and \(218\) did not locate a published statement of the four-class multiplicity pattern.

## Limitations
The four coordinates depend on the displayed integral basis, although the unordered multiplicity multiset
\[
\{86,66,65,1\}
\]
and the existence of a unique singleton shortest class are basis-independent.

The result is specific to this sixteen-vertex triangulation of \(\mathcal B_2\). It does not compare other triangulations of the same flat manifold or claim a metric systolic statement for a Euclidean structure.

An unindexed historical computation could contain the same finite census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5, Theorems 19--23 and Table 9.
2. F. H. Lutz, *The Manifold Page: Small triangulations of geometric 3-manifolds*, companion data file `flat_3manifolds.txt`, entry \(\mathcal B_2\).
