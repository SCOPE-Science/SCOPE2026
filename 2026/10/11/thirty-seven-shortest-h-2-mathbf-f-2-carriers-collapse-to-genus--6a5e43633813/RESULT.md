# Thirty-seven shortest \(H_2(\mathbf F_2)\)-carriers collapse to genus-three surfaces in the sixteen-vertex truncated cube space
## Finding
Let \(K\) be Lutz's sixteen-vertex triangulation of the truncated cube spherical space
\[
S^3/O^*,
\]
where \(O^*\) is the binary octahedral group. Direct reconstruction from the public facet table gives
\[
f(K)=(16,109,186,93).
\]

Over \(\mathbf F_2\),
\[
H_2(K;\mathbf F_2)\cong\mathbf F_2.
\]
The minimum number of vertices supporting its unique nonzero class is exactly \(9\).

Exactly \(37\) nine-vertex subsets attain this minimum. For every minimizing set \(S\), the induced subcomplex \(K[S]\) admits a sequence of elementary simplicial collapses that preserves all nine vertices and ends at a closed connected triangulated surface with
\[
f=(9,30,20)
\]
and Euler characteristic
\[
9-30+20=-1.
\]
Consequently every collapse target is the closed nonorientable genus-three surface \(N_3\).

For every one of the \(37\) carriers, the mod-two fundamental cycle of the final \(N_3\) reduces to the nonzero class in ambient
\[
H_2(K;\mathbf F_2).
\]
Exactly four minimizing induced subcomplexes are already nine-vertex \(N_3\) surfaces and need no collapse.

## Assumptions and scope
The labelled complex is the `truncated_cube_space` entry of the public spherical-three-manifold facet table. Vertices are \(1,\ldots,16\), and all \(93\) tetrahedra are embedded verbatim in `verify.py`.

For a vertex set \(S\), \(K[S]\) denotes the induced subcomplex. A set \(S\) supports the ambient class when the inclusion
\[
H_2(K[S];\mathbf F_2)\longrightarrow H_2(K;\mathbf F_2)
\]
has nonzero image.

The theorem concerns induced vertex support over \(\mathbf F_2\). Integral \(H_2(S^3/O^*;\mathbb Z)\) vanishes, so no nonzero integral second-homology class is claimed.

## Proof
The exact \(93\)-tetrahedron presentation reconstructs \(109\) edges and \(186\) triangles. Bit-exact Gaussian elimination over \(\mathbf F_2\) gives
\[
\operatorname{rank}\partial_2=93
\]
and
\[
\operatorname{rank}\partial_3=92.
\]
Hence
\[
\dim_{\mathbf F_2}H_2(K;\mathbf F_2)
=
186-93-92
=
1.
\]

For every vertex subset \(S\) with \(|S|\le9\), the verifier constructs the complete local simplicial \(2\)-cycle space of \(K[S]\). Every local cycle is then reduced modulo the global tetrahedral-boundary space
\[
\operatorname{im}\partial_3.
\]
The exact numbers of subsets with nonzero image for support sizes \(1,\ldots,9\) are
\[
0,0,0,0,0,0,0,0,37.
\]
Therefore the minimum support is \(9\), and there are exactly \(37\) minimizers.

For each minimizing set, the verifier next searches only legal elementary simplicial collapses whose free face has positive dimension, so no vertex is deleted. A successful collapse certificate is found for every carrier. The terminal complex has nine vertices, thirty edges, twenty triangles, no tetrahedra, every edge incident with exactly two triangles, connected one-skeleton, and every vertex link a connected cycle. Thus it is a closed connected triangulated surface. Its Euler characteristic is \(-1\), so the classification of closed surfaces identifies it as the nonorientable genus-three surface \(N_3\).

Finally, the mod-two sum of all twenty triangles of each terminal surface is its fundamental cycle. The verifier reduces this cycle modulo the ambient tetrahedral-boundary space and checks that the result is nonzero for all \(37\) carriers. Hence every collapse target represents the unique nonzero ambient mod-two \(H_2\)-class.

Four starting induced subcomplexes already satisfy the same closed-surface conditions and therefore require a collapse sequence of length zero.

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds the complete \(93\)-tetrahedron presentation, reconstructs all faces, computes both mod-two boundary ranks, exhausts every vertex subset through size nine, constructs complete local \(2\)-cycle spaces, produces and replays collapse certificates for all \(37\) minimizers, checks the surface links and Euler characteristic, and verifies every terminal fundamental cycle in ambient homology.

Exact successful output:

`VERIFY_OK f=16,109,186,93 H2_F2_dim=1 min_vertex_support=9 carriers9=37 already_induced_N3=4 collapse_to_9vertex_N3=37 ambient_fundamental_class_nonzero=37 support_counts_le9=0,0,0,0,0,0,0,0,37`

The support statement is exhaustive. The collapse statement is certificate-based for every one of the \(37\) minimizing supports; no sampling is used.

## Relationship to prior work
Lutz's 2003 geometric-three-manifold survey constructs a sixteen-vertex triangulation of the truncated cube space \(S^3/O^*\) and records its integral homology and face vector
\[
(16,109,186,93).
\]
The later three-manifold \(f\)-vector census again lists the same spherical space with the same smallest-known face vector. The public Manifold Page supplies the complete \(93\)-tetrahedron presentation used here.

These sources determine the spherical space, ambient homology, and finite complex, but they do not state the minimum mod-two \(H_2\) vertex support, the exact count \(37\), or the collapse of every minimum carrier to a genus-three nonorientable surface.

Focused literature searches using the truncated-cube-space name, the binary-octahedral quotient description, minimum-support terminology, induced-surface terminology, and the numerical fingerprint \(37\) did not locate a published statement covering this carrier theorem.

## Limitations
The theorem is specific to the published labelled sixteen-vertex triangulation and to induced vertex support over \(\mathbf F_2\). It does not classify larger supporting subsets, non-induced embedded surfaces, or normal-surface representatives.

The collapse targets are nine-vertex triangulations of \(N_3\); no claim is made that nine vertices are minimal for triangulating \(N_3\).

An unindexed historical finite computation could contain part or all of the same carrier census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; spherical-space section and truncated-cube theorem.
2. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; spherical-three-manifold table.
3. F. H. Lutz, *The Manifold Page*, `spherical_3manifolds.txt` and `spherical_3manifolds_hom.txt`, entry `truncated_cube_space`.
