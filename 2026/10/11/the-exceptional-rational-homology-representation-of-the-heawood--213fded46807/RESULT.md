# The exceptional rational homology representation of the Heawood independence complex

## Finding
Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane, and put \(K=\operatorname{Ind}(H)\). The canonical incidence-preserving action of \(G=\operatorname{GL}_3(\mathbb F_2)\) on the points and lines induces an action on \(K\). Its reduced rational homology is zero outside dimension three, and its nonzero representation has complexification
\[
\widetilde H_3(K;\mathbb Q)\otimes_{\mathbb Q}\mathbb C
\cong_{\mathbb C[G]} V_3\oplus\overline{V}_3,
\]
where \(V_3\) and \(\overline V_3\) denote the Galois-conjugate, inequivalent, three-dimensional complex irreducibles of \(G\cong\operatorname{PSL}_2(7)\). In particular the six-dimensional rational homology representation is irreducible over \(\mathbb Q\). Its character has values \((6,-2,0,2,-1,-1)\) on the conjugacy classes of orders \((1,2,3,4,7,7)\), respectively.

The representation is not the reduced seven-point permutation representation, whose involution trace is \(2\), rather than \(-2\).

## Assumptions and scope
The Fano points are the seven nonzero vectors \(p\in\mathbb F_2^3\). The Fano lines are the seven nonzero linear covectors \(a\in(\mathbb F_2^3)^*\), with \(p\) incident to \(a\) precisely when \(a(p)=0\). Thus \(H\) has fourteen vertices and twenty-one edges. A face of \(K\) is any set of vertices containing no incident point-line pair. The empty face is included in the augmented chain complex. The group \(G\) acts on points by \(p\mapsto gp\) and on line covectors by \(a\mapsto a\circ g^{-1}\); this preserves incidence and all simplicial boundary operators. All homology representations below have rational coefficients unless otherwise stated.

## Proof
**Rational homology concentration.** Exhaustively enumerate the \(2^{14}\) vertex subsets against the twenty-one incidence edges. The independent-set numbers at cardinalities \(0,1,\ldots,7\) are
\[
(1,14,70,154,147,56,14,2).
\]
For the full signed simplicial boundary, exact elimination modulo \(2\) gives consecutive ranks \((13,57,97,44,12,2)\) in chain degrees \(1,2,3,4,5,6\), respectively. Including the rank-one augmentation in degree zero, the reduced mod-two Betti vector is supported only in dimension three, with dimension six. Over the integers, a rational boundary rank is at least its mod-two rank, so each reduced rational Betti number is at most the corresponding mod-two Betti number. The reduced Euler characteristic computed directly from the face numbers is \(-6\). Hence the only nonzero reduced rational homology is \(\widetilde H_3(K;\mathbb Q)\cong\mathbb Q^6\).

**An exact equivariant trace identity.** Fix \(g\in G\). An independent set \(A\) is \(g\)-invariant if it is a union of cycles of the induced permutation on the fourteen vertices; write \(c_g(A)\) for the number of those cycles lying in \(A\), with \(c_g(\varnothing)=0\). On the oriented chain attached to a nonempty invariant face \(A\), the permutation sign is \((-1)^{|A|-c_g(A)}\). Its signed contribution to the reduced Lefschetz number is therefore \((-1)^{c_g(A)+1}\), also valid for the augmented empty face. Since homology is concentrated in degree three, the Hopf trace identity yields
\[
\operatorname{tr}\bigl(g\mid\widetilde H_3(K;\mathbb Q)\bigr)
=\sum_{\substack{A\subseteq V(H)\\A\text{ independent},\ gA=A}}
(-1)^{c_g(A)}.
\]
Define the orbit polynomial \(P_g(t)=\sum_{A\text{ independent},\,gA=A}t^{c_g(A)}\). Consequently the homology trace is \(P_g(-1)\).

**Finite group computation.** Enumerate all invertible \(3\)-by-\(3\) binary matrices by their linearly independent column triples. There are \(7\cdot6\cdot4=168\). For each matrix, apply the point permutation and its contragredient line permutation, partition the fourteen vertices into cycles, and enumerate the invariant independent unions. All elements of the same order give the following coefficient vectors for \(P_g(t)\), listed in increasing powers of \(t\):

| Element order | Number of elements | Coefficients of \(P_g(t)\) | Trace \(P_g(-1)\) |
| --- | ---: | --- | ---: |
| \(1\) | 1 | \((1,14,70,154,147,56,14,2)\) | \(6\) |
| \(2\) | 21 | \((1,10,32,38,15,2)\) | \(-2\) |
| \(3\) | 56 | \((1,6,9,4)\) | \(0\) |
| \(4\) | 42 | \((1,6,9,2)\) | \(2\) |
| \(7\) | 48 | \((1,2)\) | \(-1\) |

The order-seven elements split into two conjugacy classes of twenty-four elements each; the displayed trace is the same on both. Every polynomial and group-element count is verified in the finite certificate `verify.py`. A second implementation, `crosscheck.py`, constructs binary matrices from rows and computes the same character from signed invariant oriented simplices, without using the orbit-polynomial signs.

**Representation identification.** The character \(\chi\) therefore has values \((6,-2,0,2,-1,-1)\) in class-order convention \((1,2,3,4,7,7)\). The usual character inner products give
\[
\langle\chi,1_G\rangle
=\frac{6-42+84-48}{168}=0,
\qquad
\langle\chi,\chi\rangle
=\frac{36+84+168+48}{168}=2.
\]
The irreducible complex degrees of \(\operatorname{GL}_3(\mathbb F_2)\) are \(1,3,3,6,7,8\). A degree-six character with zero trivial multiplicity and norm squared two must be the sum of the *two distinct* degree-three characters. Their table values are Galois conjugate, with the seventh-order traces \(\sigma=(-1+\sqrt{-7})/2\) and \(\overline\sigma=(-1-\sqrt{-7})/2\); their sum is \(-1\) on both seventh-order classes. Thus \(\chi=\chi_{V_3}+\chi_{\overline V_3}\). Since these two characters are exchanged by rational Galois conjugation, no proper nonzero rational subrepresentation exists: the rational module is irreducible. The familiar reduced seven-point permutation representation is instead the other degree-six complex irreducible, with involution character \(2\), establishing the asserted distinction.

## Verification
The self-contained, standard-library program `verify.py` checks the Fano incidence normalization, all \(2^{14}\) candidate independent sets, the complete mod-two boundary ranks, all \(168\) group transformations, the orbit-polynomial coefficient table, and both character inner products. The independently coded `crosscheck.py` repeats the graph and group constructions using row matrices rather than column images, computes signed simplicial boundary ranks over \(\mathbb F_3\), and calculates the Lefschetz character by direct oriented-chain traces. Both were executed from their package paths and returned `VERIFY_OK` and `CROSSCHECK_OK`, respectively. Commands: `python3 verify.py` and `python3 crosscheck.py`.

## Relationship to prior work
Barmak's general star-cluster and triangle-free independence-complex methods provide homotopical context, but do not determine the specific equivariant homology module. Nilakantan and Shukla classify the homotopy type of a cyclic-neighborhood regular-bipartite family; their fourteen-vertex cubic member contains a four-cycle, whereas Heawood has girth six, so the family theorem does not specialize here. Tsukuda's incidence-complex/Alexander-duality constructions give a broader non-equivariant structural relationship but no trace values for the Fano symmetry action. An accessible published exact Heawood calculation proves \(\operatorname{Ind}(H)\simeq\bigvee^6S^3\), fixing the six-dimensional homology rank without identifying its \(\operatorname{GL}_3(\mathbb F_2)\)-representation. The present claim distinguishes two natural and inequivalent six-dimensional rational representations by their complete characters, information that does not follow from the nonequivariant homotopy equivalence. The classical character table is used to *identify* the computed module, not as evidence that this topological computation appeared previously.

## Limitations
The result is for the Fano-plane graph and its incidence-preserving \(168\)-element subgroup of automorphisms; it makes no assertion for higher-order projective planes or the full automorphism group including point-line dualities. It does not determine an integral equivariant lattice or equivariant homotopy type. The finite calculation is exhaustive for this particular complex, not a proof of a family formula. An equivalent character calculation could exist in differently indexed literature; the literature comparison is limited to the identified sources.

## References
- J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first posted 2010-07-02), https://arxiv.org/abs/1007.0418.
- N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789v1 (first posted 2017-09-14), https://arxiv.org/abs/1709.04789.
- S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), DOI:10.55016/ojs/cdm.v12i1.62277.
- *The Heawood independence complex is a wedge of six three-spheres*, publicly available mathematical calculation, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-heawood-independence-complex-is-bigvee-6-s-3--dbd95019d1e2/RESULT.md.
- Standard character table of \(\operatorname{PSL}_2(7)\cong\operatorname{GL}_3(\mathbb F_2)\), https://en.wikipedia.org/wiki/PSL(2%2C7).
