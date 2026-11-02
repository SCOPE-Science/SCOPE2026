# Sharp \(5/3\) cumulative-envy guarantee for three-value greedy allocation

## Finding

For every positive integer \(m\) and every fixed sequence \((v_1,\ldots,v_m)\in\{u,2u,3u\}^m\), where \(u>0\), two agents have the same additive valuation for all goods. Allocate each arriving good irrevocably to an agent whose current total allocated value is smaller, breaking ties arbitrarily. Let \(G\) be the sum, over all prefixes, of the maximum pairwise envy produced by this rule. Let \(O\) be the least such cumulative maximum envy over **all** allocations for that fixed order, including allocations chosen with complete future knowledge. Then

\[
G\le\frac53 O.
\]

The factor \(5/3\) is the exact supremum of \(G/O\) across these sequences and all positive horizons. It is approached by \((1,1,3,1)\) followed by \(r\) copies of \((2,3,1)\), for \(r\to\infty\), after normalizing \(u=1\).

## Assumptions and scope

There are exactly two agents. Both evaluate the same positive item of value \(v_t\) as worth \(v_t\), with no side constraints, transfers, discarded goods, or reordering. Each good is allocated exactly once on arrival. The comparison is between a nonanticipatory greedy rule and the offline optimum with the **same prescribed order**. For two identical valuations, the maximum pairwise envy at a prefix is exactly the absolute difference between the agents' bundle values. Hence, setting \(u=1\) by scaling, the objective is the sum of absolute signed prefix sums.

## Proof

**A nonnegative potential.** Let \(g\in\{0,1,2,3\}\) denote the absolute current bundle-value difference of the greedy rule and \(d\in\mathbb Z\) the signed bundle-value difference of any comparison allocation. If the next item has value \(v\in\{1,2,3\}\), the greedy state becomes \(g'=|g-v|\), while the comparison allocation chooses a sign \(\sigma\in\{-1,1\}\) and becomes \(d'=d+\sigma v\). The stated range for \(g\) is invariant from the initial value \(0\).

Define a potential \(P(g,d)\) depending only on \(g\) and \(|d|\). For \(|d|\le5\), its values are given in the table, with columns indexed by \(g=0,1,2,3\). For \(|d|\ge6\), set \(P(g,d)=0\).

| \(|d|\) | \(g=0\) | \(g=1\) | \(g=2\) | \(g=3\) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 4 |
| 1 | 4 | 0 | 3 | 6 |
| 2 | 10 | 4 | 0 | 4 |
| 3 | 13 | 6 | 3 | 0 |
| 4 | 10 | 4 | 0 | 0 |
| 5 | 3 | 0 | 0 | 0 |

Every potential is nonnegative, and \(P(0,0)=0\). The finite, exact integer transition inequality is

\[
3g'-5|d'|+P(g',d')\le P(g,d).
\]

To verify it completely, symmetry reduces \(d\) to \(0,1,\ldots,8\). For each of the four greedy states, nine nonnegative comparison states, three item values, and two possible signs, direct substitution of the displayed integers gives the inequality: \(4\cdot9\cdot3\cdot2=216\) finite substitutions. The attached standalone checker also verifies the equivalent 408 signed-state substitutions. For \(|d|\ge9\), every transition satisfies \(|d'|\ge6\), so both potential terms vanish and the left side is at most \(3\cdot3-5\cdot6=-21<0\). Thus the inequality is valid for **all** integer comparison states, not merely a bounded search.

Starting at \((g,d)=(0,0)\), sum this inequality over all \(m\) arrivals. The potential terms telescope, giving

\[
3\sum_{t=1}^m g_t-5\sum_{t=1}^m|d_t|+P(g_m,d_m)\le0.
\]

Since the terminal potential is nonnegative, \(3G\le5C\) for the cumulative envy \(C\) of every comparison allocation. Taking the minimum over comparison allocations proves \(3G\le5O\). As all items are positive and \(m\ge1\), \(O>0\), so the multiplicative ratio is defined.

**Sharpness.** For every integer \(r\ge0\), take the length-\(4+3r\) sequence

\[
(1,1,3,1,\underbrace{2,3,1,\ldots,2,3,1}_{r\text{ copies}}).
\]

The greedy absolute imbalances in the initial block are \((1,0,3,2)\), totaling \(6\). Each subsequent \((2,3,1)\) block, started at imbalance \(2\), produces \((0,3,2)\) and costs \(5\). Hence \(G=6+5r\). An alternative allocation gives signed values \((-1,-1,+3,-1)\) in the first block, with signed prefix imbalances \((-1,-2,1,0)\) and cost \(4\). Each later block uses signed values \((+2,-3,+1)\), returning the signed imbalance to zero with costs \((2,1,0)\), totaling \(3\). Therefore \(O\le4+3r\), and

\[
\frac{6+5r}{4+3r}\le\frac GO\le\frac53.
\]

As \(r\to\infty\), the left ratio tends to \(5/3\). This proves that no smaller universal multiplier is possible. Scaling all values by \(u>0\) scales both objectives and changes neither ratio nor conclusion.

## Verification

Run `python3 verify_ternary.py`. It checks all 408 signed-state transitions with \(|d|\le8\), after which the analytical large-state argument covers the infinite remainder. An independent exact dynamic program checks all \(29{,}523\) value sequences of lengths one through nine and their optimal cumulative envy; the checker also verifies \(501\) sharpness witnesses, indexed by \(r=0,\ldots,500\). The proof of the universal result is the all-state potential inequality, not the finite enumeration.

## Relationship to prior work

Goldberg, Robinson and Teh introduced cumulative maximum envy and study fixed-order computational hardness, exact dynamic programming, and guarantees for a **different rule that is allowed to choose the item order**. Their public abstract does not state the present three-value, fixed-order, lower-loaded greedy ratio. The complete source text was not obtainable for a page-by-page comparison, so potential unindexed coverage remains a substantive priority risk; the abstract alone is not evidence that the full paper lacks this result.

The binary two-value setting \(\{u,2u\}\) admits exact greedy optimality under the same objective. In contrast, \((u,u,3u,u)\) already makes greedy strictly suboptimal. Earlier exact results for one exceptional high-valued item do not provide a ratio bound for arbitrary alternating occurrences of values \(u,2u,3u\). The present theorem addresses **arbitrarily many** such occurrences, by a global potential certificate rather than a one-exception formula.

The bound is not a universal guarantee for unrestricted item values, heterogeneous valuations, more than two agents, or a rule that may reorder items.

## Limitations

The proof assumes a common additive cardinal valuation, two agents, and item values in exactly the three-level allowed alphabet. It does not claim that the greedy rule is exactly optimal on this domain, that every individual instance has ratio \(5/3\), or that a finite observed ratio attains the supremum. The result has undergone only self-review; independent scientific validation has not been performed. A plausible primary source could not be inspected in full, leaving residual originality risk.

## References

1. Paul W. Goldberg, Isaac Robinson, and Nicholas Teh, *Minimizing Cumulative Envy in Allocating a Sequence of Items*, arXiv:2610.09843v1, first posted 2026-10-07, https://arxiv.org/abs/2610.09843.
2. Kui-Wang Choi, Minming Li, and Nicholas Teh, *Temporal Fair Division of Indivisible Mixed Manna: Tractable Settings*, arXiv:2608.20033, first posted 2026-08-20, https://arxiv.org/abs/2608.20033 (different temporal EF1 criterion).
