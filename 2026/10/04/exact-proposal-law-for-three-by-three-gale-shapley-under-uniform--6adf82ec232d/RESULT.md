# Exact proposal law for three-by-three Gale–Shapley under uniform preferences
## Finding
Consider the classical stable-marriage problem with three men and three women. Every participant has a strict complete ranking of the opposite side, and all six rankings for every participant are equally likely and mutually independent. Run the men-proposing Gale–Shapley algorithm.

Let \(P\) be the total number of proposals. Across all
\[
6^6=46656
\]
labeled preference profiles, the exact law is
\[
\Pr(P=3)=\frac29,
\qquad
\Pr(P=4)=\frac13,
\qquad
\Pr(P=5)=\frac{11}{36},
\qquad
\Pr(P=6)=\frac18,
\qquad
\Pr(P=7)=\frac1{72}.
\]
No profile needs eight or nine proposals. Consequently
\[
\mathbb E[P]=\frac{35}{8}
\]
and
\[
\operatorname{Var}(P)=\frac{583}{576}.
\]

Each man proposes down his preference list until reaching his partner in the men-optimal stable matching, so \(P\) is also the sum of the three men-optimal partner ranks. The sorted rank multiset has the exact law
\[
\begin{array}{c|c}
\text{sorted ranks} & \text{probability}\\
\hline
(1,1,1) & 2/9\\
(1,1,2) & 1/3\\
(1,1,3) & 1/6\\
(1,2,2) & 5/36\\
(1,2,3) & 1/9\\
(2,2,2) & 1/72\\
(2,2,3) & 1/72
\end{array}
\]
and no other multiset occurs.

Let \(S\) be the number of stable matchings of the same profile. The exact joint profile counts, with rows indexed by \(P=3,4,5,6,7\) and columns by \(S=1,2,3\), are
\[
\begin{pmatrix}
5064&4572&732\\
10224&5004&324\\
12420&1800&36\\
5724&108&0\\
648&0&0
\end{pmatrix}.
\]
Hence every seven-proposal profile has a unique stable matching, whereas every profile with three stable matchings terminates within five proposals. The conditional proposal means are
\[
\mathbb E[P\mid S=1]=\frac{13089}{2840},
\qquad
\mathbb E[P\mid S=2]=\frac{1205}{319},
\qquad
\mathbb E[P\mid S=3]=\frac{306}{91}.
\]

The \(P=3\) atom is already known: it is exactly the one-round Gale–Shapley event in which the three men have distinct first choices. The contribution here is the complete proposal law, its men-optimal rank decomposition, the sharp seven-proposal cutoff, and the full coupling to stable-matching multiplicity.

## Assumptions and scope
The market has exactly three men and three women. Preferences are strict, complete, labeled, and independently uniform over the six linear orders. Gale–Shapley is men-proposing.

A proposal is counted whenever a currently free man applies to the next woman on his list. The total does not depend on which free man is selected next in the usual sequential implementation; the verifier cross-checks against a simultaneous-round implementation.

The number \(S\) counts all stable perfect matchings for the same strict preference profile. The theorem is a finite exact statement for the three-by-three market and does not assert an asymptotic law.

## Proof
There are \(6^6=46656\) labeled strict preference profiles. The proof is an exhaustive finite classification, with independent internal consistency checks.

For each profile, a sequential men-proposing Gale–Shapley implementation records every proposal. A second implementation processes all currently free men simultaneously in rounds, with women retaining their most-preferred proposal so far. The two implementations are required to return the same men-optimal matching and the same total number of proposals on every profile.

For each man, the set of women he proposes to is exactly the initial segment of his list ending at his men-optimal partner. Thus if his final partner has rank \(r_i\), he has made exactly \(r_i\) proposals. Therefore
\[
P=r_1+r_2+r_3.
\]
The exhaustive rank-multiset census gives counts
\[
10368,
15552,
7776,
6480,
5184,
648,
648
\]
for
\[
(1,1,1),
(1,1,2),
(1,1,3),
(1,2,2),
(1,2,3),
(2,2,2),
(2,2,3),
\]
respectively. Summing by rank gives proposal-count frequencies
\[
10368,
15552,
14256,
5832,
648
\]
for \(P=3,4,5,6,7\). Division by \(46656\) gives the stated probabilities. Exact fraction arithmetic then yields
\[
\mathbb E[P]=\frac{35}{8}
\]
and
\[
\operatorname{Var}(P)=\frac{583}{576}.
\]

Independently, all six perfect matchings are tested for stability at every preference profile. This gives marginal stable-matching counts
\[
34080,
11484,
1092
\]
for \(S=1,2,3\), matching the published three-by-three profile census. Intersecting those stable-count classes with the proposal-count classes yields the displayed joint table and therefore the conditional means and cutoff consequences.

## Verification
The embedded `verify_gs3_proposals.py` uses only exact integer and rational arithmetic from the Python standard library.

It verifies:
- all \(46656\) labeled strict preference profiles;
- exact agreement of sequential and simultaneous Gale–Shapley implementations;
- proposal count equals the sum of men-optimal partner ranks profile by profile;
- proposal frequencies \(10368,15552,14256,5832,648\) for \(P=3,4,5,6,7\);
- no eight- or nine-proposal profile;
- the seven stated rank-multiset counts;
- exact mean \(35/8\) and variance \(583/576\);
- exact stable-matching multiplicities by brute-force checking of all six perfect matchings;
- the full proposal-count by stable-count table;
- all three conditional proposal means.

Replay with:

`python3 verify_gs3_proposals.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Wilson's classical analysis made the number of Gale–Shapley proposals a central running-time statistic for random stable marriage. Later work records the familiar asymptotic picture: worst-case quadratic behavior, but average order \(n\log n\) under independent uniform random preferences.

For exact finite enumeration, Borodin and coauthors study numerous stable-marriage profile sequences. Their one-round sequence gives \(10368\) profiles at \(n=3\), exactly the \(P=3\) atom above. The same paper also tabulates the numbers of three-by-three profiles having one, two, or three stable matchings as \(34080,11484,1092\); these are used here as an external marginal cross-check.

The complete proposal-count distribution beyond the one-round atom, the sharp seven-proposal support endpoint, the full men-optimal partner-rank law, and the joint proposal-count/stable-multiplicity table were not found in the inspected literature or targeted exact-number searches.

## Limitations
The theorem concerns only three men and three women under independent uniform strict preferences. It does not claim that the finite distribution shape, the seven-proposal bound, or the conditional relation with stable-matching multiplicity persists for larger markets.

The one-round atom and the stable-matching-count marginals are prior results and are not claimed as new. Their role is to anchor and independently cross-check the new joint census.

The literature search cannot exclude an unindexed exercise, thesis, supplementary table, or software enumeration containing the same exact proposal law.

## References
1. L. B. Wilson, “An Analysis of the Stable Marriage Assignment Algorithm,” *BIT Numerical Mathematics* 12 (1972), 569–575. DOI: 10.1007/BF01932966.
2. Y. A. Gonczarowski, N. Nisan, R. Ostrovsky, and W. Rosenbaum, “A Stable Marriage Requires Communication,” arXiv:1405.7709, first submitted 29 May 2014.
3. M. Borodin, A. Duncan, B. Litchev, J. Liu, V. Moroz, M. Qian, R. Raghavan, G. Rastogi, M. Voigt, and T. Khovanova, “Sequences of the Stable Matching Problem,” *Journal of Integer Sequences* 27 (2024), Article 24.2.2.
4. OEIS Foundation Inc., OEIS A343475, one-round men-proposing Gale–Shapley preference profiles.
