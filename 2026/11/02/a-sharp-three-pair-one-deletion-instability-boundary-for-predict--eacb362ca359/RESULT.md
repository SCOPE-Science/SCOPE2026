# A sharp three-pair, one-deletion instability boundary for prediction-window deferred acceptance

## Finding

For one-to-one, strict, complete hospital–resident markets with equal sides of size \(n\), consider reciprocal deletion of pairs that retains a full-market perfect stable matching \(\mu\). Run **hospital-proposing** deferred acceptance (DA) on the pruned market, and assess stability against the *original*, complete preferences. The following is sharp.

1. For every \(n\le2\), **any** such pruning leaves the hospital-proposing DA result stable in the original market.
2. For \(n=3\), deleting **one** pair already can yield an unstable output, despite preserving the **unique** original stable matching. The deletion can arise from exact predictions of that matching's hospital-side ranks with a common symmetric window radius of one. Both the number of pairs and market size are minimal under the stated retention assumption.
3. For every \(n\), there is a safe directed boundary: if every deleted pair \((h,r)\) ranks \(r\) **strictly below** \(\mu(h)\) for that hospital, then hospital-proposing DA on the pruned instance returns **exactly the original hospital-optimal stable matching**, even if the retained lists contain noncontiguous gaps.

The smallest instability witness has hospitals' strict lists

\[
\begin{array}{c|c}
H_1 & R_1\succ R_2\succ R_3\\
H_2 & R_2\succ R_1\succ R_3\\
H_3 & R_1\succ R_2\succ R_3
\end{array}
\]

and residents' strict lists

\[
\begin{array}{c|c}
R_1 & H_2\succ H_3\succ H_1\\
R_2 & H_1\succ H_2\succ H_3\\
R_3 & H_1\succ H_2\succ H_3.
\end{array}
\]

The full market's unique stable matching is
\[
\mu=\{(H_1,R_2),(H_2,R_1),(H_3,R_3)\}.
\]
Exact hospital-side predicted ranks \((2,2,3)\), and common radius one, retain every pair except \((H_3,R_1)\). Hospital-proposing DA on the pruned market returns
\[
\nu=\{(H_1,R_1),(H_2,R_2),(H_3,R_3)\},
\]
which is blocked in the full market by the single deleted pair \((H_3,R_1)\).

## Assumptions and scope

Fix two finite sets \(H=\{H_1,\ldots,H_n\}\), \(R=\{R_1,\ldots,R_n\}\) and complete strict orders on the opposite side for each member. Every hospital and resident prefer any partner over remaining unmatched. A matching is stable if no mutually preferred unmatched pair exists. A **reciprocal pruning** chooses retained edges \(E'\subseteq H\times R\) and removes each omitted pair from both agents' lists, without changing remaining relative ranks. A stable perfect reference matching \(\mu\) **survives** if all its edges are in \(E'\). The hospital-proposing DA outcome on this incomplete market is \(\nu\); its stability is tested on the original complete market. Because a perfect stable \(\mu\) survives, rural-hospitals/invariance of matched agents (or the standard DA proposer-optimality theorem) ensures that \(\nu\) is perfect.

For the exact prediction-window construction, the predicted rank for each hospital equals the position of its assigned resident in \(\mu\), and its admissible list contains precisely positions whose absolute deviation from that rank is at most one, clipped to the range \(\{1,\ldots,n\}\). Residents reciprocally delete omitted edges.

## Proof

**Universal safe-deletion direction.** Let \(\sigma\) be the hospital-optimal stable matching of the original market. Since \(\mu\) is originally stable, every hospital weakly prefers its partner in \(\sigma\) to its partner in \(\mu\). The deleted edges are all worse than the hospital's \(\mu\)-partner, so \(\sigma\) also survives. Consequently \(\sigma\) is stable in the pruned market, and hospital-proposing DA there gives every hospital a partner weakly preferred to \(\sigma\). On the other hand, by proposer optimality against the surviving stable matching \(\mu\), each hospital weakly prefers \(\nu(h)\) to \(\mu(h)\). Therefore an omitted pair \((h,r)\), which by assumption ranks strictly below \(\mu(h)\) on \(h\)'s full list, cannot block \(\nu\). Retained pairs do not block by DA stability in the pruned market. Thus \(\nu\) is stable in the original market; original hospital optimality gives \(\sigma\) weakly preferred to \(\nu\) for all hospitals. Together with the reverse inequality, strict lists force \(\nu=\sigma\).

**Two-pair lower bound.** For \(n=1\), the unique edge in the surviving stable reference must be retained. For \(n=2\), \(\nu\) is perfect and each hospital weakly prefers \(\nu(h)\) to its \(\mu\)-partner by hospital-optimality in the pruned market. If \(\nu=\mu\), it is stable in the original market. Otherwise the two hospitals exchange their reference partners. In a strict two-by-two market each hospital then strictly prefers its new \(\nu\)-partner. The *only* unmatched original pairs under \(\nu\) are the two \(\mu\)-edges; neither can block because its hospital prefers its \(\nu\)-partner. Hence \(\nu\) is originally stable. Without any deletion the ordinary DA algorithm is originally stable, so a single deletion is a minimal positive deletion budget.

**Three-pair witness.** For the displayed strict preferences, exhaustive direct comparison of each unmatched hospital–resident pair in each of the six perfect matchings (encoded by the resident indices held by \(H_1,H_2,H_3\)) gives the following explicit blockers:

\[
\begin{array}{c|c}
(1,2,3)&(H_3,R_1)\\
(1,3,2)&(H_2,R_1)\\
(2,1,3)&\text{none}\\
(2,3,1)&(H_2,R_1)\\
(3,1,2)&(H_1,R_2)\\
(3,2,1)&(H_1,R_2).
\end{array}
\]

Hence \(\mu=(2,1,3)\) is the unique original stable matching. Its hospital ranks are \((2,2,3)\); radius one retains positions \(1,2,3\) for \(H_1\), positions \(1,2,3\) for \(H_2\), and positions \(2,3\) for \(H_3\). Exactly \((H_3,R_1)\) is deleted. Hospital-proposing DA then has \(H_1\) propose to \(R_1\), \(H_2\) to \(R_2\), and \(H_3\) to \(R_2\), which rejects \(H_3\) for \(H_2\); \(H_3\) next proposes to \(R_3\). Thus DA produces \(\nu=(1,2,3)\). Since \(H_3\) strictly prefers \(R_1\) to \(R_3\), and \(R_1\) strictly prefers \(H_3\) to \(H_1\), the omitted edge \((H_3,R_1)\) blocks \(\nu\) in the complete instance. The two-pair bound and zero-deletion case already proved make both cutoffs sharp.

## Verification

Run `python3 verify.py` (Python standard library only). The checker implements true blocking-pair tests and hospital-proposing DA on reciprocally pruned lists. It verifies (a) every reciprocal pruning retaining a reference stable perfect matching across **all** strict markets of size at most two, 290 tested combinations including duplicate edge-mask descriptions; (b) the unique full stable matching, exact rank predictions, one deleted edge, pruned DA output, and blocking pair for the displayed three-pair market; (c) the general safe-deletion statement for **1,531,392** three-pair original-stable-reference/pruning combinations across all \(46,656\) strict labeled profiles of size three. The all-size statements are proven symbolically above; finite tests do not establish them by exhaustion beyond their checked sizes.

## Relationship to prior work

McCauley, Moseley, Niaparast and Singh (2026), Lemma 3.1, already prove the **qualitative instability** of hospital-proposing DA under exact-rank prediction windows, using a four-by-four example; this is explicitly prior knowledge, not new. Their Theorem 3.4 instead proves stability for **resident-proposing** DA when a stable benchmark survives, and Section 4 treats **prefix** truncation. The present contribution isolates the jointly sharp **three-by-three market, one removed edge, common-radius-one exact window**, together with the two-by-two universal impossibility and a hospital-side safe-deletion direction for arbitrary noncontiguous retained edges. The earlier full-prefix preservation observation is not claimed as new. The standard DA optimality and rural-hospitals results are used as classical facts rather than new theorems.

Agarwal and Cole (2023) study short proposal lists under correlated random utility assumptions and asymptotic high-probability guarantees; these do not imply a deterministic all-profile minimum-size boundary for exact predicted rank windows.

## Limitations

This is a strict, balanced, one-to-one model with reciprocal removals, an originally stable matching retained by pruning, and hospital-proposing DA. It does not cover capacities, ties, incomplete original preferences, predictions with nonzero error, or unilateral removals. Its three-by-three witness is not a claim of a new *qualitative* vulnerability, which is established in the motivating paper. Full originality beyond the inspected and searched literature has not been independently certified; unindexed exact small counterexamples remain possible.

## References

- Samuel McCauley, Benjamin Moseley, Helia Niaparast, and Shikha Singh. *Stable Matching with Predictions: Robustness and Efficiency under Pruned Preferences*, arXiv:2602.02254v1 (first public 2026-02-02), Lemma 3.1, Theorem 3.4, Section 4. https://arxiv.org/html/2602.02254v1
- Ishan Agarwal and Richard Cole. *Stable Matching: Choosing Which Proposals to Make*, ICALP 2023, DOI:10.4230/LIPIcs.ICALP.2023.8. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2023.8
- David Gale and Lloyd S. Shapley. *College Admissions and the Stability of Marriage*, American Mathematical Monthly 69 (1962), 9–15 (classical DA stability and proposer optimality).
