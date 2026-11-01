# The closed-neighborhood complex of \(\mathrm{KG}(7,2)\): 260 three-spheres and repeated Specht modules

## Finding
Let \(G=\mathrm{KG}(7,2)\) be the Kneser graph with vertex set \(\binom{[7]}{2}\), two vertices being adjacent precisely when their underlying pairs are disjoint. Let \(X=\mathcal N[G]\) be the **closed-neighborhood complex**: its faces are vertex sets lying in the union of one graph vertex and all vertices adjacent to that vertex. Then the complete integral homotopy type is
\[
\boxed{|X|\simeq\bigvee^{260}S^3.}
\]
The full action of \(S_7\) by relabeling the underlying seven elements gives the following rational homology module, with \(S^\lambda\) denoting the Specht irreducible for the partition \(\lambda\) of seven:
\[
\boxed{\begin{aligned}
\widetilde H_3(X;\mathbb Q)\cong{}&S^{(5,2)}\oplus S^{(5,1,1)}\oplus2S^{(4,2,1)}\\
&\oplus S^{(4,1,1,1)}\oplus S^{(3,3,1)}\oplus S^{(3,2,2)}\\
&\oplus2S^{(3,2,1,1)}\oplus S^{(3,1,1,1,1)}\oplus S^{(2,2,1,1,1)}.
\end{aligned}}
\]
All other reduced integral homology groups vanish. The two Specht types \((4,2,1)\) and \((3,2,1,1)\) each occur **twice**, in contrast to the already-established multiplicity-free rational \(S_6\)-representation for the analogous closed-neighborhood complex of \(\mathrm{KG}(6,2)\) [3]. This is an abstract rational representation decomposition, not an integral splitting or an equivariant homotopy equivalence.

## Assumptions and scope
The seven-element set \([7]\) is labeled, and each graph vertex is an *unordered* two-element subset. The graph is undirected and simple. A closed neighborhood includes its center; thus this complex must not be confused with the Lovász *open*-neighborhood complex, or with the scale-one Vietoris–Rips clique complex.

Index the \(21\) graph vertices as lexicographically ordered pairs \(e_0,\dots,e_{20}\). The maximal faces are precisely the 21 sets
\[
F_e=\{e\}\cup\{f\in\tbinom{[7]}2:f\cap e=\varnothing\},\qquad e\in\tbinom{[7]}2,
\]
each of size \(11\). It is pure of dimension ten; since its nonzero reduced homology lies in degree three, it is not shellable. The complex is also the vertex-centered intrinsic graph Čech nerve of closed radius-one balls in the unit-edge graph metric (or scale two in the diameter convention). The symmetric-group result concerns singular/simplicial homology with rational coefficients, not integral Specht lattices.

## Proof
**Complete face set.** Generate every nonempty subset of the 21 displayed facets, represented by a 21-bit integer with set bits corresponding to graph vertices. This produces \(37,527\) distinct nonempty faces, with the face vector in dimensions \(0\) through \(10\) equal to
\[
(21,210,1330,5355,9177,9632,6930,3465,1155,231,21).
\]
The executable additionally checks **every one of the \(2^{21}-1\) nonempty vertex subsets** against the predicate of containment in some closed neighborhood, independently of the union-of-facet enumeration. This proves that no faces are omitted. The alternating face count gives \(\widetilde\chi(X)=-260\).

**Integral homotopy via an exhaustive acyclic matching.** Order the 21 vertices lexicographically. Initially mark all nonempty faces unmatched. For each index \(i=0,\dots,20\) in order, simultaneously match each currently unmatched face \(\sigma\) *not* containing \(e_i\) to \(\sigma\cup\{e_i\}\), provided both faces are still unmatched; remove both from future stages. At a fixed stage these pairs are disjoint, so their processing order does not affect the outcome. The executable implements this prescription without randomness. It obtains exactly \(18,633\) matching pairs, one critical zero-simplex, and \(260\) critical three-simplices, with no other critical faces.

To verify the nonstandard premise of the discrete-Morse argument, orient the full Hasse diagram of the face poset **upward** along the matched cover relations and **downward** along every other cover relation. All \(218,673\) codimension-one incidences between nonempty faces are explicitly constructed. Kahn's exact topological-sorting algorithm removes all \(37,527\) vertices, establishing acyclicity globally. By the discrete-Morse theorem, the realization is homotopy equivalent to a CW complex with one zero-cell and 260 three-cells, and no positive-dimensional cells of other dimensions. Every three-cell then attaches to a point, so the CW complex is the displayed wedge of three-spheres. This proves the integral homotopy statement without relying on a mod-two Betti calculation.

**The full rational character.** The original simplex chain complex is \(S_7\)-equivariant even though the chosen discrete-Morse matching need not be. For a permutation \(g\), let
\[
L(g)=\sum_{\substack{\varnothing\ne\sigma\in X\\g\sigma=\sigma}}
(-1)^{\dim\sigma}\operatorname{sgn}(g|_\sigma).
\]
Here the sign refers to the induced permutation of the 21 lexicographically ordered graph vertices in the face. The Hopf trace formula, the trivial action on \(H_0\), and the proved homology concentration in degree three yield \(\chi_3(g)=1-L(g)\). There are 15 conjugacy classes, indexed by partitions of seven. Direct signed fixed-face enumeration gives:

| Cycle type | \(\chi_3\) | Cycle type | \(\chi_3\) | Cycle type | \(\chi_3\) |
| --- | ---: | --- | ---: | --- | ---: |
| \((7)\) | 1 | \((6,1)\) | 0 | \((5,2)\) | 0 |
| \((5,1,1)\) | 0 | \((4,3)\) | 0 | \((4,2,1)\) | 0 |
| \((4,1,1,1)\) | 0 | \((3,3,1)\) | -4 | \((3,2,2)\) | 2 |
| \((3,2,1,1)\) | 0 | \((3,1,1,1,1)\) | 2 | \((2,2,2,1)\) | 0 |
| \((2,2,1,1,1)\) | -4 | \((2,1,1,1,1,1)\) | 0 | \((1,1,1,1,1,1,1)\) | 260 |

An independent computation partitions the 21 graph vertices into cycles under \(g\). An invariant face is a union of these cycles, and its alternating signed contribution equals \((-1)^r\), where \(r\) is the number of selected cycles. Summing these contributions including the empty face reproduces \(\chi_3(g)\) for all 15 classes, checking the orientations independently.

Murnaghan–Nakayama rim-hook recursion constructs all 15 irreducible characters of \(S_7\). The executable verifies their exact orthonormality with weights \(1/z_\mu\), where \(z_\mu=\prod_i i^{m_i}m_i!\) for cycle type \(\mu\). Exact rational inner products of \(\chi_3\) against these characters give multiplicities \(1,1,2,1,1,1,2,1,1\) in the order of the displayed decomposition, and zero for the other six types. Their weighted dimension sum is \(14+15+70+20+21+21+70+15+14=260\), agreeing with the identity trace. Semisimplicity of rational \(S_7\)-representations proves the claimed module isomorphism.

## Verification
Run `python3 verify.py` with Python 3.9+ and no third-party dependencies. It regenerates all 21 graph vertices and all 21 eleven-vertex facets, exhausts \(2,097,151\) possible nonempty faces, checks the face vector, constructs every matching pair, checks all \(218,673\) directed Hasse incidences for global acyclicity, and computes the full 15-class character twice by different combinatorial methods. All representation inner products use exact `Fraction` arithmetic. As an independent check on the original simplicial chain groups, it computes the mod-two boundary-rank vector \((0,20,190,1140,3955,5222,4410,2520,945,210,21)\), giving mod-two reduced Betti number 260 in degree three and zero otherwise. This field calculation corroborates but does not replace the integral Morse homotopy proof. It finishes with `ALL_VERIFY_OK` on success. The executable is a finite exhaustive proof checker for this specified graph, not an infinite-family verification and not a claim of independent auditing.

## Relationship to prior work
Matsushita [1] defines closed-neighborhood complexes, gives functorial relationships with canonical double-cover independence complexes, and relates their fundamental groups to graph fundamental groups. The relevant full text (definition, Theorem 1.2, and examples in Section 3) provides no numeric homotopy computation or \(S_7\)-character for \(\mathrm{KG}(7,2)\). Its suspension formula \(\Sigma\mathcal N[\overline{G}]\simeq\mathcal I(K_2\times G)\), with \(G=J(7,2)\), is compatible with the answer but does not alone calculate it.

Nilakantan and Singh [2] determine the **open**-neighborhood complex of the two-subset Kneser family. For seven ground elements, their theorem gives \(\bigvee^{29}S^3\); that statement does not imply the closed-neighborhood wedge of 260 spheres or the present character. The published result [3] determines the closed-neighborhood/scale-two Čech complex of \(\mathrm{KG}(6,2)\) as \(\bigvee^{64}S^2\) with a multiplicity-free \(S_6\)-character. Its hypotheses concern exactly six ground elements and provide no recurrence or theorem giving seven-ground-element homotopy or character. The published result [4] concerns the **open**-neighborhood \(S_6\)-character of the six-point graph; it likewise does not cover this construction. The categorical-product work [5] computes cases with complete-graph or cycle factors, rather than the required triangular graph \(J(7,2)\). These comparisons address object equivalence, possible dual formulations, larger coverage, and exact-tabulation overlap, rather than relying on different titles alone.

## Limitations
The classification concerns \(\mathrm{KG}(7,2)\), not the whole Kneser family. It gives no equivariant CW structure or integral Specht-module splitting, and it does not determine the persistence maps between Čech scales. The non-equivariant Morse matching is not asserted to be symmetric. The originality comparison used accessible primary texts and indexed results, but an equivalent unindexed calculation may exist. No independent mathematical audit has been performed.

## References
[1] T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608v1, first posted 2025-11-16; relevant sections 1 and 3, HTML text https://arxiv.org/html/2511.12608v2.

[2] N. Nilakantan and A. Singh, *Homotopy type of neighborhood complexes of Kneser graphs, \(\mathrm{KG}_{2,k}\)*, arXiv:1802.05848, first posted 2018-02-16, especially Theorem 1.3, https://arxiv.org/abs/1802.05848.

[3] *The scale-two Čech complex of \(\mathrm{KG}(6,2)\): 64 spheres and a multiplicity-free \(S_6\)-character*, research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-scale-two-ech-complex-of-kg-6-2-64-spheres-and-a-multiplicit--a413c6a778e4.

[4] *Rational symmetry decomposition of the Kneser neighborhood complex on six points*, research record dated 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-rational-symmetry-decomposition-of-the-kneser-neighborhood-compl--6890383e239b.

[5] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, first posted 2023-07-23, https://arxiv.org/abs/2307.12401.
