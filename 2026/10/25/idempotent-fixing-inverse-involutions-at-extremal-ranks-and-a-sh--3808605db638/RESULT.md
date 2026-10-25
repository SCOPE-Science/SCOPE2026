# Idempotent-fixing inverse involutions at extremal ranks and a sharp five-point obstruction

## Finding
Let \(\mathcal O_n\) be the monoid of all weakly order-preserving maps of \([n]=\{1,\ldots,n\}\), under composition. An **inverse involution** is a permutation \(\tau\) of \(\mathcal O_n\) such that \(\tau^2=\mathrm{id}\) and every \(\alpha\) is a mutual semigroup inverse of \(\tau(\alpha)\): \(\alpha\tau(\alpha)\alpha=\alpha\) and \(\tau(\alpha)\alpha\tau(\alpha)=\tau(\alpha)\).

For every integer \(n\geq3\), both the rank-two and the rank-\((n-1)\) strata admit explicit inverse involutions **fixing every idempotent** in the stratum. The rank-two involution has exactly \(\binom{n+1}{3}\) fixed points and \(\binom n3\) transpositions. The rank-\((n-1)\) involution has exactly \(2(n-1)\) fixed points and \(\binom{n-1}{2}\) transpositions. Both maps and their inverses are specified by the formulas below, without solving a matching problem.

Consequently every \(\mathcal O_n\) with \(n\leq4\) has an inverse involution fixing all its idempotents. The threshold is sharp: **no** inverse involution of \(\mathcal O_5\) fixes all its idempotents. In fact every inverse involution of \(\mathcal O_5\) moves at least one idempotent, and this lower bound is attained: an explicit inverse involution moves exactly one idempotent (and its nonidempotent partner) in the rank-three stratum, fixing every other idempotent of \(\mathcal O_5\).

## Assumptions and scope
All maps act on the right-to-left composition convention; the formulas are independent of the chosen notation for this convention. The rank of a map is the size of its image. Mutual inverses have equal rank, as the two inverse identities force both rank inequalities.

A rank-two map is uniquely encoded by \((a;b,c)\) with \(1\leq a<n\) and \(1\leq b<c\leq n\): its value is \(b\) on \([1,a]\) and \(c\) on \([a+1,n]\). A rank-\((n-1)\) map is uniquely encoded by \((a;b)\), with \(1\leq a<n\) and \(1\leq b\leq n\): its only nonsingleton kernel block is \(\{a,a+1\}\), and its image is \([n]\setminus\{b\}\). These data specify the unique order-preserving map.

The formulas concern inverse *matchings of sets of transformations*, not a unary anti-automorphism of the composition law. No assertion is made that the entire monoid \(\mathcal O_n\) has an inverse involution for every \(n\).

## Proof
**1. Rank-two inverse relation and involution.** Consider \(\alpha=(a;b,c)\) and \(\beta=(d;e,f)\). Two maps of the same rank are mutual inverses precisely when the image of each is a transversal of the other's kernel partition. Indeed, \(\alpha\beta\alpha=\alpha\) requires \(\beta\) to select distinct points in the two kernel classes of \(\alpha\) from its image, while the reverse identity gives the converse. Because the maps preserve order, this becomes
\[
\beta\in V(\alpha)\quad\Longleftrightarrow\quad b\leq d<c\quad\text{and}\quad e\leq a<f.
\]
Define
\[
\tau_2(a;b,c)=
\begin{cases}
(c-1;a,b),&a<b,\\
(b;c,a+1),&a\geq c,\\
(a;b,c),&b\leq a<c.
\end{cases}
\]
The last case is exactly the idempotent condition. For \(a<b<c\), the output \((c-1;a,b)\) belongs to the second case since \(c-1\geq b\), and the second application returns \((a;b,c)\). For \(b<c\leq a\), the output \((b;c,a+1)\) belongs to the first case since \(b<c\), and the second application returns the original. All coordinates lie in their prescribed ranges. The displayed inverse inequalities hold in each of the three cases, so \(\tau_2\) is an inverse involution fixing exactly the idempotents.

There are \((n-1)\binom n2\) rank-two maps. Counting idempotents at cut \(a\) gives \(a(n-a)\), hence exactly \(\sum_{a=1}^{n-1}a(n-a)=\binom{n+1}{3}\) fixed maps. The remaining count divided by two is \(\binom n3\), as stated.

**2. Corank-one inverse relation and involution.** Let \(\alpha=(a;b)\) and \(\beta=(c;d)\) be rank-\((n-1)\) maps. For \(\operatorname{im}\beta\) to be a transversal of the kernel of \(\alpha\), the missing position must be one of the two positions in the doubled block. Thus
\[
\beta\in V(\alpha)\quad\Longleftrightarrow\quad
 d\in\{a,a+1\}\quad\text{and}\quad b\in\{c,c+1\}.
\]
Define
\[
\tau_{n-1}(a;b)=
\begin{cases}
(b;a+1),&b<a,\\
(b-1;a),&b>a+1,\\
(a;b),&b\in\{a,a+1\}.
\end{cases}
\]
The first case is sent to the second, and conversely; the displayed transversal conditions hold in both cases. The third case consists exactly of the \(2(n-1)\) idempotents, all fixed. There are \(n(n-1)\) such maps, leaving \(\binom{n-1}{2}\) two-cycles.

**3. All idempotents can be fixed through four points.** The rank-one maps are constant and hence idempotent. The only full-rank order-preserving self-map of a finite chain is the identity, also idempotent. When \(n=3\), the only remaining stratum has rank two; when \(n=4\), the remaining strata have ranks two and three \((n-1)\). Apply the formulas in steps 1 and 2 in each rank, fixing the other maps. Rank preservation makes their union an inverse involution on the entire monoid.

**4. A sharp obstruction at five points.** Every fixed point of any inverse matching \(\tau\) in \(\mathcal O_n\) must be idempotent. Indeed \(\tau(\alpha)=\alpha\) implies \(\alpha^3=\alpha\). If a monotone map \(\alpha\) on a chain satisfies \(\alpha^2(y)=y\), then necessarily \(\alpha(y)=y\): otherwise monotonicity makes the two-step iterate strictly larger or strictly smaller than \(y\). With \(y=\alpha(x)\) this yields \(\alpha^2(x)=\alpha(x)\). Thus an inverse involution fixing every idempotent would have exactly the idempotents as fixed points.

For any \(n,r\), kernel partitions into \(r\) consecutive nonempty blocks have positive lengths \(\ell_1,\dots,\ell_r\) summing to \(n\). A rank-\(r\) map with these blocks is idempotent precisely when its \(i\)-th image value lies in the \(i\)-th block; there are \(\prod_i\ell_i\) choices. The generating function \((z/(1-z)^2)^r\) therefore gives
\[
\#\{\text{rank-}r\text{ idempotents in }\mathcal O_n\}
=\binom{n+r-1}{2r-1}.
\]
For \(n=5,r=3\), this equals \(\binom75=21\), whereas the whole rank-three stratum has \(\binom42\binom53=60\) elements. Fixing all 21 idempotents would leave 39 nonidempotents, none capable of being fixed, to be partitioned into two-cycles. This is impossible.

**5. The lower bound of one moved idempotent is attainable.** The file `certificate_rank3_n5.txt` gives twenty disjoint pairs of rank-three maps. In a code `ab|cde`, the two cuts are \((a,b)\) and the ascending image is \((c,d,e)\). Every pair comprises mutual inverses. They involve exactly forty distinct rank-three maps, including exactly one idempotent (`12|124`); all remaining twenty rank-three maps are idempotents. Swap the members of each of the twenty pairs and fix those twenty idempotents. This is an inverse involution of the rank-three stratum moving exactly one idempotent. Extend it by the rank-two and rank-four formulas and fix the constants and identity. The complete coverage and the mutual-inverse equations for the finite certificate are checked independently by `verify.py`; the certificate is explicit finite evidence, not an unsupported search result.

## Verification
Run `python3 verify.py` in the directory containing the companion `certificate_rank3_n5.txt`. The script uses only Python's standard library and directly computes composition \(\alpha\circ\beta\circ\alpha\) and \(\beta\circ\alpha\circ\beta\). It verifies the two formulas for all admissible parameters and every \(3\leq n\leq12\) (3,000 tests), confirms the fixed-point and transposition counts, and independently parses and checks all sixty rank-three maps on five points against the twenty-pair certificate. The recorded result is `VERIFY_OK individual_extremal_checks= 3000 rank_three_pairs= 20 fixed_idempotents= 20 moved_idempotents= 1`. The all-\(n\) assertions are proved in steps 1–4, not extrapolated from these finite tests.

## Relationship to prior work
Higgins's October 1, 2026 paper [1], Theorem B, establishes a **permutation** inverse matching of \(\mathcal O_n\) for all \(n\), via balanced deletion incidence and Birkhoff's theorem. A permutation matching need not be an involution, nor fix idempotents; the explicit rank-stratum inverse involutions and sharp idempotent-fixing obstruction are not stated there.

Higgins's 2024 work [2], Proposition 2.3, implies an involution matching when the number of columns of a combinatorial regular \(\mathcal D\)-class is an integer multiple of the number of rows. For the rank-\(r\) stratum here, that ratio is \(n/r\), so this theorem covers the rank-two stratum when \(n\) is even, but not rank two for odd \(n\), nor corank one for \(n>2\). It also does not require or guarantee fixing each idempotent, and does not settle the five-point sharp obstruction.

Higgins's earlier work [3] constructs inverse involutions on the larger monoid of cyclic orientation-preserving maps, but explicitly notes that its canonical involution does not preserve the submonoid of order-preserving maps (Example 3.1.4); hence restriction does not directly imply this result.

## Limitations
The formulas provide idempotent-fixing involutions on only the two specified nontrivial extremal ranks (which coincide when \(n=3\)). The finite certificate settles the minimum number of moved idempotents for \(\mathcal O_5\), not the corresponding minimum for every larger \(n\), and does not prove existence of involution matchings on the middle ranks for arbitrary \(n\). The literature search does not exclude a previously unindexed equivalent construction. No independent audit has been performed.

## References
[1] P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, 2026-10-01, Theorem B, Definition 3.1, and Lemma 3.3. https://arxiv.org/html/2610.01912

[2] P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, *Semigroup Forum*, 2024, Proposition 2.3 and Questions 1–4. https://doi.org/10.1007/s00233-024-10430-0

[3] P. M. Higgins, *Involution matchings, the semigroup of orientation-preserving and orientation-reversing mappings, and inverse covers of the full transformation semigroup*, arXiv:1811.04472v2 (2019), Sections 1 and 3, especially Example 3.1.4. https://arxiv.org/html/1811.04472v2
