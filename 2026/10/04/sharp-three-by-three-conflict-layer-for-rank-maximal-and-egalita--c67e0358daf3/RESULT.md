# Sharp three-by-three conflict layer for rank-maximal and egalitarian stable marriage
## Finding
Consider the complete strict Stable Marriage problem with equal sides.

For a stable matching \(M\), let
\[
p(M)=(p_1(M),p_2(M),\ldots,p_n(M)),
\]
where \(p_k(M)\) counts all agents, on both sides, whose partner is their \(k\)-th choice. A stable matching is **rank-maximal** if its profile is lexicographically maximal.

Its **egalitarian cost** is
\[
c(M)=\sum_a \operatorname{rank}_a(M(a)).
\]
A stable matching is **egalitarian** if it minimizes \(c(M)\).

Let \(R(I)\) and \(E(I)\) denote the complete rank-maximal and egalitarian optimum sets.

For every \(2\times2\) profile,
\[
R(I)=E(I).
\]

For \(3\times3\), there are
\[
6^6=46656
\]
labeled preference profiles, and the exact relation census is
\[
\begin{array}{c|r}
\text{relation} & \text{profiles}\\ \hline
R(I)=E(I) & 42756\\
R(I)\subsetneq E(I) & 2928\\
R(I)\cap E(I)=\varnothing & 972.
\end{array}
\]
No profile has \(E(I)\subsetneq R(I)\), and no profile has nonempty nonnested overlap.

Hence \(3\times3\) is the sharp first complete strict Stable Marriage market where the two fairness objectives can conflict. The total disagreement incidence is
\[
\frac{3900}{46656}=\frac{325}{3888},
\]
and disjoint optimal sets occur with exact incidence
\[
\frac{972}{46656}=\frac1{48}.
\]

A disjoint witness is
\[
\begin{aligned}
m_1&:w_1\succ w_2\succ w_3,\\
m_2&:w_1\succ w_2\succ w_3,\\
m_3&:w_2\succ w_3\succ w_1,
\end{aligned}
\qquad
\begin{aligned}
w_1&:m_3\succ m_1\succ m_2,\\
w_2&:m_2\succ m_1\succ m_3,\\
w_3&:m_1\succ m_3\succ m_2.
\end{aligned}
\]
It has exactly two stable matchings:
\[
M_E=\{(m_1,w_1),(m_2,w_2),(m_3,w_3)\}
\]
and
\[
M_R=\{(m_1,w_3),(m_2,w_2),(m_3,w_1)\}.
\]
Their six-agent rank vectors are
\[
(1,2,2,2,1,2)
\]
and
\[
(3,2,3,1,1,1).
\]
Thus
\[
p(M_E)=(2,4,0),\qquad c(M_E)=10,
\]
whereas
\[
p(M_R)=(3,1,2),\qquad c(M_R)=11.
\]
Therefore \(M_E\) is uniquely egalitarian while \(M_R\) is uniquely rank-maximal.

## Assumptions and scope
Preferences are complete and strict, the two sides have equal cardinality, and stability means absence of a blocking man-woman pair.

Rank-maximality is two-sided: every agent contributes one rank to the profile. Egalitarian cost likewise sums ranks over both sides.

The theorem exhausts all labeled profiles for \(n=2\) and \(n=3\). No statement is made about incomplete lists, ties, one-sided rank profiles, or the frequency of disagreements for \(n\ge4\).

## Proof
For \(n=2\), every one of the \(2^4=16\) complete strict profiles is enumerated. The two optimum sets coincide in all cases.

For \(n=3\), every one of the \(6^6=46656\) profiles is enumerated, and every one of the \(3!=6\) perfect matchings is checked for stability.

Stability is computed independently in two ways: by precomputed rank maps and by direct position queries in the preference lists.

Rank-maximality is also computed twice. One implementation compares profile vectors lexicographically. The second uses an exact steep-base objective with base \(7\), which is larger than the maximum number \(6\) of agents contributing to any profile coordinate; therefore one extra assignment at rank \(k\) outweighs every possible contribution at lower ranks.

Egalitarian optimality is computed directly from total rank cost and independently from the profile identity
\[
c(M)=\sum_{k=1}^{n} k\,p_k(M).
\]

All independent computations agree profile by profile.

As an additional global check, the number of stable matchings over the \(3\times3\) domain is distributed as
\[
34080\text{ profiles with one stable matching},
\]
\[
11484\text{ with two stable matchings},
\]
and
\[
1092\text{ with three stable matchings}.
\]

The optimum-set relation histogram is exactly
\[
42756,\quad2928,\quad972
\]
for equality, strict rank-maximal containment in the egalitarian set, and disjointness. The reverse-containment and nonnested-overlap cells are empty.

The displayed witness is replayed directly by the verifier and has exactly the two stated stable matchings, signatures, and costs.

## Verification
The embedded `verify_rankmax_egalitarian_stable_marriage.py` uses only the Python standard library.

It verifies:
- all \(16\) complete strict \(2\times2\) profiles;
- all \(46656\) complete strict \(3\times3\) profiles;
- two independent stability tests;
- lexicographic rank-maximality against an independent steep-base objective;
- direct egalitarian cost against the profile-weighted cost identity;
- stable-count marginal \(34080,11484,1092\);
- relation census \(42756,2928,972\);
- exact disjoint incidence \(1/48\);
- the displayed disjoint witness.

Run:

`python3 verify_rankmax_egalitarian_stable_marriage.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Irving, Leather, and Gusfield introduced the classical egalitarian stable-marriage objective and showed how weighted stable-marriage machinery can optimize rank-based objectives. Their framework also supports exponentially separated weights that encode lexicographic rank profiles.

Cooper and Manlove later formulate the two-sided rank-maximal profile explicitly and compare profile-based stable matchings empirically with cost-based fairness measures including egalitarian cost. Their full text treats rank-maximal and egalitarian stable matchings as distinct standard notions of fairness.

The contribution here is the sharp finite boundary and complete first conflict layer: equality for every \(2\times2\) profile, the exact \(3\times3\) relation census, the absence of reverse containment and partial overlap, and the exact \(1/48\) disjoint incidence.

Targeted literature and repository searches did not locate this \(42756/2928/972\) table or the sharp \(2\times2\)-to-\(3\times3\) boundary.

## Limitations
The result is a finite exact classification through \(n=3\); it does not imply any asymptotic frequency.

The earliest historical algorithmic manuscript is cited in later literature as dating from July 1985, but no exact public day for that manuscript was verified in the inspected sources. The package therefore records the first day-resolved publisher date available for the foundational article, \(1\) July \(1987\), without inventing a day for the earlier report.

An unindexed exercise, thesis table, code archive, or supplementary computation could contain an equivalent small-market census.

## References
1. R. W. Irving, P. Leather, and D. Gusfield, “An efficient algorithm for the ‘optimal’ stable marriage,” *Journal of the ACM* 34(3) (1987), 532–543. DOI: 10.1145/28869.28871.
2. F. Cooper and D. Manlove, “Two-sided profile-based optimality in the stable marriage problem,” arXiv:1905.06626, first submitted 16 May 2019.
3. D. Gusfield, “Three Fast Algorithms for Four Problems in Stable Marriage,” *SIAM Journal on Computing* 16(1) (1987), 111–128. DOI: 10.1137/0216010.
