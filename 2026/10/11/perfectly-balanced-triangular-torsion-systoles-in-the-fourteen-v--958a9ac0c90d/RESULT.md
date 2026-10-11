# Perfectly balanced triangular torsion systoles in the fourteen-vertex lens space \(L(5,2)\)
## Finding
Let \(K\) be the fourteen-vertex triangulation of the lens space \(L(5,2)\) with face vector
\[
(14,86,144,72).
\]
Then
\[
H_1(K;\mathbb Z)\cong\mathbb Z/5.
\]

The one-skeleton contains exactly \(308\) three-vertex cliques. Of these, \(144\) are triangular faces and \(164\) are nonfacial triangular cycles. Every one of the \(164\) nonfacial triangles represents a generator of \(H_1(K;\mathbb Z)\). Consequently the simple integral homology \(1\)-systole has edge length \(3\) and exactly \(164\) minimizers.

Up to reversing orientation, there are two nonzero generator classes, \(\{\pm g\}\) and \(\{\pm2g\}\), and the shortest layer is perfectly balanced:
\[
82\text{ triangular systoles represent }\{\pm g\},\qquad
82\text{ represent }\{\pm2g\}.
\]

The full simplicial automorphism group is cyclic of order \(4\). Its induced action on \(H_1(K;\mathbb Z)\cong\mathbb Z/5\) is the full unit group
\[
(\mathbb Z/5)^\times=\{1,2,3,4\},
\]
so the symmetry exchanges the two unoriented generator classes. On the \(164\) triangular systoles the automorphism group has \(39\) orbits of size \(4\) and \(4\) orbits of size \(2\).

## Assumptions and scope
The complex is the labelled seventy-two-tetrahedron \(L(5,2)\) entry on Lutz's Manifold Page. Vertices are \(1,\ldots,14\). A nonfacial triangular cycle is a three-vertex clique in the one-skeleton whose three edges are present but whose triangle is not a two-simplex.

Simple-cycle length is the number of edges. Reversing a triangle orientation negates its class in \(\mathbb Z/5\), so the intrinsic unoriented classes are \(\{\pm g\}\) and \(\{\pm2g\}\).

## Proof
Contract a spanning tree in the connected one-skeleton. Since \(f_1=86\) and there are fourteen vertices, this gives an integral graph-cycle lattice \(\mathbb Z^{73}\). Each of the \(144\) triangular faces contributes one integral relation.

A fixed \(73\times73\) minor of this facial relation matrix has determinant \(5\). Therefore the quotient is finite and its order divides \(5\). On the other hand, the full relation matrix has rank \(72\) over \(\mathbf F_5\), so every maximal minor is divisible by \(5\); hence the quotient order is divisible by \(5\). It follows that
\[
H_1(K;\mathbb Z)\cong\mathbb Z/5.
\]

The same mod-five reduction leaves a one-dimensional cocycle space after the tree contraction. The verifier constructs a nonzero cocycle \(y\) and evaluates it on every nonfacial triangular cycle. With increasing vertex orientation, the values occur with multiplicities
\[
1:41,\qquad 2:44,\qquad 3:38,\qquad 4:41.
\]
There are no zero values. Since every nonzero element of \(\mathbb Z/5\) has order five, all \(164\) nonfacial triangles are integral generators. Pairing inverse classes gives
\[
41+41=82\quad\text{for }\{\pm g\},
\qquad
44+38=82\quad\text{for }\{\pm2g\}.
\]
A simple simplicial cycle has at least three edges, so these triangles are exactly the simple integral homology systoles.

For symmetry, a vertex invariant consisting of one-skeleton degree together with the multiset of degree triples occurring in incident tetrahedra partitions the fourteen vertices into cells of sizes \(2,4,4,4\). Every simplicial automorphism preserves these cells. Exhausting the resulting \(27{,}648\) cell-preserving permutations leaves exactly four automorphisms. Their element orders are \(1,2,4,4\), hence the full group is cyclic of order \(4\). Evaluating the image of a generator cycle shows that these four automorphisms induce multiplication by \(1,2,3,4\) on \(H_1\), respectively. Exhausting their action on the systoles gives \(39\) size-four orbits and \(4\) size-two orbits.

## Verification
The standalone `verify.py` embeds all seventy-two tetrahedra and uses only the Python standard library. It reconstructs the full face vector, the contracted cycle presentation, the determinant-five certificate, the mod-five rank and cocycle, all graph triangles, and the complete simplicial automorphism group.

Its exact successful output is:

`VERIFY_OK f=14,86,144,72 H1_Z=Z/5 det_minor=5 rank_mod5=72 graph_triangles=308 facial3=144 empty3=164 all_empty3_generators=yes unoriented_class_counts=82,82 aut=C4 aut_H1_units=1,2,3,4 carrier_orbits=39x4+4x2`

The integral homology conclusion does not rely only on a finite-field experiment: the determinant-five maximal minor and the rank drop modulo five together force the integral quotient to have order exactly five.

## Relationship to prior work
Lutz--Sulanke--Swartz list \((14,86,144,72)\) as the smallest known face vector for \(L(5,2)\). Lutz's Manifold Page gives the exact seventy-two tetrahedra and records the homology group \(H_1\cong\mathbb Z/5\). Lutz's earlier geometric-three-manifold survey explains the lens-space classification and explicitly notes that \(L(5,1)\) and \(L(5,2)\) have the same homology although they are not homotopy equivalent.

The inspected sources do not state that every nonfacial triangle is a generator, the exact \(82/82\) unoriented class balance, or the full symmetry action on these shortest carriers. Focused semantic searches using exact-object, torsion-systole, empty-triangle, homology-class, and numerical formulations did not locate a covering published statement.

## Limitations
The result is specific to this labelled fourteen-vertex triangulation of \(L(5,2)\). It does not claim the same shortest-carrier spectrum for every triangulation of the lens space.

The oriented multiplicities \(41,44,38,41\) depend on the displayed cocycle and increasing-vertex orientation; the unoriented \(82/82\) balance is intrinsic. An unindexed historical computation could contain the same finite census.

## References
1. F. H. Lutz, T. Sulanke, E. Swartz, *f-Vectors of 3-Manifolds*, arXiv:`0805.1144v1`, submitted 2008-05-08; Table 3.
2. F. H. Lutz, *The Manifold Page: Small triangulations of spherical 3-manifolds*, data files `spherical_3manifolds.txt` and `spherical_3manifolds_hom.txt`, entry `L_5_2`.
3. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Geometric 3-Manifolds*, arXiv:`math/0311116v1`, submitted 2003-11-07; lens-space discussion in Section 4.
