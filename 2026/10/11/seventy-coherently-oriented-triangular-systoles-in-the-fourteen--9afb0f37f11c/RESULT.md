# Seventy coherently oriented triangular systoles in the fourteen-vertex \(S^4\times S^1\)
## Finding
Let \(K={}^{5}14^{3}_{8}\) be the Kühnel--Lassmann fourteen-vertex triangulation of
\[
S^4\times S^1,
\]
listed in the public data as `manifold_5_14_3_8`. Direct reconstruction gives
\[
f(K)=(14,84,210,280,210,70)
\]
and
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]

The one-skeleton contains exactly \(280\) three-vertex cliques. Exactly \(210\) are triangular faces, so there are \(70\) nonfacial triangular cycles. Every one of those \(70\) cycles represents a primitive generator of integral first homology. Hence the simple integral homology \(1\)-systole has edge length \(3\) and exactly \(70\) minimizers.

The vertex labeling is cyclic modulo \(14\). Under the natural shift, the \(70\) systoles split into five orbits of size \(14\), represented by
\[
\{1,3,9\},\quad
\{1,4,9\},\quad
\{1,4,10\},\quad
\{1,5,9\},\quad
\{1,5,10\}.
\]
The shift acts trivially on \(H_1(K;\mathbb Z)\). Orienting each orbit by transporting the increasing orientation of its representative makes every systole represent the same chosen generator \(g\).

Adding the natural reflection gives four carrier orbits of sizes
\[
14,\quad28,\quad14,\quad14,
\]
represented by
\[
\{1,3,9\},\quad
\{1,4,9\},\quad
\{1,5,9\},\quad
\{1,5,10\}.
\]
The reflection sends \(g\) to \(-g\).

## Assumptions and scope
The labelled complex is the `manifold_5_14_3_8` entry of the public five-manifold data table. Vertices are \(1,\ldots,14\), and all \(70\) five-simplices are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero.

The cyclic shift is
\[
i\longmapsto i+1\pmod {14},
\]
written on the labels \(1,\ldots,14\). The reflection used in the verifier is
\[
i\longmapsto 2-i\pmod {14}.
\]
Both permutations preserve the complete facet set.

## Proof
The one-skeleton has \(84\) edges. Contracting a spanning tree leaves a graph-cycle lattice of rank
\[
84-14+1=71.
\]
Each of the \(210\) triangular faces gives one integral relation.

The verifier performs only unimodular integer row and column operations on the resulting \(210\times71\) relation matrix. It reduces the matrix to an identity block of size \(70\) and one zero column. Consequently
\[
H_1(K;\mathbb Z)\cong\mathbb Z.
\]

An explicit primitive integral cocycle \(y\) is stored sparsely in `verify.py`. It annihilates every facial relation. The verifier evaluates \(y\) on every graph triangle. There are \(280\) three-vertex cliques, \(210\) of which are faces. For each of the remaining \(70\), oriented by increasing labels, the evaluation is exactly \(1\). Since \(y\) is primitive and the quotient is infinite cyclic, every nonfacial triangle represents the same primitive generator in that orientation.

A simple cycle in a simplicial graph has at least three edges. Since nonzero three-edge cycles exist, the simple integral homology systole is \(3\), and the exhaustive three-clique census proves that there are exactly \(70\) minimizers.

Finally, direct permutation checks verify that the cyclic shift and reflection preserve all \(70\) facets. Exhaustion of their action gives five cyclic carrier orbits of size \(14\), and four dihedral orbits of sizes \(14,28,14,14\). Evaluation of the transported reference cycle shows that the shift acts by \(+1\) and the reflection by \(-1\) on the generator.

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds the full facet table, reconstructs every face, performs the integral relation reduction, checks the primitive cocycle against all \(210\) facial relations, exhausts all graph triangles, and verifies the cyclic and dihedral symmetry actions.

Exact successful output:

`VERIFY_OK f=14,84,210,280,210,70 H1_Z=Z graph_triangles=280 facial3=210 empty3=70 all_empty3_primitive_same_oriented_generator=yes simple_integral_1_systole=3 minimizers=70 C14_orbits=14x5 D14_orbits=14,28,14,14 shift_action_H1=+1 reflection_action_H1=-1 missing_graph_edges=7_antipodal smith=1^70,0`

The conclusion about primitivity is integral, not inferred from finite-field homology.

## Relationship to prior work
Kühnel and Lassmann introduced the relevant family of permuted-difference-cycle sphere-bundle triangulations in 1996. Köhler and Lutz later list the fourteen-vertex \(S^4\times S^1\) example explicitly as \({}^{5}14^{3}_{8}\), with face vector
\[
(14,84,210,280,210,70)
\]
and dihedral symmetry. The public manifold tables give the complete labelled facet presentation and record first Betti number \(1\).

Those sources establish the manifold, its symmetry, and its simplicial data. The inspected accessible material does not state that all \(70\) nonfacial triangles are primitive integral systoles, that their cyclic orientations are homologically coherent, or the exact five-orbit/four-orbit carrier decomposition above. Focused literature searches using the original model name, sphere-bundle notation, shortest-homology terminology, nonfacial-triangle terminology, and the numerical fingerprint \(70\) did not locate a covering statement.

## Limitations
The theorem concerns simple simplicial cycles in this fixed fourteen-vertex triangulation. It does not compare other triangulations of \(S^4\times S^1\), geometric metric lengths, or stable norms.

The chosen positive generator is fixed by the natural cyclic action; reversing it reverses all orientation statements simultaneously.

The full text of the original 1996 construction paper was not retrievable during this check after open-access attempts, so an explicit unpublished or unindexed cycle census in that source remains a residual originality risk. The later full exact-object census and the complete public facet table were inspected directly.

## References
1. W. Kühnel and G. Lassmann, *Permuted difference cycles and triangulated sphere bundles*, Discrete Mathematics 162 (1996), 215--227, DOI `10.1016/0012-365X(95)00287-7`.
2. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24; the five-manifold table.
3. F. H. Lutz, *The Manifold Page*, `5_manifolds.txt`, `5_manifolds_hom.txt`, and `5_manifolds_type.txt`, entry `manifold_5_14_3_8`.
