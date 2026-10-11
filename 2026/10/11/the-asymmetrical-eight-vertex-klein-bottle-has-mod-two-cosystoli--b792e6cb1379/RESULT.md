# The asymmetrical eight-vertex Klein bottle has mod-two cosystolic profile \(5,6,6\)
## Finding
Let \(K\) be Cervone's unique 1133 eight-vertex triangulation of the Klein bottle. For each nonzero class \(\xi\in H^1(K;\mathbf F_2)\), let \(w(\xi)\) be the minimum number of edges in the support of a simplicial one-cocycle representing \(\xi\), and let \(m(\xi)\) be the number of representatives attaining that minimum. Then \(H^1(K;\mathbf F_2)\cong\mathbf F_2^2\), and its three nonzero classes have, in an intrinsic ordering by the cup square \(q(\xi)=\langle\xi\smile\xi,[K]\rangle\), exactly the triples \((w,m,q)=(5,1,1),(6,5,0),(6,3,1)\). The unique weight-five representative is supported on the five edges \(BC,BG,CE,DE,DG\). Every minimizing support for all three nonzero classes is a single simple cycle in the dual graph of the triangulation.

Equivalently, the complete nonzero mod-two one-cosystolic profile of \(K\) is one class of minimum support \(5\), one class of minimum support \(6\) with five minimizers, and one class of minimum support \(6\) with three minimizers. The unique square-zero nonzero class is the \((6,5,0)\) class. Thus the absolute mod-two one-cosystole is \(5\), attained by exactly one cocycle.

## Assumptions and scope
The complex \(K\) is the 1133 triangulation in Cervone's classification, on vertices \(A,B,C,D,E,F,G,H\), with triangular facets
\[
ABD,\ ABH,\ ACG,\ ACH,\ ADF,\ AEF,\ AEG,\ BCE,
\]
\[
BCG,\ BDG,\ BEF,\ BFH,\ CDE,\ CDF,\ CFH,\ DEG.
\]
It has face vector \((8,24,16)\). Cervone's classification identifies this as the unique 1133 eight-vertex Klein-bottle triangulation and records that it has no nontrivial simplicial symmetry. The statement here concerns this fixed triangulation, coefficients in \(\mathbf F_2\), and support counted by primal edges.

A simplicial one-cochain is represented by a subset of the \(24\) edges. It is a cocycle when every triangular face contains an even number of selected edges. For a cohomology class \(\xi\), the quantity \(w(\xi)\) is the smallest support cardinality among all cocycles in that class, and \(m(\xi)\) counts the cocycles at that cardinality. The cup-square bit is
\[
q(\xi)=\langle\xi\smile\xi,[K]\rangle\in\mathbf F_2,
\]
using the mod-two fundamental class. No statement is made about integral cosystoles, other triangulations of the Klein bottle, or subdivisions of \(K\).

## Proof
Order the \(24\) edges and impose the \(16\) face equations saying that a one-cochain has even edge sum on each triangle. Exact row reduction over \(\mathbf F_2\) gives rank \(15\), hence
\[
\dim Z^1(K;\mathbf F_2)=24-15=9.
\]
The vertex-coboundary space has rank \(7\), because the one-skeleton is connected on eight vertices. Therefore
\[
\dim H^1(K;\mathbf F_2)=9-7=2.
\]
There are exactly \(2^9=512\) cocycles, partitioned into four cohomology classes of \(2^7=128\) representatives each.

The finite classification is then exhaustive. For every cocycle, compute its support size and reduce it modulo the vertex-coboundary space. On an ordered triangle \([a,b,c]\), evaluate the Alexander--Whitney square by the term \(z(ab)z(bc)\), and sum this over the \(16\) triangles. The value is constant on each cohomology class. Among the three nonzero classes, exactly one has square zero. The resulting minimum data are
\[
(w,m,q)=(5,1,1),\qquad (6,5,0),\qquad (6,3,1).
\]
The unique weight-five representative is the cocycle
\[
\{BC,BG,CE,DE,DG\}.
\]
The verifier checks directly that it satisfies all \(16\) face equations and is not a coboundary.

There is also a geometric interpretation of every minimizing support. In the dual graph, a selected primal edge becomes the dual edge joining the two incident triangles. The cocycle condition forces every dual vertex to have even selected degree; because a triangle has only three sides, every active dual vertex has degree \(2\). Thus any cocycle support is a disjoint union of dual cycles. Direct connectivity checks on every minimizer show that each of the nine minimizing cocycles above consists of one component, hence one simple dual cycle, of length \(5\) or \(6\) as stated.

## Verification
Run `python3 verify.py` in the package directory. The checker reconstructs the \(16\) facets and \(24\) edges, verifies that every edge lies in exactly two triangles and that the surface is connected with Euler characteristic \(0\), and independently exhausts all degree-preserving vertex permutations to confirm that the simplicial automorphism group is trivial.

It then performs exact bit-linear algebra over \(\mathbf F_2\), generates all \(512\) cocycles and all \(128\) coboundaries, partitions the cocycles into the four cohomology classes, computes the cup-square bit for every representative, and exhaustively determines the support-weight enumerator of each nonzero class. Finally it checks that every minimizer is a single simple cycle in the dual graph.

The packaged replay output begins:

`VERIFY_OK f=8,24,16 H1_F2_dim=2 aut_order=1 nonzero_cosystolic_spectrum=5x1,6x5,6x3 unique_weight5_support=BC,BG,CE,DE,DG cup_square_zero_class=6x5 all_minimizers_single_dual_cycles=yes`

The full class weight enumerators are recorded in `verification_output.txt`.

## Relationship to prior work
Cervone's exact-object paper classifies all vertex-minimal Klein-bottle triangulations and identifies the 1133 complex as unique and asymmetric. Its full text was inspected at the 1133 classification and at the discussion of mod-two first homology. It does not state a cocycle-support minimum, a classwise cosystolic profile, or a dual shortest-cycle census; targeted full-text searches found no occurrences of “cohomology,” “cocycle,” or “systole.”

Lutz's survey places eight vertices at the minimum for the Klein bottle and supplies the topology classification context under primary MSC \(57Q15\), but does not compute this support metric. Focused publication-index searches under the exact 1133 label, Klein-bottle and cocycle aliases, dual-systole language, and cohomology-code-distance language found no statement covering the three classwise minima or their multiplicities.

A previously known primal-cycle homology census for this same triangulation does not imply the present result: primal one-cycle length and cochain support are different metrics. On a closed surface, Poincaré duality sends a cohomology class to a homology class in the dual cellulation; it does not turn a shortest primal cycle into a shortest dual cycle, nor determine the number of minimizing cocycles or the cup-square partition.

## Limitations
The result is an exact finite theorem for one fixed triangulation and mod-two coefficients. Exhaustive enumeration is the proof mechanism for the classwise weight minima and multiplicities; the checker enumerates the complete finite cocycle space, not a sample. The cup-square computation uses the displayed vertex ordering, but its class value is independently checked to be constant over every representative, so the final partition is cohomological rather than representative-dependent.

The literature comparison cannot exclude an obscure or unindexed historical computation phrased as shortest cycles in the dual cubic map or as a coding-theoretic distance. No such covering statement was located in the exact-object paper, the checked survey, or the focused semantic searches.

## References
1. D. P. Cervone, *Vertex-Minimal Simplicial Immersions of the Klein Bottle in Three Space*, Pacific Journal of Mathematics 158 (1993), 1--20, DOI 10.1007/BF01265307. An archived public copy used for source-date verification is the 2004-03-09 snapshot identified by `webarchive:20040309191227:vmkb.pdf`.
2. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv:math/0506372v1 (2005).
