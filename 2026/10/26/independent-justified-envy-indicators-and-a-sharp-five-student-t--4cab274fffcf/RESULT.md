# Independent justified-envy indicators and a sharp five-student tail reversal

## Finding
Fix a square, one-seat school-choice market with \(n\ge1\) students, \(n\) schools, **one fixed strict priority ranking shared by all schools**, and an arbitrary fixed serial-dictatorship order \(\pi=(\pi_1,\ldots,\pi_n)\). Independently for each student, draw a uniformly random strict ranking of the schools; every school is acceptable. Let \(I_t\) indicate that the student at position \(t\) justifiably envies at least one other student's assignment. Let \(r_t=\#\{j<t:\pi_t\text{ has higher common priority than }\pi_j\}\) and \(k_t=n-t+1\). Then the **entire vector** \((I_1,\ldots,I_n)\) consists of independent Bernoulli variables with
\[
\Pr(I_t=1)=\frac{r_t}{k_t+r_t}.
\]
Thus the number \(Z=\sum_t I_t\) of students with justified envy has the exact probability-generating function
\[
\mathbb E[z^Z]=\prod_{t=1}^n\frac{k_t+r_tz}{k_t+r_t},
\qquad
\Pr(Z=0)=\prod_{t=1}^n\frac{k_t}{k_t+r_t}.
\]

Swapping two adjacent students who are **out of common-priority order** so that the higher-priority student goes first strictly increases the chance that **nobody** experiences justified envy. For \(n\le4\), every such swap also weakly reduces the full count \(Z\) in first-order stochastic dominance. The latter assertion is **sharp**: with five students, a priority-improving adjacent swap can increase the probability that **two students** experience justified envy, even while decreasing the probability that **at least one** does.

## Assumptions and scope
Students are labeled \(1,\ldots,n\) in decreasing common priority, with \(1\) highest. Each student draws an independent uniformly random permutation of the \(n\) distinguishable schools. The serial order is specified ex ante, independently of the random preferences, and schools have exactly one seat. All schools are acceptable. A student \(a\) has justified envy if there is a student \(b\) assigned to school \(s\) such that \(a\) prefers \(s\) to her own school and \(a\) has higher common priority than \(b\). In this mechanism a later assignee is never envied by an earlier assignee: an earlier student selected her favorite among all schools then available.

Here stochastic dominance of the count means \(\Pr(Z_{\mathrm{after}}\ge j)\le\Pr(Z_{\mathrm{before}}\ge j)\) for every integer \(j\). The independence result refers to indicators of **having at least one justified-envy claim**, not to indicators of different blocking pairs made by the same student. No independence is asserted for correlated student preferences or school-specific priorities.

## Proof
**1. Conditional probability and joint independence.** At stage \(t\), condition on the complete history of previous preferences and school selections. Exactly \(k_t=n-t+1\) schools remain, and exactly \(r_t\) earlier-assigned schools belong to students who have lower priority than \(\pi_t\). The student at stage \(t\) takes her favorite among the \(k_t\) remaining schools. She has justified envy precisely when the most preferred school in the union of those \(k_t\) schools and the \(r_t\) previously assigned lower-priority schools is one of the latter. Because her preference permutation is independent and uniform, this happens with the history-independent probability \(r_t/(k_t+r_t)\). Therefore \(\Pr(I_t=1\mid\mathcal F_{t-1})=r_t/(k_t+r_t)\), where \(\mathcal F_{t-1}\) contains all previous full rankings and assignments. Repeated conditional expectation shows that for every choice of \(\varepsilon_t\in\{0,1\}\),
\[
\Pr(I_1=\varepsilon_1,\ldots,I_n=\varepsilon_n)
=\prod_{t:\varepsilon_t=1}\frac{r_t}{k_t+r_t}
\prod_{t:\varepsilon_t=0}\frac{k_t}{k_t+r_t}.
\]
This proves genuine joint independence and the generating function.

**2. Adjacent priority correction.** At positions \(t,t+1\), suppose a lower-priority student \(a\) is immediately before a higher-priority student \(b\). Let \(r\) be the number of students among positions \(1,\ldots,t-1\) below \(a\) in common priority, and let \(s\) be the number below \(b\); necessarily \(0\le r\le s\le t-1\). Put \(k=n-t+1\ge2\). The two independent Bernoulli success parameters before correction are
\[
\left(\frac{r}{k+r},\frac{s+1}{k+s}\right),
\]
and after placing \(b\) before \(a\), they are
\[
\left(\frac{s}{k+s},\frac{r}{k-1+r}\right).
\]
Every other parameter is unchanged, since earlier prefixes and later sets of preceding students are unchanged. The difference, after minus before, in the probability that neither of the two is envious is
\[
\frac{k(k-1)}{(k+s)(k-1+r)(k+r)}>0.
\]
Since the unaffected indicators are jointly independent of the changed pair, the probability that **no student at all** is envious strictly increases.

The difference, after minus before, in the probability that **both** changed positions are envious is
\[
\Delta_2=\frac{r\,[s-(k-1+r)]}{(k+s)(k+r)(k-1+r)}.
\]
For a pair of Bernoulli variables, stochastic dominance of its sum is characterized by tail thresholds \(1\) and \(2\). Threshold \(1\) improves strictly by the preceding no-envy calculation. Threshold \(2\) is nonincreasing if \(r=0\) or \(s\le k-1+r\). With \(n\le4\), the opposite strict inequality cannot hold: \(r\ge1\), \(s\le t-1\), \(k=n-t+1\) and \(t\le n-1\) would imply \(n\ge5\). Therefore the two-position count improves in stochastic order for \(n\le4\). Adding the independent unchanged count preserves stochastic order, proving the stated universal boundary.

**3. Sharp five-student obstruction.** Give students priority \(1\succ2\succ3\succ4\succ5\), and compare serial orders
\[
\pi=(2,3,5,4,1),\qquad\pi'=(2,3,5,1,4).
\]
The swap in the last two positions correctly moves student \(1\) ahead of student \(4\). All first three envy indicators vanish under both orders. The final two Bernoulli parameters are \((1/3,4/5)\) before and \((3/5,1/2)\) after. Hence
\[
\Pr_\pi(Z\ge1)=\frac{13}{15},\quad
\Pr_{\pi'}(Z\ge1)=\frac45;
\qquad
\Pr_\pi(Z\ge2)=\frac4{15},\quad
\Pr_{\pi'}(Z\ge2)=\frac3{10}.
\]
The chance of at least one justified-envy claimant decreases by \(1/15\), while the chance of two such claimants **increases by \(1/30\)**. This shows that a priority correction need not stochastically reduce total justified envy at \(n=5\), and the preceding argument shows that five is the smallest possible market size for this phenomenon.

## Verification
The accompanying standalone Python checker constructs all preference rankings at each stage, evaluates the original strict justified-envy definition, and propagates exact integer counts through the sequential allocation. It does **not** assume the Bernoulli formula in its definition-level calculation. For all common-priority serial orders with \(n=1,2,3,4\) it matches every joint zero-one envy pattern against the theorem; it also checks all \(43\) priority-correcting adjacent swaps in these sizes at every upper-tail threshold. It independently verifies both five-student witness orders, giving exactly \(4/15\) versus \(3/10\) for the two-claimant tail. Run from this package with `python3 check.py`; only the Python standard library is required. These finite checks complement the general argument and do not prove the all-size statement by themselves.

## Relationship to prior work
Hamdan, *Making Serial Dictatorships Fair* (initial public arXiv version dated March 5, 2026), minimizes the **expected number of justified-envy cases or blocking triples**, deriving Kemeny and weighted-Kemeny connections; its baseline assumes a **single identical realized preference ranking** across students. Its separate independent-preference analysis gives weights for pairwise cases, not the full distribution of **numbers of students** with justified envy under a fixed common priority order. The present result uses independent student preferences, gives independent student-level indicators and their joint law, and identifies an unexpected five-student tail reversal under an adjacent priority improvement.

Abdulkadiroğlu, Che, Pathak, Roth and Tercieux (2020) compare justified-envy inclusion and mean performance of mechanisms, including serial dictatorship under randomly drawn priorities. Ortega and Klein (2023) calculate expected fractions of students with justified envy in a model with random school priorities, which differs from the fixed shared-priority model here. Neither those mean statements nor pairwise-Kemeny weighting entails the stated product law or the high-tail reversal. The claims are confined to the model described above; mathematical equivalences in unindexed work remain possible.

## Limitations
The law requires independent **uniform** full rankings and a deterministic ex ante serial order. Under correlated preferences or differing school priorities, the conditional Bernoulli success probability can depend on the previous assignments and the factorization may fail. The tail-reversal comparison concerns the **count of students with at least one** justified envy claim, not the number of blocking pairs. The five-student example does not imply priority corrections increase all fairness risks; the chance of any justified envy always falls under the theorem's hypotheses. This mathematical result has not received an independent scientific audit.

## References
1. A. Hamdan, *Making Serial Dictatorships Fair*, arXiv:2603.05660 (v1, March 5, 2026; v2 June 2026), https://arxiv.org/abs/2603.05660 .
2. A. Abdulkadiroğlu, Y.-K. Che, P. A. Pathak, A. E. Roth and O. Tercieux, *Efficiency, Justified Envy, and Incentives in Priority-Based Matching*, *American Economic Review: Insights* **2** (2020), 425–442, https://doi.org/10.1257/aeri.20190307 .
3. J. Ortega and T. Klein, *The Cost of Strategy-Proofness in School Choice*, *Games and Economic Behavior* **141** (2023), 515–528, arXiv:2204.07255, https://arxiv.org/abs/2204.07255 .
