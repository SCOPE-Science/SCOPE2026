# Finite-parameter 1-type counting in the random poset is #P-complete
## Finding
Let \(\mathbb D\) be the countable random (universal ultrahomogeneous) poset, and let \(A\subseteq\mathbb D\) be finite. Write \(P\) for the finite poset induced on \(A\). For a nonalgebraic 1-type \(p(x)\) over \(A\), put
\[
L_p=\{a\in A:a<x\in p\},\qquad U_p=\{a\in A:x<a\in p\}.
\]
Then the map \(p\mapsto(L_p,U_p)\) is a bijection from the nonalgebraic 1-types over \(A\) to the pairs \((L,U)\) satisfying

1. \(L\) is an order ideal (down-set) of \(P\);
2. \(U\) is an order filter (up-set) of \(P\); and
3. \(l<u\) in \(P\) for every \(l\in L\) and \(u\in U\).

If \(c(P)\) denotes the number of such pairs, then
\[
\boxed{|S_1(A)|=|P|+c(P).}
\]
The \(|P|\) summand consists of the algebraic types \(x=a\), \(a\in A\).

The exact counting problem
\[
P\longmapsto |S_1(P)|
\]
is #P-complete under polynomial-time Turing reductions. This remains true when the input finite poset is promised to have a greatest element.

A useful reduction identity is the following. Let \(J(P)\) be the number of ideals of \(P\), and let
\[
Q_m=P\oplus C_m
\]
be the ordinal sum obtained by placing an \(m\)-element chain strictly above every point of \(P\). Then
\[
\boxed{c(Q_m)=c(P)+mJ(P)+\binom{m+1}{2}.}
\]
In particular, both \(Q_1\) and \(Q_2\) have greatest elements and
\[
\boxed{J(P)=|S_1(Q_2)|-|S_1(Q_1)|-3.}
\]
Since counting ideals is equivalent to counting antichains, a classical #P-complete problem, this gives the hardness result with only two oracle calls.

For orientation, if \(C_n\) is an \(n\)-element chain and \(A_n\) an \(n\)-element antichain, then
\[
c(C_n)=\binom{n+2}{2},\qquad c(A_n)=2^{n+1}-1.
\]

## Assumptions and scope
The random poset \(\mathbb D\) is the Fraïssé limit of the class of all finite posets. The input to the counting problem is a finite poset given by its order relation; every such poset embeds as a finite induced subposet of \(\mathbb D\), so this is exactly the finite-parameter problem for the random poset.

The complexity statement is for exact counting and uses polynomial-time Turing reductions. No parsimonious or single-query many-one completeness claim is made.

The count \(|S_1(A)|\) is the complete first-order 1-type count over the finite parameter set. Equivalently, it is the number of orbits of the pointwise stabilizer \(\operatorname{Aut}(\mathbb D)_{(A)}\) on \(\mathbb D\): ultrahomogeneity identifies elements inducing the same one-point extension over \(A\), and the Fraïssé extension property realizes every finite one-point extension. The strong amalgamation property ensures that the only algebraic 1-types are the \(|A|\) equality types.

## Proof
Fix a finite induced subposet \(P=A\) of \(\mathbb D\). Consider an element \(x\notin A\). Partition \(A\) into
\[
L=\{a:a<x\},\qquad U=\{a:x<a\},\qquad I=A\setminus(L\cup U).
\]
Transitivity immediately forces \(L\) to be a down-set and \(U\) to be an up-set. It also forces \(l<u\) for every \(l\in L\) and \(u\in U\), because \(l<x<u\).

Conversely, suppose \((L,U)\) satisfies those three conditions. Add a new point \(x\) to \(P\), declare \(l<x\) for \(l\in L\), declare \(x<u\) for \(u\in U\), and leave \(x\) incomparable with all other points. Downward closure of \(L\), upward closure of \(U\), and the cross-condition \(L<U\) are exactly what is needed for the enlarged relation to remain a partial order. Thus \((L,U)\) defines a finite one-point extension of \(P\). The Fraïssé extension property of \(\mathbb D\) realizes it, and ultrahomogeneity shows that two realizations are in the same pointwise-stabilizer orbit. This proves the bijection and the formula \(|S_1(A)|=|P|+c(P)\).

For membership in #P, a certificate for a nonalgebraic type is simply a ternary label on each point of \(P\), recording membership in \(L\), in \(U\), or in neither. The three admissibility conditions can be checked in polynomial time. Algebraic types can be represented by a separate tag and a chosen parameter. Hence the exact type-count function lies in #P.

For hardness, let \(J(P)\) be the number of ideals of an arbitrary finite poset \(P\), and form \(Q_m=P\oplus C_m\), with the chain written \(t_1<\cdots<t_m\). In a one-point extension by \(x\), the statuses of the chain points relative to \(x\) must form a word
\[
L^a I^b U^c,\qquad a+b+c=m,
\]
where \(L\) means \(t_i<x\), \(I\) means incomparable, and \(U\) means \(x<t_i\).

There are three cases.

* If every chain point is in \(U\), the relation of \(x\) to \(P\) is an arbitrary one-point type over \(P\), giving \(c(P)\) possibilities.
* If no chain point is in \(L\) and at least one is in \(I\), then \(U\cap P\) must be empty: if \(x<p\) for some \(p\in P\), then \(p<t_1\) would force \(x<t_1\), contradicting the initial incomparable block. The lower set \(L\cap P\) may be any ideal of \(P\). There are \(m\) possible nonempty incomparable blocks, hence \(mJ(P)\) possibilities.
* If at least one chain point is in \(L\), then every point of \(P\) lies below \(x\), because every point of \(P\) lies below \(t_1\). The relation to \(P\) is therefore forced. The number of triples \((a,b,c)\) with \(a\ge1\) and \(a+b+c=m\) is \(\binom{m+1}{2}\).

Adding the three cases gives
\[
c(Q_m)=c(P)+mJ(P)+\binom{m+1}{2}.
\]
Since \(|Q_m|=|P|+m\), subtraction for \(m=1,2\) yields
\[
|S_1(Q_2)|-|S_1(Q_1)|=J(P)+3.
\]
Both queried posets have a greatest element. Finally, ideals and antichains of a finite poset are in bijection: an ideal is determined by its maximal elements, and an antichain generates its downward closure. Provan and Ball proved that counting antichains in a finite partial order is #P-complete. Therefore exact finite-parameter 1-type counting for the random poset is #P-hard under a two-query polynomial-time Turing reduction, and together with membership in #P it is #P-complete under such reductions.

For the two sample formulas, a chain type is a weakly increasing word in \(L,I,U\), giving \(\binom{n+2}{2}\). In an antichain, \(L\) and \(U\) cannot both be nonempty, giving \(2^n+2^n-1=2^{n+1}-1\).

## Verification
The companion standard-library verifier independently implements the admissible-pair characterization and a direct transitivity test on the enlarged \((n+1)\)-point relation. It enumerates every naturally labeled transitive poset through five points (408 posets in total), checks equality of the two one-point-extension counts, and verifies
\[
c(P\oplus C_m)=c(P)+mJ(P)+\binom{m+1}{2}
\]
for \(m=1,2,3\) on every one of those posets. It also checks the two-query recovery identity
\[
J(P)=c(P\oplus C_2)-c(P\oplus C_1)-2
\]
and the chain/antichain closed forms through seven points. The replay ends with `VERIFY_OK`.

This finite computation is a consistency check; the all-size proof is the structural argument above.

## Relationship to prior work
Kurilić and Kuzeljević explicitly treat the random (universal ultrahomogeneous) poset among the countable ultrahomogeneous partial orders and recall the finite-stabilizer orbit language and Fraïssé extension property. Their paper supplies an eligible modern model-theoretic anchor for the structure, but it does not study exact finite-parameter type counts or counting complexity.

The one-point-extension description itself is not claimed as new. Dolinka and Mašulović use the same lower-set/upper-set data \(L,U\) for one-point extensions of finite posets, including the necessary cross-condition that every element of \(L\) lies below every element of \(U\). The present contribution is the exact identification of those extension patterns with finite-parameter 1-types of the random poset and, especially, the top-chain identity that transfers #P-completeness of ideal/antichain counting to exact type counting.

Provan and Ball proved in 1983 that counting antichains in a finite partial order is #P-complete. That hardness theorem is used as an input and is not new here.

Targeted searches for “random poset” or “generic partial order” together with “#P”, “one-point type”, “one-point extension”, “ideals”, and equivalent orbit-count formulations did not locate the displayed top-chain identity or the resulting #P-completeness statement. A semantic search over a database of recent mathematical findings returned a random-poset reduct orbit-profile result as the closest item; it concerns global ordered-tuple orbits, not pointwise-stabilizer 1-types over an input finite poset.

## Limitations
The completeness statement is under polynomial-time Turing reductions, using two oracle calls. A stronger parsimonious or single-query many-one reduction is not established here. The originality search cannot rule out an unindexed equivalent observation, and the structural description of one-point poset extensions is explicitly prior work.

No approximation-complexity claim is made, and no claim is made about efficient counting for restricted poset classes such as bounded width or bounded height.

## References
1. Miloš S. Kurilić and Boriša Kuzeljević, “Antichains of Copies of Ultrahomogeneous Structures,” arXiv:1904.00656; Archive for Mathematical Logic 61 (2022), 867–879, DOI 10.1007/s00153-022-00817-7. First arXiv posting: 1 April 2019. The preprint lists 2010 MSC 03C15 first.
2. Igor Dolinka and Dragan Mašulović, “A universality result for endomorphism monoids of some ultrahomogeneous structures,” Proceedings of the Edinburgh Mathematical Society 55 (2012), 635–656, DOI 10.1017/S0013091510001161. See Lemma 4.3 for the \(L/U\) description of a finite-poset one-point extension.
3. J. Scott Provan and Michael O. Ball, “The Complexity of Counting Cuts and of Computing the Probability that a Graph is Connected,” SIAM Journal on Computing 12 (1983), 777–788, DOI 10.1137/0212053. The abstract explicitly includes counting antichains in a partial order among the #P-complete problems.
