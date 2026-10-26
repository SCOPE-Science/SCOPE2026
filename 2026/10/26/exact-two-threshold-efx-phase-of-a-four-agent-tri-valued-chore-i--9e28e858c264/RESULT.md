# Exact two-threshold EFX phase of a four-agent tri-valued chore instance

## Finding
Consider four agents and thirteen indivisible chores: three of type \(A\), five of type \(B\), and five of type \(C\). Costs are additive, with singleton cost table
\[
\begin{array}{c|ccc}
\text{agent}&A&B&C\\\hline
1,2&r&1&7\\
3,4&r&7&1
\end{array}
\]
where \(r\) is an arbitrary real number satisfying \(r>7\). A complete allocation \(X=(X_1,X_2,X_3,X_4)\) is EFX for chores when, for every pair of agents \(i,j\) and every \(g\in X_i\),
\[
c_i(X_i\setminus\{g\})\le c_i(X_j).
\]
**Theorem.** This instance admits a complete EFX allocation **if and only if**
\[
\boxed{7<r\le19\quad\text{or}\quad r\ge21.}
\]
In particular, no EFX allocation exists for any real \(19<r<21\), whereas EFX allocations exist at both boundary values \(r=19\) and \(r=21\), and on both exterior ranges.

## Assumptions and scope
Every chore is assigned to exactly one of the four agents. Chores of one type have identical costs for all agents, but chores are individually distinct when allocated. Agents \(1,2\) have identical additive cost functions and agents \(3,4\) have identical additive cost functions. All singleton costs are positive. The definition of EFX removes an arbitrary single chore from the *envious agent's own* bundle; when that bundle is empty the condition is vacuous. No efficiency condition or particular allocation algorithm is assumed. Only the parameter \(r\) varies; multiplicities \((3,5,5)\) and the other costs \((1,7)\) are fixed.

## Proof
**1. No EFX allocation exists for \(19<r<21\): large chores cannot be doubled.** Call a type-\(A\) chore *large*. For every agent, the total cost of all chores is \(3r+40\). Suppose an agent receives at least two large chores. If she receives three large chores, or two large chores plus any other chore, removing an appropriate own chore leaves cost at least \(2r\). The combined cost of the other three bundles from her viewpoint is then at most \(r+40\) (indeed at most \(40\) in the three-large case). At least one other bundle has cost at most \((r+40)/3<21\), which is below \(2r\). This violates EFX.

The remaining possibility is a bundle containing exactly two large chores and nothing else. Removing one gives threshold \(r\), so all three other bundles must cost at least \(r>19\) to that agent. Two of those three bundles contain no large chore, and hence have nonnegative integer costs at least \(20\). Yet the cost of *all* small chores together is exactly \(40\) to either agent type. Thus these two bundles would each have cost exactly \(20\), and all small chores would belong to them. This is impossible: either agent type would require some integers \(0\le x,y\le5\) with \(x+7y=20\), but reduction modulo \(7\) forces \(x\equiv6\pmod7\), contrary to \(x\le5\). Therefore each agent receives at most one large chore. As there are three, exactly one agent receives no large chore.

**2. The unique large-free bundle must contain at least three chores of each small type.** By swapping the two agent types and interchanging \(B,C\) if necessary, call the large-free agent \(1\). Write \(x=|X_1\cap B|\) and \(y=|X_1\cap C|\). Consider any other agent \(j\) (each has exactly one large chore). If \(c_j(X_1)<r\), then EFX forces \(j\)'s bundle to consist solely of its large chore: otherwise removing a cheapest small chore would leave cost at least \(r\). The other two large-holding agents, to avoid strong envy of this singleton-large bundle, can each hold at most one additional small chore. Consequently the large-free bundle contains at least eight of the ten small chores, hence \(x\ge3\) and \(y\ge3\). Its EFX threshold for agent \(1\) is then \(x+7y-1\ge23>r\), contradicting EFX against the singleton-large bundle. It follows that \(c_j(X_1)\ge r\) for every large-holding agent \(j\).

There is a large-holding agent of each cost type. Therefore
\[
x+7y\ge r>19,\qquad 7x+y\ge r>19.
\]
Since \(x,y\) are integers between \(0\) and \(5\), if \(y\le2\) the first left side is at most \(5+14=19\); if \(x\le2\) the second is at most \(14+5=19\). Hence \(x,y\ge3\) and agent \(1\)'s EFX threshold is at least \(23\).

**3. The pigeonhole obstruction.** At most two type-\(C\) chores remain outside \(X_1\). Among the three large-holding agents there is therefore one, say \(h\), receiving no type-\(C\) chore. Since at most two type-\(B\) chores remain, agent \(1\) evaluates this agent's bundle at no more than \(r+2<23\). That is strictly below agent \(1\)'s own EFX threshold, a contradiction. Thus EFX is impossible throughout \(19<r<21\).

**4. EFX is attainable on every exterior interval.** The following seven explicit complete allocations cover all remaining real \(r>7\). A triple \((a,b,c)\) denotes the numbers of \(A,B,C\) chores in one agent's bundle. The four triples in a row appear in agent order \(1,2,3,4\). Each row uses exactly \((3,5,5)\) chores. The last column is the exact interval on which that row is EFX, computed directly from all agent-pair, own-item-removal inequalities.

| Allocation | Agent 1 | Agent 2 | Agent 3 | Agent 4 | EFX interval for \(r>7\) |
|---|---|---|---|---|---|
| P1 | \((0,3,1)\) | \((0,2,1)\) | \((2,0,0)\) | \((1,0,3)\) | \((7,13]\) |
| P2 | \((1,0,1)\) | \((0,5,2)\) | \((1,0,1)\) | \((1,0,1)\) | \([11,19]\) |
| P3 | \((1,2,0)\) | \((0,3,3)\) | \((1,0,1)\) | \((1,0,1)\) | \([21,23]\) |
| P4 | \((1,0,1)\) | \((0,4,3)\) | \((1,1,0)\) | \((1,0,1)\) | \([23,25]\) |
| P5 | \((1,0,0)\) | \((0,5,3)\) | \((1,0,1)\) | \((1,0,1)\) | \([25,38]\) |
| P6 | \((1,0,0)\) | \((0,5,4)\) | \((1,0,1)\) | \((1,0,0)\) | \([32,39]\) |
| P7 | \((1,0,0)\) | \((0,5,5)\) | \((1,0,0)\) | \((1,0,0)\) | \([39,\infty)\) |

To check a row without numerical approximation, use
\[
\tau_i=c_i(X_i)-\min_{g\in X_i}c_i(g),
\]
with \(\tau_i=0\) for an empty own bundle. EFX is equivalent to \(\tau_i\le c_i(X_j)\) for all \(i,j\). Because \(r>7\), the cheapest chore in a nonempty bundle has cost \(1\), \(7\), or \(r\), according to which of those categories is present. Consequently all inequalities for a fixed row are affine in \(r\). For example, P2 imposes \(r\ge11\) from agent \(2\)'s comparison with agent \(1\), and \(r\le19\) from agent \(1\)'s comparison with agent \(2\); every other comparison is weaker. The attached exact-arithmetic checker derives all seven reported intervals. Their union is precisely \((7,19]\cup[21,\infty)\). Together with Steps 1–3, this proves both directions.

## Verification
Run `python3 verify_phase.py` using Python's standard library only. The script recomputes all sixteen agent-pair inequalities for each of the seven allocations as exact rational affine inequalities, reproduces their parameter intervals, and checks the union covers the theorem's two existence ranges. As supplementary finite checks, it independently enumerates all \(\binom{6}{3}\binom{8}{3}^2=62{,}720\) type-count allocations at each of \(r=39/2\), \(r=20\), and \(r=41/2\), finding none EFX; it also checks representatives and endpoints of the construction intervals. The universal open-interval impossibility is established by Steps 1–3 and does not rely on finite numerical sampling.

## Relationship to prior work
He and Tao (2026, Theorem 1 and Section 3, with Appendix A) published the underlying thirteen-chore, four-agent counterexample at the single cost triple \((1,7,20)\). Their larger result proves EFX nonexistence for some tri-valued instances for every number of agents at least four. The theorem here does **not** re-claim that known nonexistence point or the general tri-valued impossibility. It fixes that exact instance's item multiplicities and the costs \((1,7)\), varies only the common large-chore cost \(r\), and determines the entire EFX feasibility phase diagram, including constructive restoration on both sides. Their proof at the published parameter does not state these two exact transition points or the exterior EFX witnesses. Aziz et al. (2023) prove EFX existence with only two types of chores, a different domain, and do not settle this three-type profile. Related EFX allocation counts and welfare results for goods do not imply the chore-cost phase boundary.

## Limitations
The complete phase classification concerns only this fixed four-agent thirteen-chore family with costs \((r,1,7)\) and \((r,7,1)\) and \(r>7\). It gives no result for arbitrary three-valued chore instances, varying item counts, Pareto optimality, randomized allocations, or dynamic arrivals. The exact parameter intervals are deterministic and require no numerical precision assumption. Establishing priority over every unpublished or inaccessible treatment remains outside the proof.

## References
1. Wentao He and Biaoshuai Tao, *EFX for Additive Chores: Nonexistence, Pareto Incompatibility, and Bi-Valued Existence*, arXiv:2606.08872, first posted 2026-06-07, especially Section 3 and Appendix A. https://arxiv.org/abs/2606.08872
2. Haris Aziz, Jeremy Lindsay, Angus Ritossa, and Mashbat Suzuki, *Fair Allocation of Two Types of Chores*, AAMAS 2023. https://www.southampton.ac.uk/~eg/AAMAS2023/pdfs/p143.pdf
3. Tzeh Yuan Neoh and Nicholas Teh, *Understanding EFX Allocations: Counting and Variants*, AAAI 2025, DOI:10.1609/aaai.v39i13.33536. https://ojs.aaai.org/index.php/AAAI/article/view/33536
