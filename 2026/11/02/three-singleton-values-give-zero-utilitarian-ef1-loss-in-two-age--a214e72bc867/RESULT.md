# Three singleton values give zero utilitarian EF1 loss in two-agent common-sign mixed manna

## Finding

For two equal-entitlement agents dividing a finite set of indivisible items with additive utilities, suppose each item is strictly positive for both agents or strictly negative for both, both signs occur, and all item utilities belong to **one common alphabet of at most three nonzero real values**. If both agents normalize their values for the entire set to \(1\), there exists a complete allocation that is simultaneously envy-free up to one item (EF1) and **maximizes utilitarian welfare**. Such an allocation is obtained using \(O(m)\) arithmetic operations and comparisons for \(m\) items.

Writing \(\operatorname{OPT}\) for the maximum possible sum of utilities and \(\operatorname{OPT}_{\mathrm{EF1}}\) for the maximum over complete EF1 allocations, the theorem gives

\[
\operatorname{OPT}_{\mathrm{EF1}}=\operatorname{OPT}\quad\text{and}\quad
\frac{\operatorname{OPT}}{\operatorname{OPT}_{\mathrm{EF1}}}=1.
\]

The **three-level bound is sharp as a uniform guarantee**: Teh (2026, Theorem 3.8) establishes, under the same normalization and sign-agreement conditions, a fixed **four-level** alphabet with instances whose ratio tends to infinity. Thus there is a sharp three-to-four cardinality transition between zero welfare loss and the possibility of unbounded welfare loss.

## Assumptions and scope

Let \(M\) be any finite set, and let each agent \(i\in\{1,2\}\) have additive valuation \(v_i\), determined by numbers \(v_i(e)\in\mathbb R\) for \(e\in M\). Assume:

1. Equal entitlements, with \(v_1(M)=v_2(M)=1\).
2. For every item \(e\), \(v_1(e)v_2(e)>0\), so both agents strictly agree whether it is a good or a chore.
3. At least one item is a common good and one is a common chore.
4. The union of all singleton values \(\{v_i(e):i\in\{1,2\},e\in M\}\) has cardinality at most three.

For a complete partition \((A_1,A_2)\), EF1 means that whenever \(v_i(A_i)<v_i(A_j)\) for \(i\ne j\), there exists either \(e\in A_j\) with \(v_i(e)>0\) and \(v_i(A_i)\ge v_i(A_j\setminus\{e\})\), or \(e\in A_i\) with \(v_i(e)<0\) and \(v_i(A_i\setminus\{e\})\ge v_i(A_j)\). These are the two permitted one-item repairs of envy in mixed manna.

The theorem is about **ordinary utilitarian welfare**, not just Pareto optimality or fractionally Pareto optimality. It is offline and imposes no ordering constraint on the items.

## Proof

**1. A unique possible nontrivial pair type.** Since the common value alphabet has at most three members and contains both signs, at most one sign has two different values. Consequently, if there are distinct values assigned to the two agents for an item, they must be one of two numbers \(u>v\) **of the same sign**. Thus every item is either *common* (both agents assign the same value \(w\)) or of one of the directed types \((v_1(e),v_2(e))=(u,v)\) and \((v,u)\). Let \(p,q\) be the respective numbers of the directed types. Equal total values imply

\[
0=v_1(M)-v_2(M)=(p-q)(u-v),
\]

so \(p=q\). If all singleton values agree across agents, take \(p=q=0\) and \(\Delta=0\); in that degenerate case the numerical choice of \(u,v\) is immaterial.

**2. Allocate all directed items optimally.** Give every \((u,v)\) item to agent 1 and every \((v,u)\) item to agent 2. This assigns each such item to a highest valuer, even if \(u,v<0\), and each agent gains a comparison advantage of exactly

\[
\Delta=p(u-v)\ge0
\]

when comparing their own directed-item bundle with the other agent's directed-item bundle under their own valuation.

**3. Signed balance of common items.** All remaining items have the same utility \(w_e\ne0\) for both agents. Process them in any order. Maintain the signed difference \(d\) between the sums of common-item utilities allotted to agent 1 and agent 2, initially zero. For a positive common item, assign it to whichever agent currently has the **smaller** common-item sum. For a negative common item, assign it to the agent with the **larger** common-item sum. Resolve ties consistently, for example in favor of agent 1.

We prove the following *witness invariant* after each prefix of common items:

- If \(d>0\), either agent 1 holds a positive common item of utility at least \(d\), or agent 2 holds a negative common item whose absolute utility is at least \(d\).
- If \(d<0\), either agent 2 holds a positive common item of utility at least \(-d\), or agent 1 holds a negative common item whose absolute utility is at least \(-d\).
- If \(d=0\), no witness is needed.

The assertion is true initially. A new signed item is always assigned to move \(d\) toward zero. If the old and new nonzero differences have the same sign, the old witness remains and its size still bounds the new absolute difference. If the sign changes, the newly assigned item itself lies on the new surplus side in the indicated sense, and its absolute utility exceeds the new absolute difference. If the old difference was zero, that new item itself is the witness. This proves the invariant by induction for all finite prefixes, with arbitrary real item magnitudes.

**4. Final EF1.** Let \(d\) denote the final common-item sum difference. Because \(p=q\), the two agents' *total* envy gaps (value of the other's bundle less the value of their own) are exactly

\[
E_1=-\Delta-d,\qquad E_2=-\Delta+d.
\]

If agent 2 envies agent 1, then \(d>\Delta\ge0\). The positive-\(d\) witness from step 3 is an item whose removal, from the other bundle if it is a good or from agent 2's own bundle if it is a chore, improves agent 2's comparison by at least \(d>E_2\). Thus the envy is removed by one permitted deletion. If agent 1 envies agent 2, then \(-d>\Delta\ge0\), and the negative-\(d\) witness provides the symmetric deletion, improving the comparison by at least \(-d>E_1\). Hence the complete allocation satisfies EF1.

**5. Welfare optimum.** Every directed item goes to a highest valuer, while every common item contributes the same utility regardless of its recipient. Therefore the sum of allocated utilities equals \(\sum_{e\in M}\max\{v_1(e),v_2(e)\}\), the unrestricted utilitarian optimum. This proves existence and optimality. The construction makes a constant number of comparisons and additions per item, giving \(O(m)\) arithmetic operations. Since each agent values all items at \(1\), the optimum is at least \(1\), so the stated welfare ratio is well-defined.

**6. Four levels really differ.** For the four-value alphabet \(\{-2/3,-1/3,1/3,2/3\}\), Teh's Theorem 3.8 supplies, for every integer \(k\ge2\), instances of the same two-agent, common-sign, normalized type with \(\operatorname{OPT}=(k+4)/3\) and \(\operatorname{OPT}_{\mathrm{EF1}}=5/3\). The resulting ratios \((k+4)/5\) diverge. This is an attributed published lower-bound construction, not a newly claimed lower-bound proof.

## Verification

The supplied standalone `verify.py` uses exact integer arithmetic, with a direct EF1 evaluator independent of the witness-invariant proof. It exhaustively checks 488,275 finite three-level item-profile sequences across five signed alphabets and lengths 1 through 7; 117,995 sequences have equal agent totals, and the computed allocation is EF1 and utilitarian-optimal in every one. An independent enumeration of every possible allocation confirms the optimal EF1 welfare on 3,186 selected equal-total profiles. An additional 13,555 randomized equal-total profiles with variable integer magnitudes and up to 14 items also pass. The verifier independently reproduces the four-level sharpness family's exact welfare optima for each integer \(k\) from 2 through 7 by exhaustive allocation enumeration.

These tests guard against implementation and small-instance errors. The theorem for all finite lengths and arbitrary real values follows from the induction and algebra above, **not** from finite experiments.

To reproduce, run `python3 verify.py` from the directory containing this file.

## Relationship to prior work

Teh (2026, Theorems 3.1 and 3.8) proves general WEF1 existence and constructs the exact unbounded four-valued welfare-price family. It does not state that all normalized common-sign instances with a three-member alphabet admit a *welfare-maximizing* EF1 allocation. The present theorem fills that boundary directly and uses its four-valued family for sharpness.

Aleksandrov and Walsh (2020, Theorem 4) in fact obtain an EF1 allocation that **maximizes utilitarian welfare** for the *different* ternary domain \(\{-a,0,b\}\), with a zero singleton-value level. Their 2019 and 2020 EFX/EF1 and Pareto-optimality results also cover identical-value domains. The present theorem addresses genuinely distinct, nonzero three-level alphabets \(\{-a,b,c\}\) or \(\{-c,-b,a\}\) with two different positive or two different negative levels and strict common signs. These valuation domains are not included in the zero-inclusive ternary domain or the identical-value cases; the cited results do not imply the theorem.

Ma et al. (2025) study utilitarian welfare approximation subject to EF1 with agents of two utility types, in a nonnegative-goods setting. That theorem does not imply this mixed-sign zero-loss statement.

The cited propositions do not directly supply this three-level zero-loss boundary or a stronger implication. An unindexed equivalent result remains possible.

## Limitations

The claim requires **two agents, equal total values, strict sign agreement on each item, a common singleton-value alphabet with at most three members, and both signs represented**. It does not claim the result for four-level alphabets, differing entitlements or total values, items whose signs disagree across agents, zero-valued items, more agents, or stronger EFX-type notions. It gives a linear number of exact arithmetic/comparison operations; encoding complexity depends on how real utilities are represented. Unindexed or inaccessible equivalent prior formulations remain a priority risk.

## References

1. Nicholas Teh, *Weighted Fair Division of Indivisible Mixed Manna*, arXiv:2609.01580, first posted 2026-09-01. https://arxiv.org/abs/2609.01580. In particular Theorem 3.8 and Section 3.6.
2. Martin Aleksandrov and Toby Walsh, *Greedy Algorithms for Fair Division of Mixed Manna*, arXiv:1911.11005, first posted 2019-11-25. https://arxiv.org/abs/1911.11005.
3. Martin Aleksandrov and Toby Walsh, *Two Algorithms for Additive and Fair Division of Mixed Manna*, arXiv:2007.04129, first posted 2020-07-08. https://arxiv.org/abs/2007.04129.
4. Jiaxuan Ma, Yong Chen, Guangting Chen, Mingyang Gong, Guohui Lin, and An Zhang, *Maximizing Social Welfare Among EF1 Allocations at the Presence of Two Types of Agents*, arXiv:2509.09641, first posted 2025-09-11. https://arxiv.org/abs/2509.09641.
