# Sharp four-agent boundary for rank-maximal matchings to lose popularity
## Finding
Consider a balanced one-sided house-allocation instance with \(n\) applicants, \(n\) unit posts, and complete strict preferences.

A matching is **popular** if no other matching is preferred by a strict majority of applicants in a head-to-head vote. A matching is **rank-maximal** if its signature
\[
(x_1,x_2,\ldots,x_n),
\]
where \(x_k\) counts applicants receiving their \(k\)-th choice, is lexicographically maximal.

Let \(P(I)\) be the set of popular perfect matchings and \(R(I)\) the set of rank-maximal perfect matchings.

For every \(2\times2\) profile,
\[
R(I)=P(I).
\]

For the complete \(3\times3\) domain of
\[
6^3=216
\]
labeled profiles, exactly \(210\) profiles admit a popular matching, and every such profile satisfies
\[
R(I)\subseteq P(I).
\]
More precisely,
\[
\begin{array}{c|r}
\text{relation} & \text{profiles}\\ \hline
R(I)=P(I) & 138\\
R(I)\subsetneq P(I) & 72\\
P(I)=\varnothing & 6
\end{array}
\]
The six profiles without a popular matching are exactly those in which all three applicants have the same preference order.

The containment is sharp at four applicants. With posts \(A,B,C,D\), consider
\[
\begin{aligned}
a_1&:D\succ B\succ A\succ C,\\
a_2&:D\succ B\succ A\succ C,\\
a_3&:C\succ D\succ B\succ A,\\
a_4&:D\succ C\succ A\succ B.
\end{aligned}
\]
The rank-maximal signature is
\[
(2,1,1,0).
\]
There are exactly four rank-maximal matchings, written as the post assigned to \(a_1,a_2,a_3,a_4\):
\[
(A,B,C,D),\quad
(D,B,C,A),\quad
(B,A,C,D),\quad
(B,D,C,A).
\]
Exactly two of these are popular:
\[
(D,B,C,A),\qquad(B,D,C,A).
\]
Thus popular matchings exist, but not every rank-maximal matching is popular. Four applicants are therefore the first balanced complete strict market where rank-maximality can fail popularity while popularity itself remains feasible.

## Assumptions and scope
Preferences are complete and strict and every post has unit capacity. Matchings are perfect.

Restricting to perfect matchings loses no popular outcome in this balanced complete setting: if an applicant and a post were both unmatched, adding that acceptable edge would make one applicant strictly better off and nobody worse off, so the original matching could not be popular.

Popularity is unweighted one-applicant-one-vote majority comparison. Rank-maximality uses the standard lexicographic signature of assigned ranks.

The universal classification is complete only through \(n=3\). At \(n=4\), the theorem claims a sharp witness rather than a census of all profiles.

## Proof
For \(n=2\), all \(2^2=4\) labeled profiles are enumerated. The popular and rank-maximal sets agree in every profile.

For \(n=3\), every one of the \(6^3=216\) labeled profiles is enumerated, and every one of the \(3!=6\) perfect matchings is tested.

Popularity is computed in two independent ways. First, each matching is compared directly with all five alternatives by applicant majority. Second, the strict-list characterization of Abraham, Irving, Kavitha, and Mehlhorn is specialized to the complete balanced case: every first-choice post must be assigned to an applicant who ranks it first, and each applicant must receive either her first-choice post or her most-preferred post that is not anyone's first choice, with a private last resort used only when no such real post exists. The two methods agree profile by profile.

Rank-maximality is also computed in two independent ways. One implementation compares signatures lexicographically. The other assigns a steep-base integer score using base \(n+1\), so that one additional assignment at any rank outweighs every possible contribution from lower ranks. The two rank-maximal sets agree profile by profile.

The exact \(3\times3\) relation histogram is
\[
138,\quad72,\quad6
\]
for equality, strict rank-maximal containment in the popular set, and nonexistence of a popular matching. All six nonexistence profiles have three identical preference orders, and there are exactly six such labeled profiles.

For the displayed \(4\times4\) witness, all \(24\) perfect matchings are examined by the same four independent computations. The common rank-maximal signature is
\[
(2,1,1,0),
\]
the rank-maximal set contains the four listed matchings, and the popular set contains exactly the two listed matchings. Hence \(R(I)\not\subseteq P(I)\) despite \(P(I)\neq\varnothing\).

## Verification
The embedded `verify_popular_rankmax_boundary.py` uses only the Python standard library.

It verifies:
- all \(4\) complete strict \(2\times2\) profiles;
- all \(216\) complete strict \(3\times3\) profiles;
- direct-majority popularity against the Abraham-Irving-Kavitha-Mehlhorn characterization;
- lexicographic rank signatures against an independent steep-base objective;
- the exact \(3\times3\) histogram \(138,72,6\);
- that the six nonexistence profiles are exactly the identical-preference profiles;
- all \(24\) perfect matchings of the displayed \(4\times4\) witness;
- the four rank-maximal witness matchings, the two popular witness matchings, and signature \((2,1,1,0)\).

Run:

`python3 verify_popular_rankmax_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Irving, Kavitha, Mehlhorn, Michail, and Paluch define rank-maximal matchings by lexicographic maximization of the matching signature and give polynomial-time algorithms for computing them.

Abraham, Irving, Kavitha, and Mehlhorn define popularity for one-sided preference systems, give an exact characterization for strict lists, and explicitly observe that rank-maximal matchings need not be popular. Their paper also gives the classical three-applicant identical-preference example with no popular matching and reports simulation evidence on popular-matching existence for larger random instances.

The present result identifies the smallest balanced complete strict market in which the two criteria can genuinely separate while popularity still exists. It shows that through three applicants every rank-maximal matching is automatically popular whenever popularity is feasible, gives the exact complete \(3\times3\) relation census, and supplies a four-applicant witness showing that the containment fails immediately afterward.

## Limitations
The result concerns complete strict one-sided preferences, equal numbers of applicants and posts, unit capacities, and unweighted popularity.

It does not cover ties, incomplete lists, unequal sides, capacities, weighted voters, two-sided preferences, or a complete \(4\times4\) profile census.

The originality search did not locate the exact \(138/72/6\) census or the sharp conditional-containment boundary. An unindexed exercise, thesis, code archive, or supplementary computation could contain an equivalent small-market classification.

## References
1. R. W. Irving, T. Kavitha, K. Mehlhorn, D. Michail, and K. E. Paluch, “Rank-maximal matchings,” *Proceedings of the Fifteenth Annual ACM-SIAM Symposium on Discrete Algorithms*, 2004, pp. 68–75; journal version, *ACM Transactions on Algorithms* 2 (2006), 602–610. DOI: 10.1145/1198513.1198520.
2. D. J. Abraham, R. W. Irving, T. Kavitha, and K. Mehlhorn, “Popular Matchings,” *Proceedings of the Sixteenth Annual ACM-SIAM Symposium on Discrete Algorithms*, 23–25 January 2005, pp. 424–432; journal version, *SIAM Journal on Computing* 37 (2007), 1030–1045. DOI: 10.1137/06067328X.
