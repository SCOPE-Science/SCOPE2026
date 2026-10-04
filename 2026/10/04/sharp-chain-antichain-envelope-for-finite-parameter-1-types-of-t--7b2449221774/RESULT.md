# Sharp chain–antichain envelope for finite-parameter 1-types of the random poset
## Finding
Let \(\mathbb D\) be the countable random (universal ultrahomogeneous) poset, let \(A\subseteq\mathbb D\) be finite with \(|A|=n\), and let \(P\) be the induced finite poset. Write
\[
\operatorname{inc}(P)=\#\{\{x,y\}:x\parallel y\},\qquad
\operatorname{cmp}(P)=\#\{\{x,y\}:x<y\text{ or }y<x\}.
\]
Thus \(\operatorname{inc}(P)+\operatorname{cmp}(P)=\binom n2\).

As in the earlier finite-parameter counting result, let \(c(P)\) denote the number of nonalgebraic 1-types over \(A\), equivalently the number of admissible one-point extensions of \(P\). Then
\[
\boxed{\binom{n+2}{2}+\operatorname{inc}(P)\ \le\ c(P)\ \le\ 2^{n+1}-1-\operatorname{cmp}(P).}
\]
Since \(|S_1(A)|=n+c(P)\), this gives the sharp universal envelope
\[
\boxed{n+\binom{n+2}{2}\ \le\ |S_1(A)|\ \le\ n+2^{n+1}-1.}
\]
The lower endpoint is attained exactly when \(P\) is a chain, and the upper endpoint exactly when \(P\) is an antichain. Equivalently, every incomparable pair forces at least one extra nonalgebraic 1-type above the chain floor, while every comparable pair forces at least one missing nonalgebraic 1-type below the antichain ceiling.

A useful exact reformulation sits behind both inequalities. Let \(J(P)\) be the number of ideals of \(P\), equivalently the number of antichains. Let \(q(P)\) be the number of ordered pairs \((X,Y)\) of **nonempty** antichains satisfying
\[
x<y\qquad\text{for every }x\in X,\ y\in Y.
\]
Then
\[
\boxed{c(P)=2J(P)-1+q(P).}
\]
Moreover,
\[
q(P)\le 2^n-J(P),
\]
because \((X,Y)\mapsto X\cup Y\) injects into the non-antichain subsets of \(P\).

## Assumptions and scope
The count \(c(P)\) is the same one-point-extension count used in the earlier ledger finding on #P-completeness of finite-parameter 1-type counting in the random poset. Namely, a nonalgebraic type is represented by a pair \((L,U)\) where \(L\) is an ideal, \(U\) is a filter, and every element of \(L\) is strictly below every element of \(U\). The Fraïssé extension property realizes every such finite one-point extension in \(\mathbb D\), and ultrahomogeneity identifies two realizations exactly when they induce the same extension over \(A\).

This finding does **not** claim that the chain and antichain endpoint formulas themselves are new; those formulas were already recorded in the earlier ledger entry. The retained contribution is the all-poset extremal theorem, the unique extremizers, and the pair-sensitive stability bounds involving \(\operatorname{inc}(P)\) and \(\operatorname{cmp}(P)\).

## Proof
For an admissible one-point extension, let
\[
L=\{p\in P:p<x\},\qquad U=\{p\in P:x<p\}.
\]
Then \(L\) is an ideal, \(U\) is a filter, and \(L<U\) pointwise. Map this pair to
\[
X=\max L,\qquad Y=\min U,
\]
with the convention that the maximum/minimum antichain of the empty set is empty. The sets \(X,Y\) are antichains and every \(x\in X\) lies below every \(y\in Y\).

Conversely, if \(X,Y\) are antichains and \(X<Y\) pointwise, then
\[
L=\downarrow X,\qquad U=\uparrow Y
\]
is admissible: if \(l\le x<y\le u\), then \(l<u\). These constructions are inverse because an ideal is determined by its maximal elements and a filter by its minimal elements. Therefore \(c(P)\) is exactly the number of ordered pairs of antichains \((X,Y)\) with \(X<Y\).

Pairs with at least one side empty contribute \(2J(P)-1\), so
\[
c(P)=2J(P)-1+q(P),
\]
where \(q(P)\) counts the separated pairs with both sides nonempty.

For the upper bound, send a nonempty separated pair \((X,Y)\) to \(X\cup Y\). The union is not an antichain, and the map is injective: in the induced order on \(X\cup Y\), every point of \(X\) is minimal and every point of \(Y\) is maximal, so
\[
X=\min(X\cup Y),\qquad Y=\max(X\cup Y).
\]
Exactly \(J(P)\) subsets of \(P\) are antichains, hence
\[
q(P)\le 2^n-J(P).
\]
Thus
\[
c(P)\le 2J(P)-1+2^n-J(P)=2^n+J(P)-1.
\]
Every comparable two-element subset is a non-antichain, so \(2^n-J(P)\ge\operatorname{cmp}(P)\), or
\[
J(P)\le 2^n-\operatorname{cmp}(P).
\]
Substitution gives
\[
c(P)\le 2^{n+1}-1-\operatorname{cmp}(P).
\]

For the lower bound, the empty set, all \(n\) singletons, and every incomparable two-element subset are distinct antichains. Hence
\[
J(P)\ge 1+n+\operatorname{inc}(P).
\]
Every comparable unordered pair \(\{x,y\}\), written with \(x<y\), contributes the separated singleton pair \((\{x\},\{y\})\), so
\[
q(P)\ge\operatorname{cmp}(P).
\]
Therefore
\[
\begin{aligned}
c(P)
&=2J(P)-1+q(P)\\
&\ge 2(1+n+\operatorname{inc}(P))-1+\operatorname{cmp}(P)\\
&=\binom{n+2}{2}+\operatorname{inc}(P),
\end{aligned}
\]
using \(\operatorname{cmp}(P)=\binom n2-\operatorname{inc}(P)\).

If \(P\) is a chain, its only antichains are the empty set and singletons, and the admissible positions of a new point are the weakly increasing \(L/I/U\) words, giving
\[
c(P)=\binom{n+2}{2}.
\]
If \(P\) is not a chain then \(\operatorname{inc}(P)>0\), so the lower stability inequality is strict above the chain value. Thus chains are exactly the minimizers.

If \(P\) is an antichain, \(L\) and \(U\) cannot both be nonempty, so
\[
c(P)=2^n+2^n-1=2^{n+1}-1.
\]
If \(P\) is not an antichain then \(\operatorname{cmp}(P)>0\), so the upper stability inequality is strict below the antichain value. Thus antichains are exactly the maximizers.

## Verification
The companion standard-library verifier enumerates every naturally labeled finite poset through six vertices. Any finite poset admits a linear extension, so every isomorphism type occurs in this enumeration after relabeling. The row counts are
\[
1,1,2,7,40,357,4824
\]
for sizes \(0,1,\ldots,6\), for a total of 5232 posets.

For each poset, the verifier computes \(c(P)\) in two independent ways: directly from ternary one-point statuses using the ideal/filter/cross conditions, and from separated antichain pairs. It checks the identity
\[
c(P)=2J(P)-1+q(P),
\]
both stability inequalities, and the claimed equality cases. The observed minimum/maximum values are
\[
1,3,6,10,15,21,28
\]
and
\[
1,3,7,15,31,63,127,
\]
respectively, exactly the chain and antichain formulas. The replay returns `VERIFY_OK`.

The finite replay is only a consistency check; the proof above establishes the theorem for all finite posets.

## Relationship to prior work
Kurilić and Kuzeljević explicitly include the random (universal ultrahomogeneous) poset among the countable ultrahomogeneous partial orders. Their paper is used only as the eligible modern structural anchor; it does not state the extremal finite-parameter type theorem above.

Dolinka and Mašulović explicitly encode a one-point extension of a finite poset by
\[
L=\{p:p<x\},\qquad U=\{p:x<p\},
\]
and note the pointwise cross-condition \(L<U\). That structural description is treated as prior.

The immediately preceding ledger finding on the random poset already proved \(|S_1(A)|=|A|+c(P)\), established #P-completeness of computing it, and recorded the chain and antichain endpoint formulas as examples. The present finding is narrower and complementary: it proves those examples are the **unique global extremizers** and gives quantitative stability away from both endpoints.

Targeted published-finding corpus searches for random-poset one-point-extension extrema, finite-poset one-point-extension extrema, chain/antichain extremizers, and finite-parameter random-poset type extrema found no direct match. Exact-phrase and broader web searches for “number of one-point extensions” or “one-element extensions” of finite posets likewise did not locate the displayed inequalities or extremal classification. The residual risk is that this short argument exists as unindexed folklore or under different terminology.

## Limitations
The theorem controls only the number of complete 1-types over a finite parameter set. It does not address higher-arity type counts, asymptotics for random finite parameter posets, or finer distributional information about one-point extensions.

The originality search cannot certify absence from all theses, lecture notes, or unpublished folklore. The antichain-pair reformulation and inequalities are elementary enough that independent rediscovery is plausible.

## References
1. Miloš S. Kurilić and Boriša Kuzeljević, “Antichains of Copies of Ultrahomogeneous Structures,” arXiv:1904.00656; Archive for Mathematical Logic 61 (2022), 867–879, DOI 10.1007/s00153-022-00817-7. First arXiv posting: 1 April 2019. The published metadata lists 03C15 among the classifications.
2. Igor Dolinka and Dragan Mašulović, “A universality result for endomorphism monoids of some ultrahomogeneous structures,” Proceedings of the Edinburgh Mathematical Society 55 (2012), 635–656, DOI 10.1017/S0013091510001161. Lemma 4.3 gives the lower-set/upper-set description of a finite-poset one-point extension.
