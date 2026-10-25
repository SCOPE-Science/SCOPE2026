# Conjugacy classes in the units of layered diamond incidence algebras

## Finding

For a prime power \(q\) and integer \(b\ge2\), let \(P_b\) have a unique minimum \(0\), a unique maximum \(1\), and an antichain \(\{m_1,\ldots,m_b\}\), with precisely \(0<m_i<1\). Put \(G_b(q)=I(P_b;\mathbb F_q)^\times\). Then the number \(k(G_b(q))\) of ordinary group-conjugacy classes is
\[
\boxed{k(G_b(q))=q(q-2)(q+1)^b+(2q)^b+(q-1)^{b+1}.}
\]
This holds uniformly for every finite field, including characteristic two. Equivalently, the formula counts complex irreducible characters of \(G_b(q)\). For \(q=2\), the answer is \(4^b+1\). The same identity holds for \(b=1\), where it reduces to the previously known Borel-group count \(q^3-2q+1\).

The closely related radical-square-zero incidence algebra of the complete height-two bipartite poset with levels of sizes \(2\) and \(b\) has unit-group class number \(q(q-2)(q+1)^b+(2q)^b\), as is implied by known graphic-Tutte formulas. Thus introducing the composable paths through the intermediate antichain and their common central \((0,1)\) interval contributes exactly \((q-1)^{b+1}\) additional classes. This comparison concerns a different algebra of the same total number of radical generators; it is not a claim of an inclusion of groups.

## Assumptions and scope

The coefficient field is \(\mathbb F_q\) for an arbitrary prime power \(q\ge2\). The parameter \(b\) is an integer at least \(2\); \(b=1\) is included only as a boundary consistency check. The incidence-algebra multiplication is interval convolution. The algebra has dimension \(3b+3\). Its Jacobson radical \(J\) is the strict-interval subspace, \(J^2=\mathbb F_q e_{0,1}\ne0\), and \(J^3=0\). The unipotent group \(1+J\) is two-step nilpotent, nonabelian for every \(b\ge1\), and has order \(q^{2b+1}\). No claim is made for arbitrary height-three posets or for primary conjugacy of the full nonunit monoid.

Each unit can be uniquely represented by \(b+2\) nonzero diagonal coefficients \(a,c_1,\ldots,c_b,d\), two vectors \(X=(X_i)\), \(Y=(Y_i)\) of length \(b\), and one coefficient \(Z\), all over \(\mathbb F_q\). In the linear extension \(0,m_1,\ldots,m_b,1\), these are the diagonal entries, the \((0,m_i)\)-entries, the \((m_i,1)\)-entries, and the \((0,1)\)-entry, respectively. The unit-group order is \(\lvert G_b(q)\rvert=(q-1)^{b+2}q^{2b+1}\).

## Proof

Write a second unit using diagonal entries \(\alpha,\gamma_i,\delta\) and strict entries \(X_i',Y_i',Z'\). Multiplication in the incidence algebra shows that the two units commute if and only if, for every \(1\le i\le b\),
\[
(a-c_i)X_i'-(\alpha-\gamma_i)X_i=0,\qquad
(c_i-d)Y_i'-(\gamma_i-\delta)Y_i=0,
\]
and
\[
(a-d)Z'-(\alpha-\delta)Z+\sum_{i=1}^b(X_iY_i'-X_i'Y_i)=0.
\]
These are necessary and sufficient because the incidence algebra has no other strict intervals. For diagonal *pairs* define \(u=(a,\alpha)\), \(v=(d,\delta)\), \(w_i=(c_i,\gamma_i)\) in the torus \((\mathbb F_q^\times)^2\).

First suppose \(u\ne v\). There are \((q-1)^2q(q-2)\) choices of the two outer diagonal pairs. For a fixed intermediate pair \(w_i\), if \(w_i=u\) or \(w_i=v\), the first two displayed equations have \(q^3\) solutions for the four entries \((X_i,X_i',Y_i,Y_i')\); for each of the remaining \((q-1)^2-2\) possible \(w_i\), there are \(q^2\) solutions. Summing over \(w_i\) gives \(2q^3+((q-1)^2-2)q^2=q^2(q^2-1)\). The last displayed equation has \(q\) solutions for \((Z,Z')\), since its coefficient pair \((a-d,\alpha-\delta)\) is nonzero. Thus the total commuting-pair contribution from unequal outer pairs is
\[
N_{\ne}=(q-1)^2q(q-2)\,q^{2b+1}(q^2-1)^b.
\]
When \(q=2\), this case is empty; the factor \(q-2\) correctly makes its contribution zero.

Next suppose \(u=v\). There are \((q-1)^2\) choices of the common outer diagonal pair. For every \(w_i\ne u\), the two length-two vectors \((X_i,X_i')\) and \((Y_i,Y_i')\) belong to the same one-dimensional kernel of a nonzero linear functional. Hence they have \(q^2\) possibilities in total, and their determinant \(X_iY_i'-X_i'Y_i\) vanishes. For each \(w_i=u\), all four entries are initially free. If precisely \(k\) of the intermediate diagonal pairs equal \(u\), the remaining condition is the vanishing of the standard nondegenerate pairing on two vectors of length \(2k\):
\[
\sum_{i:w_i=u}(X_iY_i'-X_i'Y_i)=0.
\]
For \(k\ge1\), the number of such vector pairs is \(q^{4k-1}+(q-1)q^{2k-1}\): the first vector is either zero (\(q^{2k}\) choices for the other), or nonzero (\((q^{2k}-1)q^{2k-1}\) choices). The same expression equals \(1\) when \(k=0\), as required. The entries \((Z,Z')\) are arbitrary and contribute \(q^2\). Each of the remaining \(b-k\) middle diagonal pairs has \((q-1)^2-1=q(q-2)\) possibilities. Summing over \(k\) with the binomial theorem gives
\[
\begin{aligned}
N_{=}&=(q-1)^2q^{2b+1}\sum_{k=0}^{b}\binom bk[q(q-2)]^{b-k}\bigl(q^{2k}+(q-1)\bigr)\\
&=(q-1)^2q^{2b+1}\left[(2q(q-1))^b+(q-1)^{2b+1}\right].
\end{aligned}
\]

For every finite group, its number of conjugacy classes equals its number of commuting ordered pairs divided by its order. Consequently
\[
\begin{aligned}
k(G_b(q))
&=\frac{N_{\ne}+N_{=}}{(q-1)^{b+2}q^{2b+1}}\\
&=q(q-2)(q+1)^b+(2q)^b+(q-1)^{b+1},
\end{aligned}
\]
as asserted. All steps are valid in characteristic two, since the determinant-counting argument uses neither division by two nor signs requiring odd characteristic.

The radical-square-zero height-two comparator has the first two terms by the general graphic-Tutte unit-conjugacy formula: for the complete bipartite graph \(K_{2,b}\), the coefficient computation gives \(q(q-2)(q+1)^b+(2q)^b\). This comparator is already covered by the broader square-zero theory. The added term in the present height-three group therefore isolates the contribution from the nontrivial central composition relation.

## Verification

The standalone `verify.py` checks the commutation equations by directly enumerating all ordered pairs of group elements over the prime fields of orders \(2\) and \(3\) in four small instances. It additionally enumerates all diagonal strata and evaluates their exact linear-equation solution counts for six further parameter pairs, including a field-size-four case in which no underlying field arithmetic is presumed in the symbolic count. The checks print `ALL_CHECKS_OK` when successful. They support, but do not replace, the exact general proof. The direct class counts include \(5\) for \((q,b)=(2,1)\), \(17\) for \((2,2)\), \(65\) for \((2,3)\), and \(22\) for \((3,1)\); symbolic counts include \(92\) for \((3,2)\), \(291\) for \((4,2)\), and \(704\) for \((5,2)\).

## Relationship to prior work

Can's 2021 incidence-monoid paper introduces relevant algebraic-monoid and automorphism structures but does not give this finite-field height-three unit-group conjugacy-class formula in the examined portions. Can, Casimiro and Malheiro's 2022 incidence-monoid study treats conjugacy in antichain submonoids for height-two bipartite posets; its group-conjugacy arguments use abelian unipotent radicals. Here the radical is not square-zero, the unipotent unit subgroup is nonabelian, and those abelian-radical results do not directly apply. The known graphic-Tutte class-number formula for radical-square-zero quivers covers the height-two comparator, not this composable height-three poset. The parameter \(b=1\) reduces to the classical upper-triangular three-by-three case and is not asserted to be new.

## Limitations

This is the exact number of **ordinary group-conjugacy classes of units**, not the number of primary-conjugacy classes in the entire incidence monoid and not a classification of individual conjugacy representatives. The formula is specialized to the three-level diamond family; it is not a general three-level-poset formula. Earlier generalized orbit-count methods might supply an unrecognized equivalent specialization, and the existence of a prior identical formula outside the inspected literature cannot be ruled out. No independent audit or independent validation has been performed.

## References

1. Mahir Bilen Can, “Incidence Monoids: Automorphisms and Complexity,” arXiv:2105.09826, first publicly posted 20 May 2021. https://arxiv.org/abs/2105.09826
2. Mahir Bilen Can, Ana Casimiro, António Malheiro, “Idempotent Varieties of Incidence Monoids and Bipartite Posets,” arXiv:2208.01073, first publicly posted 1 August 2022; *Algebras and Representation Theory* 26 (2023), 1975–2000. https://arxiv.org/abs/2208.01073
