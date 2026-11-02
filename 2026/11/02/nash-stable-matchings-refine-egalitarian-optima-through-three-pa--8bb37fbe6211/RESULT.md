# Nash stable matchings refine egalitarian optima through three pairs, with a sharp four-pair reversal

## Finding

Let \(I\) be a classical balanced stable-marriage instance with \(n\) agents on each side, complete strict preference lists, and perfect matchings. Give each agent whose assigned partner has zero-based rank \(r_a(M)\) the positive Borda-type utility \(n-r_a(M)\). For each stable matching \(M\), define the egalitarian rank cost and Nash product by
\[
E(M)=\sum_{a=1}^{2n}r_a(M),\qquad P(M)=\prod_{a=1}^{2n}(n-r_a(M)).
\]

**Complete three-pair ordering theorem.** For every such instance with \(1\le n\le3\), and every pair of stable matchings \(M,N\),
\[
E(M)<E(N)\quad\Longrightarrow\quad P(M)>P(N).
\]
Consequently every Nash-product-maximizing stable matching minimizes egalitarian rank cost. Writing \(\mathcal N(I)=\arg\max_{M\ \mathrm{stable}}P(M)\) and \(\mathcal E(I)=\arg\min_{M\ \mathrm{stable}}E(M)\),
\[
\mathcal N(I)\subseteq\mathcal E(I)\qquad(1\le n\le3).
\]

For the \((3!)^6=46{,}656\) labeled complete strict three-pair profiles, precisely \(43{,}728\) have \(\mathcal N(I)=\mathcal E(I)\), while precisely \(2{,}928\) have strict containment \(\mathcal N(I)\subsetneq\mathcal E(I)\). No other relation occurs. All sixteen two-pair profiles give equality.

**Sharpness.** At four pairs the order can reverse, and Nash and egalitarian objectives can have disjoint unique stable optimizers. An explicit four-pair instance with exactly two stable matchings is given below, with a lower-cost solution of Nash product \(4096\) and a higher-cost solution of Nash product \(4608\).

## Assumptions and scope

There are exactly \(n\) men and \(n\) women. All agents rank all agents on the other side strictly. The matchings are bijections, and stability means that no unmatched man-woman pair both strictly prefer one another to their partners. Each participant contributes once to both objectives. Ranks start at zero, so first-choice utility is \(n\), last-choice utility is \(1\), and \(P(M)>0\). The Nash geometric mean has the same maximizers as the product \(P\).

All ties in the objectives are preserved in their complete optimizer sets. The theorem does *not* assert that all egalitarian minimizers are Nash maximizers; this fails for \(2{,}928\) of the three-pair profiles. The implication in the theorem concerns pairs with *strictly unequal* rank sums, and does not claim equality of Nash scores when rank sums tie.

## Proof

**Step 1: An exhaustive finite proof for all markets of size at most three.** For each \(n\in\{1,2,3\}\), the checker enumerates every tuple of \(2n\) strict preference lists. Each list is one of \(n!\) permutations, so this covers exactly \((n!)^{2n}\) labeled profiles, without sampling or symmetry assumptions. For every profile, it enumerates every one of the \(n!\) perfect matchings and tests all potential blocking man-woman pairs. Two independently written stability tests, one using integer rank tables and one using explicit preference prefixes, agree on every candidate matching.

For each resulting stable matching, the checker computes all \(2n\) partner ranks, the *exact integer* sum \(E\), and the *exact integer* product \(P\). It tests the strict inequality \(E(M)<E(N)\implies P(M)>P(N)\) for every unordered pair of distinct stable matchings, and computes the *full* argmin and argmax sets without tie breaking. Thus no unexamined profile or potential stable matching remains in the finite domain.

At \(n=1\) there is one profile with one stable matching. At \(n=2\) all sixteen profiles have coincident optimizer sets. At \(n=3\), all \(46{,}656\) profiles pass the asserted pairwise implication. The distribution of the number of stable matchings is
\[
\begin{array}{c|rrr}\text{stable matching count}&1&2&3\\\hline\text{profiles}&34080&11484&1092\end{array}.
\]
The complete comparison includes \(14{,}760\) unordered pairs of stable matchings over all profiles, of which \(8{,}304\) have distinct rank sums, \(3{,}696\) tie on rank sums but differ in Nash product, and \(2{,}760\) tie on both objectives.

For additional reproducibility, the complete stratification of the \(8{,}304\) strict-cost comparisons is below. The final column is the *smallest observed positive integer gap* \(P(M_{\mathrm{lower\ cost}})-P(M_{\mathrm{higher\ cost}})\) in the indicated rank-sum cell:

| Lower \(E\) | Higher \(E\) | Pair comparisons | Minimum product gap |
|---:|---:|---:|---:|
| 2 | 3 | 288 | 162 |
| 2 | 4 | 144 | 243 |
| 3 | 4 | 1656 | 54 |
| 3 | 5 | 504 | 108 |
| 3 | 6 | 24 | 189 |
| 4 | 5 | 3096 | 9 |
| 4 | 6 | 648 | 45 |
| 5 | 6 | 1944 | 6 |

Every minimum gap is strictly positive. This exact finite calculation proves the stated implication for all size-at-most-three profiles. Any Nash maximizer outside the egalitarian minimum set would have strictly greater \(E\) than an egalitarian minimizer, hence strictly smaller \(P\), a contradiction. The exact optimum-set counts are \(43{,}728\) equal and \(2{,}928\) proper containment.

**Step 2: Four-pair counterexample.** Label both sides \(0,1,2,3\). In the following table, entries are opposite-side agents listed in decreasing preference order:

| Agent | Strict preference list |
|:---|:---|
| Man 0 | 1, 3, 2, 0 |
| Man 1 | 2, 0, 1, 3 |
| Man 2 | 1, 0, 3, 2 |
| Man 3 | 0, 3, 2, 1 |
| Woman 0 | 3, 1, 0, 2 |
| Woman 1 | 3, 1, 0, 2 |
| Woman 2 | 3, 0, 2, 1 |
| Woman 3 | 2, 3, 1, 0 |

Write a matching as a tuple of women assigned to men \(0,1,2,3\). Exhaustively checking all \(4!=24\) permutations gives exactly two stable matchings:
\[
M_E=(1,2,3,0),\qquad M_P=(2,1,3,0).
\]
Their eight-agent zero-based rank vectors, with men followed by women, are
\[
\begin{aligned}
r(M_E)&=(0,0,2,0,0,2,3,0),\\
r(M_P)&=(2,2,2,0,0,1,1,0).
\end{aligned}
\]
Thus
\[
\begin{array}{c|cc}&E&P\\\hline M_E&7&4096\\ M_P&8&4608\end{array}.
\]
As there are no other stable matchings, \(M_E\) uniquely minimizes \(E\) and \(M_P\) uniquely maximizes \(P\). This proves both strict reversal and the sharp four-pair boundary.

## Verification

Run the standalone Python 3 standard-library checker from the same directory:

`python3 verify_nash_egalitarian_boundary.py`

Successful execution terminates with `VERIFY_OK exact_profiles_3=46656 pairwise_stable_comparisons_3=14760`. It independently evaluates the blocking-pair test in two equivalent ways; tests all matchings for all labeled profiles through three pairs; reconstructs every full optimizer set and strict pairwise comparison; checks the exact profile histogram; and verifies the four-pair witness against all twenty-four perfect matchings. Integer arithmetic is exact throughout, with no floating-point tolerance.

These exhaustive computations constitute a finite proof for the stated finite market-size range. They do not establish the pairwise implication in larger markets, and the provided four-pair instance disproves its extension to all market sizes.

## Relationship to prior work

Desai, Rasheed, Ghalme, and Gujar, *Fair Stable Matching: A Nash Social Welfare Approach* (first publicly posted September 2, 2026), define the same positive rank-induced utilities and prove an algorithmic reduction for Nash-optimal stable marriage. Their manuscript compares Nash and egalitarian fairness empirically and reports polynomial-time algorithms. The present finding is instead an exact structural implication for *all* stable outcomes at sizes at most three, with full optimizer-set counts and a minimal counterexample for the implication at four; that statement is not given in the inspected main text and appendices.

Irving, Leather, and Gusfield established the egalitarian stable-marriage objective and its optimization. Related published small-market results compare egalitarian matchings to minimum-regret matchings, and rank-maximal matchings to egalitarian matchings. Neither comparison substitutes the Nash product for its other objective. In particular, knowing that Nash optimum sets lie within the minimum-regret optimum set and that egalitarian and minimum-regret sets are nested does not imply the present Nash-versus-egalitarian inclusion in profiles where the egalitarian set is a proper subset of the minimum-regret set.

The exhaustive profile count also has a different logical content from the existing small-market classification of rank-maximal versus egalitarian optimum sets, which sometimes have *disjoint* optimizers at three pairs. The present Nash-versus-egalitarian optimum sets never do at that size.

## Limitations

The result is an exact finite-domain theorem through size three and one explicit size-four counterexample. It does not give a general formula for larger stable-marriage markets, heterogeneous cardinal utilities, incomplete lists, ties, or non-bipartite matching. The checker is one reproducible implementation with two independent stability formulations, rather than an externally audited certificate. Publicly available research records and accessible full texts were compared, but an unindexed earlier finite classification could still overlap. No independent scientific audit has been performed.

## References

1. P. Desai, M. Rasheed, G. Ghalme, and S. Gujar, "Fair Stable Matching: A Nash Social Welfare Approach," arXiv:2609.02354v1, first posted September 2, 2026. https://arxiv.org/abs/2609.02354
2. R. W. Irving, P. Leather, and D. Gusfield, "An efficient algorithm for the 'optimal' stable marriage," *Journal of the ACM* 34(3) (1987), 532–543. DOI: 10.1145/28869.28871.
3. "Sharp coincidence boundary for egalitarian and minimum-regret stable marriage," publicly accessible research record with full result: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-coincidence-boundary-for-egalitarian-and-minimum-regret-st--57631882a89b
4. "Sharp three-by-three conflict layer for rank-maximal and egalitarian stable marriage," publicly accessible research record with full result: https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-sharp-three-by-three-conflict-layer-for-rank-maximal-and-egalita--c67e0358daf3
