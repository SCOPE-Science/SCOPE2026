# The exact second-minimum one-type spectrum of the generic partial order

## Finding
Let \(\mathbb P\) be the countable universal homogeneous (random) strict partial order. For an \(n\)-element induced subposet \(P\subseteq\mathbb P\), let \(t(P)\) be the number of **nonalgebraic** complete one-types over the individually named elements of \(P\). Write \(C_r\) for an \(r\)-element chain, \(A_2\) for a two-element antichain, \(\oplus\) for ordinal sum, and \(\sqcup\) for disjoint poset union. Empty chains \(C_0\) are allowed in ordinal sums.

**Theorem.** For every integer \(n\ge2\), and every \(n\)-element finite poset \(P\),
\[
\binom{n+2}{2}\le t(P)\le 2^{n+1}-1.
\]
Equality on the left holds exactly for chains, and equality on the right exactly for antichains. More sharply, if \(P\) is not a chain, then
\[
\boxed{t(P)\ge\binom{n+2}{2}+n-1.}
\]
**Equality in this nonchain bound occurs if and only if** \(P\) is isomorphic to either
\[
C_{n-1}\sqcup C_1,
\]
or
\[
C_a\oplus A_2\oplus C_b\qquad(a,b\ge0,\ a+b=n-2).
\]
All of these extremizers attain the displayed value. At \(n=2\) the descriptions coincide; for \(n\ge3\) they give \(n\) nonisomorphic second-minimizing posets (the \(n-1\) positions of the doubled level and one isolated-point family).

Equivalently, counting **all** complete one-types including the \(n\) equality types adds precisely \(n\) to every number displayed above. The extremal classifications are unchanged.

## Assumptions and scope
All posets here are finite strict posets, and the parameters are individually named. A nonalgebraic one-type means the new point differs from every parameter; this is an orbit of the pointwise stabilizer, not an unlabelled one-point extension modulo parameter automorphisms. The Fraïssé extension and ultrahomogeneity properties guarantee that every consistent one-point extension type occurs and that distinct order patterns give distinct types. No dimension, width, connectedness or additional promise is imposed. We make no assertion that the number of types decreases when one comparison is inserted: such monotonicity is generally false.

The established description of types is the following. A nonalgebraic type corresponds bijectively to a pair \((L,U)\) of subsets of \(P\), where \(L\) is an order ideal, \(U\) an order filter, and \(l<u\) for all \(l\in L,u\in U\). Empty \(L\) and \(U\) are allowed. The proposed novelty is the global sharp **runner-up bound and complete equality classification**, not the basic type description or the separately known chain and antichain formulas.

## Proof
### A maximal-point extension identity
Fix a maximal point \(x\) of \(P\), let \(Q=P\setminus\{x\}\), put \(m=|Q|\) and \(D=\{q\in Q:q<x\}\). Thus \(D\) is an order ideal in \(Q\) and \(F=Q\setminus D\) an order filter. Let \(J(R)\) denote the number of ideals of the induced finite poset \(R\), including the empty ideal.

For a type \((L,U)\) over \(Q\), its extensions to the parameter \(x\) are precisely these three mutually exclusive choices for the relation of the further new point \(y\) to \(x\):

* \(x<y\): available exactly when \(D\subseteq L\) and \(U=\varnothing\).
* \(y<x\): available exactly when \(L\subseteq D\).
* \(x\parallel y\): available exactly when \(U\cap D=\varnothing\).

This list is exhaustive by transitivity, down/up-closure and maximality of \(x\). If \(U\ne\varnothing\), it is impossible that both \(L\not\subseteq D\) and \(U\cap D\ne\varnothing\): choose \(d\in U\cap D\); every \(l\in L\) satisfies \(l<d\) and hence belongs to the ideal \(D\). Consequently every type on \(Q\) has at least one extension. A type with \(U=\varnothing\) has two extensions whenever \(L\) is comparable by inclusion with \(D\), and the unique type \((D,\varnothing)\) has three. A type with \(U\ne\varnothing\) has a second extension exactly when \(L\subseteq D\) and \(U\cap D=\varnothing\).

Write \(E_Q(D)\) for the number of types \((L,U)\) on \(Q\) with \(U\ne\varnothing\), \(L\subseteq D\) and \(U\cap D=\varnothing\). The number of ideals \(L\subseteq D\) is \(J(D)\), and the number of ideals \(L\supseteq D\) is \(J(F)\). Counting the additional extensions beyond one per type, and including the extra third extension at \(L=D,U=\varnothing\), yields the **exact identity**
\[
\boxed{t(P)-t(Q)=J(D)+J(F)+E_Q(D).}\tag{1}
\]
In particular, \(J(D)\ge|D|+1\), \(J(F)\ge|F|+1\), and \(E_Q(D)\ge0\), so
\[
t(P)-t(Q)\ge m+2=|P|+1.\tag{2}
\]
If \(Q\) is not a chain, this last inequality is strict. Indeed, if \(D=Q\) then \(J(D)\ge m+2\); if \(D\ne Q\), the filter \(F\ne\varnothing\) supplies a type \((\varnothing,F)\) counted by \(E_Q(D)\), so \(E_Q(D)\ge1\).

There are at most two extensions of each type apart from the unique \((D,\varnothing)\), which has three. Hence also
\[
t(P)\le2t(Q)+1.\tag{3}
\]
Equality in (3) requires \(D=\varnothing\) and \(Q\) an antichain: if \(D\ne\varnothing\), a type \((\varnothing,\uparrow d)\) with \(d\in D\) has only one extension; if \(D=\varnothing\) but \(Q\) has \(a<b\), the valid type \((\downarrow a,\uparrow b)\) has only one. Conversely, an isolated \(x\) over an antichain gives equality.

### Absolute extrema
For a one-point chain \(t(C_1)=3\). Repeated application of (2) yields
\[
t(P)\ge 3+\sum_{j=2}^{n}(j+1)=\binom{n+2}{2}.
\]
Choosing maximal points successively, equality at every step requires each remaining \(Q\) to be a chain and \(D=Q\); equivalently \(P\) is a chain. The chain itself has \(\binom{n+2}{2}\) types, given by the words \(L^aI^bU^c\) with \(a+b+c=n\).

Repeated application of (3), with \(t(C_1)=3\), gives \(t(P)\le 2^{n+1}-1\). Equality forces every removed maximal point to be isolated over an antichain, so \(P\) is an antichain. Conversely, an antichain permits either \(L\) or \(U\) to be nonempty but not both, yielding \(2^{n+1}-1\) types.

### The runner-up inequality
Define the excess \(g(P)=t(P)-\binom{|P|+2}{2}\). If \(Q\) is a chain with \(m=n-1\) elements, then \(D\) is a prefix of some length \(k\in\{0,\ldots,m\}\). Every nonempty upper filter \(U\subseteq F\) begins at one of \(m-k\) possible positions, and each of the \(k+1\) lower prefixes \(L\subseteq D\) is compatible. Thus \(E_Q(D)=(k+1)(m-k)\). Both induced parts are chains, so (1) yields
\[
\boxed{g(P)=(k+1)(m-k).}\tag{4}
\]
For \(k=m\) this is zero and \(P\) is a chain. For nonchains, \(0\le k\le m-1\) and the identity
\[
(k+1)(m-k)-m=k(m-k-1)\ge0
\]
shows \(g(P)\ge m=n-1\); equality occurs exactly at \(k=0\) or \(k=m-1\). These give \(C_m\sqcup C_1\) and \(C_{m-1}\oplus A_2\), respectively.

If \(Q\) is not a chain, induction on the number of elements gives \(g(Q)\ge m-1\). The strict version of (2) yields \(g(P)\ge g(Q)+1\ge m=n-1\). The base case is the two-element antichain, with excess one. This proves the sharp nonchain lower bound for every \(n\ge2\).

### Complete equality classification
For any \(r\)-element finite poset \(R\), \(J(R)\ge r+1\), with equality exactly for chains. Moreover \(J(R)=r+2\) if and only if \(R\cong C_a\oplus A_2\oplus C_b\) with \(a+b=r-2\). For the latter elementary ideal-lattice fact: prefixes of a linear extension produce one ideal at each cardinality; exactly one additional ideal gives a single rank containing two ideals, with all other ranks containing one. The unique lower and upper chains of ideals force all elements except the two exchanged at that rank into a totally ordered prefix and suffix, with the exchanged pair incomparable. Conversely, such a doubled level creates exactly one additional ideal.

Suppose \(n\ge3\), \(P\) is not a chain and equality \(g(P)=n-1\) holds. If \(Q\) is a chain, (4) already gives the two indicated shapes. Otherwise necessarily \(g(Q)=n-2\) and \(t(P)-t(Q)=n+2\); in (1) this says
\[
[J(D)-(|D|+1)]+[J(F)-(|F|+1)]+E_Q(D)=1.\tag{5}
\]
If \(D=Q\), then \(E_Q(D)=0\) and (5) gives \(J(Q)=m+2\). Hence \(Q\) has a unique doubled level; adjoining a top point gives another poset of the \(C_a\oplus A_2\oplus C_b\) family.

If \(D\ne Q\), then \((\varnothing,U)\) is counted by \(E_Q(D)\) for **every nonempty filter \(U\)** of \(F\). Hence \(E_Q(D)\ge|F|\). Equality in (5) forces \(|F|=1\), both \(D\) and \(F\) chains, and \(E_Q(D)=1\). Write \(F=\{z\}\). If some \(d\in D\) were below \(z\), the distinct type \((\downarrow d,\{z\})\) would also contribute to \(E_Q(D)\), a contradiction. Thus \(z\) is isolated from the chain \(D\), so \(Q\cong C_{m-1}\sqcup C_1\) and \(P\cong C_m\sqcup C_1\). This exhausts all equality cases.

For the converse, (4) gives excess \(n-1\) for \(C_{n-1}\sqcup C_1\) and for a doubled top level. Every additional greatest element increases the excess by one when the remainder has a single doubled level, by (1) and \(J(C_a\oplus A_2\oplus C_b)=n+1\) at the relevant size. Hence every \(C_a\oplus A_2\oplus C_b\) attains equality. The theorem follows.

## Verification
The standalone standard-library file `verify_extrema.py` enumerates every transitively closed strict relation representable using a fixed linear-extension labelling on \(2\le n\le6\) vertices (numbers of distinct such relations \(2,7,40,357,4824\)). Independently of the proof recurrence, it computes types using ideal and filter subset zeta transforms and verifies the absolute extrema and the runner-up equality classification. It reports `ALL_CHECKS_PASS`. Its finite range is a cross-check, not the basis of the unrestricted theorem; the proof above establishes every \(n\ge2\).

## Relationship to prior work
Finite-poset one-point extensions are standard in Fraïssé theory. Dolinka and Mašulović, Lemma 3.3 of arXiv:1009.2892, explicitly use the lower and upper sets \(L,U\) and their comparability condition in an unrelated homomorphism-extension argument; that normal form is prior mathematics. A previously published published-finding corpus finding, “Finite-parameter 1-type counting in the random poset is #P-complete,” explicitly gives the characterization of nonalgebraic types, the chain/antichain formulas and the counting-complexity result. No part of those assertions is claimed here as new. The present theorem sharpens the elementary chain count to an all-size strict nonchain gap and gives **every** equality shape. Neither a general #P-completeness result nor a formula for chains and antichains implies this runner-up structural theorem. Targeted comparisons did not identify a published covering equality-classification result, but unindexed equivalences remain possible.

## Limitations
The invariant counts nonalgebraic complete one-types over named parameters; it is not a count of arbitrary unlabelled extensions. The claimed novelty is the second-minimum threshold and complete equality classification, not the chain or antichain formulas. No analogous second-maximum classification, monotonicity under adding comparisons, or efficient general counting algorithm is asserted. Published literature coverage is necessarily incomplete, and no independent external mathematical validation has been performed.

## References
1. Igor Dolinka and Dragan Mašulović, “A universality result for endomorphism monoids of some ultrahomogeneous structures,” arXiv:1009.2892 (first posted 15 September 2010), Lemma 3.3; *Proc. Edinburgh Math. Soc.* 55 (2012), 635–656. https://arxiv.org/abs/1009.2892
2. Péter Pál Pach, Michael Pinsker, Gabriella Pluhár, András Pongrácz, and Csaba Szabó, “Reducts of the random partial order,” arXiv:1111.7109 (first posted 30 November 2011), *Adv. Math.* 235 (2013/2014). https://arxiv.org/abs/1111.7109
3. “Finite-parameter 1-type counting in the random poset is #P-complete,” published published-finding corpus finding (2026), identifier `2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1`, especially Finding and Proof; this supplies the known one-type characterization, chain/antichain values and a different complexity conclusion.
