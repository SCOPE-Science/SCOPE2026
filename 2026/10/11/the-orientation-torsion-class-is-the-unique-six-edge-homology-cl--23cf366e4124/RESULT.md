# The orientation-torsion class is the unique six-edge homology class in a nine-vertex genus-five surface
## Finding
Let \(K\) be the nine-vertex complex `manifold_2_9_4_1` with triangular facets
\[
124,125,138,139,149,156,167,178,237,239,246,259,
268,278,346,347,356,358,457,458,489,579,679,689.
\]
The published manifold tables identify \(K\) as a vertex-transitive triangulation of the closed nonorientable surface of genus \(5\), with
\[
H_1(K;\mathbb Z)\cong \mathbb Z^4\oplus\mathbb Z/2.
\]

For nonzero \(\alpha\in H_1(K;\mathbf F_2)\), define \(\ell(\alpha)\) to be the least number of edges in a simple cycle representing \(\alpha\). The complete nonzero mod-two spectrum is
\[
\ell=3^{\times24},\qquad
4^{\times3},\qquad
5^{\times3},\qquad
6^{\times1}.
\]
Thus all \(31\) nonzero classes already have simple representatives on at most six edges.

The shortest-representative multiplicities refine this spectrum. Among the \(24\) classes with \(\ell=3\), exactly \(3,9,9,3\) classes have respectively \(1,2,3,4\) shortest cycles. Each of the three length-four classes has \(6\) shortest cycles, each of the three length-five classes has \(18\), and the unique length-six class has \(66\).

All \(60\) missing triangles are nonzero homology cycles, and they exhaust the length-three minimizers. The simplicial automorphism group has order \(18\). Its seven orbits on nonzero mod-two homology have the triples
\[
(1,6,66),\ (3,3,1),\ (3,3,4),\ (3,4,6),\ (3,5,18),\ (9,3,2),\ (9,3,3),
\]
where a triple records orbit size, minimum length, and number of shortest representatives per class.

The unique length-six class has a canonical topological meaning. Orient every facet by increasing vertex order and let \(z\) be their integral sum. Since the mod-two sum of all facets is the fundamental cycle of the closed surface, every coefficient of \(\partial z\) is even. The integral cycle
\[
c=\frac12\partial z
\]
has nonzero mod-two homology class, while \(2[c]=0\) integrally. Therefore \([c]\) is the unique order-two element of \(H_1(K;\mathbb Z)\). Its mod-two reduction is precisely the unique class with \(\ell=6\), represented by exactly \(66\) simple six-cycles. It is also the unique singleton orbit under the full simplicial automorphism group.

## Assumptions and scope
All cycles are unoriented simple cycles in the complete one-skeleton of the displayed complex. Cycle length means number of edges. Homology lengths and multiplicities are taken over \(\mathbf F_2\), so reversing a cycle does not change its class. The integral statement concerns only the canonical order-two class detected by the displayed Bockstein construction.

The result is specific to this labelled vertex-transitive genus-five triangulation. It does not claim the same spectrum for the other vertex-minimal nine-vertex triangulation of the same surface.

## Proof
The facet list gives face vector
\[
(9,36,24).
\]
Every one of the \(36\) edges occurs in exactly two triangles, and the one-skeleton is \(K_9\). Over \(\mathbf F_2\), the edge boundary map has rank \(8\) and the triangle boundary map has rank \(23\). Hence
\[
\dim H_1(K;\mathbf F_2)=36-8-23=5,
\]
so there are exactly \(31\) nonzero classes.

The verifier represents edge chains by bit vectors and row-reduces the \(24\) triangular boundary vectors. Reduction modulo that boundary row space gives an exact class identifier for every one-cycle. It then enumerates every unoriented simple cycle of lengths three through six: respectively \(84,378,1512,5040\) cycles. For each nonzero class it records the first length at which the class occurs and the number of representatives at that first length. All \(31\) classes are reached by length six, giving the stated complete spectrum and multiplicities. Among the \(84\) triangles, the \(24\) facial triangles reduce to zero and all \(60\) missing triangles reduce to nonzero classes.

Next, all \(9!\) vertex permutations are tested against the facet set. Exactly \(18\) are simplicial automorphisms. Acting on one shortest representative of each nonzero homology class gives seven class orbits with the displayed profiles.

For the torsion statement, let \(z\) be the sum of the \(24\) increasingly oriented facets. In the oriented edge basis, \(\partial z\) has coefficient profile
\[
(-2)^{\times6},\quad 0^{\times12},\quad 2^{\times18}.
\]
Thus \(c=(\partial z)/2\) is an integral one-cycle and \(2[c]=0\). Its mod-two reduction is checked against the same exact quotient and is nonzero; therefore \([c]\) is not an integral boundary. The published integral homology has exactly one order-two summand, so \([c]\) generates it. The exhaustive simple-cycle census places its mod-two class uniquely at length six with \(66\) minimizers, and the automorphism census gives its orbit size one.

## Verification
The standalone `verify.py` reconstructs the exact facet set and checks all finite claims directly. It uses only Python's standard library and exact bit-vector arithmetic. It verifies the face vector, edge incidences, mod-two boundary rank, every simple cycle through length six, every one of the \(9!\) vertex permutations, every homology orbit, and the integral half-boundary construction.

Its exact successful output is:

`VERIFY_OK f=9,36,24 H1_F2_dim=5 nonzero_classes=31 min_lengths=3:24,4:3,5:3,6:1 triangular_multiplicities=1:3,2:9,3:9,4:3 length4_multiplicity=6x3 length5_multiplicity=18x3 length6_multiplicity=66x1 missing3=60 essential3=60 aut=18 class_orbits=1:6:66|3:3:1|3:3:4|3:4:6|3:5:18|9:3:2|9:3:3 bockstein_length=6 bockstein_minimizers=66 bockstein_fixed=yes`

The computation is exhaustive for the stated finite domains. No claim about cycles longer than six is needed because every nonzero class already occurs by length six.

## Relationship to prior work
Köhler and Lutz enumerate vertex-transitive triangulations with few vertices and provide the archive-era classification context for this complex. The Lutz manifold tables give the exact facets, topology, and integral homology. Sulanke and Lutz later enumerate equivelar triangulations of the nonorientable genus-five surface. Leopold's realization work identifies two vertex-minimal, neighborly nine-vertex triangulations of that surface and proves they do not admit polyhedral immersions in \(\mathbb R^3\).

The inspected classification sources describe the complexes through facets, topology, symmetry/enumeration, and realizability. Targeted searches found no statement giving the complete simple-cycle homology length spectrum, the \(24,3,3,1\) distribution, the shortest-representative multiplicities, or the identification of the unique longest class with the integral Bockstein torsion generator. The closest indexed homology result concerns the six-vertex projective plane, a different surface and complex.

## Limitations
The originality assessment is literature-based rather than a proof of bibliographic uniqueness. An unindexed computation could contain the same finite spectrum. The automorphism calculation is combinatorial and does not identify an abstract presentation of the order-\(18\) group. The result does not compare the second nine-vertex genus-five triangulation.

## References
1. E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:`math/0506520v1`, submitted 2005-06-24.
2. F. H. Lutz, *The Manifold Page*, datasets `manifold_2_9_4_1`, `homology`, and `topology`.
3. T. Sulanke and F. H. Lutz, *Isomorphism-free lexicographic enumeration of triangulated surfaces and 3-manifolds*, arXiv:`math/0610022v1`, submitted 2006-09-30.
4. U. Leopold, *Non-existence of polyhedral immersions of triangulated surfaces in \(\mathbb R^3\)*, arXiv:`1606.04848v1`, submitted 2016-06-15.
