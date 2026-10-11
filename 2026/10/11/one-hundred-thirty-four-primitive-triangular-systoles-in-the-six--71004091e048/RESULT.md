# One hundred thirty-four primitive triangular systoles in the sixteen-vertex sixth-turn flat three-manifold
## Finding
Let \(K\) be the sixteen-vertex triangulation of the orientable flat three-manifold \(\mathcal G_5\), the sixth-turn space, with
\[
f(K)=(16,112,192,96).
\]
Then \(H_1(K;\mathbb Z)\cong\mathbb Z\). The simple integral homology \(1\)-systole, measured by number of edges, is \(3\).

The one-skeleton has \(470\) three-vertex cliques: \(192\) are triangular faces and \(278\) are nonfacial triangular cycles. Exactly \(134\) of the nonfacial triangles represent nonzero integral classes, and every one is primitive, hence equals \(\pm g\) for a generator \(g\) of \(H_1(K;\mathbb Z)\). The other \(144\) are integrally null-homologous.

With increasing orientations on edges and triangular cycles, the explicit cohomology generator below pairs as \(+1\) with \(85\) primitive triangles and as \(-1\) with \(49\). Reversing the generator swaps those two counts.

## Assumptions and scope
The exact labelled complex is the public `G5.scb` realization in the simpcomp three-manifold library. Lutz identifies \(\mathcal G_5\) as the flat torus bundle obtained from a \(2\pi/6\) rotation and records the same face vector and homology.

A simple integral homology \(1\)-systole is a simple simplicial cycle with the fewest edges among cycles representing nonzero integral first homology. This is not a statement about a Riemannian flat-metric systole.

## Proof
Choose the fixed spanning tree encoded in `verify.py`. The integral graph-cycle lattice is then \(\mathbb Z^{97}\), using coefficients on the \(97\) cotree edges. The \(192\) triangular faces give integral relation rows.

The verifier selects \(96\) relation rows and deletes the coordinate corresponding to edge \(\{3,12\}\). The resulting \(96\)-by-\(96\) matrix has determinant \(1\). Hence the facial-boundary lattice has a primitive rank-\(96\) sublattice.

Define an integral one-cochain \(w\), zero on the spanning-tree edges. Its nonzero values on increasingly oriented cotree edges are
\[
\begin{aligned}
&w(3,12)=w(3,13)=w(3,14)=w(3,15)=w(3,16)=1,\\
&w(4,5)=w(4,12)=w(4,13)=w(4,14)=w(4,15)=w(4,16)=1,\\
&w(5,10)=-1,\quad w(6,13)=1,\\
&w(7,12)=w(7,13)=w(7,14)=w(7,16)=1,\\
&w(8,12)=w(8,13)=1,\\
&w(9,12)=w(9,13)=w(9,16)=1,\\
&w(10,11)=w(10,12)=w(10,13)=w(10,14)=w(10,15)=w(10,16)=1.
\end{aligned}
\]
Exact evaluation gives zero on every facial triangle relation. Thus the relation rank is at most \(96\); the determinant-one minor makes it exactly \(96\) and primitive. Therefore
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]

Exhausting all graph triangles gives \(278\) nonfacial cycles. Their \(w\)-values are exactly \(144\) zeros, \(85\) values \(+1\), and \(49\) values \(-1\). Because the induced map on the rank-one homology has image containing \(1\), it is an isomorphism up to sign. Hence zero value is exactly null-homology and values \(\pm1\) are primitive. No simple simplicial cycle has fewer than three edges, proving the systolic statement.

## Verification
The standalone `verify.py` contains all \(96\) tetrahedra and uses only the Python standard library. It reconstructs the face vector, checks the integral cocycle on all \(192\) triangular faces, verifies the determinant-one lattice certificate by fraction-free Bareiss elimination, and exhausts every three-vertex clique.

Its exact successful output is:

`VERIFY_OK f=16,112,192,96 H1_Z=Z unit_minor_det=1 cliques3=470 facial3=192 empty3=278 null_empty3=144 primitive_systoles=134 oriented_pairings=+1:85,-1:49 cocycle_support=28`

All finite sets used in the claim are exhausted. No sampled computation is promoted to a statement about longer cycles.

## Relationship to prior work
Lutz's 2003 survey constructs and classifies the compact flat three-manifolds in this setting. It identifies \(\mathcal G_5\) as the \(2\pi/6\) twisted torus bundle and records for its small triangulation both \(H_1\cong\mathbb Z\) and \(f=(16,112,192,96)\). The exact simpcomp data supply the labelled tetrahedra used here.

The inspected literature does not state the integral homology class of every nonfacial triangular cycle. Focused searches under the \(\mathcal G_5\), sixth-turn, empty-triangle, shortest-loop, exact-face-vector, and numerical \(134\)-triangle formulations did not locate a covering indexed statement. Later work on coverings of \(\mathcal G_5\) confirms its abstract first homology but studies subgroups rather than these simplicial cycles.

## Limitations
The theorem concerns this labelled sixteen-vertex triangulation. It does not prove sixteen-vertex minimality for \(\mathcal G_5\), compare other triangulations of the sixth-turn space, or convert edge count into geometric length.

The \(85/49\) split depends on labels, increasing orientations, and the sign chosen for the cohomology generator. The basis-free content is the \(134/144\) primitive-versus-null partition.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5 and Table 9.
2. simpcomp-team, *simpcomp*, `complexes/manifolds/3Manifolds/G5.scb`, exact labelled complex used for verification.
3. G. Chelnokov and A. Mednykh, *The enumeration of coverings of closed orientable Euclidean manifolds \(\mathcal G_3\) and \(\mathcal G_5\)*, arXiv:`1905.13558`.
