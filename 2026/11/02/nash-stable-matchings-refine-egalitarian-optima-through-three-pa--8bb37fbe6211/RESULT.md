# Strict rank-sum ordering of Nash products in stable marriage through three pairs

## Finding

In a balanced stable-marriage instance with complete strict preferences and \(n\) agents on each side, let \(r_a(M)\) be agent \(a\)'s zero-based partner rank under the perfect matching \(M\). Define the egalitarian rank sum and positive rank-induced Nash product by
\[
E(M)=\sum_{a=1}^{2n}r_a(M),\qquad P(M)=\prod_{a=1}^{2n}(n-r_a(M)).
\]
For \(1\le n\le 3\), **every pair** of stable matchings satisfies
\[
E(M)<E(N)\quad\Longrightarrow\quad P(M)>P(N).
\]
This compares even stable matchings that optimize neither objective. At \(n=3\), the 46,656 labeled profiles contain 14,760 unordered stable-matching pairs. Of those pairs, 8,304 have unequal rank sums, and in each such pair the lower rank sum has strictly larger product. The smallest product difference among these strict comparisons is 6. The remaining 6,456 pairs tie on rank sum; 3,696 of them have different products and 2,760 agree on both scores.

At four pairs a reversal already occurs with **exactly two stable outcomes**. This is the smallest number of stable outcomes in which a reversal can occur. The two solutions in the example below have \((E,P)=(7,4096)\) and \((8,4608)\), respectively.

## Assumptions and scope

Matchings are bijections between the two sides. A matching is stable if no unmatched pair both strictly prefer each other to their assigned partners. All \(2n\) agents enter both scores once, and the geometric mean has the same order as \(P\). The result concerns the particular utilities \(n-r\), not arbitrary cardinal utilities consistent with the preferences. It imposes no product equality when rank sums tie.

## Proof

For each \(n=1,2,3\), form every ordered tuple of \(2n\) preference permutations of the opposite-side labels. For each of these \((n!)^{2n}\) tuples, form all \(n!\) bijections. A bijection passes the stability test precisely when the set of edges that a first-side agent would prefer to their assigned edge has empty intersection with the set of edges that a second-side agent would prefer to their assigned edge. These sets consist exactly of the corresponding strict preference prefixes. For every bijection that passes, compute its integer \(E\) and \(P\). Sort each unordered pair of such matchings by \(E\); if its costs differ, compute the product difference in that order. This finite procedure uses every possible input and every candidate stable pair, without any symmetry assumption.

At \(n=1\) the single profile has a single stable matching. At \(n=2\), fourteen profiles have one stable matching and two have two; both comparisons tie on both objectives. At \(n=3\), 34,080 profiles have one stable matching, 11,484 have two and 1,092 have three, giving \(11{,}484+3(1{,}092)=14{,}760\) stable pairs. The exact strict-cost comparisons are:

| Lower \(E\) | Higher \(E\) | Pairs | Minimum \(P_{\rm lower\ cost}-P_{\rm higher\ cost}\) |
|---:|---:|---:|---:|
| 2 | 3 | 288 | 162 |
| 2 | 4 | 144 | 243 |
| 3 | 4 | 1656 | 54 |
| 3 | 5 | 504 | 108 |
| 3 | 6 | 24 | 189 |
| 4 | 5 | 3096 | 9 |
| 4 | 6 | 648 | 45 |
| 5 | 6 | 1944 | 6 |

All gaps are positive, which proves the assertion by exhaustive finite computation. In particular it gives a stronger statement than the known inclusion of optimizer sets: a stable matching with nonminimal \(E\) loses to *every* stable matching with lower \(E\), whether or not either is an optimizer.

For the reversal, preferences are listed in decreasing order:

| Agent | Preferences |
|:---|:---|
| Man 0 | 1, 3, 2, 0 |
| Man 1 | 2, 0, 1, 3 |
| Man 2 | 1, 0, 3, 2 |
| Man 3 | 0, 3, 2, 1 |
| Woman 0 | 3, 1, 0, 2 |
| Woman 1 | 3, 1, 0, 2 |
| Woman 2 | 3, 0, 2, 1 |
| Woman 3 | 2, 3, 1, 0 |

Man 3 and woman 0 are mutual first choices and must be paired. Man 2 cannot be paired with woman 2, since woman 3 would then form a blocking pair with him. He cannot be paired with woman 1, since man 0 would then prefer woman 1 to his partner and she prefers man 0 to man 2. Thus man 2 must pair with woman 3. Both bijections of the remaining men 0 and 1 to women 1 and 2 pass the blocking-pair test. Writing the partner labels in men's order, the complete stable set and scores are therefore:

| Matching | Ranks (men, then women) | \(E\) | \(P\) |
|:---|:---|---:|---:|
| `(1,2,3,0)` | `(0,0,2,0,0,2,3,0)` | 7 | 4096 |
| `(2,1,3,0)` | `(2,2,2,0,0,1,1,0)` | 8 | 4608 |

The scores strictly reverse, and no other stable outcome is needed to produce the reversal.

## Reproducibility

Run the accompanying standard-library script `python3 verify_nash_egalitarian_boundary.py`. It enumerates the complete finite domain, tests blocking pairs both by rank comparisons and by preference prefixes, checks the product inequality for every unequal-cost stable pair, and prints the strict comparison strata. It also verifies both stable outcomes of the four-pair witness over all 24 bijections. The success marker is `VERIFY_OK exact_profiles_3=46656 pairwise_stable_comparisons_3=14760`. The script also reproduces the known optimizer-set census as a consistency check rather than a new claim.

## Relationship to prior work and limitations

The earlier record [*Four pairs are the sharp separation threshold for Nash-welfare and egalitarian stable matching*](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-four-pairs-are-the-sharp-separation-threshold-for-nash-welfare-a--6a4f1b95ac69/RESULT.md) already proves optimizer-set inclusion through three pairs, gives the 43,728 equality and 2,928 proper-containment counts at three pairs, and shows a reversal at four pairs with four stable outcomes. Inclusion constrains the global maximizers but does not settle the product order of all distinct-cost stable pairs. Its accompanying checker tests the optimizer sets, not the strict order for every pair. The present claim is the all-pairs order with its exact comparison strata, together with a two-outcome witness at the known boundary size. It does not claim the optimizer-set counts or the existence of a four-pair reversal as new.

Desai, Rasheed, Ghalme and Gujar, [*Fair Stable Matching: A Nash Social Welfare Approach*](https://arxiv.org/abs/2609.02354), use these rank utilities and study Nash optimization and empirical comparisons with other stable-matching objectives. Results about minimizing the worst rank or lexicographically maximizing a rank profile compare different objectives and do not give the rank-sum/product pairwise implication. This exact finite classification does not extend to arbitrary market sizes, ties, incomplete lists, or alternative utility scales. Historical priority beyond the inspected comparisons is not established.
