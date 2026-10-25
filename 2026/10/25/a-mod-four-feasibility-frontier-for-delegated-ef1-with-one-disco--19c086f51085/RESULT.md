# A mod-four feasibility frontier for delegated EF1 with one discounted agent

## Finding
Fix two centers, each containing two agents. Every one of \(m\ge4\) indivisible goods is worth \(1\) to three agents and the same number \(\varepsilon\in(0,1)\) to the fourth agent, who belongs to the second center. Agents compare bundles across both centers (inter-EF1). Centers assess their own allocation by realized total utility, but evaluate another center's goods by the **maximum** utility they could produce if the goods were freely reassigned to their own members (item-based realized valuation). The allocation must satisfy EF1 for both centers as well as inter-EF1 for all four agents.

Write \(m=4q+r\), where \(q\ge1\) and \(r\in\{0,1,2,3\}\). Such an allocation exists **if and only if** \(\varepsilon\ge\tau(m)\), where

\[
\tau(4q)=\frac{q-1}{q},\qquad
\tau(4q+1)=\max\!\left\{0,\frac{q-2}{q}\right\},\qquad
\tau(4q+2)=\frac{q-1}{q},\qquad
\tau(4q+3)=\frac{q-1}{q+1}.
\]

The boundary is inclusive; when \(\tau(m)=0\), every permitted \(\varepsilon>0\) is feasible. In this one-discounted-agent family, eight goods are the smallest inventory size permitting nonexistence: for \(0<\varepsilon<1/2\), feasibility holds at \(m=4,5,6,7\), fails at \(m=8\), returns at \(m=9\), and fails again at \(m=10\). This inventory nonmonotonicity is a consequence of whole-good balancing and asymmetric center valuations.

## Assumptions and scope
Let the agents be \(A,B,C,D\), with first center \(\{A,B\}\) and second center \(\{C,D\}\). The \(m\) goods are distinct but have identical valuations: each good is worth \(1\) to \(A,B,C\) and \(\varepsilon\) to \(D\). Values are additive, no goods may remain unallocated, and \(m\ge4\). The analysis is for the **item-based realized** center semantics of Deligkas, Fasoulakis, Ioannidis, Mancho, and Markakis (2026): a center's own value is the sum actually received by its members, while a rival's goods are hypothetically reassigned among its own members to maximize utility. Center EF1 removes one rival good *before* that hypothetical redistribution. Inter-EF1 requires EF1 for all ordered pairs of individual agents, including those in different centers.

For bundle counts \((a,b,c,d)\in\mathbb{Z}_{\ge0}^{4}\) with \(a+b+c+d=m\), the two realized center utilities are \(a+b\) and \(c+\varepsilon d\). After deletion of any one good in a rival center, the observing center can give every remaining good to a member valuing it at \(1\). Thus its item-based potential valuation equals the number of remaining goods. The paper's center definitions therefore specialize exactly to

\[
a+b\ge c+d-1,\qquad c+\varepsilon d\ge a+b-1.
\]

## Proof
**1. Individual EF1 forces almost-equal bundle sizes.** For a particular agent, all goods have the same strictly positive per-item utility. Removing any one good from another bundle eliminates envy exactly when the first agent's item count is no smaller than the second's count minus one. Applied to all ordered pairs, inter-EF1 is therefore equivalent to

\[
\max\{a,b,c,d\}-\min\{a,b,c,d\}\le1.
\]

Consequently the four counts comprise exactly \(r\) copies of \(q+1\) and \(4-r\) copies of \(q\), where \(m=4q+r\).

**2. The first center's fairness forces its total.** The center-1 EF1 inequality is \(2(a+b)\ge m-1\), or equivalently \(a+b\ge\lfloor m/2\rfloor\). Given step 1 and \(0<\varepsilon<1\), this sharply limits the possible distributions. In the following table, the two entries under each center are the numbers of goods held by its agents; interchanging the two entries in the first center is immaterial.

| Inventory | First center: \(A,B\) | Second center: \(C,D\) | Required \(\varepsilon\) |
| --- | --- | --- | --- |
| \(4q\) | \(q,q\) | \(q,q\) | \(\varepsilon\ge(q-1)/q\) |
| \(4q+1\) | \(q,q\) | \(q+1,q\) | \(\varepsilon\ge(q-2)/q\) |
| \(4q+2\) | \(q,q+1\) | \(q+1,q\) | \(\varepsilon\ge(q-1)/q\) |
| \(4q+3\) | \(q,q+1\) | \(q+1,q+1\) | \(\varepsilon\ge(q-1)/(q+1)\) |

Here is why these are exhaustive, not merely constructions. For residue \(0\), balance fixes all counts at \(q\). For residue \(1\), placing the sole \(q+1\) bundle into the first center makes \(a+b=2q+1\) and leaves \(c=d=q\); the second-center inequality then demands \(\varepsilon\ge1\), excluded by assumption. Hence the first center holds two \(q\)-bundles, and the second center places its larger bundle with \(C\), the unit-value member, since this maximizes its realized value. For residue \(2\), the first center cannot take two \(q\)-bundles because that violates its own EF1. If it instead takes both \(q+1\)-bundles, the second-center inequality requires \(\varepsilon\ge1+1/q>1\). Thus each center must get one larger bundle, with \(C\) receiving the larger bundle within the second center. For residue \(3\), putting both \(q+1\)-bundles in the first center leaves the second center one \(q+1\) and one \(q\); even the best assignment of those two sizes requires \(\varepsilon\ge1\). Therefore the first center has one \(q\) and one \(q+1\), leaving two \(q+1\)-bundles to the second center.

**3. The remaining inequality gives an exact threshold.** Substitute each forced row into \(c+\varepsilon d\ge a+b-1\). The four resulting inequalities are exactly the formulas for \(\tau(m)\) in the Finding section, with a vacuous inequality replaced by threshold \(0\) in residue \(1\). Thus every allocation satisfying both layers implies \(\varepsilon\ge\tau(m)\). Conversely, when this inequality holds, allocate any \(m\) distinct goods in the quantities of the corresponding table row. Step 1 supplies agent inter-EF1; the first-center inequality is satisfied by construction; and the second-center inequality is the assumed threshold. Hence a simultaneous allocation exists.

For example, at \(m=8\) all four agents must receive two goods. The second center has realized utility \(2+2\varepsilon\), while the first center's goods after deletion are worth \(3\) to it. This is feasible exactly for \(\varepsilon\ge1/2\). At \(m=9\), counts \((2,2,3,2)\) satisfy both center inequalities for every \(\varepsilon>0\). At \(m=10\), the only potentially feasible count template is \((2,3,3,2)\), which again requires \(\varepsilon\ge1/2\). The four smaller inventories \(m=4,5,6,7\) all have threshold zero. These examples prove the asserted first obstruction and nonmonotonicity.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic and independently enumerates every possible four-agent count vector for inventories \(4\le m\le80\), for a fixed grid of rational \(\varepsilon\) values and additional exact/below/above-threshold checks. For each vector, it checks the original ordered-pair agent EF1 inequalities and the two center EF1 comparisons, then compares existence to the formula. Running `python3 verify.py` completed 1,122 exact-rational inventory/parameter checks plus the explicit small-inventory boundary assertions without disagreement. These finite tests are corroboration; the proof above establishes the statement for every integer \(m\ge4\) and every real \(\varepsilon\in(0,1)\).

## Relationship to prior work
Deligkas, Fasoulakis, Ioannidis, Mancho, and Markakis (2026), Section 4.2, Theorem 11, establish nonexistence of simultaneous center EF1 and agent inter-EF1 under item-based realized values, using precisely the same one-discounted-agent valuation pattern with twelve goods and a sufficiently small discount. Their theorem supplies a nonexistence witness but not an exact feasibility frontier across inventory sizes. The present result determines every inventory and discount threshold in that pattern, finds its first obstruction at eight goods, and proves that feasibility can return at nine goods. The comparison concerns the strength of the mathematical statements, not the order of titles.

Kawase and Mahara (2026) and Cookson, Shah, and Verma (2026) prove broad existence results for individually balanced EF1 allocations, including arbitrary additive valuations in the latter work. Those results do not impose separate delegated-center EF1 under asymmetric realized-versus-counterfactual center utility. Hence they guarantee the first layer of this theorem but do not imply its two-layer feasibility classification.

## Limitations
This is a complete classification **only** of the specified four-agent family with identical goods, three unit-value agents, one uniformly discounted agent, two centers of two, and item-based realized center valuations. It is not a claim about general heterogeneous goods, arbitrary center sizes, bundle-based or item-based potential values, or general minimal counterexamples outside this family. The verification code cannot substitute for proof for arbitrarily large inventories. Priority over unpublished or unindexed equivalent analyses has not been established; no independent scientific audit has been performed.

## References
1. A. Deligkas, M. Fasoulakis, S. D. Ioannidis, A. Mancho, and E. Markakis, *Delegated Fair Division*, arXiv:2607.27743, first public version 2026-07-30. In particular Definitions 4–5, Section 4.2, Theorem 11, and discussion in Section 6.
2. Y. Kawase and R. Mahara, *Fair and Efficient Balanced Allocation for Indivisible Goods*, arXiv:2603.05956, first public version 2026-03-06.
3. B. Cookson, N. Shah, and P. Verma, *Fair and Efficient Balanced Allocations for Additive Valuations*, arXiv:2608.06325, first public version 2026-08-06.
