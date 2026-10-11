# Sixty induced seven-vertex tori are the shortest \(H_2(\mathbf F_2)\)-carriers in the fifteen-vertex three-torus
## Finding
Let \(K=M^3_1(15)\) be the Kühnel--Lassmann neighborly fifteen-vertex triangulation of the three-torus. Its tetrahedra are the \(\mathbb Z/15\mathbb Z\)-translates of
\[
0137,\quad 0157,\quad 0237,\quad 0267,\quad 0457,\quad 0467.
\]
Thus
\[
f(K)=(15,105,180,90).
\]

Over \(\mathbf F_2\),
\[
H_2(K;\mathbf F_2)\cong \mathbf F_2^3.
\]
The minimum number of vertices supporting a simplicial \(2\)-cycle with nonzero ambient homology class is exactly \(7\).

Exactly \(60\) seven-vertex subsets attain that minimum. For every such subset \(S\), the induced subcomplex \(K[S]\) has
\[
f(K[S])=(7,21,14),
\]
contains no tetrahedron, and is an orientable closed surface of Euler characteristic zero. Hence each minimum carrier is a seven-vertex triangulated torus, and its mod-two fundamental cycle maps nontrivially into \(H_2(K;\mathbf F_2)\).

The \(60\) minimum carriers represent exactly four of the seven nonzero classes in \(H_2(K;\mathbf F_2)\), with exactly \(15\) carriers in each represented class. Define
\[
\alpha=[K[\{0,1,2,3,4,5,6\}]],\qquad
\beta=[K[\{0,1,2,3,8,9,10\}]],
\]
and
\[
\gamma=[K[\{0,1,4,5,8,9,12\}]].
\]
These three classes are linearly independent, and the fourth represented class is
\[
\alpha+\beta+\gamma,
\]
carried for example by
\[
K[\{0,2,4,6,8,10,12\}].
\]

The published affine automorphism group of order \(120\) acts transitively on all \(60\) minimum carriers. The cyclic translation subgroup of order \(15\) preserves each represented homology class and acts transitively on its \(15\) carriers.

## Assumptions and scope
Vertices are labeled by \(\mathbb Z/15\mathbb Z\). For a vertex set \(S\), \(K[S]\) denotes the induced subcomplex.

The vertex support of a simplicial chain is the union of the vertices of its simplices with nonzero coefficient. A vertex set supports a nonzero ambient \(H_2\)-class when some \(2\)-cycle in \(K[S]\) maps to a nonzero class under inclusion
\[
H_2(K[S];\mathbf F_2)\longrightarrow H_2(K;\mathbf F_2).
\]

The result is mod-two. It classifies the complete minimum vertex-support layer in degree two; it does not classify larger supports or integral orientations of all \(60\) embedded tori.

## Proof
The six cyclic tetrahedron generators reconstruct exactly \(90\) tetrahedra, \(180\) triangles, and all
\[
\binom{15}{2}=105
\]
edges. Exact mod-two elimination gives
\[
\operatorname{rank}\partial_2=88,\qquad
\operatorname{rank}\partial_3=89,
\]
and therefore
\[
\dim_{\mathbf F_2}H_2(K;\mathbf F_2)=180-88-89=3.
\]

For every vertex subset \(S\) of size at most \(7\), the verifier computes the full kernel of the triangle-to-edge boundary map on \(K[S]\). Every local \(2\)-cycle is then reduced modulo the global tetrahedral-boundary space \(\operatorname{im}\partial_3\).

All subsets with at most six vertices have zero image in ambient \(H_2\). Exactly \(60\) seven-subsets have nonzero image, and every one has one-dimensional image.

For each of those \(60\) subsets, the induced complex has \(21\) edges, \(14\) triangles, and no tetrahedra. Every induced edge lies in exactly two induced triangles. The verifier also propagates compatible signs across adjacent triangles and succeeds globally in every case, proving orientability. Thus each carrier is a connected orientable closed triangulated surface with Euler characteristic
\[
7-21+14=0,
\]
so each is a torus.

Reducing the \(60\) torus fundamental cycles modulo \(\operatorname{im}\partial_3\) gives exactly four nonzero quotient vectors, each with multiplicity \(15\). The classes \(\alpha,\beta,\gamma\) displayed above are independent. Exact reduction gives
\[
[\{0,2,4,6,8,10,12\}]=\alpha+\beta+\gamma.
\]

Finally, the verifier checks all \(120\) affine permutations
\[
x\longmapsto ux+v\pmod {15},
\qquad
u\in\{\pm1,\pm2,\pm4,\pm8\},
\]
against the complete tetrahedron set. The orbit of one minimum carrier has size \(60\), hence is the whole carrier set. For each of the four displayed class representatives, its \(15\) translates are distinct carriers and all have the same ambient homology class.

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs the complex from the six published cyclic generators, computes the global mod-two chain ranks, exhausts every vertex subset of size at most seven, reconstructs every local cycle space, verifies the surface and orientability conditions of all \(60\) minimum carriers, classifies their ambient homology classes, and checks the full published affine symmetry action.

Its exact successful output is:

`VERIFY_OK f=15,105,180,90 H2_F2_dim=3 min_vertex_support=7 supports7=60 all_supports_induced_orientable_tori=yes class_counts=15,15,15,15 classes=001|010|100|111 affine_auts_checked=120 support_orbit=60 translation_orbits=15_per_class`

The minimum statement is exhaustive over all vertex supports of size at most seven. No random search or partial enumeration is used.

## Relationship to prior work
Kühnel and Lassmann introduced the fifteen-vertex three-torus in 1984 as a quotient of a periodic tessellation of Euclidean three-space and identified its affine symmetry group. Brehm and Kühnel later gave the exact six cyclic tetrahedron generators and again described the order-\(120\) symmetry group. Lutz, Sulanke, and Swartz record the face vector \((15,105,180,90)\) and the homology of \(T^3\).

The inspected full later treatment explicitly calls the complex a natural three-dimensional analogue of the unique seven-vertex triangulation of the two-torus, but it does not state that the three-torus contains exactly \(60\) induced seven-vertex tori, that these are precisely the minimum \(H_2\)-supports, or that they split \(15,15,15,15\) among four ambient classes.

The older 1984 article is the historical primary source. Its publicly accessible page supplied the abstract and bibliographic metadata, while its full text was not available through the inspected open route. This leaves a residual originality risk, recorded below, rather than being treated as evidence of absence.

## Limitations
The result is over \(\mathbf F_2\). It does not identify integral normal vectors for the four represented classes or classify non-minimum embedded surfaces.

The original 1984 article is publicly dated only to February 1984 in the inspected metadata. The machine-readable source date used for this package is the earliest day-resolved public source inspected that explicitly records the fifteen-vertex \(T^3\), namely the 2008-05-08 arXiv submission of Lutz--Sulanke--Swartz; no calendar day has been invented for the 1984 source.

An inaccessible passage of the original article or another unindexed historical computation could contain part of the finite \(60\)-torus census.

## References
1. W. Kühnel and G. Lassmann, *The rhombidodecahedral tessellation of 3-space and a particular 15-vertex triangulation of the 3-dimensional torus*, Manuscripta Mathematica 49 (1984), 61--77, DOI `10.1007/BF01174871`.
2. U. Brehm and W. Kühnel, *Lattice triangulations of \(E^3\) and of the 3-torus*, Stuttgart Mathematical Preprint 2009/001; Section 3 gives the six cyclic tetrahedron generators and the affine symmetry.
3. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08.
