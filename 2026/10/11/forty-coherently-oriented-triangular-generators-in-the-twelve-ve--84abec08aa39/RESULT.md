# Forty coherently oriented triangular generators in the twelve-vertex \(S^3\times S^1\)
## Finding
Let \(K={}^4_{\times}12^{di}_2\) be the centrally symmetric twelve-vertex triangulation `product_4_12_di_2` of
\[
S^3\times S^1.
\]
Its face vector is
\[
(12,60,120,120,48),
\]
and its six missing edges are
\[
\{1,7\},\{2,8\},\{3,9\},\{4,10\},\{5,11\},\{6,12\}.
\]

Exactly \(40\) three-vertex cliques are nonfacial triangles. Orient every edge increasingly and orient every three-cycle by its increasing vertex order. Then all forty nonfacial triangular cycles represent the same positive primitive generator
\[
g\in H_1(K;\mathbb Z)\cong\mathbb Z.
\]
Thus the integral combinatorial homology \(1\)-systole has length \(3\), and it has exactly \(40\) simple minimizers.

The full simplicial automorphism group has order \(24\). Its action on these forty minimum carriers has three orbits of sizes
\[
4,\qquad 12,\qquad 24,
\]
with representatives
\[
\{1,5,9\},\qquad \{1,3,8\},\qquad \{1,4,8\}.
\]
Every vertex lies in exactly ten of the forty carriers.

## Assumptions and scope
Cycle length is the number of edges. A nonfacial triangle is a three-vertex clique in the one-skeleton whose triangular face is absent. The increasing orientation of a triple \(a<b<c\) is the one-cycle
\[
[b,c]-[a,c]+[a,b].
\]

The sign assertion is labeling-dependent: reversing the chosen generator of \(H_1\) changes every sign simultaneously. The basis-free content is that all forty increasing triangular cycles are homologous and primitive. The result is specific to the displayed centrally symmetric twelve-vertex triangulation.

## Proof
The published facet presentation reconstructs \(48\) four-simplices and the face vector
\[
(12,60,120,120,48).
\]
The one-skeleton is the complete graph on twelve vertices with the six antipodal pairs deleted. It has \(160\) three-vertex cliques. Exactly \(120\) are triangular faces, leaving \(40\) nonfacial triangular cycles.

Over \(\mathbf F_2\), the graph cycle space has dimension
\[
60-12+1=49,
\]
while the span of the triangular face boundaries has rank \(48\). Hence
\[
\dim_{\mathbf F_2}H_1(K;\mathbf F_2)=1.
\]
Exact reduction shows that all forty nonfacial triangular cycles are nonzero in this quotient.

For the integral statement, define an integer one-cochain \(w\) on increasingly oriented edges. Give coefficient \(1\) to
\[
38,48,49,58,59,5\,10,68,69,6\,10,6\,11,78,79,7\,10,7\,11,7\,12
\]
and coefficient \(0\) to every other edge. Direct evaluation on all \(120\) triangular faces gives zero, so \(w\) is a cocycle. Direct evaluation on every one of the forty increasing nonfacial triangles gives exactly \(1\).

The published topology identifies \(H_1(K;\mathbb Z)\cong\mathbb Z\). Since the homomorphism induced by \(w\) takes value \(1\) on a cycle, it is surjective and therefore represents a primitive generator of \(H^1(K;\mathbb Z)\). A class of \(H_1(K;\mathbb Z)\cong\mathbb Z\) on which that generator evaluates to \(1\) is the positive primitive generator. Therefore all forty triangular cycles represent the same \(g\). No simple cycle has fewer than three edges, so these are precisely the integral homology \(1\)-systoles.

For symmetry, every simplicial automorphism preserves the six missing edges. The verifier therefore exhausts all
\[
2^6\cdot6!=46080
\]
permutations that permute the six antipodal pairs and optionally swap their endpoints. Exactly \(24\) preserve the facet set. Their action on the forty nonfacial triangles gives the three stated orbits. Direct incidence counting gives ten carriers through each vertex.

## Verification
The standalone `verify.py` contains the complete forty-eight-facet presentation and uses only the Python standard library. It reconstructs every face, checks the six missing edges, computes the mod-two boundary rank, evaluates the explicit integral cocycle on all facial and nonfacial triangles, exhausts every automorphism candidate allowed by the antipodal matching, and recomputes the carrier orbits and vertex incidences.

Its exact successful output is:

`VERIFY_OK f=12,60,120,120,48 H1_F2_dim=1 empty3=40 all_empty3_nonzero=yes integral_pairings=+1:40 aut=24 carrier_orbits=4,12,24 reps=159|138|148 carrier_vertex_degree=10`

The integral conclusion uses the published identification of the complex with \(S^3\times S^1\); all carrier and cocycle assertions are checked directly from the facet list.

## Relationship to prior work
Lutz's centrally symmetric sphere-product census gives this exact twelve-vertex \(S^3\times S^1\), its face vector, the dihedral orbit presentation, and the ambient crosspolytope structure. Those data and the existence of the vertex-transitive symmetry are prior work.

The inspected source does not classify nonfacial triangular cycles by integral homology. Focused searches using the exact dataset name, the sphere-product notation, empty-triangle terminology, primitive-generator language, and shortest-homology-loop formulations did not locate a statement that all forty increasing triangles are the same primitive generator, nor the \(4,12,24\) carrier-orbit decomposition. The nearest indexed torsion and finite-model results concern different spaces and do not imply this rank-one integral statement.

## Limitations
The positive sign uses the displayed vertex labeling and the explicit cocycle. The result does not classify longer representatives of the generator or compare the other centrally symmetric sphere-product triangulations. An unindexed historical computation could contain the same forty-cycle census.

## References
1. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Centrally Symmetric Spheres and Products of Spheres*, arXiv:`math/0404465v1`, submitted 2004-04-26; Theorem 12 and Table 4.
2. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24, primary MSC 57Q15.
3. F. H. Lutz, *The Manifold Page: Centrally symmetric products of spheres*, datasets `product_4_12_di_2` and `products_of_spheres_type`.
