# Exact cumulative maximum envy for two agents and unit–double goods

## Finding
For two agents with identical additive valuation \(v\), each sequentially arriving indivisible good has value either \(u\) or \(2u\), with \(u>0\). An irrevocable allocation incurs the sum of the maximum pairwise envy after every arrival.

**Fixed-order theorem.** For every integer \(m\ge 0\) and every fixed order of \(m\) goods from this value alphabet, assigning each arriving good to an agent with smaller current total value (arbitrarily breaking ties) globally minimizes cumulative maximum envy among all allocations, even those knowing the entire arrival order. Normalize the good values as \(w_t=v(g_t)/u\in\{1,2\}\). Initialize \(d_0=0\) and iterate
\[
d_t=|d_{t-1}-w_t| \qquad (1\le t\le m).
\]
The exact minimum cumulative envy is \(u\sum_{t=1}^{m}d_t\), and every \(d_t\in\{0,1,2\}\). The rule is online: future arrivals are not needed.

**Free-order theorem.** Suppose that the order itself may be chosen, with exactly \(a\) unit goods and \(b\) double-unit goods. For all nonnegative integers \(a,b\), the exact minimum is
\[
\operatorname{OPT}_{\mathrm{free}}(a,b)=u\left[b+\left\lceil\frac{a}{2}\right\rceil+\mathbf 1_{\{a=0,\ b\text{ odd}\}}\right].
\]
The lower bound is achieved by explicitly ordered and oriented blocks given below.

**Sharp alphabet limitation.** For the fixed order \((u,u,3u,u)\), greedy's successive absolute load gaps are \((u,0,3u,2u)\), summing to \(6u\). Allocation signs \((+,+,-,+)\) give gaps \((u,2u,u,0)\), summing to \(4u\). Thus fixed-order greedy optimality does not extend to all two-value alphabets.

## Assumptions and scope
There are exactly two agents, each valuing every good identically and additively. Each good has strictly positive value \(u\) or \(2u\). At round \(t\), the arriving item must go wholly and irrevocably to one agent. There are no transfers or empty waiting rounds. If their cumulative bundle values are \(L_1(t)\) and \(L_2(t)\), the maximum pairwise envy is exactly \(|L_1(t)-L_2(t)|\), not the envy of a fixed named agent. The objective is its sum over all completed rounds, including the last. Empty sequences have value zero. The two optimization settings differ only in whether item order is fixed or chosen.

## Proof
**1. A folding reduction for any fixed order.** By homogeneous scaling take \(u=1\). For an arbitrary allocation, write the signed load gap as \(D_0=0\) and \(D_t=D_{t-1}+\epsilon_t w_t\), with \(\epsilon_t\in\{-1,1\}\). The cost is \(\sum_t|D_t|\). Define the distance to the nearest multiple of four, \(\phi(z)=\min_{k\in\mathbb Z}|z-4k|\in\{0,1,2\}\). Because distance to a set containing zero never exceeds distance to zero, \(\phi(z)\le |z|\).

For each step \(w_t\in\{1,2\}\), the folded states \(s_t=\phi(D_t)\) obey the following complete transition rules:

| Before | Unit step | Double-unit step |
|---|---|---|
| \(0\) | \(1\) | \(2\) |
| \(1\) | \(0\) or \(2\) | \(1\) |
| \(2\) | \(1\) | \(0\) |

Conversely, **every** transition displayed can be realized by choosing a signed increment from an actual nonnegative absolute load gap equal to that state. Indeed, from each state \(s\in\{0,1,2\}\), the available next gaps are \(|s-w_t|\) and \(s+w_t\), and all tabulated targets are among these. Therefore any allocation's folded sequence can be reproduced by an actual allocation, with cumulative cost \(\sum_ts_t\le\sum_t|D_t|\). Thus some optimum always lies entirely in these three states.

**2. Exchange at the only branching state.** The only optional transition inside the three-state system occurs when a unit good arrives at gap \(1\): the next gap may be \(0\) or \(2\). Choosing \(0\) immediately saves two cost units. Until the next unit good (if any), all intervening goods have size \(2\), and simply swap gaps \(0\) and \(2\). Thus, over the initial decision and all consecutive double-unit goods, starting at \(0\) has a total cost either two less or exactly equal to starting at \(2\), according to the parity of the number of intervening doubles. At the next unit good, both paths reach gap \(1\) and can share the same continuation. If no further unit exists, the same comparison holds through the horizon. Replacing every transition \(1\to 2\) upon a unit arrival by \(1\to0\) consequently never increases total cost. The resulting unique gap evolution is \(d_t=|d_{t-1}-w_t|\), precisely lower-load-first greedy. The argument applies to every fixed order, without future knowledge.

**3. Lower bound when items may be reordered.** Let \(T=a+2b\) denote total normalized item value. For every allocation, the triangle inequality \(w_t=|D_t-D_{t-1}|\le |D_t|+|D_{t-1}|\) gives
\[
T\le 2\sum_{t=1}^m|D_t|-|D_m|,
\qquad C/u\ge (T+|D_m|)/2.
\]
Because \(D_m\equiv a\pmod2\), we have \(|D_m|\ge 1\) when \(a\) is odd; otherwise \(|D_m|\ge0\). Hence in all cases \(C/u\ge b+\lceil a/2\rceil\). If \(a=0\) and \(b\) is odd, \(D_m\) is twice an odd integer, forcing \(|D_m|\ge2\), so \(C/u\ge b+1\).

**4. Explicit order attaining every lower bound.** We use zero-return signed blocks: a pair of unit items \((+1,-1)\) has cumulative gap cost \(1\); a pair of double-unit items \((+2,-2)\) has cost \(2\); and a mixed block \((+1,-2,+1)\) has successive gaps \((1,1,0)\) and cost \(2\). All begin and finish with zero gap and hence may be concatenated freely. A leftover unit good, placed at the end, costs \(1\). A mixed ending block \((+1,-2)\) has successive gaps \((1,1)\) and cost \(2\) and must be last.

If \(b\) is even, pair all the double-unit goods, pair the unit goods, and if \(a\) is odd add one final unit. This costs \(b+\lceil a/2\rceil\). If \(b\) is odd and \(a\ge2\) is even, use one three-item mixed zero-return block, then pair the remaining goods: cost \(2+(b-1)+(a-2)/2=b+a/2\). If \(b\) and \(a\) are both odd, use a final two-item mixed block and pair the other goods: cost \(2+(b-1)+(a-1)/2=b+(a+1)/2\). Finally, if \(a=0\) and \(b\) is odd, pair all but one double-unit good and put the last one at the end, costing \(b+1\). These cases exhaust \(a,b\ge0\). Rescaling by \(u\) finishes the proof.

## Verification
The included standalone standard-library program `verify.py` enumerates all \(32{,}767\) words over \(\{1,2\}\) of length at most \(14\), comparing greedy cost against an independent exact dynamic program over all allocation choices. It separately checks every pair of item counts \((a,b)\) with \(0\le a,b\le16\), totaling \(289\) instances, using an independent dynamic program that optimizes both arrival order and assignment. It checks the \(\{1,3\}\) four-item boundary. Run `python verify.py`; expected output is `VERIFY_OK fixed_words=32767 free_count_pairs=289 sharp_fixed_counterexample=(1,1,3,1)`. These finite computations corroborate, but do not replace, the proofs for unbounded lengths.

## Relationship to prior work
Goldberg, Robinson and Teh (2026), *Minimizing Cumulative Envy in Allocating a Sequence of Items*, introduce the present cumulative-maximum-envy objective. Their Proposition 1 proves optimality of a greedy rule for identical **binary** valuations, meaning \(\{0,1\}\), and their Section 4 gives an exact pseudopolynomial dynamic program for bounded values. Their Section 5 provides a \(3/2\)-approximation under free ordering for two agents with arbitrary identical valuations. These results do not state an exact fixed-order greedy law for two strictly positive levels \(\{u,2u\}\), nor the free-order count formula. A constant baseline shift or splitting a double-valued good into two unit goods does not preserve intermediate-round cumulative envy; hence binary optimality does not imply the present result by a trivial conversion.

Elkind et al. (2024), *Temporal Fair Division of Indivisible Items*, establish temporal EF1 guarantees for two item types, but do not optimize the sum of maximum envy. Amanatidis et al. (2025), *Online Fair Division for Personalized 2-Value Instances*, study guarantees for approximate maximin share and EF1/EF2; their model and benchmark differ. The present theorem is an exact objective-specific characterization for the common-value two-agent case, not a general two-value fairness guarantee.

## Limitations
The result does not cover heterogeneous agents, three or more agents, other valuation ratios, zero-valued padding rounds, or more general item-order constraints. An identical-positive two-value alphabet other than \(\{u,2u\}\) may behave differently, as the \(\{u,3u\}\) counterexample shows. The literature comparisons are best-effort and do not establish publication priority; in particular, differently phrased results from load-balancing or discrepancy theory could cover some or all of the theorem. No independent expert review has been performed.

## References
1. P. W. Goldberg, I. Robinson and N. Teh, *Minimizing Cumulative Envy in Allocating a Sequence of Items*, arXiv:2610.09843v1 (2026), https://arxiv.org/html/2610.09843v1 .
2. E. Elkind, A. Lam, M. Latifian, T. Y. Neoh and N. Teh, *Temporal Fair Division of Indivisible Items*, arXiv:2410.14593v1 (2024), https://arxiv.org/html/2410.14593v1 .
3. G. Amanatidis, A. Lolos, E. Markakis and V. Turmel, *Online Fair Division for Personalized 2-Value Instances*, arXiv:2505.22174v1 (2025), https://arxiv.org/abs/2505.22174 .
