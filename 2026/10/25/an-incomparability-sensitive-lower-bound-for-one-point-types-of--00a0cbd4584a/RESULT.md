# An incomparability-sensitive lower bound for one-point types of the generic poset

## Finding
Let \(P\) be any finite partial order on \(n\ge0\) elements, embedded as individually named parameters in the countable universal homogeneous partial order. Write \(t(P)\) for its number of complete **nonalgebraic** one-types and \(j(P)\) for the number of unordered incomparable pairs. Then
\[
\boxed{t(P)\ge \binom{n+2}{2}+j(P).}
\]
**Equality holds if and only if \(P\) is a disjoint union of at most two (possibly empty) chains**, with no comparabilities between the nonempty chains.

More precisely, let \(i(P)\) count order ideals (including the empty ideal), let \(c(P)=\binom n2-j(P)\) count strict comparable pairs, and let \(m(P)\) count admissible nonalgebraic one-point extensions having at least one old point below and at least one above the new point. The following exact, nonnegative defect decomposition holds:
\[
t(P)-\binom{n+2}{2}-j(P)
=2\bigl(i(P)-n-1-j(P)\bigr)+\bigl(m(P)-c(P)\bigr).
\]
Both summands are nonnegative. The second vanishes exactly for disjoint unions of chains. For a disjoint union of \(k\) nonempty chains of sizes \(n_1,\ldots,n_k\), the entire defect is \(2\sum_{r=3}^{k}e_r(n_1,\ldots,n_k)\), where \(e_r\) is an elementary symmetric polynomial; thus the zero-defect cases have at most two nonempty chains.

## Assumptions and scope
The universal homogeneous poset is the Fraïssé limit of all finite strict partial orders. A complete nonalgebraic one-type over the named set \(P\) is determined by the disjoint sets \(L=\{a\in P:a<x\}\) and \(U=\{a\in P:x<a\}\). The admissibility conditions are: \(L\) is downward closed; \(U\) is upward closed; and every element of \(L\) is strictly below every element of \(U\). Every such pair is realized, and homogeneity identifies realizations with identical data. A down-set called an ideal here need not be directed (the finite combinatorial convention). The empty poset is allowed, and an empty chain is not counted among nonempty components. No algebraic equality types are included in \(t(P)\).

## Proof
**Step 1: Separate pure and mixed extensions.** An admissible pair \((L,U)\) with \(U=\varnothing\) is specified by an arbitrary ideal \(L\), and one with \(L=\varnothing\) by an arbitrary filter \(U\). Their only duplication is \((\varnothing,\varnothing)\). Poset duality equates the ideal and filter counts. Consequently
\[t(P)=2i(P)-1+m(P).\]

**Step 2: The ideal-count inequality.** We prove \(i(P)\ge n+1+j(P)\) by induction on \(n\). The empty case is immediate. Choose a maximal element \(x\), put \(Q=P\setminus\{x\}\), and let \(D\subseteq Q\) consist of the strict predecessors of \(x\). Let \(H=Q\setminus D\) with the induced order. Since \(x\) is maximal, the elements of \(H\) are precisely the elements of \(Q\) incomparable with \(x\); put \(h=|H|\). The ideals excluding \(x\) are precisely the ideals of \(Q\). Those containing \(x\) are exactly \(D\cup\{x\}\cup S\), where \(S\) ranges over all ideals of \(H\). Indeed, \(D\) is an ideal of \(Q\), and a predecessor in \(Q\) of any member of \(S\) lies in \(D\cup S\). Thus
\[i(P)=i(Q)+i(H),\qquad j(P)=j(Q)+h.\]
Every finite \(h\)-element poset has at least \(h+1\) ideals: the successive prefixes of any linear extension supply distinct ideals. Applying induction to \(Q\),
\[
i(P)\ge |Q|+1+j(Q)+h+1=n+1+j(P).
\]
This argument also covers \(H=\varnothing\).

**Step 3: Every comparable pair supplies a different mixed extension.** To each strict comparable pair \(a<b\) assign
\[L=\mathord\downarrow a,\qquad U=\mathord\uparrow b.\]
These sets form an admissible mixed extension, because every member of \(L\) lies below every member of \(U\). Distinct pairs give distinct extensions: \(a\) is the unique greatest member of \(L\), and \(b\) the unique least member of \(U\). Hence \(m(P)\ge c(P)\).

**Step 4: Sharp inequality and defect.** Combine Steps 1–3:
\[
\begin{aligned}
t(P)&=2i(P)-1+m(P)\\
&\ge 2(n+1+j(P))-1+c(P)\\
&=\binom{n+2}{2}+j(P).
\end{aligned}
\]
Keeping the two slacks rather than discarding them gives the displayed exact defect identity.

**Step 5: Characterize equality.** If a connected component of the undirected comparability graph is not a chain, choose two incomparable vertices at graph distance two, say \(a,c\), with a common neighbor \(b\). Transitivity forces either \(a,c<b\) or \(b<a,c\). In the first case the pair \(L=\downarrow a\cup\downarrow c\), \(U=\uparrow b\) is an admissible mixed extension not arising from any strict comparable pair: \(L\) has two incomparable maximal elements. In the second case use \(L=\downarrow b\), \(U=\uparrow a\cup\uparrow c\), where \(U\) has two incomparable minimal elements. So \(m(P)>c(P)\) unless every component is a chain. Conversely, if \(P\) is a disjoint union of chains, every mixed extension lies inside one chain and is uniquely \((\downarrow a,\uparrow b)\) for some \(a<b\), so \(m(P)=c(P)\).

Suppose then that the nonempty chain components have sizes \(n_1,\ldots,n_k\). Ideals are independent selections of prefixes, giving
\[i(P)=\prod_{s=1}^{k}(n_s+1)=1+n+e_2+\sum_{r=3}^{k}e_r,\qquad j(P)=e_2.\]
Consequently the defect equals \(2\sum_{r=3}^{k}e_r\). All \(n_s\) are positive, so the defect vanishes precisely when \(k\le2\). This includes \(k=0\) for the empty poset. The classification and theorem follow.

## Verification
A standalone standard-library Python program, `check.py`, exhaustively enumerates all transitive labeled strict relations through five vertices. It computes ideals, filters, admissible mixed types, comparability pairs, both nonnegative defect contributions and the asserted equality structures directly. The run checks \(4474\) posets in total, with \(4231\) at five vertices. Its output is recorded in `check_output.txt` and ends `ALL_CHECKS_PASS`. This finite enumeration tests, but does not replace, the unrestricted proof above.

As illustrative sharp instances, two disjoint chains of sizes \(a,b\) have \(j(P)=ab\) and exactly \(t(P)=\binom{a+b+2}{2}+ab\) nonalgebraic one-types. Three isolated points have \(j(P)=3\) but defect \(2\), exhibiting why two nonempty components are the exact equality limit.

## Relationship to prior work
Dolinka and Mašulović describe admissible lower/upper sets in one-point extensions of finite posets (arXiv:1009.2892, §3.1), and Pach–Pinsker–Pluhár–Pongrácz–Szabó establish the homogeneous generic-poset setting (arXiv:1111.7109, §§1–3). The public finite-parameter counting-complexity theorem identifies the same ideal/filter parametrization and gives the chain and antichain baseline counts, but its primary result is a counting-hardness reduction, not an incomparability-sensitive estimate or an equality classification. The contribution here is the exact nonnegative defect decomposition, the coefficient-one penalty per incomparable pair, and the complete global equality classification for all finite posets. Related exact extremal calculations for specialized posets or the second-smallest type count do not imply this inequality uniformly over large incomparability counts.

## Limitations
The displayed lower bound is attained only when the prescribed incomparability count can be realized by at most two disjoint chains. For a fixed nonattainable pair of size and incomparability count, the theorem does not determine the optimal larger minimum. It does not calculate arbitrary \(t(P)\) more efficiently or imply any new complexity classification. Searches and textual comparisons cannot exclude unindexed or implicit prior statements of this elementary-looking inequality; independent originality review remains outstanding.

## References
1. Igor Dolinka and Dragan Mašulović, “A universality result for endomorphism monoids of some ultrahomogeneous structures,” arXiv:1009.2892, first posted 2010-09-15; §3.1 (one-point poset extensions). DOI: 10.1017/S0013091510001161.
2. Péter Pál Pach, Michael Pinsker, Gabriella Pluhár, András Pongrácz and Csaba Szabó, “Reducts of the random partial order,” arXiv:1111.7109, first posted 2011-11-30; §§1–3 (homogeneity and finite extension property).
3. “Finite-parameter 1-type counting in the random poset is #P-complete,” publicly available mathematical research record (2026); source for the ideal/filter counting formulation and comparison, not for the new lower bound.
