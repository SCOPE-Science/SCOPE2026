# Universal Lorenz balance for unit-divisible two-size goods, with a sharp divisibility boundary

## Finding

Let \(n\ge1\) agents have the **same additive valuation**, and suppose there are \(k\ge0\) goods worth \(r\) and \(m\ge0\) goods worth \(1\), with integer \(r\ge2\). A complete allocation has normalized load vector \(u=(u_1,\dots,u_n)\). For any vector \(z\), write \(z_{[1]}\ge\cdots\ge z_{[n]}\) for its entries sorted in decreasing order. We say \(u\) is Lorenz dominant here when

\[\sum_{i=1}^j u_{[i]}\le \sum_{i=1}^j v_{[i]}\quad (1\le j\le n)\]

for **every** feasible allocation vector \(v\); the sums at \(j=n\) are equal. In other words, \(u\) is majorized by every feasible load vector.

**Theorem.** The following simple allocation is Lorenz dominant for every \(n,k,m\): distribute the \(k\) large goods so their agent counts differ by at most one, and then assign each small good to a currently least-loaded agent. Consequently this *single* allocation simultaneously maximizes every symmetric Schur-concave welfare functional of the common load vector, including Nash-product welfare and maximin welfare.

In fact the exact sorted load profile can be obtained using a constant number of integer divisions, even with all multiplicities encoded in binary. Write \(k=qn+s\), where \(0\le s<n\), and \(L=rq\). Then:

* If \(s=0\), write \(m=dn+u\) with \(0\le u<n\); the loads comprise \(n-u\) copies of \(L+d\) and \(u\) copies of \(L+d+1\).
* If \(s>0\) and \(m<r(n-s)\), write \(m=d(n-s)+u\) with \(0\le u<n-s\); the loads comprise \(n-s-u\) copies of \(L+d\), \(u\) copies of \(L+d+1\), and \(s\) copies of \(L+r\).
* If \(s>0\) and \(m\ge r(n-s)\), write \(m-r(n-s)=dn+u\) with \(0\le u<n\); the loads comprise \(n-u\) copies of \(L+r+d\) and \(u\) copies of \(L+r+d+1\).

Thus the optimal Nash product is exactly the product of the displayed values raised to their displayed multiplicities, with \(0^0\) interpreted as \(1\). If each agent instead values every good by a positive agent-specific scalar \(c_i\) times the common valuation, the same allocation still maximizes the ordinary Nash product (which is multiplied by the fixed factor \(\prod_i c_i\)); the full Lorenz statement is about the unscaled common utilities.

**Sharp boundary for this two-stage rule.** Let the two common goods values be \(1\) and \(r>1\), with \(r\) real. The universal Lorenz-optimality assertion for the stated two-stage rule holds for **all** finite counts precisely when \(r\) is an integer. Indeed, for any noninteger \(r>1\), take two agents, two large goods, and \(m\) small goods, where \(m\) is a positive odd integer satisfying \(|2r-m|<1\). The two-stage allocation has discrepancy \(1\), whereas putting both large goods together and all small goods together has strictly smaller discrepancy \(|2r-m|\). The latter allocation is therefore strictly better for every strictly Schur-concave criterion (at that fixed sum). This is a limitation of the **two-stage rule**, not a claim that no Lorenz-optimal allocation exists at noninteger ratios.

## Assumptions and scope

Goods are indivisible and fully allocated, and agents share one normalized additive valuation of every item. The number of agents is a positive finite integer. There are no assignment restrictions, subsidy budgets or strategic constraints. The structural theorem applies to any integer \(r\ge2\) with arbitrarily large finite multiplicities \(k,m\). The ratio-boundary statement permits every real \(r>1\); the normalization to smaller value \(1\) is without loss of generality for positive two-size common values. The theorem does not assert majorization for heterogeneous valuations, nor generalize to three positive item sizes.

## Proof

**Lemma 1 (balancing the large-good counts).** Suppose an allocation gives large-good counts \(h_i\) and \(h_j\) with \(h_i-h_j=\Delta\ge2\). Let \(t\) be the total number of small goods these two agents jointly hold. At fixed counts of large goods, the attainable differences between their loads are precisely

\[r\Delta-t+2x,\quad x=0,1,\ldots,t.\]

If one large good is transferred from the first to the second agent and their \(t\) small goods are redistributed, the corresponding differences are

\[r(\Delta-2)-t+2x,\quad x=0,1,\ldots,t.\]

For integers \(r\ge2\), both attainable difference sets have the **same parity**, and their nonnegative centers \(r\Delta\) and \(r(\Delta-2)\) satisfy \(0\le r(\Delta-2)<r\Delta\). The least attainable absolute difference for a center \(c\ge0\) and \(t\) unit tokens is the smallest nonnegative value of the fixed parity at or above \(\max\{c-t,0\}\). Hence its value cannot increase when the center moves from \(r\Delta\) to \(r(\Delta-2)\). Select the redistribution achieving this lesser absolute difference. Relative to the original two-agent load pair, it has the same sum and no larger absolute difference, so it is majorized by the original pair. Replacing only those two coordinates makes the entire allocation vector weakly smaller in majorization order.

Repeat whenever two large-good counts differ by at least two. Each repetition strictly decreases \(\sum_i h_i^2\), so the process terminates with counts \(q\) or \(q+1\). Transitivity proves that for every feasible allocation there is a weakly majorizing improvement whose large-good counts are balanced.

**Lemma 2 (unit-load water filling).** Fix any nonnegative integer initial loads \(b_i\), and distribute \(m\) indistinguishable unit goods. For every convex function \(\varphi:\mathbb R_{\ge0}\to\mathbb R\), the marginal increments

\[\varphi(b_i+t+1)-\varphi(b_i+t),\quad t=0,1,\ldots\]

are nondecreasing in \(t\) and in the current load \(b_i+t\). A feasible assignment of \(m\) units selects an initial prefix from each of these chains. Selecting the globally smallest \(m\) marginal increments gives the minimum \(\sum_i\varphi(b_i+x_i)\) over nonnegative integer \(x_i\) summing to \(m\); the least-loaded-first procedure makes exactly these choices, regardless of the selected convex function. It therefore minimizes **every** separable convex sum simultaneously. Since all resulting load vectors have the same total, the standard convex-function characterization of majorization shows that the greedy vector is majorized by every other vector with the same baselines.

All balanced large-good-count choices have the same baseline multiset (\(n-s\) copies of \(L\) and \(s\) copies of \(L+r\)), differing only by permutation. Combining Lemmas 1 and 2 proves the global Lorenz assertion, for arbitrary finite \(n,k,m\) and every weakly Schur-concave welfare functional. In particular the product is Schur-concave on the nonnegative orthant (including zeros by continuity).

**Compressed formula.** If \(s=0\), every baseline equals \(L\), so unit goods distribute as evenly as possible. For \(s>0\), the \(n-s\) lower baselines are \(r\) below the \(s\) higher baselines. Greedy allocates exactly the first \(r(n-s)\) small goods to the lower group, bringing them to \(L+r\); before that threshold it spreads units evenly among the lower group, and afterwards evenly among all agents. This yields the three displayed formulas, each using constant many arithmetic operations on the binary input.

**Noninteger boundary.** For \(r>1\) noninteger, write \(2r\) between its neighboring odd integers (which differ by \(2\)). At least one positive odd neighbor \(m\) has \(|2r-m|<1\); equality could occur only if \(2r\) were an even integer, i.e. if \(r\) were an integer. In the indicated two-agent two-large-good instance, balanced large-good counts force one large good per agent. An odd number of small goods then gives minimum possible load discrepancy \(1\) for the second phase. The alternative allocation has discrepancy \(|2r-m|<1\) with exactly the same total, and thus strictly Lorenz improves the rule's output. Necessity and sufficiency are established.

## Verification

The standalone `lorenz_verify.py` implements the closed-form profile, independently enumerates every labeled assignment in a finite collection of small instances, and compares every descending partial sum with the candidate. Its exact-integer tests cover \(685\) parameter instances and \(2{,}127{,}810\) assignments. An independent rational-arithmetic loop tests the noninteger witness across reduced fractions in a bounded grid. The expected console line is `VERIFY_OK profiles=685 assignments=2127810 rational_boundary=all_coprime_pq_tested`. These finite checks do not establish the universal claim, which follows from the preceding lemmas.

## Relationship to prior work

Nguyen and Elbassioni (2026) analyze compactly represented \(p\)-mean allocation with few item types, giving approximation schemes and exact compact algorithms for one type and two-type egalitarian welfare. Their manuscript supplies the high-multiplicity motivation but does not state this common-valuation Lorenz-minimal three-case profile or the specific two-stage-rule ratio characterization. Akrami et al. (2022) give exact Nash optimization for general bi-valued preferences with divisible value ratios; their result is stronger regarding heterogeneity, but does not itself assert simultaneous Lorenz optimality or this compressed common-instance formula. Cousins, Viswanathan and Zick (2023) give broad algorithms for leximin and \(p\)-mean optimization for bivalued submodular valuations, including a much more general class; here the single *same* common-value allocation is explicitly proved to optimize all symmetric Schur-concave criteria, with a concrete ratio obstruction for the two-stage rule. Vu et al. (2026) study related bi-valued egalitarian algorithms and hardness but not this majorization profile. The claim is a sharply scoped structural specialization, not a claim to resolve the general exact two-item-type Nash problem.

## Limitations

The explicit sorting formula and universal majorization property require identical normalized valuations and integral value ratio. The construction cannot be asserted for nonintegral ratios, and the two-agent witness isolates exactly that algorithmic boundary. This proof supplies no welfare hardness result. Its formula is an exponent-compressed output: expanding all goods or the complete enormous Nash product may require output length proportional to the multiplicities. Related general leximin and Nash algorithms create a genuine residual priority risk; no claim of independent literature certification is made.

## References

1. Trung Thanh Nguyen and Khaled Elbassioni, *Maximizing p-Mean Social Welfare in the High-Multiplicity Setting: Few Agent Types and Few Item Types*, arXiv:2610.04417v1 (first public 2026-10-03), https://arxiv.org/html/2610.04417v1.
2. Hannaneh Akrami et al., *Maximizing Nash Social Welfare in 2-Value Instances*, AAAI 2022, https://doi.org/10.1609/aaai.v36i5.20402, preprint https://arxiv.org/pdf/2107.08965.
3. Cyrus Cousins, Vignesh Viswanathan, and Yair Zick, *Dividing Good and Better Items Among Agents with Bivalued Submodular Valuations*, arXiv:2302.03087v3 (2023), https://arxiv.org/pdf/2302.03087.
4. Thi Ngoc Anh Vu, Trung Thanh Nguyen, Khaled Elbassioni, and Jörg Rothe, *Settling the Computational Complexity of Max-Min Allocation with Ternary Valuations*, arXiv:2610.05237v1 (2026), https://arxiv.org/html/2610.05237v1.
