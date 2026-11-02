# Exact four-school justified-envy distribution for optimally ordered serial dictatorship

## Finding
In the four-student, four-unit-school model defined below, let \(\pi=(\pi_1,\ldots,\pi_4)\in S_4^4\) be the school-priority profile, and let
\[
 K(\pi)=\min_{\rho\in S_4}\sum_{s=1}^{4}\operatorname{KT}(\rho,\pi_s),\qquad
 M(\pi)=\left|\operatorname*{argmin}_{\rho\in S_4}\sum_{s=1}^{4}\operatorname{KT}(\rho,\pi_s)\right|.
\]
Under four independently uniform school priorities, the complete exact distribution of \(K\) (a denominator of \(24^4=331{,}776\) equally likely profiles) is:

| Minimum total Kendall distance \(K\) | Number of priority profiles |
|---:|---:|
| 0 | 24 |
| 1 | 288 |
| 2 | 1,560 |
| 3 | 5,472 |
| 4 | 14,232 |
| 5 | 28,800 |
| 6 | 46,896 |
| 7 | 62,208 |
| 8 | 66,744 |
| 9 | 56,160 |
| 10 | 34,056 |
| 11 | 12,960 |
| 12 | 2,376 |

The exact distribution of the number \(M\) of optimal serial orders is:

| Number \(M\) of optimal serial orders | Number of priority profiles |
|---:|---:|
| 1 | 51,192 |
| 2 | 74,232 |
| 3 | 74,592 |
| 4 | 37,224 |
| 5 | 25,200 |
| 6 | 26,136 |
| 8 | 26,784 |
| 12 | 14,040 |
| 24 | 2,376 |

For each fixed priority profile, the minimal expected number of justified-envy cases over the common random student preference equals \(K(\pi)/4\). Consequently, averaging also over school priorities,
\[
\mathbb E_{\pi}\left[\min_{\rho}\mathbb E_{P}[\mathrm{JE}(\rho,P,\pi)\mid\pi]\right]=\frac{8641}{4608}.
\]
A uniformly random serial order has expected justified envy exactly \(3\) for **each** fixed priority profile. Hence optimizing the order reduces the doubly averaged expectation by exactly \(5183/4608\), approximately \(37.49\%\) of the random-order baseline.

A structural characterization explains the no-improvement atom: \(K(\pi)=12\), equivalently all \(24\) serial orders have the same expected justified envy, if and only if **every unordered pair of students is ordered in opposite directions by exactly two schools each**. This happens for exactly \(2{,}376\) of the \(331{,}776\) labeled school-priority profiles, probability \(11/1536\). Exactly \(51{,}192\) profiles have a unique optimal serial order (probability \(79/512\)).

## Assumptions and scope
There are exactly four distinct students and four distinct schools, each with one seat. Every school has a complete, strict priority permutation over students; the four priority permutations are independent and uniformly distributed on \(S_4\). Independently, all four students have the same complete, strict school preference, drawn uniformly from the \(24\) possible school orders. The serial dictatorship mechanism chooses a fixed student order \(\rho\) from the priority profile alone, before this common preference is revealed. At their turn, students choose their best remaining school. Justified envy is counted by ordered student-school blocking cases: a later student who prefers an earlier student's assigned school and has higher priority there contributes one case. These cases coincide with the pairwise justified-envy incidences because all assigned schools are distinct. The choice among multiple optimizing serial orders is arbitrary, since they have the same conditional expected count. The result measures the expectation over the unknown common preference, then over independent school priorities.

For permutations \(\rho,\sigma\in S_4\), \(\operatorname{KT}(\rho,\sigma)\) is the number of unordered student pairs ranked in opposite orders. All distributions, probabilities, and counts refer to **ordered school-priority profiles**; no quotient by student or school relabeling is taken.

## Proof
**Step 1: mechanism-to-distance identity.** Fix a priority profile and a serial order \(\rho=(\rho(1),\ldots,\rho(4))\). Under a common strict preference, student \(\rho(t)\) receives the school in position \(t\) of that preference. Every later student \(\rho(u)\), for \(u>t\), strictly prefers the school of \(\rho(t)\) to their own. This envy is justified exactly when school \(s(t)\) ranks \(\rho(u)\) ahead of \(\rho(t)\). As the common preference is uniformly random, \(s(t)\) is uniformly distributed among the four schools for every \(t\). By linearity of expectation, the expected number of justified-envy cases is
\[
\mathbb E_{P}[\mathrm{JE}(\rho,P,\pi)\mid\pi]
=\frac14\sum_{s=1}^{4}\sum_{t<u}
\mathbf 1\{\rho(u)\text{ precedes }\rho(t)\text{ in }\pi_s\}
=\frac14\sum_{s=1}^{4}\operatorname{KT}(\rho,\pi_s).
\]
This proves that Kemeny-minimizing serial orders attain conditional expected justified envy \(K(\pi)/4\). The identity and its general form are established in Hamdan's Theorem 1 [1]; the following finite distribution is computed separately here.

**Step 2: exact finite census.** Enumerate the \(24\) permutations of four labels in lexicographic order, with indices \(0,\ldots,23\). For each ordered pair of permutations, compute the Kendall distance by checking all \(\binom42=6\) unordered student pairs. Enumerate **all** \(24^4\) ordered quadruples of school permutations and, for each quadruple, evaluate the sum of the four precomputed distances for **each** of the \(24\) candidate serial orders. Increment the histogram of the least total distance \(K\) and the histogram of how many candidate orders attain it. The complete loops, integer comparisons, and expected vectors appear in `verify_kemeny.cpp`. Their asserted counts total \(331{,}776\) in each histogram, and their weighted sum is
\[
\sum_{\pi\in S_4^4}K(\pi)=2{,}488{,}608.
\]
This is a finite proof by exhaustive case analysis: the code enumerates the complete finite domain, not a sample. A separate pairwise-margin implementation in `verify_pairwise.py` recomputes each objective from all six school-majority counts and matches both histograms.

**Step 3: exact expectation and random-order comparison.** Division by \(4\cdot 24^4\) gives \(\mathbb E[K/4]=8641/4608\). For any fixed four-school priority profile, a uniformly random serial order reverses each unordered student pair against a fixed school priority with probability \(1/2\); there are six pairs and four schools. Therefore its expected total Kendall distance is \(4\cdot6/2=12\), and its expected justified envy is \(12/4=3\). The difference is \(3-8641/4608=5183/4608\).

**Step 4: characterization of no improvement.** For every fixed priority profile, averaging the total Kendall distance over all \(24\) serial orders gives \(12\), so \(K\le12\). If \(K=12\), all \(24\) serial orders must have score \(12\). Given any pair of students, choose a serial order where they are adjacent, then swap them; the only changed pairwise contribution is theirs. Equality of all scores forces precisely two school rankings in each direction. Conversely, if every student pair splits two schools to two, each of the six unordered pairs contributes exactly two to every total Kendall score, making all scores \(12\). The exhaustive census gives \(2{,}376\) such profiles; the alternative characterization provides a direct structural explanation of the atom. The same census gives \(51{,}192\) profiles with \(M=1\).

## Verification
Compile and run `verify_kemeny.cpp` with a conforming C++17 compiler using `c++ -O2 -std=c++17 verify_kemeny.cpp -o verify_kemeny && ./verify_kemeny`. The program enumerates \(331{,}776\) profiles, asserts the full score and optimizer-multiplicity histograms, and checks the exact score sum. Independently run `python verify_pairwise.py` with Python 3 and NumPy; this implementation uses school pairwise margins instead of a Kendall distance matrix, asserts both histograms and repeats a direct expected justified-envy check over \(24\) common preferences for one nontrivial priority profile. Both were executed successfully on the embedded source content. The finite exhaustiveness follows from the loops' explicitly bounded permutation domains; the analytical identities and the all-tied structural lemma are proved above, not inferred from numerical tests.

## Relationship to prior work
Hamdan [1] proves the general rank-aggregation reduction for priority-aware serial dictatorship under a uniformly random common preference. That theorem **covers the optimization principle** used here; no novelty is claimed for the Kemeny mechanism or its fairness identity. This result supplies new finite quantitative information not stated in the inspected theorem or discussion: the complete four-school optimal-risk histogram, optimizer-set multiplicities, an exact mean and improvement over random priority, and the structural no-improvement equivalence. Clémençon and Irurozki [2] study Kemeny medians and consensus ranking distributions in a broader statistical framework, but the inspected definitions, algorithmic and numerical sections do not give these four-priority exact distributions. The general Kemeny median algorithms and pairwise-margin representation can compute the answer but do not alone imply the enumerated numerical values without further calculation.

## Limitations
The population and school count are fixed at four, preferences are identical and uniformly random, and school priority orders are independent uniform strict permutations. No claim is made for empirical school-priority correlations, non-identical preferences, unequal capacities, or arbitrary market sizes. The fairness measure is the **expected count** of justified-envy cases, not zero envy for every realized preference profile. An earlier unindexed exact census of four-permutation Kemeny medians would overlap with the numerical core; the literature search cannot rule out that possibility. No independent external audit or publication is asserted.

## References
[1] Adam Hamdan, *Making Serial Dictatorships Fair*, arXiv:2603.05660 (first public version March 5, 2026), Theorem 1 and Section 5. https://arxiv.org/abs/2603.05660 ; full inspected text: https://arxiv.org/html/2603.05660v2 .

[2] Stephan Clémençon and Ekhine Irurozki, *Beyond Kemeny Medians: Consensus Ranking Distributions Definition, Properties and Statistical Learning*, arXiv:2602.10640 (February 11, 2026), Sections 2 and 4 and numerical appendix. https://arxiv.org/html/2602.10640v1 .
