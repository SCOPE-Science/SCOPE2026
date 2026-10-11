# Four integral triangle types in the sixteen-vertex quarter-turn flat three-manifold
## Finding
Let \(K\) be the published sixteen-vertex triangulation of the orientable flat three-manifold \(\mathcal G_4\). The published face vector is
\[
(16,115,198,99),
\]
and
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]

The one-skeleton contains exactly \(494\) three-vertex cliques. Of these, \(198\) are triangular faces and \(296\) are nonfacial triangular cycles.

Exactly \(259\) of the \(296\) nonfacial triangles represent nonzero integral homology. Hence the simple integral homology \(1\)-systole has edge length \(3\) and exactly \(259\) minimizers.

Choose a primitive free generator \(g\) and let \(t\) denote the nonzero element of the torsion summand. Up to reversing orientation, the \(259\) systoles have the complete class distribution
\[
t:112,\qquad
\pm g:69,\qquad
\pm(g+t):78.
\]
The remaining \(37\) empty triangles are integrally null-homologous.

Thus every infinite-order triangular systole is primitive, and both torsion lifts of the primitive free direction already occur at the minimum simple-cycle length.

## Assumptions and scope
The complex is the \(\mathcal G_4\) entry of the published `flat_3manifolds.txt` data table. Vertices are \(1,\ldots,16\), and all \(99\) tetrahedra are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero.

The basis \((g,t)\) is fixed by the verifier as follows. The triangle \(\{1,2,9\}\), oriented \(1\to2\to9\to1\), has coordinate \((1,0)\), while \(\{1,2,7\}\) has coordinate \((0,1)\). Reversing orientation changes the free coordinate sign and leaves the order-two coordinate unchanged.

## Proof
The \(99\)-facet presentation reconstructs \(115\) edges and \(198\) triangular faces. Contracting a spanning tree leaves a graph-cycle lattice of rank
\[
115-16+1=100.
\]
Every facial triangle gives an integral relation in this lattice.

The verifier applies only unimodular integer row and column operations to the resulting \(198\times100\) relation matrix. It first isolates \(98\) unit pivots. The remaining \(100\times2\) block has every nonzero entry equal to \(\pm2\); dividing that residual block by \(2\) gives an integer matrix whose Smith reduction has exactly one unit pivot and one zero column. Therefore the full Smith form is
\[
\operatorname{diag}(1,\ldots,1,2,0),
\]
with \(98\) unit entries, and consequently
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2.
\]

An explicit integral cocycle \(y\), stored sparsely in `verify.py`, annihilates all \(198\) facial relations and evaluates to \(1\) on the oriented triangle \((1,2,9)\). Hence it gives the exact free coordinate.

A second explicit mod-two cocycle \(w\) annihilates all facial relations modulo \(2\), vanishes on \((1,2,9)\), and evaluates to \(1\) on \((1,2,7)\). Since the quotient has already been proved to be \(\mathbb Z\oplus\mathbb Z/2\), \(w\) is exactly the torsion coordinate relative to the chosen splitting.

The verifier exhausts every three-vertex clique. The \(296\) nonfacial triangles have the exact coordinate counts
\[
(0,0):37,\qquad
(0,1):112,\qquad
(\pm1,0):69,\qquad
(\pm1,1):78.
\]
No nonfacial triangle has free coordinate of absolute value greater than \(1\). Thus all \(147\) infinite-order minimum carriers are primitive, and the \(112\) free-zero nontrivial carriers are exactly the pure torsion class.

A simple cycle in a simplicial graph has at least three edges. Since nonzero three-edge cycles occur, the simple integral homology systole is exactly \(3\).

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds all \(99\) tetrahedra, reconstructs every face, builds the contracted integral cycle presentation, verifies the Smith data, checks both cocycles against every facial relation, and exhausts every three-vertex clique.

Exact successful output:

`VERIFY_OK f=16,115,198,99 H1_Z=Z+Z/2 graph_triangles=494 facial3=198 empty3=296 null_empty3=37 systoles=259 pure_torsion=112 primitive_free=69 primitive_free_plus_torsion=78 smith=1^98,2,0`

The integral classification is not inferred from finite-field homology alone.

## Relationship to prior work
Lutz, Sulanke, and Swartz list \(\mathcal G_4\) among the orientable flat three-manifolds and record the smallest known face vector
\[
(16,115,198,99)
\]
together with homology
\[
(\mathbb Z,\mathbb Z\oplus\mathbb Z/2,\mathbb Z,\mathbb Z).
\]
The companion public data tables supply the complete tetrahedron list and the same homology group.

Those sources determine the ambient topology and homology but do not state which nonfacial triangular cycles are null, torsion, or primitive infinite-order classes. Focused searches using the exact manifold label, quarter-turn-space alias, empty-triangle terminology, shortest-homology terminology, and the numerical fingerprint \(296\) did not locate the complete \(37/112/69/78\) classification.

Later work on finite-sheeted coverings of \(\mathcal G_4\) studies subgroups of its crystallographic fundamental group and again records the ambient first homology, but it does not determine shortest simplicial cycles in this fixed triangulation.

## Limitations
The theorem concerns simple simplicial cycles in this fixed sixteen-vertex triangulation. It does not compare other triangulations of \(\mathcal G_4\), geometric Euclidean lengths, or stable norms.

The chosen splitting \(H_1\cong\mathbb Z\oplus\mathbb Z/2\) is not canonical. The intrinsic content is the multiset of class multiplicities up to automorphisms of the abstract homology group: one pure torsion class occurs \(112\) times, and the two torsion lifts of a primitive free direction occur \(69\) and \(78\) times.

An unindexed historical finite computation could contain the same triangular census.

## References
1. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; Table 7.
2. F. H. Lutz, *The Manifold Page*, `flat_3manifolds.txt` and `flat_3manifolds_hom.txt`, entry \(\mathcal G_4\).
3. G. Chelnokov and A. Mednykh, *On the coverings of closed orientable Euclidean manifolds G2 and G4*, Communications in Algebra 48 (2020), 2725--2739, DOI `10.1080/00927872.2019.1705468`.
