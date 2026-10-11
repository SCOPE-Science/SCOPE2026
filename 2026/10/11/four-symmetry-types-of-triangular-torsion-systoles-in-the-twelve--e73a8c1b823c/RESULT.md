# Four symmetry types of triangular torsion systoles in the twelve-vertex \(24\)-cell quotient \(\mathbb{RP}^3\)
## Finding
Let \(K\) be the Köhler--Lutz twelve-vertex vertex-transitive triangulation
\[
{}^{3}12^{13}_{2}
\]
of \(\mathbb{RP}^3\). The published classification identifies it with the antipodal quotient of the boundary of the regular \(24\)-cell and gives
\[
f(K)=(12,60,96,48).
\]

Define the simple integral homology \(1\)-systole to be the least number of edges in an unoriented simple cycle representing a nonzero integral first-homology class. Then the systole of \(K\) is \(3\).

Exactly \(64\) simple three-edge cycles attain this minimum. They are precisely the three-vertex cliques that are not triangular faces, and every one represents the unique nonzero element of
\[
H_1(K;\mathbb Z)\cong\mathbb Z/2.
\]

The full simplicial automorphism group has order \(24\). On the \(64\) systoles it has exactly four orbits, of sizes
\[
4,\ 12,\ 24,\ 24.
\]
Representatives may be chosen as
\[
\{1,5,9\},\qquad
\{1,2,12\},\qquad
\{1,2,4\},\qquad
\{1,2,6\}.
\]
The exceptional four-element orbit is
\[
\{1,5,9\},\ \{2,6,10\},\ \{3,7,11\},\ \{4,8,12\},
\]
so it is a parallel class: its four shortest torsion loops are pairwise vertex-disjoint and partition the twelve vertices.

## Assumptions and scope
The exact labelled complex is the facet set published as `manifold_3_12_13_2`. Its six missing graph edges are
\[
\{1,7\},\{2,8\},\{3,9\},\{4,10\},\{5,11\},\{6,12\}.
\]
Thus the complement of the one-skeleton is a perfect matching.

A simple three-edge cycle is the boundary of a three-vertex clique. Facial triangles are simplicial boundaries and hence homologically trivial. The result concerns the combinatorial unit-edge metric and this particular vertex-transitive triangulation; it is not a claim about metric geodesics in a Riemannian realization.

## Proof
The complete \(48\)-facet list reconstructs \(60\) edges and \(96\) triangular faces. Because the graph is the complete graph on twelve vertices with the six antipodal matching edges removed, it has exactly \(160\) three-vertex cliques. Subtracting the \(96\) facial triangles leaves exactly
\[
160-96=64
\]
nonfacial triangular cycles.

Over \(\mathbf F_2\), the graph cycle space has dimension
\[
60-12+1=49.
\]
Exact row reduction shows that the \(96\) facial triangle boundaries span a subspace of rank \(48\). Consequently
\[
\dim_{\mathbf F_2}H_1(K;\mathbf F_2)=1.
\]
The verifier reduces every one of the \(64\) nonfacial triangular boundaries modulo the facial-boundary space and finds every one nonzero.

The published topology is \(K\cong\mathbb{RP}^3\), hence
\[
H_1(K;\mathbb Z)\cong\mathbb Z/2.
\]
Since \(H_0(K;\mathbb Z)\) is torsion-free, the universal coefficient theorem identifies the reduction of the unique nonzero integral first-homology class with the unique nonzero mod-two class. Therefore every one of the \(64\) nonfacial triangular cycles represents the integral torsion generator. A simple cycle cannot use fewer than three edges, so these are exactly the simple integral homology systoles.

For symmetry, any simplicial automorphism preserves the one-skeleton and therefore its complement, the six-edge perfect matching. Hence every automorphism permutes the six antipodal pairs and may swap vertices within each pair. The verifier exhausts all
\[
6!\,2^6=46{,}080
\]
such permutations and retains exactly \(24\) preserving the full facet set. This independently recovers the published full automorphism-group order.

Acting with these \(24\) automorphisms on all \(64\) systoles gives exactly four orbits with sizes \(4,12,24,24\) and the displayed representatives. The size-\(4\) orbit is checked pairwise disjoint. The four carrier orbits are individually vertex-regular, with each vertex lying respectively in \(1,3,6,6\) carriers; hence every vertex belongs to \(16\) shortest torsion loops in total.

## Verification
The standalone `verify.py` contains the complete \(48\)-facet presentation and uses only the Python standard library. It reconstructs all faces, identifies the antipodal missing-edge matching, computes mod-two first homology by exact bit-vector elimination, checks all \(160\) three-vertex cliques, and verifies all \(64\) nonfacial triangles are nonzero.

For the group calculation it exhausts every pair-preserving permutation allowed by the complement graph, tests facet preservation, and computes the complete carrier-orbit decomposition.

Exact successful output:

`VERIFY_OK f=12,60,96,48 missing_edges=6 H1_F2_dim=1 cliques3=160 facial3=96 essential3=64 aut=24 carrier_orbits=4,12,24,24 reps=159|1212|124|126 orbit_vertex_degrees=1,3,6,6 small_orbit_parallel=yes total_vertex_degree=16`

Every finite set used in the claim is exhausted. The integral torsion conclusion uses the published identification with \(\mathbb{RP}^3\) together with the universal coefficient theorem; it is not inferred from mod-two data alone.

## Relationship to prior work
Köhler and Lutz classify the vertex-transitive triangulation, identify its topology as \(\mathbb{RP}^3\), record the face vector, the order-\(24\) full simplicial automorphism group, and the description as the antipodal quotient of the boundary of the \(24\)-cell. Those facts are treated as prior.

The new statement concerns the complete shortest nonzero integral-homology loop layer and the action of the known symmetry group on that layer. The inspected classification tables and exact facet data do not state that all \(64\) nonfacial triangular cycles are torsion generators, nor do they give the \(4,12,24,24\) carrier-orbit decomposition or its four-loop parallel class.

## Limitations
The theorem concerns one canonical vertex-transitive twelve-vertex triangulation of \(\mathbb{RP}^3\), not all triangulations of that manifold. It classifies shortest simple homology representatives only; it does not classify longer representatives, free-homotopy classes beyond what follows from \(\pi_1(\mathbb{RP}^3)\cong\mathbb Z/2\), or geometric lengths in a metric realization.

An older dissertation contains the vertex-transitive census at year-level bibliographic resolution. To avoid inventing a calendar day, the machine-readable public date uses the earliest day-resolved exact-object source inspected, the 2005 arXiv classification.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24, primary MSC 57Q15.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices and Vertex-Transitive Group Actions*, dissertation, TU Berlin, 1999.
3. F. H. Lutz, Manifold Page, exact facet data for `manifold_3_12_13_2`.
