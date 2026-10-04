# Six vertices are minimal for a fixed-simplex triangulation of the two-sphere
## Finding
A finite simplicial complex has the fixed simplex property if every simplicial endomorphism fixes some nonempty simplex setwise. Among finite simplicial triangulations of the two-sphere, the minimum vertex number for this property is six.

Up to combinatorial isomorphism, exactly one six-vertex triangulation has the fixed simplex property. On vertices \(0,1,2,3,4,5\), it has facets
\[
\{0,1,4\},\ \{0,1,5\},\ \{0,2,4\},\ \{0,2,5\},\ \{1,4,5\},\ \{2,3,4\},\ \{2,3,5\},\ \{3,4,5\}.
\]
It is obtained by stellar subdivision of one triangular face of the five-vertex triangular bipyramid. The other six-vertex sphere triangulation, the octahedral boundary, does not have the fixed simplex property. Neither does the unique four-vertex or five-vertex sphere triangulation.

## Assumptions and scope
All complexes are finite abstract simplicial complexes, all maps are simplicial maps on vertices, and a simplex is required to be nonempty. A triangulation of the two-sphere means a finite simplicial complex whose realization is homeomorphic to \(\mathbb S^2\). Degenerate simplicial maps, which may identify vertices of a simplex, are allowed.

The statement is a minimum-vertex and minimum-order uniqueness result only. It does not classify sphere triangulations on seven or more vertices and does not assert an analogous minimum in higher dimensions.

## Proof
First reduce the fixed simplex question to automorphisms. Let \(K\) be any finite triangulation of \(\mathbb S^2\), and let \(f:K\to K\) be a simplicial endomorphism with no invariant simplex. If \(|f|\) fixed a point \(x\), let \(\sigma\) be the unique simplex whose relative interior contains \(x\). Since \(x=|f|(x)\) lies in \(|f(\sigma)|\), the carrier property gives \(\sigma\subseteq f(\sigma)\). But a simplicial map cannot increase dimension, so \(f(\sigma)=\sigma\), a contradiction. Hence \(|f|\) is fixed-point-free.

The Lefschetz number of a self-map of \(\mathbb S^2\) is \(1+\deg(f)\). A fixed-point-free map therefore has Lefschetz number zero, so \(\deg(f)=-1\). In particular the degree is nonzero.

A simplicial self-map of a finite closed triangulated surface with nonzero degree is a simplicial automorphism. Indeed, choose an interior point of each target triangle. Nonzero degree forces a preimage in the interior of at least one source triangle that maps nondegenerately onto that target triangle. The source and target contain the same number of triangles, and a source triangle maps nondegenerately onto at most one target triangle, so every source triangle maps nondegenerately and the map permutes the triangles. Every target vertex belongs to a target triangle and therefore has a preimage vertex in its unique preimage triangle. Thus the vertex map is surjective, hence bijective because domain and codomain have the same finite vertex set. Therefore a fixed-simplex-free endomorphism of a sphere triangulation must be an automorphism.

It remains to inspect the sphere triangulations on at most six vertices. For a triangulated two-sphere with \(v\) vertices, Euler's relation and the fact that every edge belongs to two triangles give \(e=3v-6\). Every vertex has degree at least three.

For \(v=4\), there is only the tetrahedral boundary. The automorphism \((0\ 1\ 2\ 3)\) has no invariant nonempty simplex.

For \(v=5\), the one-skeleton has nine edges, so it is \(K_5\) minus one edge, the triangular bipyramid. With the missing edge \(\{0,2\}\), the permutation \((0\ 2)(1\ 3\ 4)\) is a simplicial automorphism. Its only nonempty invariant vertex subsets are unions of its two cycles; \(\{0,2\}\) is not an edge and \(\{1,3,4\}\) is not a face, so it fixes no simplex.

For \(v=6\), the degree sum is twenty-four. If every vertex has degree at least four, all six degrees are four. The complement of the one-skeleton is then a perfect matching, so the triangulation is the octahedral boundary. A six-cycle of the vertices preserving the three opposite pairs is a simplicial automorphism with no invariant nonempty simplex.

Otherwise a degree-three vertex exists. Its link is a three-cycle. Deleting that vertex and filling its link by one triangle produces a five-vertex sphere triangulation, hence the triangular bipyramid. The triangular bipyramid is face-transitive, so inserting a new vertex into any one face gives, up to isomorphism, a unique second six-vertex sphere triangulation. This is the displayed complex \(K\).

The vertex degrees of \(K\) are \(3,3,4,4,5,5\), in the paired classes \(\{1,3\}\), \(\{0,2\}\), and \(\{4,5\}\). Adjacency forces any automorphism that swaps \(0\) and \(2\) also to swap \(1\) and \(3\), while \(4\) and \(5\) may be swapped independently. Thus
\[
\operatorname{Aut}(K)=\{1,(4\ 5),(0\ 2)(1\ 3),(0\ 2)(1\ 3)(4\ 5)\}.
\]
The identity fixes vertices; \((4\ 5)\) fixes vertices \(0,1,2,3\); \((0\ 2)(1\ 3)\) fixes vertices \(4,5\); and \((0\ 2)(1\ 3)(4\ 5)\) fixes the edge \(\{4,5\}\) setwise. Hence every automorphism fixes a simplex. By the reduction above, every simplicial endomorphism fixes a simplex, so \(K\) has the fixed simplex property.

The four- and five-vertex failures and the octahedral six-vertex failure prove minimality and uniqueness at six vertices.

## Verification
The standalone script `artifacts/verify.py` checks the four explicit sphere complexes, verifies that the displayed six-vertex complex is the claimed stellar subdivision, checks the three fixed-simplex-free automorphisms, and exhaustively enumerates all \(6^6=46{,}656\) vertex maps of the displayed six-vertex complex. Exactly \(6{,}658\) are simplicial endomorphisms and none is fixed-simplex-free. It also enumerates all six-vertex permutations and finds exactly four automorphisms, the four listed in the proof.

A successful replay prints:
`VERIFY_OK target_endomorphisms=6658 target_bad=0 automorphisms=4 sphere_types_le6=1,1,2 explicit_failures=3`

The exhaustive enumeration is an independent finite check of the six-vertex target. The quantified minimum theorem is established by the structural proof above rather than inferred from finite experimentation.

## Relationship to prior work
Barmak defined the fixed simplex property in this form and observed that although spheres do not have the ordinary fixed point property, \(\mathbb S^n\) has triangulations with the fixed simplex property for every \(n\ge 2\). His Proposition 3 obtains such triangulations after suitable subdivisions of pseudomanifolds. That existence theorem does not give the minimum vertex number for \(\mathbb S^2\) or identify the unique minimum triangulation.

Idzik and Zapart proved the fixed simplex property for retractable complexes; that criterion does not cover a triangulation of \(\mathbb S^2\), which is noncontractible. Earlier fixed-point work of Baclawski and Björner includes a finite poset model of \(\mathbb S^2\) with the order-theoretic fixed point property, a different object and property from the minimum simplicial triangulation problem here. A 1996 survey of finite-poset fixed-point algorithms also discusses sphere-induced examples but does not state this six-vertex fixed-simplex cutoff.

## Limitations
The result concerns only the first possible vertex count for triangulations of \(\mathbb S^2\). It does not enumerate all larger triangulations having the fixed simplex property, optimize other size measures, or determine higher-dimensional minimum vertex counts. The literature comparison did not locate the exact six-vertex cutoff, but absence from searched sources is not a proof that the statement has never appeared in an unindexed catalog, note, or exercise.

## References
1. J. A. Barmak, “The fixed point property in every weak homotopy type,” arXiv:1307.1722v1, first public 2013-07-05. Primary MSC 55M20.
2. A. Idzik and A. Zapart, “Fixed Simplex Property for Retractable Complexes,” Fixed Point Theory and Applications 2010, Article ID 303640, DOI:10.1155/2010/303640.
3. K. Baclawski and A. Björner, “Fixed points in partially ordered sets,” Advances in Mathematics 31 (1979), 263–287, DOI:10.1016/0001-8708(79)90045-8.
4. B. S. W. Schröder, “Algorithms for the Fixed Point Property,” survey dated 1996-07-29.
