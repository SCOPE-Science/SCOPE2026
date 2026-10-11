# All fifteen nonzero \(H_1\)-classes occur among triangular systoles of the seventeen-vertex flat manifold \(\mathcal G_6\)
## Finding
Let \(K\) be Lutz's seventeen-vertex triangulation of the orientable flat three-manifold \(\mathcal G_6\). The published complex has
\[
f(K)=(17,124,214,107).
\]
Its first integral homology is
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/4)^2.
\]

The one-skeleton contains exactly \(519\) three-vertex cliques. Of these, \(214\) are triangular faces and \(305\) are nonfacial triangular cycles.

Every one of the \(305\) nonfacial triangles represents a nonzero integral homology class. Consequently the simple integral homology \(1\)-systole has edge length \(3\), with exactly \(305\) minimizers.

More strongly, every one of the \(15\) nonzero elements of
\[
(\mathbb Z/4)^2
\]
has a triangular representative at this minimum length.

Up to reversing orientation, the six inverse-pair classes of order \(4\) have carrier multiplicities
\[
52,\quad51,\quad51,\quad48,\quad45,\quad38,
\]
and the three nonzero order-\(2\) classes have carrier multiplicities
\[
13,\quad5,\quad2.
\]

## Assumptions and scope
The complex is the labelled \(\mathcal G_6\) entry of the published `flat_3manifolds.txt` data table. Vertices are \(1,\ldots,17\), and all \(107\) tetrahedra are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero.

For an increasing triple \(a<b<c\), its triangular cycle is oriented
\[
a\to b\to c\to a.
\]
The verifier obtains an explicit basis of
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/4)^2
\]
from a deterministic integral reduction. In that basis, the triangles \(\{2,4,11\}\) and \(\{1,3,9\}\) have coordinates \((1,0)\) and \((0,1)\), respectively.

The displayed multiplicity multisets are independent of how the two basis generators are named. No claim is made about Euclidean metric length or about other triangulations of the same flat manifold.

## Proof
Contract a spanning tree of the one-skeleton. Since the triangulation has \(124\) edges and \(17\) vertices, the resulting graph-cycle lattice is
\[
\mathbb Z^{108}.
\]
Each of the \(214\) triangular faces gives an integral relation in this lattice.

The verifier applies only unimodular integral row and column operations to the resulting \(214\times108\) relation matrix. It isolates \(106\) unit pivots with all cross-terms zero. Every entry of the residual two-column relation block is divisible by \(4\). Dividing that block by \(4\) gives an integral matrix whose unimodular reduction is a rank-\(2\) identity block. Therefore the full Smith form is
\[
\operatorname{diag}(1^{106},4,4),
\]
so
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/4)^2.
\]

The column change-of-basis matrix from the same reduction supplies two exact mod-\(4\) coordinate functionals on graph cycles. The verifier checks directly that both annihilate every one of the \(214\) facial relations.

It then exhausts every three-vertex clique in the one-skeleton. There are \(519\), and deleting the \(214\) facial triangles leaves \(305\) nonfacial cycles. Their oriented coordinate multiplicities are
\[
\begin{aligned}
&(1,0):34,\quad(3,0):18,\quad(0,1):18,\quad(0,3):30,\\
&(1,1):20,\quad(3,3):25,\quad(1,3):15,\quad(3,1):23,\\
&(1,2):25,\quad(3,2):26,\quad(2,1):30,\quad(2,3):21,\\
&(2,0):13,\quad(0,2):5,\quad(2,2):2.
\end{aligned}
\]
Thus all \(15\) nonzero classes occur and the zero class does not occur.

Identifying each class with its negative combines the twelve order-\(4\) elements into six inverse pairs. Their multiplicities are
\[
52,51,51,48,45,38.
\]
The three nonzero order-\(2\) classes are self-inverse and occur \(13,5,2\) times.

A simple cycle in a simplicial graph has at least three edges. Since every nonfacial triangle is nonzero, edge length \(3\) is the simple integral homology systole.

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds all \(107\) tetrahedra, reconstructs every face, contracts a deterministic spanning tree, computes the integral Smith data, derives exact mod-\(4\) quotient coordinates, verifies those coordinates on every facial relation, and exhausts every three-vertex clique.

Its exact successful output is:

`VERIFY_OK f=17,124,214,107 H1_Z=Z4+Z4 graph_triangles=519 facial3=214 empty3=305 all_empty3_nonzero=yes all_15_nonzero_classes=yes order4_inverse_pair_counts=52,51,51,48,45,38 order2_counts=13,5,2 smith=1^106,4,4`

The statement that all \(15\) nonzero classes occur is an exact exhaustive computation in the certified integral quotient, not an inference from the abstract homology group alone.

## Relationship to prior work
Lutz's geometric three-manifold survey constructs small triangulations of all ten closed flat three-manifolds. For \(\mathcal G_6\), it records a seventeen-vertex triangulation with
\[
H_1(\mathcal G_6;\mathbb Z)\cong(\mathbb Z/4)^2
\]
and face vector
\[
(17,124,214,107).
\]
The companion Manifold Page supplies the complete \(107\)-tetrahedron data set and independently records the same first homology.

Those sources determine the ambient topology, homology, and labelled triangulation but do not state which nonfacial triangular cycles represent which homology classes. Focused searches using the exact manifold label, Hantzsche--Wendt and didicosm terminology, empty-triangle language, simplicial-systole language, and the numerical fingerprint \(305\) did not locate the complete minimum-length class spectrum.

## Limitations
The theorem concerns simple simplicial cycles in this fixed seventeen-vertex triangulation. It does not compare alternate triangulations of \(\mathcal G_6\), Euclidean metric systoles, or stable norms.

The explicit coordinate basis is computational rather than canonical. The basis-independent content is that every nonzero homology class occurs at length \(3\), together with the multiplicity multisets for the six order-\(4\) inverse pairs and the three nonzero order-\(2\) classes.

An unindexed historical finite computation could contain the same triangular census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5, Theorem 21 and Table 9.
2. F. H. Lutz, *The Manifold Page*, `flat_3manifolds.txt` and `flat_3manifolds_hom.txt`, entry \(\mathcal G_6\).
