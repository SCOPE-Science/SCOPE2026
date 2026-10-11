# Every nonzero first-homology class has a triangular systole in the eighteen-vertex Weeks manifold
## Finding
Let \(K\) be the eighteen-vertex simplicial triangulation `or_0.94270736` of the Weeks manifold. Its face vector is
\[
f(K)=(18,139,242,121).
\]
An independent integral chain calculation gives
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/5)^2.
\]

The one-skeleton contains exactly \(619\) three-vertex cliques. Exactly \(242\) are triangular faces, leaving \(377\) nonfacial triangular cycles.

Every one of those \(377\) nonfacial triangles is integrally homologically nonzero. Therefore the simple integral homology \(1\)-systole has edge length \(3\) and exactly \(377\) minimizers.

More strongly, every nonzero class of
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/5)^2
\]
has a triangular systolic representative. Up to reversing orientation there are twelve possible nonzero class pairs \(\{x,-x\}\), and all twelve occur. Their carrier multiplicities, as an unordered multiset, are
\[
\{11,15,15,17,19,30,33,39,45,49,52,52\}.
\]

There are six cyclic subgroups of order \(5\), equivalently six projective directions in the two-dimensional \(\mathbf F_5\)-homology. Every direction occurs among the triangular systoles, with total carrier multiplicities
\[
\{50,50,60,64,71,82\}.
\]

## Assumptions and scope
The labelled complex is the public `or_0.94270736` entry associated with the Weeks manifold. Vertices are \(1,\ldots,18\), and all \(121\) tetrahedra are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero. A triangular carrier is a three-edge simple cycle that is not itself a two-simplex.

The class-pair and projective-direction multiplicity multisets are basis-independent. The verifier chooses one explicit basis of the mod-five quotient only to compute them.

## Proof
Contract the deterministic spanning tree used in `verify.py`. The graph-cycle lattice then has rank
\[
139-18+1=122.
\]
Each of the \(242\) triangular faces supplies an integral relation among these cycle generators.

The verifier selects \(122\) facial relations that are linearly independent modulo \(2\). Their exact Bareiss determinant has absolute value
\[
25.
\]
Hence the finite integral quotient has order dividing \(25\). On the other hand, the complete facial relation matrix has rank \(120\) modulo \(5\). Therefore at least two Smith invariant factors are divisible by \(5\), so the quotient order is divisible by \(25\). It follows that the Smith data are
\[
1^{120},5,5,
\]
and hence
\[
H_1(K;\mathbb Z)\cong(\mathbb Z/5)^2.
\]

The same mod-five row reduction yields two explicit cocycles annihilating all \(242\) facial relations. Since the integral group has already been proved to be \((\mathbb Z/5)^2\), these cocycles give exact coordinates on every integral homology class.

The verifier then exhausts every three-vertex clique in the one-skeleton. There are \(619\) in total, \(242\) of which are facial, so \(377\) are nonfacial. Every nonfacial triangle has nonzero coordinates. Because a simple cycle in a simplicial graph has at least three edges, this proves that the simple integral homology \(1\)-systole is \(3\) and that all \(377\) nonfacial triangles are minimizers.

Grouping those exact coordinates first by \(\{x,-x\}\) gives all twelve nonzero unoriented class pairs and the stated twelve multiplicities. Grouping further by scalar multiples in \(\mathbf F_5^\times\) gives all six one-dimensional homology directions and the stated six direction totals. Reversing a triangular cycle changes \(x\) to \(-x\), so occurrence of all twelve sign-pairs is equivalent to occurrence of all \(24\) nonzero oriented classes.

## Verification
The standalone `verify.py` uses only the Python standard library. It reconstructs all faces from the \(121\) tetrahedra, checks that every triangle lies in two tetrahedra, builds the contracted graph-cycle presentation, proves the integral quotient using an exact maximal minor together with mod-five rank, constructs the two exact mod-five quotient coordinates, and exhausts every three-vertex clique.

Exact successful output:

`VERIFY_OK f=18,139,242,121 H1_Z=Z5^2 graph_triangles=619 facial3=242 empty3=377 all_empty3_nonzero=yes simple_integral_1_systole=3 minimizers=377 all_nonzero_H1_classes_hit=yes nonzero_classes=24 unoriented_class_pairs=12 pair_profile=11,15,15,17,19,30,33,39,45,49,52,52 projective_directions=6 direction_profile=50,50,60,64,71,82 maximal_minor_absdet=25 rank_mod5=120`

No sampling, numerical linear algebra, or external homology package is used.

## Relationship to prior work
Lutz, Sulanke, and Swartz identify `or_0.94270736` as the Weeks manifold, record
\[
H_1\cong(\mathbb Z/5)^2
\]
and the face vector \((18,139,242,121)\), and explain that these proper simplicial triangulations were obtained from Hodgson--Weeks census triangulations by subdivision followed by bistellar simplification. The public manifold table supplies the complete \(121\)-tetrahedron presentation.

Those sources determine the ambient manifold, homology, and face vector, but they do not state which nonfacial triangular cycles are essential, whether every nonzero homology class has a length-three representative, or the twelve-pair and six-direction multiplicity spectra.

General combinatorial-systolic work studies shortest nontrivial edge loops in triangulations, but does not compute this exact Weeks-manifold triangulation.

## Limitations
The theorem concerns simple edge cycles in this fixed labelled eighteen-vertex triangulation. It does not compare the nine-tetrahedron pseudo-simplicial Weeks triangulations, other proper simplicial triangulations of the same manifold, hyperbolic geodesic length, or stable norms.

The class coordinates used internally are basis-dependent, while the assertions that all nonzero classes occur and the two multiplicity multisets are intrinsic.

An unindexed historical computation could contain part or all of the same triangular homology census.

## References
1. F. H. Lutz, T. Sulanke, and E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144`, first submitted 2008-05-08; Section 6 and Table 11.
2. F. H. Lutz, *The Manifold Page*, `hyperbolic_3manifolds.txt`, `hyperbolic_3manifolds_hom.txt`, and `hyperbolic_3manifolds_f_vec.txt`, entry `or_0.94270736`.
3. R. Kowalick, J.-F. Lafont, and B. Minemyer, *Combinatorial systolic inequalities*, arXiv:`1506.07121`.
