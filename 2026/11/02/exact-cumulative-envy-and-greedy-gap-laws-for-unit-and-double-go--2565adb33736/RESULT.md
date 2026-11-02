# Exact cumulative-envy and greedy-gap laws for unit-and-double goods

## Finding

For two agents with identical additive valuations, let there be \(a\ge0\) unit-valued goods and \(b\ge0\) double-valued goods. The planner may choose the arrival permutation and allocate each good irrevocably upon arrival. Let \(\mathrm{OPT}(a,b)\) be the least cumulative maximum pairwise envy, summed after every arrival. Then
\[
\mathrm{OPT}(a,b)=\begin{cases} b+\lceil a/2\rceil,&a\ge1,\\ 2\lceil b/2\rceil,&a=0.\end{cases}
\]
For the policy that releases all unit-valued goods first, all double-valued goods second, and always allocates the next good to an agent of lower current total value, the exact cumulative cost is
\[
G(a,b)=\begin{cases}\lceil a/2\rceil+b,&a\text{ odd},\\a/2+2\lceil b/2\rceil,&a\text{ even}.\end{cases}
\]
Therefore \(G(a,b)-\mathrm{OPT}(a,b)=1\) exactly when \(a\ge2\) is even and \(b\) is odd, and otherwise it is zero. In the exceptional family, the exact approximation ratio is \(1+1/(a/2+b)\). The previously published three-good instance \((a,b)=(2,1)\) is its smallest member.

## Assumptions and scope

There are exactly two agents. Both assign each good the same value, either \(1\) or \(2\), independently of other goods (additive utilities). There are finitely many goods. Before allocation, the planner knows all goods and can choose their order; assignments are irrevocable after each arrival. There are no entitlement weights, capacity restrictions, missing goods or zero-valued goods. The empty instance is included with cumulative cost zero.

Write \(d_t\) for the signed difference between the agents' cumulative received values after step \(t\), with \(d_0=0\). For two agents with identical values the maximum envy at step \(t\) is exactly \(|d_t|\), hence the objective is \(C=\sum_{t=1}^{a+b}|d_t|\).

## Proof

**Universal lower bound.** If the value of the \(t\)-th released good is \(w_t\in\{1,2\}\), then \(d_t-d_{t-1}\) equals \(w_t\) or \(-w_t\). The triangle inequality yields \(w_t\le|d_{t-1}|+|d_t|\). Summing gives
\[
a+2b\le 2C-|d_{a+b}|.
\]
Because \(C\) is integral, \(C\ge\lceil(a+2b)/2\rceil=b+\lceil a/2\rceil\). This is the stated bound when \(a\ge1\).

**Achievability when \(a\ge1\).** Release one unit-valued good first, creating \(|d|=1\) and cost \(1\). Next release all \(b\) double-valued goods, assigning each to the presently lower-value agent. Every such step changes \(d=1\) to \(-1\) or vice versa, so it costs exactly \(1\). If \(a\) is odd, the remaining \(a-1\) unit goods form successive pairs: from \(|d|=1\), give the first of each pair to the lower-value agent (new gap \(0\)), then the second to either agent (new gap \(1\)). Each pair costs \(1\). The resulting cost is \(1+b+(a-1)/2=b+\lceil a/2\rceil\). If \(a\ge2\) is even, use one further unit good immediately after the double goods to cancel the gap to zero (cost \(0\)). Allocate the remaining \(a-2\) unit goods in pairs, each pair generating gaps \(1,0\) and costing \(1\). The total is \(1+b+(a-2)/2=b+a/2\). Thus the bound is attained for every \(a\ge1\).

**The pure-double case.** If \(a=0\), after any odd number of steps the signed difference is a nonzero multiple of \(2\), so the absolute gap is at least \(2\). The cumulative cost is at least \(2\lceil b/2\rceil\). Alternating allocations of consecutive double-valued goods yields gaps \(2,0,2,0,\ldots\), attaining equality, including \(b=0\).

**Greedy classification.** Processing the \(a\) unit goods first and assigning each to the currently lower-value agent produces successive gaps \(1,0,1,0,\ldots\), with cumulative cost \(\lceil a/2\rceil\). If \(a\) is odd, the starting gap for the double goods is \(1\), and every double step toggles its sign, leaving absolute gap \(1\): the extra cost is \(b\). If \(a\) is even, the gap starts at zero and subsequent double goods produce gaps \(2,0,2,0,\ldots\), adding \(2\lceil b/2\rceil\). Subtracting the optimal values gives exactly the stated indicator and ratio.

## Verification

The accompanying `verify.py` uses exact integer dynamic programming over the remaining unit/double counts and the current signed load gap. It minimizes every possible choice of next size and recipient, exhaustively for \(0\le a,b\le22\), and compares against both formulas, including all parity boundaries and the empty case. The verifier also simulates the prescribed ascending-order greedy policy; execution returned `VERIFY_OK exact_count_pairs= 529 max_a=max_b=22`. The proof above, not the finite experiment, establishes the claim for all nonnegative integers \(a,b\).

## Relationship to prior work

Goldberg, Robinson and Teh (2026) introduced cumulative maximum envy for temporal allocation, proved a universal lower bound for identical agents, and proved that freely reordering goods is NP-complete even for two identical agents. Their nondecreasing-value, least-loaded greedy rule is a \(3/2\)-approximation for two agents. Appendix C.5 (Example 3) already identifies the case of two unit goods and one double good as a tight example, so neither that example nor the general lower bound is claimed as new. Their full accessible preprint (main sections 4–5 and the relevant appendix) does not state the two-parameter exact optimal-cost formula or a complete if-and-only-if greedy gap classification. The present result supplies this classification for all multiplicities, rather than an isolated witness or an approximation bound. Other valuation models are not reduced to the present one.

## Limitations

The statement assumes the planner controls arrival order and valuations are exactly \(1\) and \(2\). It makes no claim about online algorithms without future knowledge, arbitrary integer weights, fixed arrival orders, or three or more agents. A prior derivation in unindexed or differently named literature remains possible. The result is a natural two-valued structural classification, not a hardness breakthrough or an independent validation.

## References

Goldberg, P. W., Robinson, I., and Teh, N. (2026). *Minimizing Cumulative Envy in Allocating a Sequence of Items*. arXiv:2610.09843v1 (public 2026-10-07), Sections 4–5 and Appendix C.5. https://arxiv.org/html/2610.09843v1
