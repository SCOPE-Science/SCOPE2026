# Twenty induced projective planes are the shortest mod-two \(H_2\)-carriers in Walkup's eleven-vertex \(\mathbb{RP}^3\)
## Finding
Let \(K\) be the forty-tetrahedron eleven-vertex triangulation of
\[
\mathbb{RP}^3
\]
listed in the public spherical-three-manifold data. Its face vector is
\[
f(K)=(11,51,80,40).
\]

Over \(\mathbf F_2\),
\[
H_2(K;\mathbf F_2)\cong\mathbf F_2.
\]
The minimum number of vertices supporting the unique nonzero class is exactly \(6\).

Exactly \(20\) six-vertex subsets attain this minimum. For every minimizing set \(S\), the induced subcomplex \(K[S]\) has
\[
f(K[S])=(6,15,10),
\]
contains no tetrahedron, every edge belongs to exactly two induced triangles, every vertex link is a cycle, and
\[
\chi(K[S])=6-15+10=1.
\]
Thus every minimum carrier is the six-vertex triangulation of \(\mathbb{RP}^2\), and its mod-two fundamental cycle maps nontrivially into ambient \(H_2\).

The full simplicial automorphism group has order \(48\). It has exactly two orbits on the twenty minimum carriers, of sizes
\[
12\quad\text{and}\quad8.
\]
Representatives are
\[
\{2,3,4,5,10,11\}
\]
and
\[
\{2,3,4,9,10,11\}.
\]

## Assumptions and scope
Vertices are labelled \(1,\ldots,11\), and the forty tetrahedra are embedded verbatim in `verify.py` from the public data table.

For a vertex set \(S\), \(K[S]\) denotes the induced subcomplex. A set \(S\) supports the ambient mod-two \(H_2\)-class when the inclusion map
\[
H_2(K[S];\mathbf F_2)\longrightarrow H_2(K;\mathbf F_2)
\]
has nonzero image.

The result is a mod-two middle-homology statement. Integral \(H_2(\mathbb{RP}^3;\mathbb Z)\) vanishes, so the carrier surfaces are not asserted to define nonzero integral second-homology classes.

## Proof
From the forty tetrahedra, the verifier reconstructs \(51\) edges and \(80\) triangles.

Over \(\mathbf F_2\), exact bit-vector elimination gives
\[
\operatorname{rank}\partial_2=40,\qquad
\operatorname{rank}\partial_3=39.
\]
Therefore
\[
\dim_{\mathbf F_2}H_2(K;\mathbf F_2)=80-40-39=1.
\]

For every vertex subset \(S\) with \(|S|\le6\), the verifier computes the entire local \(2\)-cycle space of \(K[S]\). Each local cycle is then reduced modulo the global tetrahedral-boundary space
\[
\operatorname{im}\partial_3.
\]
No subset on at most five vertices has nonzero image in ambient \(H_2\). Exactly twenty six-vertex subsets do, and each has one-dimensional image.

For every one of those twenty sets, induced-face reconstruction gives exactly \(15\) edges and \(10\) triangles and no tetrahedron. Every induced edge is incident to two induced triangles. Every vertex link is checked to be a connected cycle. The one-skeleton is complete, so the surface is connected, and its Euler characteristic is \(1\). By classification of closed connected surfaces, each induced complex is \(\mathbb{RP}^2\).

Finally, the verifier exhausts all degree-compatible vertex permutations, prunes by triangular-face membership, and verifies the complete tetrahedron set at each leaf. This gives exactly \(48\) simplicial automorphisms. Their action on the twenty minimum carriers has exactly two orbits, of sizes \(12\) and \(8\).

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs the complex from all forty tetrahedra, computes the ambient mod-two chain ranks, exhausts every vertex subset of size at most six, reconstructs every local \(2\)-cycle space, verifies the surface structure of all twenty minimizers, and independently enumerates the full simplicial automorphism group.

Exact successful output:

`VERIFY_OK f=11,51,80,40 H2_F2_dim=1 min_vertex_support=6 carriers6=20 all_carriers_induced_RP2=yes aut=48 carrier_orbits=12,8 reps=23451011|23491011`

The support minimum is exhaustive over every vertex subset of size at most six. No sampling or heuristic search is used.

## Relationship to prior work
The public Manifold Page records this eleven-vertex \(\mathbb{RP}^3\) triangulation with face vector \((11,51,80,40)\), marks that face vector as vertex-minimal, supplies all forty tetrahedra, and records integral first homology \(\mathbb Z/2\).

The earlier literature establishes the eleven-vertex minimality context for triangulations of \(\mathbb{RP}^3\). The inspected sources do not state that ambient mod-two \(H_2\) first appears on six vertices, that exactly twenty induced six-vertex projective planes realize it, or that those twenty split into two simplicial-symmetry orbits of sizes \(12\) and \(8\).

The standard six-vertex triangulation of \(\mathbb{RP}^2\) is well known and appears in published finite-complex censuses. That fact identifies the topology of each carrier after its exact induced incidence data have been established; it does not imply that twenty such carriers occur inside this particular eleven-vertex three-manifold triangulation.

## Limitations
The theorem concerns induced vertex support over \(\mathbf F_2\). It does not classify larger supporting subsets, non-induced embedded projective planes, or normal-surface representatives.

The two orbit representatives depend on the public vertex labeling, while the orbit sizes and the twenty-carrier count are combinatorial invariants of the labelled complex up to isomorphism.

An unindexed historical computation could contain part or all of the same induced-projective-plane census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07.
2. F. H. Lutz, *The Manifold Page*, `spherical_3manifolds.txt`, `spherical_3manifolds_hom.txt`, and `spherical_3manifolds_f_vec.txt`, entry `RP^3`.
3. Published finite-complex censuses identifying the unique six-vertex closed triangulation with Euler characteristic \(1\) as \(\mathbb{RP}^2\).
