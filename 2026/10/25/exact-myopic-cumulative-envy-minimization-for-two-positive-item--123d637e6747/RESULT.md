# Exact myopic cumulative-envy minimization for two positive item values

## Finding
For every finite, fixed arrival sequence of indivisible goods, two agents with **identical additive values** in the set \(\{a,2a\}\), where \(a>0\), minimize cumulative maximum envy by assigning each arriving good to an agent with the **currently smaller total bundle value**. This irrevocable rule is optimal among **all** allocations that know the entire arrival sequence in advance; its running time and memory use are linear and constant, respectively. Ties may be broken arbitrarily.

This is the exact boundary for the common positive **integer** alphabet \(\{1,\ldots,K\}\): for \(K\le 2\) the myopic rule is always optimal, whereas for every integer \(K\ge3\) there is a four-good input drawn from that alphabet where it is not. In fact, for every integer \(k\ge3\), sequence \((1,1,k,1)\) costs \(2k\) under the rule and has optimum \(2k-2\). No three-good sequence with arbitrary positive common additive values can defeat the rule.

## Assumptions and scope
Let \(m\ge0\) goods arrive in a specified order, one per stage, and be irrevocably allocated to one of two agents. Both agents use the same additive utility \(v\). At stage \(t\) let \(L_i(t)\) be agent \(i\)'s total utility from her own bundle. The stagewise maximum positive envy and the cumulative objective are
\[
E_t=\max\{0,L_1(t)-L_2(t),L_2(t)-L_1(t)\}=|L_1(t)-L_2(t)|,\qquad C=\sum_{t=1}^{m}E_t.
\]
The first theorem assumes that each arriving good has the strictly positive value \(a\) or \(2a\), common to both agents. Values need not appear in sorted order. The comparator may select assignments after seeing the entire future; the greedy allocation does not use that information. For the integer-alphabet threshold, each item instead has a value among \(\{1,\ldots,K\}\), again common to both agents, and the statement is uniform over all finite sequences. The counterexample uses only strictly positive values. The scope does not include item-specific or agent-specific values outside this identical two-level model, more than two agents, a reorderable sequence, or a discounted objective.

## Proof
Rescale by \(a>0\). It suffices to treat item weights \(w_t\in\{1,2\}\). Because the objective is symmetric under interchanging the agents, its optimal remaining cost depends only on the current nonnegative imbalance \(d=|L_1-L_2|\).

For any finite **suffix** \(W=(w_1,\ldots,w_h)\), define \(F_W(d)\) as the minimum sum of imbalances produced over these future \(h\) stages, given initial imbalance \(d\). The terminal function is \(F_{\varnothing}(d)=0\). Writing \(f=F_{(w_2,\ldots,w_h)}\) when the first suffix weight is \(w=w_1\), the Bellman recurrence is
\[
F_W(d)=\min\big\{|d-w|+f(|d-w|),\;d+w+f(d+w)\big\},\quad d\ge0.
\]
We prove by backward induction that for **every** such suffix the following four assertions hold:
\[
\begin{aligned}
&F_W(d+2)\ge F_W(d)\quad (d\ge1),\\
&F_W(0)-2\le F_W(2)\le F_W(0),\\
&F_W(4)\ge F_W(0).
\end{aligned}
\tag{1}
\]
The empty suffix satisfies them. Suppose the remainder's value function \(f\) satisfies (1).

**Next weight \(w=1\).** Its recurrence and the inductive inequalities give
\[
F_W(0)=1+f(1)=F_W(2),\qquad
F_W(1)=\min\{f(0),2+f(2)\}=f(0).
\]
Also
\[
F_W(3)=\min\{2+f(2),4+f(4)\}\ge f(0)=F_W(1),
\]
where the two lower bounds use \(f(0)\le f(2)+2\) and \(f(4)\ge f(0)\). Finally,
\[
F_W(4)=\min\{3+f(3),5+f(5)\}\ge1+f(1)=F_W(0).
\]
For every \(d\ge2\), the two possible next imbalances from \(d+2\) are each exactly two larger than the corresponding ones from \(d\), and the remainder function is nondecreasing under such two-step shifts at positive arguments. Thus \(F_W(d+2)\ge F_W(d)\). This proves (1) for \(w=1\).

**Next weight \(w=2\).** The recurrence and (1) for \(f\) give
\[
\begin{aligned}
F_W(0)&=2+f(2)=F_W(4),\\
F_W(2)&=\min\{f(0),4+f(4)\}=f(0),\\
F_W(1)&=\min\{1+f(1),3+f(3)\}=1+f(1)=F_W(3).
\end{aligned}
\]
Because \(f(2)\le f(0)\le f(2)+2\), the new difference is
\[
0\le F_W(0)-F_W(2)=2+f(2)-f(0)\le2.
\]
In particular, \(F_W(4)\ge F_W(2)\). For every \(d\ge3\), both next imbalances from \(d+2\) are two larger than the corresponding next imbalances from \(d\), which are positive; the inductive two-step monotonicity therefore yields \(F_W(d+2)\ge F_W(d)\). This proves (1) for \(w=2\).

It remains to show optimality of a myopic action on the states it actually reaches. The rule sends each good to the less-loaded agent; if \(d>0\) and the next item has weight \(w\), the next imbalance is \(|d-w|\). Starting at \(d=0\), the rule remains entirely in \(\{0,1,2\}\). For any future-value function \(f\) satisfying (1), a myopic next action minimizes the full Bellman expression: at \(d=1,w=1\) this is \(f(0)\le2+f(2)\); at \(d=1,w=2\) and \(d=2,w=1\) it follows from \(f(3)\ge f(1)\); and at \(d=2,w=2\) it follows from \(f(4)\ge f(0)\). At \(d=0\) the two actions tie by symmetry. Thus every myopic action along the entire trajectory is globally Bellman-optimal. Backward induction proves the first theorem for all sequence lengths and both tie choices. Multiplying the costs by \(a\) restores the general scale.

**Sharp integer-alphabet failure.** With weights \((1,1,k,1)\) for \(k\ge3\), myopic next imbalances are \((1,0,k,k-1)\), producing cost \(2k\). If the first two goods instead go to the self-review, the third goes to the other agent, and the fourth returns to the first agent, the imbalances are \((1,2,k-2,k-3)\), producing cost \(2k-2\). The latter is optimal: after the first item, the second-stage imbalance is either \(0\) or \(2\); for any current imbalance \(z\ge0\) with two stages of weights \((k,1)\) remaining, the optimal continuation chooses the smaller imbalance at the third stage because \(y\mapsto y+|y-1|\) is nondecreasing on \([0,\infty)\). The two possible total costs are therefore exactly \(2k\) and \(2k-2\). As a result, the smallest integer upper bound \(K\) permitting failure is \(3\).

**Minimal number of goods.** For any strictly positive first three common values \(a,b,c\), only the second assignment can disagree with the greedy policy up to interchange of agent labels. The second-stage imbalance is either \(|a-b|\) or \(a+b\). With a single stage remaining, choosing the best third assignment makes the costs incurred in stages two and three equal to \(g(z)=z+|z-c|\), a nondecreasing function of the second-stage imbalance \(z\ge0\). Hence choosing \(|a-b|\) cannot be worse. For one or two goods optimality is immediate. The four-good example is thus length-minimal even among all positive-valued two-agent common-valuation sequences.

## Verification
`CHECK.py` uses exact integer arithmetic and independent dynamic programming over all possible current imbalances. Running `python3 CHECK.py` reproduces: (i) agreement of greedy and optimum on all \(8191\) words over \(\{1,2\}\) of lengths zero through twelve; (ii) all inequalities (1) for \(2047\) words of lengths zero through ten, every suffix and imbalances through \(30\); (iii) greedy optimality for \(820\) integer-valued sequences of length at most three with values from \(1\) through \(9\); and (iv) the four-good family for \(k=3,\ldots,20\). None of those finite calculations substitutes for the universal induction above.

The tradeoff is genuine rather than just stagewise optimality: for the sequence \((1,1,2)\), greedy incurs imbalances \((1,0,2)\) and an alternative incurs \((1,2,0)\); both have cumulative cost \(3\). Hence the theorem does not follow from minimizing each individual stage's imbalance.

## Relationship to prior work
Goldberg, Robinson, and Teh (2026, arXiv:2610.09843), Section 4 and Appendix 0.B.1, prove myopic optimality when agents have identical **binary** valuations \(\{0,1\}\). They treat general fixed-order cumulative maximum envy by dynamic programming. The present theorem addresses two strictly positive, unequal values \(\{a,2a\}\), where the stagewise-minimum proof of their binary case does not apply. Their paper's sequencing-variant approximation results allow reordering and therefore do not imply this fixed-order exact statement.

Amanatidis, Lolos, Markakis, and Turmel (2025, arXiv:2505.22174) study personalized two-value *online* guarantees for maximin share and EF relaxations; these are different objectives from exact cumulative-maximum-envy minimization. Choi, Li, and Teh (2026, arXiv:2608.20033) obtain temporal EF1 guarantees for a bounded number of item types, which likewise do not imply minimum summed prefix envy. The result also concerns a classical signed prefix-balancing viewpoint; possible unindexed formulations under scheduling or discrepancy terminology remain a publication-priority risk.

## Limitations
The proof is restricted to two agents and identical additive valuations with positive item values in the exact ratio \(2\), or one repeated positive value. It makes no assertion for arbitrary two-value ratios, heterogeneous valuations, more agents, or zero-valued arrivals, which can alter the temporal weighting of unequal stages. The four-good failure for \(\{1,3\}\) establishes only the **integer-alphabet** boundary, not a universal real-valued ratio threshold. The result is a mathematical claim with self-review; no independent audit or independent novelty certification has been performed.

## References
Goldberg, P. W., Robinson, I., and Teh, N. (2026). *Minimizing Cumulative Envy in Allocating a Sequence of Items.* arXiv:2610.09843, first posted 2026-10-07. https://arxiv.org/html/2610.09843v1

Amanatidis, G., Lolos, A., Markakis, E., and Turmel, V. (2025). *Online Fair Division for Personalized 2-Value Instances.* arXiv:2505.22174, first posted 2025-05-28. https://arxiv.org/abs/2505.22174

Choi, K.-W., Li, M., and Teh, N. (2026). *Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings.* arXiv:2608.20033, first posted 2026-08-20. https://arxiv.org/abs/2608.20033
