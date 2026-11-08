# A complete codimension-two reaching-distance spectrum for the Černý automata

## Finding

For every integer \(n\ge3\), let \(Q=\{0,1,\ldots,n-1\}\), and let the standard two-letter Černý automaton act from left to right on subsets by
\[
a(i)=\begin{cases}0,&i=n-1,\\i,&0\le i<n-1,\end{cases}
\qquad b(i)=i+1\pmod n.
\]
For integers \(0\le u<v<n\), let \(T_{u,v}=Q\setminus\{u,v\}\), and let \(d_n(u,v)\) be the minimum length of a word \(w\in\{a,b\}^{*}\) for which \(Qw=T_{u,v}\). Then
\[
\boxed{
d_n(u,v)=\begin{cases}
n+2,&v=n-1,\ u=0,\\
u+3,&v=n-1,\ 1\le u\le n-2,\\
n+u+3,&v=u+1\le n-2,\\
v+3,&v\le n-2,\ v-u\ge2.
\end{cases}}
\]
In particular the complete *graded reaching-distance spectrum* is
\[
\boxed{\sum_{0\le u<v<n}z^{d_n(u,v)}=
\sum_{\ell=4}^{n+1}(\ell-3)z^\ell+
\sum_{\ell=n+2}^{2n}z^\ell.}
\]
Every integer distance from \(4\) to \(2n\) occurs. The longest distance \(2n\) occurs for the unique target \(Q\setminus\{n-3,n-2\}\), while the shorter distances have the displayed explicit multiplicities.

## Assumptions and scope

Both letters are the *specified labeled transformations*, not arbitrary cyclic and rank-deficient transformations. The word length counts both letters at unit cost, with no free cyclic relabeling at the beginning or end. A target is an exact image, not merely a containing image. The empty word has image \(Q\). At all steps the image cardinality cannot increase. All claims hold for every \(n\ge3\), including \(n=3\), when the target is a singleton.

For the proof, write \(H=Q\setminus S\) for the omitted-state set of the current image \(S\). The cyclic letter sends \(H\) to \(H+1\) modulo \(n\). The merging letter acts by
\[
H\stackrel a\longmapsto
\begin{cases}
H,& n-1\in H,\\
(H\setminus\{0\})\cup\{n-1\},& n-1\notin H,\ 0\in H,\\
H\cup\{n-1\},&0,n-1\notin H.
\end{cases}
\]
The number of holes therefore never decreases.

## Proof

**1. An exhaustive upper construction using two effective merging letters.** The first \(a\) sends \(Q\) to \(Q\setminus\{n-1\}\). For \(k\) in \(\{2,\ldots,n-1\}\), the word \(ab^ka\) has exactly two holes, \(\{n-1+k,n-1\}\) modulo \(n\). (For \(k=0\), the second merging letter does nothing; for \(k=1\), it transports the only hole rather than creating another.) Consequently
\[
Qab^kab^t=Q\setminus\{n-1+k+t,n-1+t\}\pmod n.
\]
For a desired pair \(\{u,v\}\), choose which hole \(e\in\{u,v\}\) was created by the second \(a\), let \(o\) denote the other, and define the least nonnegative residues
\[
t=[e+1]_n,\qquad k=[o-e]_n.
\]
The orientation is admissible precisely when \(2\le k\le n-1\). At least one orientation is admissible because the two oriented differences sum to \(n\). The minimum length of these normal-form witnesses is
\[
F_n(\{u,v\})=2+\min_{e\in\{u,v\},\,[o-e]_n\ge2}\bigl([e+1]_n+[o-e]_n\bigr).\tag{1}
\]
Thus \(d_n(u,v)\le F_n(\{u,v\})\).

**2. A lower-bound potential that rules out any advantage from extra merging letters.** Define a function \(F\) on all hole sets of cardinality at most two by
\[
F(\varnothing)=0,\qquad F(\{h\})=1+[h+1]_n,
\qquad F(\{u,v\})=F_n(\{u,v\}).
\]
Every value is attained by a word with exactly as many effective merging letters as there are holes, as shown above for pairs (and by \(ab^{[h+1]_n}\) for singletons). We claim that, whenever an operation \(c\in\{a,b\}\) transforms a set of at most two holes \(H\) to another such set \(H'\),
\[
F(H')\le F(H)+1.\tag{2}
\]
For \(c=b\), append \(b\) to an attaining word; this gives a witness of length \(F(H)+1\) still using only the same effective merging letters. Any final exponent of \(b\) may be reduced modulo \(n\), so (2) follows.

For \(c=a\), the displayed hole action leaves \(H\) unchanged whenever \(n-1\in H\). From the empty set it creates \(\{n-1\}\), increasing \(F\) by exactly one. From \(\{0\}\) it moves the hole to \(\{n-1\}\), decreasing \(F\). From \(\{h\}\), where \(1\le h\le n-2\), it creates \(\{h,n-1\}\); (1) gives \(F(\{h,n-1\})=h+3=F(\{h\})+1\). Finally, from a two-hole set not containing \(n-1\), either it creates a third hole (which cannot occur on a path ending with only two holes), or the set is \(\{0,x\}\) for \(1\le x\le n-2\), and it is transported to \(\{x,n-1\}\). Formula (1) gives
\[
F(\{x,n-1\})=x+3\le F(\{0,x\}),
\]
where the right side is \(x+3\) for \(x\ge2\) and \(n+3\) for \(x=1\). These are all cases, proving (2).

Starting at \(H=\varnothing\), inequality (2) implies by induction that \(F(H)\) is a lower bound for the number of letters required to reach \(H\), provided no intermediate set has more than two holes. Since the number of holes is nondecreasing, this proviso holds for *every* word whose final omitted set has exactly two members. Thus \(d_n(u,v)\ge F_n(\{u,v\})\). Combined with step 1, the bound is exact. In particular, arbitrary extra \(a\) letters, including hole-transporting ones, cannot shorten an optimal word.

**3. Closed forms.** Suppose \(u<v\le n-2\). Choosing \(e=u\) in (1) costs \(v+3\) when \(v-u\ge2\), and is inadmissible when \(v=u+1\). Choosing \(e=v\) always costs \(n+u+3\). Therefore the two cases with \(v\le n-2\) follow. If \(v=n-1\), choosing \(e=u\) costs \(n+2\) when \(u\le n-3\), while choosing \(e=n-1\) costs \(u+3\) when \(u\ge1\). The formulas also cover the adjacent endpoint pair \(\{n-2,n-1\}\). This proves the displayed four-case formula.

**4. Complete distribution.** The pairs with \(v\le n-2\) and \(v-u\ge2\) contribute \(v-1\) targets at distance \(v+3\), for \(2\le v\le n-2\). The pairs \(\{u,n-1\}\) with \(1\le u\le n-2\) contribute one target at each distance \(4,5,\ldots,n+1\). The pair \(\{0,n-1\}\) contributes distance \(n+2\), and the remaining adjacent pairs \(\{u,u+1\}\), \(0\le u\le n-3\), contribute one each at distances \(n+3,\ldots,2n\). Summing these contributions gives the stated polynomial and the unique maximizer.

## Verification

`artifacts/verify_reaching.py` independently performs breadth-first search from the full image in the subset automaton, checks the predicted threshold of every \((n-2)\)-element target, and replays explicit optimal normal-form words. For every \(3\le n\le15\), the script checks all targets and the complete distance histogram: 559 target pairs across 65,515 reachable nonempty subset states. It additionally checks the potential inequality (2) on all hole sets of sizes zero, one, and two for \(3\le n\le140\). The transcript in `artifacts/verification_output.txt` ends with `VERIFY_OK`. These are finite checks; the preceding argument, not the finite enumeration, proves the theorem for arbitrary \(n\).

Run with `python3 artifacts/verify_reaching.py` from the package directory; no dependencies beyond the Python standard library are needed.

## Relationship to prior work

Zhu (2024) and Casas–Volkov (2023) study bounds for reaching arbitrary subsets in binary completely reachable automata, including standardized subclasses. Their general theorems do not give the target-specific shortest-distance function here. Ferens–Szykuła (2022) establish general quadratic bounds; Hoffmann (2020) addresses complete reachability and transformation groups. These are background, not exact pair enumerations.

The public result *Two-defect reachability in cyclic defect-one automata* (2026) proves the existence of at-most-\(2n\)-length two-merge witnesses for a broader class, and explicitly does **not** classify shortest reaching words target by target. The public result *Exact \(k\)-avoiding thresholds of the Černý automata* (2026) determines a maximum over forbidden subsets, including the sharp \(2n\) endpoint, but not the individual exact-reaching distances or the complete distribution. The public result *Exact early deficiency profile of the Černý automata* (2026) determines a minimum over all targets of a given cardinality, including the value \(4\) at deficiency two; it also does not determine the full target-dependent distribution. These earlier bounds and extrema are credited rather than asserted as new.

The contribution claimed here is the *whole target-indexed function* \(d_n(u,v)\), its proof of optimality even among words with rank-preserving merging letters, and its all-length multiplicity polynomial. No uniqueness claim about this theorem in all published literature is made.

## Limitations

Only targets of codimension exactly two are classified; no formula is asserted for codimension three or greater, for arbitrary defect-one letters, or for unlabelled or conjugacy-invariant distances. A published equivalent under a different terminology may exist. The result does not resolve Don's conjecture for general completely reachable automata and does not independently validate itself through human or external review.

## References

1. Y. Zhu, *Around Don's conjecture for binary completely reachable automata*, arXiv:2402.19089v1, first public 2024-02-29, https://arxiv.org/html/2402.19089v1.
2. D. Casas and M. V. Volkov, *Don's conjecture for binary completely reachable automata: an approach and its limitations*, arXiv:2311.00077v1, first public 2023-10-31, https://arxiv.org/html/2311.00077v2.
3. R. Ferens and M. Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on the reaching threshold*, arXiv:2208.05956, first public 2022-08-11, https://arxiv.org/abs/2208.05956.
4. S. Hoffmann, *Completely Reachable Automata, Primitive Groups and the State Complexity of the Set of Synchronizing Words*, arXiv:2007.09104, first public 2020-07-17, https://arxiv.org/html/2007.09104v2.
5. *Two-defect reachability in cyclic defect-one automata*, public record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-two-defect-reachability-in-cyclic-defect-one-automata--3d0ad329ab1e.
6. *Exact k-avoiding thresholds of the Černý automata*, public record, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f.
7. *Exact early deficiency profile of the Černý automata*, public record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3.
