# Forty shortest integral sphere carriers in the Clebsch neighborhood complex

## Finding
Let \(F=\operatorname{Cay}(\mathbb F_2^4,D)\), where \(D=\{1,2,4,8,15\}\) acts by bitwise XOR; this is the five-regular Clebsch graph, or folded five-cube. Let \(K=\mathcal N(F)\) be the **open** Lovász neighborhood complex: a nonempty vertex set is a simplex precisely when its vertices have a common graph neighbor.

Exactly \(40\) four-vertex subsets \(W\) induce a tetrahedral two-sphere \(K[W]\cong\partial\Delta^3\). Each of their oriented fundamental classes is nonzero and **primitive** in \(H_2(K;\mathbb Z)\), and no set of fewer than four vertices supports a nonzero ambient second-homology class. Furthermore, the \(40\) classes generate the entire integral group
\[
H_2(K;\mathbb Z)\cong\mathbb Z^{31}.
\]
An explicitly identified subfamily of \(31\) is an integral basis, so their \(40\)-generator relation lattice is free of rank \(9\).

The \(40\) supporting sets are exactly the affine four-point planes
\[
 W_{t,J}=t+\{a,b,c,a+b+c\},\qquad J=\{a,b,c\}\in\binom{D}{3},\quad t\in\mathbb F_2^4,
\]
where arithmetic is XOR and repeated translations of the same set are identified. The affine subgroup \(\mathbb F_2^4\rtimes S_5\) is transitive on them. If \(P\) is the rank-\(40\) signed permutation lattice of their oriented sphere boundaries, this supplies the natural equivariant exact sequence
\[
0\longrightarrow R\longrightarrow P\longrightarrow H_2(K;\mathbb Z)\longrightarrow0,
\qquad R\cong\mathbb Z^9\text{ as an abelian group}.
\]
No decomposition of \(R\) as a group representation is asserted.

## Assumptions and scope
All groups and homology are integral unless a coefficient field is specified. Vertices are the integers \(0,\ldots,15\), interpreted as four-bit vectors, and their adjacency is XOR with a member of \(D\). The five Cayley directions have the unique nonempty linear dependence involving all five, namely \(1+2+4+8+15=0\) over \(\mathbb F_2\). Faces and their orientations are ordered by increasing vertex labels. A support means the set of vertices used by a simplicial cycle, equivalently an induced subcomplex carrying its ambient class; no minimum number of triangles or least metric length is asserted. The complex is not the clique or independence complex of the graph, and the graph is not the ten-regular complementary Clebsch graph.

## Proof
**1. Neighborhood incidence.** The sixteen maximal facets are the distinct five-element sets \(N(v)=v+D\). For distinct graph vertices, their open neighborhoods meet in either zero or two vertices: each difference expressible as a sum of two distinct members of \(D\) has exactly two ordered such expressions, and the ten unordered pair sums are distinct. Consequently every triangle or higher-dimensional face belongs to exactly one maximal facet. The face vector, in dimensions zero through four, is
\[
(f_0,f_1,f_2,f_3,f_4)=(16,80,160,80,16).
\]

**2. Exactly forty candidate minimal carriers.** A nonzero simplicial \(2\)-cycle must involve at least four vertices: the one possible triangle on three vertices has nonzero boundary. On four vertices, a nonzero \(2\)-cycle exists precisely when all four triples are faces; it is their alternating sum, the boundary of the formal oriented tetrahedron. This cycle is null in the induced complex if the tetrahedron is a face, and is the fundamental cycle of \(\partial\Delta^3\) otherwise.

Choose any triple \(x+a,x+b,x+c\) of vertices in one neighborhood \(N(x)\), with pairwise distinct \(a,b,c\in D\). If a fourth vertex makes all four triples faces but not a tetrahedral face, then the unique alternative common neighbors of each of the original three pairs are \(x+a+b\), \(x+a+c\), and \(x+b+c\). Their unique common neighbor is \(x+a+b+c\), by the sole five-direction linear relation. Thus the fourth vertex is forced. Conversely, the four vertices \(\{x+a,x+b,x+c,x+a+b+c\}\) have every triple in a neighborhood but have no common neighbor all together. The ten choices of three direction vectors yield ten distinct two-dimensional direction subspaces, each with four affine translates. Therefore there are exactly \(10\cdot4=40\) induced tetrahedral spheres, precisely the sets displayed above. The verifier also checks this classification by enumeration of all \(\binom{16}{4}\) four-sets.

**3. Exact integral basis, not just field ranks.** Write \(\partial_k\) for the signed simplicial boundary on \(k\)-simplices. The cellular ranks are \(\operatorname{rank}C_1=80\), \(\operatorname{rank}C_2=160\), \(\operatorname{rank}C_3=80\), \(\operatorname{rank}C_4=16\). Over \(\mathbb F_2,\mathbb F_3\), and \(\mathbb F_{101}\), exact elimination gives
\[
(\operatorname{rank}\partial_1,\operatorname{rank}\partial_2,\operatorname{rank}\partial_3,\operatorname{rank}\partial_4)=(15,65,64,16).
\]
These are also the ranks over \(\mathbb Q\): the lower bounds follow from the field computations, while \(\partial_1\partial_2=0\) bounds \(\operatorname{rank}\partial_2\le80-15=65\), and \(\partial_3\partial_4=0\) bounds \(\operatorname{rank}\partial_3\le80-16=64\). Thus \(Z_2=\ker\partial_2\) is a saturated rank-\(95\) sublattice of the rank-\(160\) group \(C_2\).

The files `certificate.json` and `verify.py` give a completely specified \(95\times95\) **integer** minor of the \(160\times95\) chain matrix consisting of \(64\) columns of \(\partial_3\) followed by \(31\) alternating tetrahedral-sphere cycles. Rows are triangles in lexicographic order; all selections are explicit zero-based indices in `certificate.json`. The exact determinant is
\[
\boxed{\det(M)=-1}.
\]
The program obtains this by exactly \(95\) unit pivots using only integer row/column swaps and elementary row operations. Since all ninety-five columns are integral \(2\)-cycles, are independent, and generate a primitive rank-\(95\) sublattice of \(C_2\), they form an integral basis of \(Z_2\): any element of \(Z_2\) is rationally in their span, and a primitive sublattice contains every integral point of its rational span. The first \(64\) chosen boundary columns similarly form a primitive rank-\(64\) sublattice of \(Z_2\), hence equal \(\operatorname{im}\partial_3\), which has that rank. Therefore the remaining \(31\) selected sphere cycles form an integral basis of \(H_2(K;\mathbb Z)\), with no hidden index or torsion. The \(40\)-generator map is surjective and has a free rank-nine kernel.

**4. Primitivity and symmetry.** Every permutation of the five elements of \(D\) extends uniquely to a linear automorphism of \(\mathbb F_2^4\), because their sole relation is their full sum. Together with all sixteen translations these give the faithful subgroup \(\mathbb F_2^4\rtimes S_5\). It acts transitively on the ten direction triples and on the four cosets for each triple, hence on all \(40\) sphere supports. The integral basis from Step 3 contains a primitive sphere class. Graph automorphisms act by invertible integral homology transformations, so transitivity makes **every** one of the forty classes primitive and nonzero. On oriented boundaries, the affine group acts by the sign of the induced permutation of the four sorted support vertices, establishing the stated equivariant surjection and its rank-nine kernel.

## Verification
Run `python3 verify.py certificate.json` in the directory containing the two files (Python standard library only). The verifier reconstructs all graph neighborhoods and faces, all signed boundary matrices, the complete forty-member affine-plane list, and the three finite-field rank profiles. It checks both consecutive boundary products vanish, reproduces the specified \(64\) boundary and \(31\) sphere columns and ninety-five selected rows, and reduces the selected integer minor using ninety-five actual unit pivots to obtain determinant \(-1\). It also constructs all \(16\cdot120=1920\) affine maps from translations and direction permutations and verifies transitivity on the forty four-vertex supports. No external dataset, saved computation, or numerical floating-point output is needed.

## Relationship to prior work
Previously published calculations establish \(\mathcal N(FQ_5)\simeq\bigvee^{31}S^2\) and a uniform two-sphere-wedge homotopy formula for odd folded cubes. A separate published calculation gives the translation-group rational character, and a full-automorphism rational character statement determines a representation without specifying shortest integral generators. Those statements determine homology ranks or group characters, **but not** the forty induced sphere supports, the primitive geometric images, or the explicit unimodular thirty-one-generator lattice. The general fundamental-group and degree-at-most-four neighborhood-complex results likewise do not imply this support classification. The added information is specifically an integral, geometric, minimum-support presentation, not a different computation of the already-known wedge type.

## Limitations
The theorem concerns the one five-regular folded cube and the ordinary open-neighborhood complex; no uniform minimum-support theorem for all folded cubes is claimed. The equivariant exact sequence does not identify the integral representation carried by the rank-nine relation lattice or split the sequence. Primitivity refers to integral \(H_2\), not simple-homotopy, systolic mass, or fundamental-group data. Possible equivalent statements in unindexed literature remain a bibliographic risk; independent scientific validation has not been performed.

## References
1. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077 (first public 2005-12-04), especially the neighborhood-complex definition and homological context: https://arxiv.org/abs/math/0512077.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first public 2012-10-10): https://arxiv.org/abs/1210.2803.
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (first public 2018-02-13): https://arxiv.org/abs/1802.04526.
4. *The neighborhood complexes of odd folded hypercubes are wedges of two-spheres*, published result and full proof: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-neighborhood-complexes-of-odd-folded-hypercubes-are-wedges-o--438357602cff.
5. *The five-regular Clebsch neighborhood complex is a wedge of thirty-one two-spheres*, published proof: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a.
6. *Translation-character decomposition for odd folded-cube neighborhood complexes*, published full proof: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-translation-character-decomposition-for-odd-folded-cube-neighbor--4651ea532edd.
