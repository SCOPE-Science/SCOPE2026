# Exact feasibility and a one-quarter group-size transition for two signed indivisible items

## Finding
Consider two indivisible items assigned in full to two groups of prescribed sizes \(p\ge q\ge1\), whose memberships may be chosen simultaneously with the item allocation. Each agent has an additive valuation \((\pm1,\pm1)\), and all members of a group receive the utility of its entire bundle. Adopt mixed-item envy-freeness up to one item (EF1): an agent must not envy the other group either initially or after deleting at most one item from the other bundle or at most one item from her own bundle.

**Exact feasibility theorem.** Let \(c_{++},c_{+-},c_{-+},c_{--}\) denote the four numbers of agents with the indicated ordered valuation types. An EF1 outcome exists if and only if
\[
\min\{c_{++},c_{+-},c_{-+},c_{--}\}\le q.
\]
In particular, **every** signed valuation profile admits an EF1 outcome if and only if \(n=p+q\le4q+3\), equivalently \(q\ge\lfloor n/4\rfloor\). When \(n\ge4q+4\), an infeasible profile exists.

**Uniform random valuations.** Suppose each agent's two item values are independent fair signs, independently between agents. For fixed prescribed sizes \(p,q\), the exact probability \(B_{n,q}\) that no EF1 outcome exists is
\[
B_{n,q}=\frac{n!}{4^n}[z^n]\left(e^z-\sum_{j=0}^{q}\frac{z^j}{j!}\right)^4.
\]
For every fixed positive \(q\), as \(n\to\infty\) with \(p=n-q\),
\[
1-B_{n,q}\sim \frac{4n^q}{q!\,3^q}\left(\frac34\right)^n.
\]
For any sequence of integer group sizes with \(q_n\le n/2\) and \(q_n/n\to\alpha\), the infeasibility probability tends to \(1\) if \(\alpha<1/4\), whereas if \(\alpha>1/4\), feasibility holds identically for all sufficiently large \(n\). The transition has a Gaussian window: for \(t\ge0\) and \(q_n=n/4-t\sqrt n+o(\sqrt n)\), rounded to integers,
\[
B_{n,q_n}\longrightarrow\Pr\!\left(\min_{1\le j\le4}Z_j\ge-t\right),
\]
where \(Z\) is a centered four-variate Gaussian with diagonal covariance \(3/16\), off-diagonal covariance \(-1/16\), and \(\sum_j Z_j=0\). At \(t=0\) this limiting probability is zero. The statement assumes \(q_n\ge1\) eventually.

## Assumptions and scope
There are exactly two labeled, indivisible items \(g_1,g_2\); each of \(n\ge2\) labeled agents values each item at exactly \(+1\) or \(-1\), independently of bundle composition. The two groups must have precisely \(p\) and \(q\) agents, with \(p\ge q\ge1\), and every item is allocated to exactly one group. The allocation and group memberships can be selected jointly after valuations are known. For each agent \(i\) assigned own bundle \(A\) and facing other bundle \(B\), mixed EF1 means at least one of these holds: \(v_i(A)\ge v_i(B)\); \(v_i(A)\ge v_i(B\setminus\{g\})\) for some \(g\in B\); or \(v_i(A\setminus\{g\})\ge v_i(B)\) for some \(g\in A\). In the random model the four complete agent types are iid uniform; this does not follow merely from marginally fair individual signs without independence.

## Proof
**1. The four possible item allocations.** When \(g_1\) is assigned to the first group and \(g_2\) to the second, type \((+1,-1)\) is forced into the first group and type \((-1,+1)\) into the second. A member of the wrong group suffers utility \(-1\) rather than \(+1\); removing the only opposite item improves the comparison merely to zero, and removing the only own item likewise leaves zero, so EF1 fails. The two remaining types have equal bundle utilities and may belong to either group. Swapping the item allocation swaps the two forced types.

When both items go to the first group, type \((+1,+1)\) is forced into the first group: in the other group its own utility is zero and the other bundle has value \(2\), or value \(1\) after removing any one item. Type \((-1,-1)\) is forced into the second group because keeping both chores yields \(-2\), or \(-1\) after deleting one, versus zero. The two mixed-sign types value both bundles at zero and can join either. Swapping groups swaps the forced types. Consequently each of the four allocations fixes **exactly one** of the four agent types in the smaller group, fixes its antipodal type in the larger group, and leaves the remaining types free. Conversely, all assignments respecting these forced placements satisfy EF1 by the cases above.

**2. Necessity and sufficiency.** If every type has more than \(q\) agents, every possible allocation demands that a type with more than \(q\) agents be placed in the size-\(q\) group. Thus no allocation works. Conversely, suppose some type \(s\) has \(c_s\le q\). Let \(s^*\) denote its antipode (flipping both signs). If \(c_{s^*}\le p\), choose the allocation forcing \(s\) into the small group and \(s^*\) into the large group, and fill the vacancies with freely assignable agents. If \(c_{s^*}>p\), the other antipodal pair jointly contains fewer than \(q\) agents, since \(c_s+c_{s^*}>p\) and the population is \(p+q\). Choose an allocation forcing either of those types into the small group and its antipode into the large group. Both capacities are met, so the remaining flexible agents fill the groups. This proves the iff criterion. Since four nonnegative counts sum to \(n\), their minimum is always at most \(\lfloor n/4\rfloor\); this yields the universal guarantee. If \(n\ge4(q+1)\), choose each of the four counts at least \(q+1\) and distribute any remaining agents arbitrarily. This gives the sharp obstruction.

**3. Exact random probability.** Under the stated iid fair-sign model, the count vector is multinomial with four equal probabilities. Infeasibility is the event that every count exceeds \(q\). Its probability is \(4^{-n}\) times the sum of the multinomial coefficients over all four-component compositions of \(n\) with each component at least \(q+1\). The exponential generating-function identity gives the displayed exact coefficient formula.

**4. Fixed-\(q\) asymptotic.** Each marginal type count is binomial \(\operatorname{Bin}(n,1/4)\), so for fixed \(q\),
\[
\Pr(C_1\le q)\sim\binom nq 4^{-q}(3/4)^{n-q}
\sim\frac{n^q}{q!\,3^q}(3/4)^n.
\]
The probability that two specified type counts are both at most \(q\) is \(O(n^{2q}2^{-n})\), by summing the joint multinomial probabilities. This is exponentially smaller than the single-type event. Inclusion–exclusion therefore makes the four single-type lower-tail events asymptotically disjoint, proving the expression for \(1-B_{n,q}\).

**5. Fractional and Gaussian thresholds.** The multinomial law of large numbers gives \(C_j/n\to1/4\) simultaneously in probability. If \(q_n/n<1/4\) by a fixed margin, all four counts exceed \(q_n\) with probability tending to one. If \(q_n/n>1/4\) by a fixed margin, \(q_n\ge\lfloor n/4\rfloor\) eventually, so the deterministic guarantee applies. At the boundary the multinomial central limit theorem gives convergence of \(((C_j-n/4)/\sqrt n)_{j=1}^4\) to the stated Gaussian. The event \(\min_j C_j\ge q_n+1\) maps to \(\min_j Z_j\ge-t\); its boundary has Gaussian probability zero because each marginal has a continuous density. The Gaussian components sum to zero, hence their minimum is strictly negative almost surely and the limit at \(t=0\) is zero.

## Verification
A standalone Python program `verify_two_item.py` enumerates complete item assignments and all group memberships directly under the mixed-EF1 definition, independently of the four-type criterion. It checked every labeled valuation profile and every permissible group size for \(2\le n\le7\): **123,792** profile/size comparisons with no mismatches. It separately evaluates exact multinomial probabilities, including \(B_{8,1}=315/8192\), and asserts the zero/nonzero universal cutoff for small instances. These finite checks corroborate, but do not prove, the theorems for unbounded \(n\).

## Relationship to prior work
Gölz, Igarashi, Manurangsi, and Suksompong (2025; arXiv:2511.06218) establish EF1 existence for arbitrary **monotone** valuations in variable-sized groups, as well as a random **envy-free** existence threshold with a different goods-count regime. Neither implies the present signed two-item characterization: in this setting some items are chores and the monotonicity premise is false. Earlier group fair-division literature develops variable-group fairness predominantly for nonnegative goods. Deligkas et al. (arXiv:2610.28213, first publicly posted October 20, 2026) study signed heterogeneous preferences and exhibit the **already known** eight-agent, two-item obstruction with the four types each represented twice. That witness is not presented here as novel. Their parameterized-complexity results and example do not state the exact all-profile criterion, the population-quarter universality boundary, or its multinomial probability/critical Gaussian window. The present theorem does not supersede their general algorithms or complexity classifications.

## Limitations
The exact iff criterion relies on **two** items and valuation magnitudes identically one. It does not cover general real-valued utilities, more items or groups, fixed memberships, or a different convention for mixed-item EF1. The probability laws require independence and, except for the deterministic criterion, equiprobable valuation types. The critical Gaussian law is a limit for a specified group-size scaling, not a bound on finite sampling errors. A formula derivable from a stronger unindexed group-valuation theorem remains a publication-priority risk. Independent scientific validation has not been performed.

## References
1. P. Gölz, A. Igarashi, P. Manurangsi, W. Suksompong, *Fair Allocation of Indivisible Goods with Variable Groups*, arXiv:2511.06218, first submitted November 9, 2025. https://arxiv.org/html/2511.06218v1
2. M. Kyropoulou, W. Suksompong, A. A. Voudouris, *Almost Envy-Freeness in Group Resource Allocation*, arXiv:1901.08463, 2019. https://arxiv.org/abs/1901.08463
3. A. Deligkas, E. Eiben, R. Ganian, T.-L. Goldsmith, M. Gründel, S. Wietheger, *Subjective Valuations Make It Hard to Be Fair: The Complexity of Resource Allocation to Groups of Agents*, arXiv:2610.28213, first submitted October 20, 2026. https://arxiv.org/html/2610.28213v1
