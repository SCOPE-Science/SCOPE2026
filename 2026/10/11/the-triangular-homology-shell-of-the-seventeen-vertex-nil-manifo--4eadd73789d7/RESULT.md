# The triangular homology shell of the seventeen-vertex Nil manifold \(M_2\)
## Finding
Let \(K\) be the public seventeen-vertex triangulation `Nil_Oo1_2` of the orientable Nil three-manifold
\[
M_2=\{Oo,1\mid2\}.
\]
Its face vector is
\[
f(K)=(17,120,206,103),
\]
and an independent integral chain calculation gives
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/2.
\]

The one-skeleton contains exactly \(467\) three-vertex cliques. Exactly \(206\) are triangular faces, leaving \(261\) nonfacial triangular cycles.

Every one of those \(261\) nonfacial triangles is integrally homologically nonzero. Hence the simple integral homology \(1\)-systole has edge length \(3\) and exactly \(261\) minimizers.

There is an explicitly certified basis \(g_1,g_2\) of the free quotient and a nonzero order-two class \(t\) for which the unoriented minimum carriers have the complete distribution
\[
t:56,
\]
\[
\pm g_1:35,\qquad \pm(g_1+t):34,
\]
\[
\pm g_2:34,\qquad \pm(g_2+t):34,
\]
and
\[
\pm(g_1-g_2):37,\qquad \pm(g_1-g_2+t):31.
\]

Thus every infinite-order triangular systole is primitive. After projecting away the torsion, the complete triangular layer is exactly the six-vector shell
\[
\{\pm g_1,\ \pm g_2,\ \pm(g_1-g_2)\},
\]
and both torsion lifts occur in each of its three unoriented directions.

## Assumptions and scope
The labelled complex is the `Nil_Oo1_2` entry of the public `nil_3manifolds.txt` table. Vertices are \(1,\ldots,17\), and all \(103\) tetrahedra are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero. A class whose image in the free quotient is primitive is called primitive infinite-order here.

The displayed splitting
\[
H_1(K;\mathbb Z)\cong\langle g_1,g_2\rangle\oplus\langle t\rangle
\]
is a certified computational splitting. It is not asserted to be a canonical basis of the torus-bundle homology.

## Proof
Contract the deterministic spanning tree used in `verify.py`. The graph-cycle lattice then has rank
\[
120-17+1=104.
\]
Each of the \(206\) triangular faces supplies an integral relation.

The verifier performs only unimodular integral row and column operations on the resulting \(206\times104\) relation matrix. It isolates \(101\) unit pivots. Every entry in the residual three-column block is divisible by \(2\); after dividing that residual block by \(2\), a second unimodular reduction yields one unit pivot and two zero columns. Therefore the Smith data are
\[
1^{101},2,0,0,
\]
so
\[
H_1(K;\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/2.
\]

Two explicit integral cocycles \(y_1,y_2\) annihilate all \(206\) facial relations and give the two free coordinates. A third explicit mod-two cocycle \(w\) annihilates every facial relation modulo \(2\). Three triangular cycles have evaluation vectors
\[
(-1,0,0),\qquad(0,-1,0),\qquad(0,0,1),
\]
so these evaluations are jointly onto
\[
\mathbb Z^2\oplus\mathbb Z/2.
\]
Since the Smith calculation has already proved that this is the entire first homology group, the three evaluations give exact homology coordinates.

The verifier exhausts every three-vertex clique. The \(261\) nonfacial triangles have no zero coordinate. Up to reversing orientation their exact coordinate multiplicities are
\[
(0,0,1):56,
\]
\[
(1,0,0):35,\qquad(1,0,1):34,
\]
\[
(0,1,0):34,\qquad(0,1,1):34,
\]
\[
(1,-1,0):37,\qquad(1,-1,1):31.
\]
No other coordinate occurs.

A simple cycle in a simplicial graph has at least three edges. Since homologically nonzero three-edge cycles occur, the simple integral homology \(1\)-systole is exactly \(3\). Every infinite-order minimizer has primitive free coordinate, proving the primitivity statement.

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs all faces from the \(103\) tetrahedra, performs the integral Smith reduction, checks all three cocycles on every facial relation, verifies explicit generators for the three quotient coordinates, exhausts every graph triangle, and checks the complete oriented and unoriented coordinate distributions.

Exact successful output:

`VERIFY_OK f=17,120,206,103 H1_Z=Z^2+Z/2 graph_triangles=467 facial3=206 empty3=261 all_empty3_nonzero=yes pure_torsion=56 free_shell=g1:35,34|g2:34,34|g1-g2:37,31 smith=1^101,2,0,0`

The group structure and free-coordinate primitivity are proved integrally; the order-two coordinate is used only after the integral Smith type has been established.

## Relationship to prior work
Lutz, Sulanke, and Swartz list the Nil manifold
\[
\{Oo,1\mid2\}
\]
with the same smallest-known face vector
\[
(17,120,206,103)
\]
and record the general homology formula
\[
H_1(\{Oo,1\mid b\};\mathbb Z)\cong\mathbb Z^2\oplus\mathbb Z/b.
\]
The earlier geometric-three-manifold survey identifies \(M_b=\{Oo,1\mid b\}\) as a Nil \(T^2\)-bundle over \(S^1\). The public manifold table supplies the exact \(103\)-tetrahedron presentation.

Those sources determine the ambient topological type, homology, and face vector, but they do not state which nonfacial triangular cycles are essential, the exact number \(261\), or the seven-type homology spectrum above. Focused searches using the exact data-set label, the Seifert notation, Nil and Heisenberg aliases, shortest-homology terminology, empty-triangle terminology, and the numerical fingerprints did not locate a covering statement.

## Limitations
The theorem concerns simple simplicial cycles in this fixed labelled triangulation. It does not compare other triangulations of \(M_2\), geometric lengths in a Nil metric, or stable norms.

The basis \(g_1,g_2\) is computational. The intrinsic content is that all \(261\) empty triangles are essential and primitive after free projection, and that under an explicit integral splitting their free projections occupy exactly three unoriented primitive directions, with both order-two torsion lifts present in every direction.

An unindexed historical computation could contain part or all of the same finite census.

## References
1. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; Section 6 and Table 10.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 6 and Table 10.
3. F. H. Lutz, *The Manifold Page*, `nil_3manifolds.txt` and `nil_3manifolds_hom.txt`, entry `Nil_Oo1_2`.
