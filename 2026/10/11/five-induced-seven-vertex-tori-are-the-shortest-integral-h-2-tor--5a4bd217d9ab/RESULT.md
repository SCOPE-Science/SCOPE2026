# Five induced seven-vertex tori are the shortest integral \(H_2\)-torsion carriers in \(\mathcal B_3\)
## Finding
Let \(K\) be the published seventeen-vertex triangulation of the nonorientable flat three-manifold \(\mathcal B_3\). Its exact tetrahedron data reconstruct
\[
f(K)=(17,119,204,102),
\]
and the integral chain complex gives
\[
H_2(K;\mathbb Z)\cong\mathbb Z/2.
\]

The minimum number of vertices supporting an integral simplicial \(2\)-cycle in the unique nonzero class is exactly \(7\). Exactly five seven-vertex subsets attain the minimum:
\[
\{1,2,4,5,9,11,13\},\qquad
\{1,2,4,5,9,11,14\},
\]
\[
\{1,4,5,6,9,11,13\},\qquad
\{1,5,6,8,9,11,13\},
\]
and
\[
\{1,6,8,9,10,11,13\}.
\]

For each support \(S\), the induced subcomplex \(K[S]\) has
\[
f(K[S])=(7,21,14),
\]
contains no tetrahedron, and is a connected orientable closed surface. Since its Euler characteristic is zero, every minimum carrier is a seven-vertex torus. Its integral fundamental cycle represents the unique nonzero order-two class of \(H_2(K;\mathbb Z)\).

Thus the torsion class has exactly five minimum-support induced torus representatives. Each is also vertex-minimal among all triangulated tori.

## Assumptions and scope
The labelled complex is the \(\mathcal B_3\) entry of the public `flat_3manifolds.txt` table. Vertices are \(1,\ldots,17\), and all \(102\) tetrahedra are embedded verbatim in `verify.py`.

The vertex support of a simplicial chain is the union of vertices occurring in simplices with nonzero coefficient. The finding minimizes support among integral \(2\)-cycles representing the nonzero class of \(H_2(K;\mathbb Z)\), not area in a Euclidean metric.

The five surfaces are induced subcomplexes: every simplex of \(K\) whose vertices lie in the support is included.

## Proof
Let
\[
\partial_2:C_2(K;\mathbb Z)\longrightarrow C_1(K;\mathbb Z)
\]
and
\[
\partial_3:C_3(K;\mathbb Z)\longrightarrow C_2(K;\mathbb Z)
\]
be the integral simplicial boundary maps. The reconstructed complex has \(119\) edges, \(204\) triangles, and \(102\) tetrahedra.

The certificate supplies an integer matrix \(B\) with \(204\) rows and \(102\) columns and an integer left inverse \(L\) with
\[
\partial_2B=0,
\qquad
LB=I_{102}.
\]
A direct rank computation modulo \(3\) gives
\[
\operatorname{rank}\partial_2=102.
\]
Hence \(B\) is the full integral cycle lattice: if an integral cycle is \(x=Bc\) over \(\mathbb Q\), then \(c=Lx\) is integral.

Writing
\[
H=L\partial_3,
\]
the verifier checks
\[
BH=\partial_3
\]
and computes by fraction-free Bareiss elimination
\[
\lvert\det H\rvert=2.
\]
Therefore
\[
H_2(K;\mathbb Z)
\cong
\mathbb Z^{102}/H\mathbb Z^{102}
\cong
\mathbb Z/2.
\]

Modulo \(2\), the matrix \(H\) has rank \(101\). The verifier computes the unique nonzero linear functional \(\lambda\) on the quotient and pulls it back through \(L\) to a parity functional on triangle chains. Every integral representative of the nonzero torsion class reduces modulo \(2\) to a \(2\)-cycle on which this functional is \(1\).

The verifier then exhausts every vertex subset of size at most seven. For each support it computes the complete mod-two span of supported triangle columns, augmented by the detector coordinate. No subset with at most six vertices supports a mod-two cycle with detector \(1\). Exactly the five displayed seven-subsets do. This proves the lower bound and leaves only those five possible minimum supports.

For each of the five supports, the induced complex has \(21\) edges, \(14\) triangles, and no tetrahedra. Every edge lies in exactly two triangles, every vertex link is a single cycle, and coherent triangle orientations propagate globally. Thus each induced complex is a connected orientable closed surface. Its Euler characteristic is
\[
7-21+14=0,
\]
so it is a torus. The resulting oriented fundamental chain is checked integrally against \(\partial_2\), and its quotient detector is \(1\), proving that it represents the nonzero class in \(H_2(K;\mathbb Z)\).

Finally, any triangulated torus with \(v\) vertices satisfies \(e=3v\). Since \(e\leq\binom v2\), one has \(v\geq7\). Hence each of these induced tori is itself vertex-minimal.

## Verification
The standalone `verify.py` uses only the Python standard library. `certificate.json` contains the exact integral cycle-basis matrix \(B\), its left inverse \(L\), and the expected five supports.

The verifier reconstructs the complete simplicial complex, checks the integral kernel certificate, recomputes the quotient matrix \(H\), proves its determinant has absolute value \(2\), constructs the unique mod-two quotient detector, exhausts every support through seven vertices, verifies all five induced surfaces by edge incidence and vertex links, reconstructs integral fundamental cycles, and checks their nonzero torsion class.

Exact successful output:

`VERIFY_OK f=17,119,204,102 H2_Z=Z/2 min_vertex_support=7 carriers7=5 all_carriers_induced_orientable_tori=yes all_carriers_nonzero_torsion=yes support_counts_le7=0,0,0,0,0,0,5 supports=1-2-4-5-9-11-13;1-2-4-5-9-11-14;1-4-5-6-9-11-13;1-5-6-8-9-11-13;1-6-8-9-10-11-13`

The support lower bound is exhaustive and does not infer impossibility from a search timeout or partial enumeration.

## Relationship to prior work
Lutz's geometric three-manifold survey constructs small triangulations of all four nonorientable flat three-manifolds and records a seventeen-vertex triangulation of \(\mathcal B_3\). Its table gives
\[
H_2(\mathcal B_3;\mathbb Z)\cong\mathbb Z/2
\]
and face vector \((17,119,204,102)\). The companion public data file supplies the complete \(102\)-tetrahedron presentation.

Those sources establish the ambient torsion class and the finite complex, but they do not state its minimum vertex support, identify induced seven-vertex torus representatives, or give the exact count five. Focused literature searches using the \(\mathcal B_3\) label, nonorientable-flat-manifold aliases, induced-torus language, minimum-\(H_2\)-support language, and seven-vertex terminology did not locate a covering statement.

The closest indexed seven-vertex-torus work found in those searches concerns the standalone minimal torus and its self-maps rather than embedded surfaces in \(\mathcal B_3\). Work on small torsion complexes in other dimensions likewise does not imply the present inclusion-sensitive statement.

## Limitations
The theorem is specific to the labelled seventeen-vertex triangulation and to vertex support. It does not compare other triangulations of \(\mathcal B_3\), classify larger torus carriers, or minimize geometric area in a flat metric.

The ZIB report associated with the source is dated only to November 2003 in the inspected metadata. The machine-readable source date therefore uses the earliest inspected day-resolved public release, arXiv v1 on 2003-11-07; no calendar day is invented for the month-only report.

An unindexed historical finite computation could contain part or all of the same five-torus census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5, Theorem 23 and Table 9.
2. F. H. Lutz, *The Manifold Page*, `flat_3manifolds.txt`, entry `B3`.
3. F. H. Lutz, *The Manifold Page*, `flat_3manifolds_hom.txt`, entry `B3`.
