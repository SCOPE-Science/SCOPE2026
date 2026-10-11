# A one-vertex Bockstein gap in the seventeen-vertex flat manifold \(\mathcal B_4\)
## Finding
Let \(K\) be the published seventeen-vertex triangulation of the nonorientable flat three-manifold \(\mathcal B_4\). Direct reconstruction from the complete facet table gives
\[
f(K)=(17,117,200,100).
\]
Exact integral chain calculations give
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/4,
\qquad
H_2(K;\mathbb Z)\cong\mathbb Z/2,
\]
and exact mod-two elimination gives
\[
H_2(K;\mathbf F_2)\cong\mathbf F_2^2.
\]

Let \(c\) be the unique nonzero class in the image of reduction
\[
H_2(K;\mathbb Z)\longrightarrow H_2(K;\mathbf F_2),
\]
and let
\[
\beta:H_2(K;\mathbf F_2)\longrightarrow H_1(K;\mathbb Z)
\]
be the Bockstein for the coefficient sequence \(0\to\mathbb Z\xrightarrow{\,2\,}\mathbb Z\to\mathbf F_2\to0\).

The class \(c\) has minimum vertex support exactly \(7\), attained by exactly seven vertex sets:
\(\{2,5,6,7,10,13,15\}\),
\(\{2,5,6,7,13,15,16\}\),
\(\{2,5,6,10,12,13,15\}\),
\(\{2,5,9,10,12,14,16\}\),
\(\{5,7,9,10,12,14,16\}\),
\(\{5,7,9,11,12,14,15\}\),
\(\{5,7,9,12,14,15,16\}\).
For each of these sets \(S\), the induced subcomplex \(K[S]\) has face vector
\[
(7,21,14),
\]
contains no tetrahedron, is a connected orientable closed surface, and therefore is a seven-vertex torus. Its integral fundamental cycle represents the unique nonzero class of \(H_2(K;\mathbb Z)\).

The other two nonzero classes of \(H_2(K;\mathbf F_2)\) both have Bockstein equal to the unique order-two class in the \(\mathbb Z/4\) summand of \(H_1(K;\mathbb Z)\). Neither can be carried on seven vertices. Both first occur on eight vertices, and their complete minimum-carrier counts are
\[
15\quad\text{and}\quad20.
\]
For every one of those \(35\) minimum supports, the image of the induced mod-two homology map into ambient \(H_2\) is exactly the corresponding one-dimensional class. In particular, none of the \(35\) eight-vertex minimum supports contains one of the seven integral torus carriers.

Thus this triangulation exhibits an exact one-vertex Bockstein gap: the mod-two class that lifts integrally appears on seven vertices, while both classes with nonzero Bockstein require eight.

## Assumptions and scope
For a vertex set \(S\), \(K[S]\) denotes the induced subcomplex. A class has vertex support at most \(m\) when it lies in the image of the inclusion-induced homology map from some \(K[S]\) with \(|S|\le m\). Minimum-carrier counts refer to vertex sets, not to individual cycles inside one induced subcomplex.

The computational mod-two basis used in `carrier_census.json` is not canonical. The invariant distinction is canonical: there is one nonzero class with zero Bockstein, namely the reduction of the integral \(H_2\)-torsion class, and two nonzero classes with the same nonzero Bockstein. Accordingly, the unordered pair \(\{15,20}\) is intrinsic to the two Bockstein-nonzero classes, while assigning one count to a named computational coordinate is basis-dependent.

## Proof
The complete \(100\)-tetrahedron presentation reconstructs \(117\) edges and \(200\) triangular faces.

For integral degree-two homology, `integral_certificate.json` gives a \(200\times100\) integer matrix \(B\) and a \(100\times200\) integer matrix \(L\). The verifier checks
\[
\partial_2B=0,
\qquad
LB=I_{100},
\]
and independently verifies \(\operatorname{rank}\partial_2=100\). Hence the columns of \(B\) form a primitive integral basis of \(\ker\partial_2\). Expressing tetrahedral boundaries in that basis gives
\[
H=L\partial_3,
\]
a \(100\times100\) integer matrix. Exact fraction-free determinant evaluation gives
\[
\det H=-2.
\]
Therefore
\[
H_2(K;\mathbb Z)\cong\mathbb Z/2.
\]

For degree-one homology, contract the certified spanning tree of the one-skeleton. The resulting graph-cycle lattice has rank \(101\). Unimodular row and column operations on the \(200\) facial triangle relations isolate \(99\) unit Smith factors; the residual block is four times a primitive rank-one matrix with one zero column. Thus
\[
H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/4.
\]
The certificate also supplies an integral free cocycle and a mod-four torsion cocycle, both checked on every facial relation, so Bockstein values can be evaluated exactly.

Over \(\mathbf F_2\), the verifier computes
\[
\dim\ker\partial_2=101,
\qquad
\dim\operatorname{im}\partial_3=99,
\]
so \(H_2(K;\mathbf F_2)\cong\mathbf F_2^2\). For a mod-two \(2\)-cycle \(z\), the verifier computes
\[
\beta([z])=\left[\frac{\partial z}{2}\right]\in H_1(K;\mathbb Z)
\]
using the exact integral edge boundary and the certified \(H_1\) coordinates. Among the three nonzero mod-two classes, exactly one has Bockstein zero; the other two map to the order-two element of \(\mathbb Z/4\). By exactness of the coefficient sequence, the zero-Bockstein class is precisely the reduction of the nonzero integral class.

The verifier then exhausts every vertex set through size eight. No nonzero mod-two class is carried on at most six vertices. At size seven, only the zero-Bockstein class appears, on exactly the seven sets listed above. At size eight, the two Bockstein-nonzero classes first appear, on exactly \(15\) and \(20\) supports. The complete support lists are recorded in `carrier_census.json` and are replayed from the facet table rather than trusted as input.

Finally, every seven-vertex carrier is checked directly: it has \(21\) induced edges, \(14\) induced triangles, no induced tetrahedron, every edge lies in exactly two triangles, and triangle orientations propagate consistently across all edges. Hence each carrier is an orientable closed surface with Euler characteristic \(0\), therefore a torus.

## Verification
The package contains `verify.py`, `integral_certificate.json`, and `carrier_census.json`. The verifier uses only the Python standard library. It reconstructs the full complex, checks the integral homology certificates, computes the mod-two quotient and Bockstein, exhausts all vertex supports through size eight, verifies the exact carrier lists, and checks the surface structure of all seven integral minimizers.

Exact successful output:

`VERIFY_OK f=17,117,200,100 H1_Z=Z+Z/4 H2_Z=Z/2 H2_F2_dim=2 bockstein=nonzero_classes_to_order2 integral_reduction_min_support=7 integral_reduction_carriers=7 all_integral_min_carriers_induced_tori=yes bockstein_min_supports=8,8 bockstein_carrier_counts=15,20 minimal_support_images_rank1=yes`

The support statements are exhaustive finite classifications. No random search, timeout inference, or partial enumeration is used.

## Relationship to prior work
Lutz's geometric three-manifold survey constructs small triangulations of all ten closed flat three-manifolds. For \(\mathcal B_4\), its flat-space table records
\[
H_1\cong\mathbb Z\oplus\mathbb Z/4,
\qquad
H_2\cong\mathbb Z/2,
\qquad
f=(17,117,200,100),
\]
and explains that the nonorientable examples arise from twisted products followed by bistellar simplification. The Manifold Page gives the complete labelled facet list used here. Lutz--Sulanke--Swartz later record the same \(\mathcal B_4\) homology and face vector in their flat-manifold table.

Those sources determine the ambient topology, homology, and simplicial input, but they do not state the support filtration of the three nonzero classes in \(H_2(K;\mathbf F_2)\), the exact coefficient-Bockstein distinction, the seven induced torus carriers, or the \(15/20\) eight-vertex carrier counts. Focused literature searches under the \(\mathcal B_4\) label, flat-manifold aliases, Bockstein language, induced-torus language, minimum-support language, and the numerical fingerprints did not locate a covering statement.

## Limitations
The result concerns vertex support in this fixed seventeen-vertex triangulation. It does not classify larger supports, other triangulations of \(\mathcal B_4\), geometric-area minimizers, or stable norms.

The two Bockstein-nonzero classes are canonically a two-element coset of the integral-reduction line, but they have no preferred ordering; the counts \(15\) and \(20\) should therefore be regarded as an unordered pair unless the explicit computational basis is fixed.

An unindexed historical finite computation could contain part or all of the same support census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; Section 5, Theorems 21--23 and Table 9.
2. F. H. Lutz, *The Manifold Page*, `flat_3manifolds.txt` and `flat_3manifolds_hom.txt`, entry `B4`.
3. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; Table 7.
