# Seven homology classes exhaust the triangular systoles of a sixteen-vertex Klein-bottle product
## Finding
Let \(X\) be the sixteen-vertex triangulation of \(K_{\mathrm{Kl}}\times S^1\), where \(K_{\mathrm{Kl}}\) denotes the Klein bottle, with face vector
\[
(16,115,198,99).
\]
Its first integral homology is
\[
H_1(X;\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/2.
\]

The one-skeleton contains exactly \(495\) three-vertex cliques. Of these, \(198\) are triangular faces and \(297\) are nonfacial triangular cycles. Every one of the \(297\) nonfacial triangles represents a nonzero integral homology class. Therefore the simple integral homology \(1\)-systole has edge length \(3\), with exactly \(297\) minimizers.

In the integral coordinate system certified below, with the last coordinate in \(\mathbb Z/2\), the unoriented shortest classes and their multiplicities are
\[
(0,0,1):55,
\]
\[
(0,1,0):54,\qquad (0,1,1):33,
\]
\[
(1,0,0):41,\qquad (1,0,1):36,
\]
\[
(1,-1,0):40,\qquad (1,-1,1):38.
\]
Thus the shortest layer consists of the pure order-two class together with both torsion lifts of three primitive free directions. The three free directions are exactly
\[
\pm(0,1),\qquad \pm(1,0),\qquad \pm(1,-1),
\]
which form the three unoriented directions of the standard \(A_2\)-type hexagonal shell in the chosen basis.

## Assumptions and scope
The complex is the labelled \(99\)-tetrahedron data set listed as \(K_{\mathrm{Kl}}\times S^1\) on the Manifold Page. Vertices are \(1,\ldots,16\). Every edge is oriented from its smaller endpoint to its larger endpoint, and an increasing triangle \(a<b<c\) is oriented as the cycle \(a\to b\to c\to a\).

The final coordinate is mod two. Reversing the orientation of a triangle negates the two free coordinates and leaves the torsion coordinate unchanged, so the table is stated up to orientation. The claim concerns simple cycles measured by edge length and does not classify longer representatives.

## Proof
Use the star at vertex \(1\) as a spanning tree. Contracting its fifteen edges identifies the graph cycle lattice with \(\mathbb Z^{100}\). The \(198\) triangular faces give an integral \(198\times100\) relation matrix.

The verifier applies only unimodular integer row and column operations. It first extracts \(97\) unit pivots. The residual block has exactly one nonzero column, all of whose nonzero entries are \(\pm2\). Since their gcd is \(2\), the remaining block reduces unimodularly to the single invariant factor \(2\). Hence the Smith invariants are
\[
1^{97},2,
\]
with two zero columns, proving
\[
H_1(X;\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/2.
\]

Two explicit integral cocycles \(y_1,y_2\), stored in `verify.py`, vanish on every facial relation. Their evaluations on the triangular cycles \(\{1,2,7\}\) and \(\{1,3,6\}\) are respectively
\[
(-1,0)\quad\text{and}\quad(0,1),
\]
so they give a surjection from \(H_1\) onto \(\mathbb Z^2\). Because the Smith calculation already proves that the free rank is exactly two, this map identifies the free quotient.

A third explicitly stored mod-two cocycle \(z\) also vanishes on every facial relation. The triangle \(\{1,2,10\}\) has coordinates
\[
(0,0,1).
\]
It lies in the kernel of the free coordinate map but is detected by \(z\); since that kernel is the unique order-two subgroup, \(z\) is exactly a torsion coordinate. Thus the three coordinates determine the full integral homology class of every triangular cycle.

Exhaustion of all graph triangles gives \(495\) cliques and \(297\) nonfaces. Their seven nonzero homology classes have precisely the multiplicities displayed in the finding. No nonfacial triangle has coordinates \((0,0,0)\). Every class with nonzero free part has coprime free coordinates and is therefore primitive of infinite order; the remaining \(55\) triangles represent the unique order-two class.

A simple cycle in a simplicial graph has at least three edges. Since all \(297\) nonfacial triangles are homologically nonzero, edge length \(3\) is the exact simple integral homology systole.

## Verification
The standalone `verify.py` embeds all \(99\) tetrahedra and uses only the Python standard library. It reconstructs the full face vector, proves the Smith invariants by unimodular reduction, checks all three cocycles against every facial relation, certifies the free and torsion coordinate tests, and exhausts every three-vertex clique.

Exact successful output:

`VERIFY_OK f=16,115,198,99 H1_Z=Z^2+Z/2 graph_triangles=495 facial3=198 empty3=297 all_empty3_nonzero=yes torsion_systoles=55 primitive_infinite_systoles=242 classes_up_to_sign=7 counts=55,54,41,40,38,36,33 free_directions=01|10|1-1 torsion_lifts=both`

The integral conclusion is not inferred from a finite-field experiment; the free and torsion structure is certified directly over \(\mathbb Z\), with the final torsion detector checked mod two only after the Smith type is established.

## Relationship to prior work
Lutz's earlier flat-manifold survey identifies \(\mathcal B_1=K_{\mathrm{Kl}}\times S^1\), where \(K_{\mathrm{Kl}}\) is the Klein bottle, and records its homology. Lutz, Sulanke, and Swartz later list a sixteen-vertex triangulation with face vector \((16,115,198,99)\), improving the earlier seventeen-vertex entry. The companion data page supplies the exact \(99\)-tetrahedron complex used here.

The inspected literature concerns face vectors, small triangulations, and ambient homology. It does not state the complete shortest integral homology-loop spectrum of this labelled triangulation. Focused searches using the product-manifold notation, the \(\mathcal B_1\) alias, nonfacial-triangle language, shortest-homology language, and the numerical fingerprint \(297\) did not locate the seven-class spectrum.

## Limitations
The coordinates depend on the certified basis of the free quotient and the chosen torsion detector. The basis-independent content is that all \(297\) nonfacial triangles are systoles, that \(55\) represent the pure order-two class, and that the remaining \(242\) occupy both torsion lifts of exactly three primitive unoriented free directions with multiplicity pairs \(54/33\), \(41/36\), and \(40/38\).

The result is specific to this sixteen-vertex triangulation and does not compare other triangulations of \(K_{\mathrm{Kl}}\times S^1\). An unindexed historical computation could contain the same finite census.

## References
1. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; Table 7 lists \(K_{\mathrm{Kl}}\times S^1\) with face vector \((16,115,198,99)\), primary MSC 57Q15.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5 identifies \(\mathcal B_1=K_{\mathrm{Kl}}\times S^1\), where \(K_{\mathrm{Kl}}\) is the Klein bottle, and records its homology.
3. F. H. Lutz, *The Manifold Page: Small triangulations of geometric 3-manifolds*, companion data file `flat_3manifolds.txt`, entry `KxS^1`.
