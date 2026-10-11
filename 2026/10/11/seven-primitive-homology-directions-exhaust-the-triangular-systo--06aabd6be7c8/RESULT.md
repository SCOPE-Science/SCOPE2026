# Seven primitive homology directions exhaust the triangular systoles of Bagchi--Datta's fifteen-vertex tight \(4\)-manifold
## Finding
Let \(K=M^{4}_{15}\) be Bagchi--Datta's fifteen-vertex triangulation of
\[
(S^3\mathbin{\widetilde\times}S^1)^{\#3}.
\]
The published face vector is
\[
f(K)=(15,105,230,240,96),
\]
and an independent integral chain calculation gives
\[
H_1(K;\mathbb Z)\cong\mathbb Z^3.
\]

The one-skeleton is complete, so it has
\[
\binom{15}{3}=455
\]
three-vertex cliques. Exactly \(230\) are triangular faces, leaving \(225\) nonfacial triangular cycles. Every one of these \(225\) cycles represents a nonzero primitive integral homology class. Consequently the simple integral homology \(1\)-systole has edge length \(3\), with exactly \(225\) minimizers.

There is an integral basis \(g_1,g_2,g_3\) of \(H_1(K;\mathbb Z)\) for which, up to reversing orientation, the complete minimum-length spectrum is
\[
\pm g_1:46,\qquad \pm g_2:46,\qquad \pm g_3:46,
\]
\[
\pm(g_1+g_2):18,\qquad \pm(g_1+g_3):18,\qquad \pm(g_2+g_3):18,
\]
and
\[
\pm(g_1+g_2+g_3):33.
\]
No other integral class is represented by a triangular systole.

The published order-three simplicial automorphism cyclically permutes \(g_1,g_2,g_3\). Hence it also cyclically permutes the three singleton directions and the three pair-sum directions, while fixing the triple-sum direction. Reduction modulo \(2\) sends these seven primitive integral sign-classes bijectively onto all seven nonzero classes of
\[
H_1(K;\mathbf F_2)\cong\mathbf F_2^3.
\]

## Assumptions and scope
The labelled complex is the explicit \(96\)-facet complex \(M^{4}_{15}\) printed in the primary source. The vertices are
\[
a_1,\ldots,a_5,b_1,\ldots,b_5,c_1,\ldots,c_5.
\]
All \(96\) four-simplices are embedded verbatim in `verify.py`.

A simple integral homology \(1\)-systole means a simple edge cycle of minimum edge length whose class in \(H_1(K;\mathbb Z)\) is nonzero. Two carrier classes are identified in the displayed spectrum only after reversing orientation, so a listed class \(\pm x\) denotes the pair \(\{x,-x\}\).

The basis is chosen to respect the order-three symmetry. One may take \(g_1,g_2,g_3\) to be represented by the oriented missing triangles
\[
(a_1,a_2,b_4),\qquad(b_1,b_2,c_4),\qquad(c_1,c_2,a_4),
\]
respectively. The published automorphism sends these cycles cyclically in the displayed order.

## Proof
Since the one-skeleton is complete, contracting the star at \(a_1\) leaves an integral graph-cycle lattice of rank
\[
105-15+1=91.
\]
Each of the \(230\) triangular faces gives an integral relation among these generators.

The verifier performs only unimodular integral row and column operations on the resulting \(230\times91\) relation matrix. It reduces the matrix exactly to
\[
\operatorname{diag}(1^{88},0,0,0).
\]
Therefore
\[
H_1(K;\mathbb Z)\cong\mathbb Z^3,
\]
and the tracked column operations give exact integral coordinates for every edge cycle.

There are exactly
\[
455-230=225
\]
nonfacial three-cycles. The verifier evaluates every one in the exact quotient basis. None has zero coordinate, and every coordinate vector has greatest common divisor \(1\), so every nonfacial triangle represents a primitive nonzero class.

After the unimodular basis change adapted to the order-three symmetry, identifying a coordinate vector with its negative gives exactly seven vectors:
\[
(1,0,0),\ (0,1,0),\ (0,0,1),
\]
with multiplicity \(46\) each,
\[
(1,1,0),\ (1,0,1),\ (0,1,1),
\]
with multiplicity \(18\) each, and
\[
(1,1,1)
\]
with multiplicity \(33\). These multiplicities sum to
\[
3\cdot46+3\cdot18+33=225.
\]

The facet set is then checked directly to be invariant under
\[
a_i\mapsto b_i\mapsto c_i\mapsto a_i
\]
for every \(1\le i\le5\). The three explicit carrier cycles above have quotient coordinates \((1,0,0)\), \((0,1,0)\), and \((0,0,1)\), and the automorphism cycles them. This proves the symmetry statement.

Finally, a simple cycle in a simplicial graph has at least three edges. Since nonzero three-edge cycles exist, the simple integral homology \(1\)-systole is exactly \(3\).

## Verification
The standalone `verify.py` uses only the Python standard library. It embeds all \(96\) facets, reconstructs the complete face vector, performs the integral unimodular reduction with tracked quotient coordinates, exhausts all \(455\) vertex triples, verifies primitivity of all \(225\) nonfacial cycles, checks the seven-class multiplicity spectrum, and verifies the order-three simplicial symmetry on the full facet set and on the chosen basis carriers.

Exact successful output:

`VERIFY_OK f=15,105,230,240,96 H1_Z=Z^3 graph_triangles=455 facial3=230 empty3=225 all_empty3_nonzero_primitive=yes simple_integral_1_systole=3 unoriented_classes=7 binary_subset_shell=yes singleton_counts=46x3 pair_counts=18x3 triple_count=33 order3_basis_cycle=yes smith=1^88,0^3`

The integral class spectrum is not inferred from mod-two tightness. The Smith reduction and every coordinate used in the spectrum are integral.

## Relationship to prior work
Bagchi and Datta constructed \(M^{4}_{15}\), proved that it triangulates the connected sum of three twisted \(S^3\)-bundles over \(S^1\), gave the face vector \((15,105,230,240,96)\), printed all \(96\) facets, and identified the order-three automorphism. Their revised paper also records that the triangulation is tight.

Tightness already has an important implication for the present problem: because the complex is two-neighborly, every missing triangle induces a simplicial circle, and mod-two tightness forces its nonzero \(H_1\)-class to survive in the ambient complex. Thus generic nonvanishing of missing triangles is not claimed here as the originality boundary by itself.

The new statement is the exact integral refinement: all \(225\) triangular carriers are primitive, they occupy only seven integral sign-classes, their multiplicities are \(46,46,46,18,18,18,33\), these classes are precisely the nonzero binary subset sums in a symmetry-adapted integral basis, and reduction modulo \(2\) hits every nonzero mod-two class exactly at this minimum cycle length. Focused literature searches under the exact manifold notation, connected-sum description, missing-triangle language, shortest-homology language, symmetry language, and the numerical fingerprints did not locate this spectrum.

## Limitations
The theorem concerns simple edge cycles in this one fixed labelled triangulation. It does not classify longer cycles, alternate triangulations of the same topological manifold, or geometric lengths under an external metric.

The basis \(g_1,g_2,g_3\) is symmetry-adapted but not asserted to be canonical from the topology alone. The invariant content is the seven primitive sign-classes with multiplicity multiset \(46^3,18^3,33\), together with the cyclic symmetry action and the bijection to all nonzero mod-two classes.

An unindexed historical finite computation could contain part or all of the same integral carrier spectrum.

## References
1. B. Bagchi and B. Datta, *On Walkup's class \(\mathcal K(d)\) and a minimal triangulation of \((S^3\mathbin{\widetilde\times}S^1)^{\#3}\)*, arXiv:`0804.2153v1`, submitted 2008-04-14; revised version `0804.2153v3` contains the explicit facet table and final tightness statement.
2. B. Bagchi and B. Datta, *On stellated spheres and a tightness criterion for combinatorial manifolds*, arXiv:`1102.0856v1`; general tightness framework and later placement of the fifteen-vertex example among tight neighborly manifolds.
