# Primitive one-systoles in the 15-vertex three-torus
## Finding
Let \(K\) be the Kühnel--Lassmann 15-vertex triangulation of the three-torus, labeled by \(\mathbb Z/15\mathbb Z\) so that its tetrahedra are the translates of the six orderings of the step multiset \(\{1,2,4\}\). Then the simple integral homology \(1\)-systole of \(K\) has edge length \(3\). Exactly \(275\) unoriented simple three-edge cycles attain this length: they are precisely the boundaries of the missing triangles, and every one represents a primitive nonzero class of \(H_1(K;\mathbb Z)\cong\mathbb Z^3\). Up to sign these \(275\) cycles represent exactly seven homology classes, six with multiplicity \(45\) and one with multiplicity \(5\). In the deck-lattice basis \(b_1=(15,0,0), b_2=(-2,1,0), b_3=(-4,0,1)\), the seven unoriented classes are \((0,-1,0),(0,-1,1),(0,-2,1),(-1,0,-3),(-1,-2,-2),(-1,-1,-3),(-1,-3,-2)\). The exceptional multiplicity-five class \((-1,0,-3)\) is represented exactly by the five triangles \(\{i,i+5,i+10\}\). Under the full order-\(120\) simplicial automorphism group, the systolic cycles split into five orbits of sizes \(5,30,60,60,120\), while the seven unoriented homology classes split into orbits of sizes \(1,2,4\), with the exceptional class fixed.

## Assumptions and scope
The complex \\(K\\) is the classical Kühnel--Lassmann triangulation of \\(S^1\\times S^1\\times S^1\\) on the vertex set \\(\\mathbb Z/15\\mathbb Z\\). For each \\(i\\in\\mathbb Z/15\\mathbb Z\\) and each permutation \\((p,q,r)\\) of \\((1,2,4)\\), take the tetrahedron
\\[
\\{i,\ i+p,\ i+p+q,\ i+7\\}.
\\]
This gives \\(90\\) tetrahedra and face vector \\((15,105,180,90)\\). The original paper identifies the resulting complex as a neighborly triangulation of the three-torus and realizes its universal cover as a periodic triangulation of Euclidean three-space.

A *simple integral homology one-systole* means a simple edge cycle of least edge length among cycles whose class in \\(H_1(K;\\mathbb Z)\\) is nonzero. Cycles are counted without orientation, so a class and its negative are identified when class multiplicities are reported.

## Proof
Use the standard Freudenthal triangulation of \\(\\mathbb R^3\\) with vertices \\(\\mathbb Z^3\\). Label a lattice vertex \\((a,b,c)\\) by
\\[
\\phi(a,b,c)=a+2b+4c\\pmod {15}.
\\]
The tetrahedra in one unit cube are obtained by ordering the three coordinate increments, so the quotient by \\(L=\\ker\\phi\\) has exactly the tetrahedra above. Hence the universal cover is contractible and
\\[
H_1(K;\\mathbb Z)\\cong L.
\\]
A convenient basis of \\(L\\) is
\\[
b_1=(15,0,0),\qquad b_2=(-2,1,0),\qquad b_3=(-4,0,1).
\\]

For an oriented edge from vertex \\(x\\) to vertex \\(y\\), let \\(d=y-x\\pmod {15}\\). For \\(d=1,\ldots,7\\), choose the lift increments
\\[
1\\mapsto(1,0,0),\ 2\\mapsto(0,1,0),\ 3\\mapsto(1,1,0),\ 4\\mapsto(0,0,1),
\\]
\\[
5\\mapsto(1,0,1),\ 6\\mapsto(0,1,1),\ 7\\mapsto(1,1,1),
\\]
and use the negatives for \\(d=8,\ldots,14\\). The sum around an oriented triangle lies in \\(L\\); for every actual two-simplex of \\(K\\) this sum is zero. Thus a missing triangle has a well-defined deck displacement equal to the integral homology class of its boundary.

The complete graph on \\(15\\) vertices has \\(\\binom{15}{3}=455\\) vertex triples, while \\(K\\) has \\(180\\) triangular faces. Hence there are exactly \\(275\\) missing triangles. Exhausting them with the displacement rule gives exactly seven nonzero classes up to sign. In the basis \\((b_1,b_2,b_3)\\) they are
\\[
(0,-1,0),\ (0,-1,1),\ (0,-2,1),\ (-1,0,-3),\ (-1,-2,-2),\ (-1,-1,-3),\ (-1,-3,-2).
\\]
Their multiplicities are \\(45,45,45,5,45,45,45\\), respectively. Every coordinate triple has greatest common divisor \\(1\\), so every class is primitive. Moreover three of these seven vectors have determinant \\(\\pm1\\), independently confirming that the observed shortest classes generate all of \\(L\\).

Because the one-skeleton is complete, a simple edge cycle cannot have length below \\(3\\). A three-edge cycle is the boundary of a vertex triple; it is null if the triple is a face and, by the exhaustive calculation above, is nonzero if the triple is missing. Therefore the integral one-systole is exactly \\(3\\), and its complete set of minimizers is the set of \\(275\\) missing-triangle boundaries.

Translation by \\(1\\) gives \\(18\\) orbits of size \\(15\\) and one orbit of size \\(5\\). The latter is exactly
\\[
\\{\\{i,i+5,i+10\\}:i=0,1,2,3,4\\}
\\]
and carries the exceptional class \\((-1,0,-3)\\). Generating the full simplicial automorphism group from the published generators yields order \\(120\\). Its action on the \\(275\\) systoles has orbit sizes \\(5,30,60,60,120\\); its induced action on the seven unoriented homology classes has orbit sizes \\(1,2,4\\), with \\((-1,0,-3)\\) fixed.

## Verification
The embedded `artifacts/verify.py` reconstructs the complex from the six difference tetrahedra, rebuilds every face, verifies the face vector, checks that the deck-displacement map vanishes on all \\(180\\) triangular faces, and exhausts all \\(275\\) missing triangles. It verifies nontriviality, primitivity, the seven-class multiplicity spectrum, the exceptional five-cycle family, the translation orbits, and the full order-\\(120\\) automorphism action. It also computes the first two simplicial boundary ranks over \\(\\mathbf F_p\\) for \\(p=2,3,5,7\\), obtaining ranks \\(14\\) and \\(88\\), hence first Betti number \\(3\\) in every checked characteristic.

A successful replay prints:

`VERIFY_OK f=15,105,180,90 H1_rank=3 missing3=275 essential3=275 primitive3=275 classes=7 multiplicities=45x6+5 translation_orbits=15x18+5 full_group=120 systole_orbits=5,30,60,60,120 class_orbits=1,2,4 exceptional=0-5-10`

## Relationship to prior work
Kühnel and Lassmann introduced this exact \\(15\\)-vertex three-torus, printed its \\(90\\) tetrahedra, proved neighborliness, identified the full affine symmetry group of order \\(120\\), and described the periodic Euclidean universal cover. Their later general construction gives the difference description by permuting the steps \\(1,2,4\\) and translating modulo \\(15\\). Köhler and Lutz later tabulated the same vertex-transitive complex and its symmetry generators.

The inspected sources establish the object, topology, covering geometry, face vector, and symmetry, but they do not state the complete shortest integral-homology cycle census, the seven-class multiplicity spectrum, the exceptional five-cycle class, or the five full-group systole orbits. Searches using missing-triangle, systolic, primitive-homology, numerical, affine-symmetry, and equivalent cycle language found no statement implying this classification.

## Limitations
The theorem concerns the fixed Kühnel--Lassmann triangulation and simple edge cycles in its one-skeleton. It is not a metric systolic statement for arbitrary flat metrics on the continuous three-torus, and it does not claim that the seven displayed homology directions are intrinsically preferred after forgetting the triangulation. The originality assessment is based on inspected primary full texts and indexed searches; an unindexed historical computation could still exist.

## References
- W. Kühnel and G. Lassmann, *The rhombidodecahedral tessellation of 3-space and a particular 15-vertex triangulation of the 3-dimensional torus*, Manuscripta Mathematica 49 (1984), 61--77. DOI: 10.1007/BF01174871.
- W. Kühnel and G. Lassmann, *Combinatorial d-tori with a large symmetry group*, Discrete & Computational Geometry 3 (1988), 169--176. DOI: 10.1007/BF02187905.
- E. G. Köhler and F. H. Lutz, *Triangulated Manifolds with Few Vertices: Vertex-Transitive Triangulations I*, arXiv:math/0506520v1 (24 June 2005), MSC 57Q15.
