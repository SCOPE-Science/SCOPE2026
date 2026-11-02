# The three-to-four size threshold for exact online maximin fairness under itemwise upgrades

## Finding
Consider two agents who share the **same strictly positive additive valuation** for goods arriving one at a time. Each good has value either \(1\) or a fixed integer \(r\ge 2\). After each arrival, a complete allocation must attain **exact maximin share** (MMS) for each agent, while every previously held good must either remain with its owner or be replaced for that owner by a *distinct* good of at least equal value. No arrival horizon or future values are known.

A deterministic online algorithm satisfying both requirements on **every finite arrival sequence and every prefix** exists **if and only if \(r\in\{2,3\}\)**. For these two ratios the construction is constant-time per arrival with suitable bundle lists, and reassigns at most one previously allocated unit good per arrival. Its allocations are also EFX and Pareto optimal. For every integer \(r\ge4\), the fixed five-good arrival sequence \((1,1,1,1,r)\) makes simultaneous prefixwise exact MMS and itemwise upgrades impossible, even with advance knowledge of the sequence.

## Assumptions and scope
Fix \(r\in\mathbb Z\) with \(r\ge2\). Exactly two labeled agents have an identical additive valuation \(v(S)=\sum_{g\in S}w_g\) with \(w_g\in\{1,r\}\). Arriving goods must all be allocated, though existing goods may be reassigned at each arrival. If agent \(i\) has old bundle \(X_i\) and new bundle \(Y_i\), the **itemwise upgrade constraint** demands an injection \(\phi_i:X_i\longrightarrow Y_i\) with \(w_{\phi_i(g)}\ge w_g\) for each old good \(g\). The relevant two-agent MMS at each prefix \(G\) is \(\mu(G)=\max_{S\subseteq G}\min\{v(S),v(G\setminus S)\}\). Both allocated bundles must have value at least \(\mu(G)\). With two agents of identical values this is equivalent to attaining the optimal minimum load.

All results quantify over arbitrary finite arrival words over the two sizes and require fairness after each prefix, including when either type has not appeared. Statements here do not address heterogeneous valuations, noninteger ratios, or three or more agents.

## Proof
**Step 1: A canonical exact-MMS partition.** Let \(H\) and \(L\) denote the numbers of value-\(r\) and value-\(1\) goods currently seen. Define the parity-compatible shortfall
\[
\delta_r(L)=\max\{d\in\mathbb Z:0\le d\le\min\{r,L\},\ d\equiv L\pmod 2\}.
\]
When \(H\) is even, split the large goods equally and the unit goods as equally as possible. When \(H\) is odd, one agent has one more large good; put \((L+\delta_r(L))/2\) unit goods with the agent having fewer large goods and \((L-\delta_r(L))/2\) with the other. Both counts are nonnegative integers. The absolute value discrepancy is
\[
D_r(H,L)=\begin{cases}
L\bmod2,&H\text{ even},\\
r-\delta_r(L),&H\text{ odd}.
\end{cases}
\]
This is the **minimum discrepancy across all partitions**. If \(H\) is even, the displayed discrepancy is zero or one, the minimum permitted by parity of total value. If \(H\) is odd and \(L\ge r-1\), the discrepancy is also zero or one and therefore parity-minimal. If \(H\) is odd and \(L<r-1\), every partition gives the two agents an odd difference of at least one in the number of large goods, and even putting all \(L\) unit goods on the large-good-poor side leaves value discrepancy at least \(r-L\); the displayed split attains that bound. Thus the canonical allocation has minimum bundle value
\[
\mu(H,L)=\frac{rH+L-D_r(H,L)}2
\]
and satisfies exact MMS.

**Step 2: Online transition for \(r=2\) or \(r=3\).** Maintain the canonical split, recording each agent's large-good and unit-good counts and holding actual goods in lists. For these two ratios, \(\delta_r(L)\) takes the following values: for \(r=2\), it is zero at \(L=0\), two at positive even \(L\), and one at odd \(L\); for \(r=3\), it is zero at \(L=0\), two at positive even \(L\), one at \(L=1\), and three at odd \(L\ge3\).

On arrival of a unit good, if \(H\) is even assign it to an agent with fewer unit goods. If \(H\) is odd, the next \(\delta_r\) differs from the current one by exactly \(+1\) or \(-1\); assign the new unit to the large-good-poor side in the first case and to the large-good-rich side in the second. The canonical invariant is preserved without reassignment.

On arrival of a large good when \(H\) is even, assign it to an agent with fewer unit goods (break ties consistently). Before the arrival the unit-good discrepancy is \(\epsilon=L\bmod2\). The recipient becomes large-good-rich. Move
\[
q=\frac{\delta_r(L)-\epsilon}{2}
\]
unit goods from that recipient to the other agent. If instead \(H\) was odd, give the arriving large good to the agent previously having fewer large goods; this agent previously had \(\delta_r(L)\) more unit goods. Move the same number \(q\) of unit goods from the recipient to the other agent, leaving unit-good discrepancy \(\epsilon\). In both cases the resulting allocation is canonical.

For \(r\in\{2,3\}\), direct inspection of the above parity formulas gives \(q\in\{0,1\}\). Whenever \(q=1\), the recipient already holds at least one unit good: in the even-\(H\) case \(L\ge2\) and the recipient holds \(\lfloor L/2\rfloor\) units; in the odd-\(H\) case \(\delta_r(L)\ge2\) and the recipient holds \((L+\delta_r(L))/2\). Hence the described move exists.

The only possible displacement is one old unit good from the recipient of the newly arrived large good. Map that old unit good to the new large good in the recipient's upgrade injection, keep all other old goods fixed, and include the displaced unit in the other agent's new bundle. Every old good is therefore retained or upgraded injectively. All operations use constant-size integer bookkeeping and at most one list transfer. Induction from the empty allocation proves all-prefix exact MMS and itemwise upgrades for every arrival word.

**Step 3: Additional fairness and the sharp obstruction.** Any complete two-agent allocation in which both agents receive at least their MMS is EFX: if agent \(i\) envied agent \(j\) even after deletion of a positive good \(g\) from \(j\)'s bundle, the two-set partition \((A_i\cup\{g\},A_j\setminus\{g\})\) would give both parts strictly more than \(v(A_i)\ge\mu\), a contradiction. Pareto optimality follows because both identical valuations sum to the fixed value of all goods.

For any \(r\ge4\), consider four unit goods followed by one value-\(r\) good. After the first four goods, exact MMS is two, so each agent must hold two goods. After the last good, exact MMS is four: one bundle can contain the large good, while the other can contain the four units. Any allocation achieving value at least four for both agents must give all four unit goods to one agent and the large good alone to the other, since the bundle lacking the large good can only use units. The new singleton owner had previously held two units but now holds only one good, contradicting the required upgrade injection. This proves impossibility without appealing to adaptive adversaries, and the two positive cases show the cutoff is sharp. \(\square\)

## Verification
Run `python verify.py` from this package. It independently computes exact MMS by enumerating every two-way split of the high and low multiplicities. For both positive ratios, it checks the explicit online algorithm after every prefix of all binary arrival words of length fourteen, verifies the count-based equivalent of the itemwise injections, and checks both directions of EFX. It separately enumerates the five-good obstruction for integer ratios from four through thirty. Recorded output:

`VERIFY_OK histories=32768 prefix_checks=458752 ratios=2,3 obstruction_ratios=4..30`

The **unbounded theorem** follows from the invariant proof and the five-good obstruction, not from the finite enumeration. Count-based injection checks are valid here because all agents agree on the two item values and high items can replace low ones, but not vice versa.

## Relationship to prior work
Huang and Teh, *Online Fair Division with Upgrade Recourse* (arXiv:2610.16943v1, first posted October 12, 2026), introduce the precise itemwise-upgrade model and establish a sharp general two-agent MMS approximation factor of \(2/3\), even for identical valuations. Their Theorem B.2 establishes that general bound; Appendix B.11 uses many small and large goods to force impossibility with unrestricted value ratios. Their exact two-agent MMS existence theorem instead permits the strictly weaker **bundle-level** upgrade rule. The present result concerns the intervening structurally restricted domain of **two identical denominations** and determines exactly when the stronger itemwise rule permits exact fairness.

Amanatidis, Lolos, Markakis, and Turmel, *Online Fair Division for Personalized 2-Value Instances* (arXiv:2505.22174v1, May 28, 2025), investigate two-valued utilities but require **irrevocable allocations**; those guarantees do not provide itemwise reassignment algorithms or the ratio cutoff here. Classical two-machine covering concerns the static maximin partition; an optimal partition at each prefix alone does not ensure that successive partitions respect replacement injections. No priority claim is made beyond the literature and research-record searches described in the accompanying review.

## Limitations
The positive construction depends on common valuations, exactly two agents, and integer ratio two or three. It does not characterize arbitrary real ratios or the best approximation for ratios four and above. The negative result is a five-good impossibility for exact fairness under itemwise upgrades, not for bundle-level upgrades or final-only fairness. The original motivating paper was inspected in accessible full-text HTML, but published or unindexed equivalent restricted-domain theorems remain possible; independent literature validation has not been performed.

## References
1. Y. Huang and N. Teh, *Online Fair Division with Upgrade Recourse*, arXiv:2610.16943v1, October 12, 2026. https://arxiv.org/abs/2610.16943 ; complete accessible text: https://www.paperpeel.com/paper/2610.16943 . Relevant sections 2.2, 3, 4, B.4, B.11.
2. G. Amanatidis, A. Lolos, E. Markakis, and V. Turmel, *Online Fair Division for Personalized 2-Value Instances*, arXiv:2505.22174v1, May 28, 2025. https://arxiv.org/abs/2505.22174 .
