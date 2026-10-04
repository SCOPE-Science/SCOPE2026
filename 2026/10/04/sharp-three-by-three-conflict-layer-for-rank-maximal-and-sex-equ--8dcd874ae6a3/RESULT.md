# Sharp three-by-three conflict layer for rank-maximal and sex-equal stable marriage
## Finding
Consider complete strict Stable Marriage with equal sides.

For a stable matching \(M\), let
\[
p(M)=(p_1(M),p_2(M),\ldots,p_n(M)),
\]
where \(p_k(M)\) counts all agents, on both sides, whose partner is their \(k\)-th choice. A stable matching is **rank-maximal** when its profile is lexicographically maximal over the stable matchings.

Let
\[
c_M(M)=\sum_{m}\operatorname{rank}_m(M(m)),
\qquad
c_W(M)=\sum_{w}\operatorname{rank}_w(M(w)).
\]
Its **sex-equality score** is
\[
s(M)=|c_M(M)-c_W(M)|.
\]
A stable matching is **sex-equal** when it minimizes \(s(M)\).

Write \(R(I)\) and \(X(I)\) for the complete rank-maximal and sex-equal optimum sets.

For every complete strict market with at most \(2\) agents per side,
\[
R(I)=X(I).
\]

For \(3\) agents per side there are
\[
6^6=46656
\]
labeled preference profiles. Their exact optimum-set relation census is
\[
\begin{array}{c|r}
\text{relation} & \text{profiles}\\ \hline
R(I)=X(I) & 39084\\
R(I)\cap X(I)=\varnothing & 6204\\
X(I)\subsetneq R(I) & 864\\
R(I)\subsetneq X(I) & 504.
\end{array}
\]
There is no profile with nonempty nonnested overlap.

Hence three-by-three is the sharp first market where rank-maximal and sex-equal fairness can conflict. The total disagreement incidence is
\[
\frac{7572}{46656}=\frac{631}{3888}.
\]
Disjoint optimum sets occur with exact incidence
\[
\frac{6204}{46656}=\frac{517}{3888}.
\]
The two one-sided containment incidences are
\[
\frac{864}{46656}=\frac1{54}
\]
for \(X(I)\subsetneq R(I)\), and
\[
\frac{504}{46656}=\frac7{648}
\]
for \(R(I)\subsetneq X(I)\).

A concrete disjoint witness is
\[
\begin{aligned}
m_1&:w_1\succ w_2\succ w_3,\\
m_2&:w_1\succ w_2\succ w_3,\\
m_3&:w_1\succ w_3\succ w_2,
\end{aligned}
\qquad
\begin{aligned}
w_1&:m_1\succ m_2\succ m_3,\\
w_2&:m_1\succ m_3\succ m_2,\\
w_3&:m_2\succ m_1\succ m_3.
\end{aligned}
\]
It has exactly two stable matchings:
\[
M_X=\{(m_1,w_1),(m_2,w_2),(m_3,w_3)\}
\]
and
\[
M_R=\{(m_1,w_1),(m_2,w_3),(m_3,w_2)\}.
\]

For \(M_X\), the six-agent rank vector is
\[
(1,2,2,1,3,3),
\]
so
\[
p(M_X)=(2,2,2)
\]
and
\[
s(M_X)=|5-7|=2.
\]

For \(M_R\), the six-agent rank vector is
\[
(1,3,3,1,2,1),
\]
so
\[
p(M_R)=(3,1,2)
\]
and
\[
s(M_R)=|7-4|=3.
\]

Therefore \(M_X\) is uniquely sex-equal, while \(M_R\) is uniquely rank-maximal.

## Assumptions and scope
Preferences are complete and strict, the two sides have equal cardinality, and stability means absence of a blocking man-woman pair.

Rank-maximality is two-sided: every agent contributes one coordinate to the profile count. Sex equality uses the standard absolute difference between the aggregate rank burdens of the two sides.

The theorem exhausts all labeled markets with one, two, and three agents per side. It does not address incomplete lists, ties, one-sided rank-maximality, balanced stable matching, or frequencies for markets of size at least four.

## Proof
For \(n=1\), there is only one stable matching.

For \(n=2\), all
\[
2^4=16
\]
complete strict profiles are enumerated, and \(R(I)=X(I)\) in every case.

For \(n=3\), every one of the
\[
6^6=46656
\]
preference profiles is enumerated. For each profile, all
\[
3!=6
\]
perfect matchings are tested for stability.

Stability is computed independently in two ways: one implementation uses precomputed rank maps, while the second compares positions directly in the preference lists.

Rank-maximality is also computed twice. The first implementation compares the two-sided profile vectors lexicographically. The second assigns a steep exact integer weight with base
\[
2n+1=7.
\]
Since at most \(2n=6\) agents contribute to any lower-rank coordinates, one additional rank-\(k\) assignment outweighs every possible contribution below rank \(k\), so the steep objective is exactly equivalent to lexicographic profile maximization.

Sex equality is computed in two equivalent but independently coded forms. One uses
\[
\left|\sum_m r_m-\sum_w r_w\right|.
\]
The other counts, on each side, the number of opposite-side agents preferred to the assigned partner:
\[
\sum_m(r_m-1)
\quad\text{and}\quad
\sum_w(r_w-1).
\]
Because the same constant \(n\) is subtracted from both side totals, the two absolute differences agree exactly. The implementations agree on every stable matching of every profile.

The number of stable matchings over the full three-by-three domain is independently tallied as
\[
34080
\]
profiles with one stable matching,
\[
11484
\]
with two, and
\[
1092
\]
with three.

The complete optimum-set relation histogram is exactly
\[
39084,\quad6204,\quad864,\quad504
\]
for equality, disjointness, strict sex-equal containment in the rank-maximal set, and strict rank-maximal containment in the sex-equal set. No nonempty nonnested overlap occurs.

The displayed witness is replayed directly by the verifier, including its two stable matchings, profile vectors, sex-equality scores, and the uniqueness of each optimum.

## Verification
The embedded `verify_rankmax_sexequal_stable_marriage.py` uses only the Python standard library and exact integer arithmetic.

It verifies:
- the one-agent base case;
- all \(16\) complete strict two-by-two profiles;
- all \(46656\) complete strict three-by-three profiles;
- two independent stability tests;
- lexicographic rank-maximality against an independent steep-base objective;
- rank-sum sex equality against the equivalent preferred-alternatives formulation;
- stable-count marginal \(34080,11484,1092\);
- relation census \(39084,6204,864,504\);
- exact disagreement incidence \(631/3888\);
- exact disjoint incidence \(517/3888\);
- the displayed disjoint witness.

Run:

`python3 verify_rankmax_sexequal_stable_marriage.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Rank-maximal and sex-equal stable matchings are established fairness concepts in the Stable Marriage literature.

Cooper and Manlove give a full two-sided profile-based treatment of rank-maximal stable matching. They define the two-sided profile, define rank-maximality by lexicographic maximization, explain the classical exponential-weight construction, and in their experimental section explicitly compare rank-maximal stable matchings using sex-equality scores.

Their introduction also defines sex-equal stable matching as minimizing the difference between the aggregate rank sums of men and women and cites the classical hardness literature.

Romero-Medina introduced the sex-equal concept as minimizing the absolute difference between the numbers of more-preferred alternatives on the two sides. In complete strict markets this is exactly the rank-sum difference used here.

These sources establish the two objectives and their conceptual distinction. The contribution here is the sharp first-market boundary and complete three-by-three optimum-set relation census. Targeted searches for the exact counts \(39084,6204,864,504\), the total probability \(631/3888\), and a complete three-by-three rank-maximal/sex-equal classification did not locate an equivalent published theorem or table.

## Limitations
The theorem is a finite exact classification through three agents per side and does not imply asymptotic frequencies.

The finding concerns complete optimum sets, not a particular tie-breaking rule among multiple rank-maximal or sex-equal stable matchings.

An older working-paper literature exists for sex-equal stable matching, but the exact public day was not verified in the inspected record. The metadata therefore uses the earliest day-resolved public repository source inspected that is directly about sex-equal Stable Marriage.

An unindexed thesis appendix, teaching dataset, or software enumeration could contain an equivalent three-by-three census.

## References
1. H. Yanagisawa, S. Miyazaki, and K. Iwama, “Approximation Algorithms for the Sex-Equal Stable Marriage Problem,” IEICE Technical Report COMP2007-55, 2008.
2. F. Cooper and D. Manlove, “Two-sided profile-based optimality in the stable marriage problem,” arXiv:1905.06626, first submitted 16 May 2019.
3. A. Romero-Medina, “Sex-equal Stable matching,” UC3M Working Papers, Economics 6075, 1998; later *Theory and Decision* 50(3) (2001), 197–212.
4. R. W. Irving, P. Leather, and D. Gusfield, “An efficient algorithm for the ‘optimal’ stable marriage,” *Journal of the ACM* 34(3) (1987), 532–543.
