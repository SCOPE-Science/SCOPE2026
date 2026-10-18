# Complete affine homology character and trivial three-torsion action of the Paley-17 neighborhood complex

## Finding
Let \(P_{17}\) be the Paley graph on \(\mathbb F_{17}\), and let \(X=\mathcal N(P_{17})\) be its ordinary **open** Lovász neighborhood complex. Its full automorphism group is \(G=\mathbb F_{17}\rtimes\langle2\rangle\cong C_{17}\rtimes C_8\), of order \(136\). Let \(W=\mathbb Q(\zeta_{17})\) with the \(G\)-action
\[
(b,a)\cdot x=\zeta_{17}^{\,b}\,\sigma_a(x),\qquad\sigma_a(\zeta_{17})=\zeta_{17}^{\,a},
\]
where \(a\in\langle2\rangle\leq\mathbb F_{17}^{\times}\), \(b\in\mathbb F_{17}\), and \(\zeta_{17}\) is a primitive seventeenth root of unity. Let \(E\) be the three-dimensional augmentation representation of \(\mathbb Q[C_4]\), inflated along \(G\twoheadrightarrow C_8\twoheadrightarrow C_4\). Then
\[
\boxed{\widetilde H_3(X;\mathbb Q)\cong W^{\oplus2}\oplus E\quad\text{as }\mathbb Q[G]\text{-modules}.}
\]
Moreover, the full automorphism group acts **trivially** on the integral torsion group
\[
\boxed{\widetilde H_2(X;\mathbb Z)\cong\mathbb Z/3.}
\]
The rational character of third homology is explicitly
\[
\chi_3(b,a)=\begin{cases}
35 & a=1,\ b=0,\\
1 & a=1,\ b\ne0,\\
3 & a=-1,\\
-1 & a\notin\{1,-1\}.
\end{cases}
\]
In particular, \(\dim\widetilde H_3(X;\mathbb Q)^G=0\), whereas its translation-fixed subspace has dimension \(3\). The rational representation splits into three distinct rational irreducible isomorphism types, of dimensions \(16\), \(1\), and \(2\), with multiplicities \(2\), \(1\), and \(1\), respectively.

## Assumptions and scope
The vertex set is \(\mathbb Z/17\mathbb Z\). Put \(Q=\{1,2,4,8,9,13,15,16\}\), the nonzero quadratic residues modulo \(17\). Two different vertices are adjacent if their difference lies in \(Q\). The faces of \(X\) are precisely all nonempty subsets of the seventeen open neighbor sets \(v+Q\), together with the empty face of the augmented chain complex. The definition excludes the center \(v\) of each neighborhood; it is not a closed-neighborhood, clique, or independence complex. Orient every face by increasing vertex order.

The group acts through the affine permutations \((b,a):v\mapsto av+b\) with \(a\in Q\). Its size and completeness as the graph automorphism group follow from the classical Paley graph automorphism theorem (see References); the proof below verifies every one of its \(136\) elements as a chain action.

## Proof
**1. Integral homology and the finite chain model.** The face vector in dimensions zero through seven is
\[
(17,136,612,1122,952,476,136,17),
\]
so there are exactly \(3468\) nonempty faces. On the face poset, take vertex stages \(v=0,\ldots,16\), visiting still-unmatched faces in increasing cardinality and then increasing bit-mask order, and match \(\sigma\) to \(\sigma\cup\{v\}\) whenever both are still unmatched. This gives \(1711\) pairs. Reverse the associated matched codimension-one arrows, directing all other arrows down. A topological sort visits all \(3468\) faces, proving that the matching is acyclic. The critical cells consist of one vertex, five triangles, and forty tetrahedra, with no critical cells in other dimensions.

The signed integral Morse boundary \(B:\mathbb Z^{40}\to\mathbb Z^{5}\) is calculated by recursively projecting each triangle to the five critical triangles across matched triangle–tetrahedron pairs, using signed simplicial incidences. Its \(5\times40\) matrix has \(99\) nonzero entries. The determinant of its submatrix with all five rows and zero-indexed columns \((0,1,3,4,8)\) equals \(-3\); the determinant on rows \((0,1,2,3)\) and columns \((0,1,4,8)\) equals \(-1\). Its rank modulo \(3\) is \(4\) and its rank modulo \(2\) is \(5\). The first fact forces every maximal minor to be divisible by \(3\); the first displayed minor gives maximal determinantal divisor exactly \(3\); and the unit four-minor forces all lower determinantal divisors to be \(1\). Therefore its nonzero Smith factors are exactly \((1,1,1,1,3)\). The integral Morse complex proves
\[
\widetilde H_2(X;\mathbb Z)=\mathbb Z/3,\qquad
\widetilde H_3(X;\mathbb Z)=\mathbb Z^{35},
\]
with no other reduced integral homology. This finite calculation independently reconstructs the known nonequivariant result and is used here only to justify the new equivariant assertions.

**2. Complete rational Lefschetz character.** For an affine automorphism \(g\), enumerate the faces that it preserves setwise. Their orientation signs are the parities of the permutations induced on their ascending vertex lists. The reduced Lefschetz number is
\[
\widetilde L(g)=\sum_{d=0}^{7}(-1)^d\operatorname{tr}(g\mid C_d(X;\mathbb Q))-1.
\]
The preceding integral calculation shows that rational reduced homology occurs only in degree \(3\); consequently \(\chi_3(g)=-\widetilde L(g)\). Exhaustive exact evaluation for each of the \(136\) affine permutations gives the four-case character in the Finding: its values at the identity, the other \(16\) translations, the \(17\) maps with multiplier \(-1\), and the remaining \(102\) maps are respectively \(35,1,3,-1\).

**3. Rational module identification.** The rational cyclotomic module \(W\) has character \(16\) at the identity, \(-1\) at every nonidentity translation, and \(0\) on elements with nonidentity multiplier: a nonidentity multiplier is conjugate by a translation to a nontrivial field automorphism, whose trace in the root-of-unity basis is zero. The augmented \(C_4\)-regular module \(E\), inflated to \(G\), has character \(3\) when the multiplier exponent of \(2\) is divisible by \(4\), and \(-1\) otherwise. Thus \(2\chi_W+\chi_E\) is exactly the four-case Lefschetz character. Complete reducibility and uniqueness of rational characters for finite groups give the boxed isomorphism.

Restriction of \(W\) to the normal \(C_{17}\) is the irreducible \(16\)-dimensional cyclotomic representation, so \(W\) itself is irreducible over \(\mathbb Q\). The augmentation \(E\) splits into the one-dimensional order-two character and the two-dimensional rational order-four character. Both are irreducible, and neither is isomorphic to \(W\). Their characters contain no trivial constituent. The formula also shows \(\dim\widetilde H_3(X;\mathbb Q)^{C_{17}}=3\) and \(\widetilde H_3(X;\mathbb Q)^G=0\).

**4. Integral torsion symmetry.** Over \(\mathbb F_3\), the simplicial boundary \(\partial_2\) has rank \(120\), leaving a \(492\)-dimensional kernel. Choose its canonical free-triangle-coordinate cycle basis by sparse column elimination in increasing face order. The images of the \(1122\) tetrahedron boundaries, projected to those free coordinates, have rank \(491\). One resulting nonboundary mod-three cycle has ascending-oriented triangular bit masks \(35,37,38,67,69,70\) with coefficients \(2,1,2,1,2,1\), respectively. An explicitly constructed linear functional on the \(492\) coordinates annihilates this boundary image, has \(184\) nonzero entries, and pairs with that cycle to give \(2\in\mathbb F_3\). The resulting one-dimensional \(H_2(X;\mathbb F_3)\) is checked directly under all \(136\) affine maps: every induced scalar equals \(1\). In particular the generators \(v\mapsto v+1\) and \(v\mapsto 2v\) both act as \(+1\). Because \(H_1(X;\mathbb Z)=0\), the universal coefficient theorem identifies \(H_2(X;\mathbb Z)\otimes\mathbb F_3\) equivariantly with \(H_2(X;\mathbb F_3)\); and because the former is \(\mathbb Z/3\), the same trivial action holds integrally.

## Verification
Run `python3 verify_paley17.py` with Python 3 and its standard library only. The program constructs all faces from the quadratic-residue definition; verifies the acyclicity of the exact integer Morse pairing; computes the two determinant certificates and modular ranks; independently reconstructs the mod-three cycle and cocycle that detect integral torsion; and checks the scalar on that torsion class together with the rational character formula for every affine map. It terminates with `All exact finite checks passed.` if every assertion holds. The computational enumeration is finite and exhaustive for this specified graph; it does not establish a theorem for other Paley orders.

## Relationship to prior work
The nonequivariant homotopy calculation \(X\simeq M(\mathbb Z/3,2)\vee\bigvee^{35}S^3\) is previously available in *Three-torsion in the neighborhood complex of the Paley graph of order seventeen* (the same-object study in References). It provides the integral groups and a finite Morse matrix, but no action or character of the affine automorphism group. The present statement is a refinement about group modules, not a new claim for the nonequivariant homotopy type. The presence of \(35\) rational generators and one order-three class alone imposes neither their particular character nor the triviality of the torsion action.

Jones describes the Paley graph's affine symmetry and its regular embeddings; that analysis concerns maps on surfaces rather than the chain homology of this neighborhood complex. Matsushita's general neighborhood-complex theorem describes fundamental groups, not the rational third-homology module or its torsion symmetry. Results about Paley-17 **clique** complexes or directed-flag complexes of Paley **tournaments** concern different simplicial constructions and do not imply the character computed here.

## Limitations
This result is specific to the order-seventeen ordinary open-neighborhood complex, its indicated complete affine automorphism group, its rational third homology, and its order-three integral second homology. It does **not** classify the integral \(G\)-lattice \(H_3(X;\mathbb Z)\), all equivariant homotopy types, higher-order Paley complexes, or an infinite family. Exact finite computations certify the displayed data only; a mathematically equivalent formula could exist in unindexed literature. No priority claim beyond the stated searches is made.

## References
1. G. A. Jones, *Characterisations and Galois conjugacy of generalised Paley maps*, arXiv:1006.0514 (first submitted 2010-06-02), https://arxiv.org/abs/1006.0514 .
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first submitted 2012-10-10), https://arxiv.org/abs/1210.2803 .
3. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, public mathematical finding (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 .
4. *Paley graph P17*, DistanceRegular.org, https://www.math.mun.ca/distanceregular/graphs/paley17.html .
