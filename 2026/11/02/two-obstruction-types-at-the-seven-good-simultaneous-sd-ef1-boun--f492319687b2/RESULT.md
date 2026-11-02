# Two obstruction types at the seven-good simultaneous SD-EF1 boundary

## Finding

In the two-agent, seven-good market-value fair-division model with three **strict** rankings (the common market ranking and one subjective ranking for each agent), exactly \(6{,}144\) of the \((7!)^2=25{,}401{,}600\) ordered subjective-ranking pairs admit **no** complete allocation that is stochastic-dominance envy-free up to one good (SD-EF1) simultaneously under both subjective preferences and the common market value. The market ranking can be fixed arbitrarily. Thus, for three independently uniform strict rankings, the exact nonexistence probability is

\[
\Pr(\text{no simultaneous SD-EF1 allocation})
=\frac{6{,}144}{25{,}401{,}600}=\frac{8}{33{,}075}.
\]

All nonexistence profiles belong to **exactly two** feasibility-preserving structural types. To specify representatives, fix the market ranking \(1\succ2\succ3\succ4\succ5\succ6\succ7\). In each subjective ranking, the displayed list is ordered from highest to lowest:

| Type | Agent 1's ranking | Agent 2's ranking | Number of exceptional paired-order profiles |
| --- | --- | --- | ---: |
| I | \(1,3,2,5,4,7,6\) | \(1,5,2,3,6,7,4\) | \(48\) |
| II | \(1,3,2,7,4,5,6\) | \(3,5,6,7,1,4,2\) | \(48\) |

A *paired-order profile* records each agent's ordered three consecutive unordered pairs and their final singleton, omitting the order within each pair. Two paired-order profiles are equivalent here under exchange of the two agents and arbitrary permutations of the three market pairs \(\{1,2\},\{3,4\},\{5,6\}\), including swaps of the members of each pair (with good \(7\) fixed). These are feasibility-preserving transformations, not necessarily automorphisms of the entire numerical valuation profile. Each type consists of one orbit of \(48\) paired-order profiles, and every paired-order profile has \(2^6=64\) strict-order refinements. The types are distinguished by the position of the market-lowest good \(7\): it is in the third subjective pair for both agents in Type I, and in the second subjective pair for both agents in Type II.

As an additional quantitative consequence, the exact expected number of simultaneous SD-EF1 allocations under the uniform model is \(128/25\). Type I is the counterexample printed in Barman, Ebadian, Latifian and Shah (2024); the two-type completeness, distinct Type II, and exact incidence are the present finding.

## Assumptions and scope

There are exactly two labeled agents and exactly seven labeled indivisible goods, all allocated and with no disposal. Each agent has a strictly positive additive utility with a strict singleton ranking; the market has a strictly positive additive value function with a strict singleton ranking. Only these rankings affect SD-EF1. A bundle \(X\) SD-dominates a bundle \(Y\), for a strict ranking \(\rho\), when for every prefix \(T\) of \(\rho\), \(|X\cap T|\ge |Y\cap T|\). An allocation \((A_1,A_2)\) is SD-EF1 for agent \(i\) if either the other bundle is empty or a single good can be removed from it to yield an SD-dominated bundle. It is market SD-EF1 when this holds in both directions for the common market ranking.

For the stated probability, the market order and both subjective orders are sampled independently and uniformly from the \(7!\) strict rankings. Relabeling goods lets the market order be fixed to \(1,2,\ldots,7\) without changing the fraction.

## Proof

**1. Prefix criterion.** Fix any strict ranking \(\rho\), and an allocation \((A_i,A_j)\). The agent-\(i\) SD-EF1 condition is equivalent to

\[
|A_i\cap T_\ell(\rho)|\ \ge\ |A_j\cap T_\ell(\rho)|-1
\qquad\text{for every }\ell=1,\ldots,7.
\]

Necessity follows because removing one good changes every prefix count by at most one. For sufficiency, remove the highest-ranked good in \(A_j\). Prior to its first appearance, the other bundle has no goods in the prefix; after its appearance, its count drops by exactly one. Therefore the displayed inequalities witness SD dominance with **one common removed good**. With two agents, the inequalities simplify to

\[
|A_i\cap T_\ell(\rho)|\ge\lfloor \ell/2\rfloor.
\]

Every odd-index condition follows from the immediately preceding even-index condition, so only the prefixes of lengths \(2,4,6\) matter. Consequently the ranking is relevant only through the ordered three *unordered* adjacent pairs and final unpaired good. There are precisely \(7!/(2!)^3=630\) such paired orders per subjective agent and exactly \(8\) strict rankings refining each.

**2. Market allocations.** Applying the prefix criterion to both agents under the market ranking gives \(|\,|A_1\cap T_\ell|-|A_2\cap T_\ell|\,|\le1\) for all prefixes. At even indices, parity forces equality of the two counts. Hence each of the market pairs \(\{1,2\}\), \(\{3,4\}\), and \(\{5,6\}\) must be split one good per agent, while good \(7\) can go to either agent. Conversely every such split satisfies the market constraints. Exactly \(2^4=16\) complete allocations are market SD-EF1.

**3. Exact first-layer exhaustion.** Enumerate all \(630^2=396{,}900\) ordered paired-order profiles. For each of the \(16\) market allocations test the six scalar inequalities

\[
|A_1\cap T_{2t}(\rho_1)|\ge t,
\qquad
|A_2\cap T_{2t}(\rho_2)|\ge t,
\qquad t\in\{1,2,3\}.
\]

The complete, executable algorithm is `verify.py`. It finds exactly \(96\) profiles for which **none** of the \(16\) allocations passes all inequalities. There is no sampling: the program iterates every possible paired-order profile and every market-compatible complete allocation. Independently, `independent_full.cpp` enumerates all \(5{,}040^2\) strict-ranking pairs, using a prefix-discrepancy SD-EF1 predicate, and obtains exactly \(6{,}144\) failures. The two enumeration spaces agree because each paired-order profile corresponds to exactly \(8^2=64\) strict-ranking pairs.

**4. Classification into two types.** The \(48\) item relabelings that permute the three market pairs and may flip each pair preserve the set of market-compatible allocations. Relabeling the two subjective paired orders accordingly preserves their prefix constraints, and exchanging the two agents complements the allocation. Thus the equivalence transformations preserve existence. The `verify.py` certificate generates the orbit of each displayed representative; each orbit has \(48\) paired-order profiles and both orbits are disjoint. Their union has size \(96\) and is exactly the exhaustively computed exceptional set. Their disjointness can also be seen from the invariant pair containing market good \(7\): both subjective rankings put it in the third pair in Type I and in the second pair in Type II.

The probability formula follows by multiplying \(96\) by \(64\) and dividing by \((7!)^2\). For the mean allocation count, a fixed split among the sixteen market-compatible allocations gives bundles of sizes \(3\) and \(4\). Under a uniform subjective ranking, the chance that a fixed three-good bundle satisfies the own-prefix inequalities is \(14/35=2/5\); for a fixed four-good bundle it is \(28/35=4/5\). Independence, symmetry and linearity of expectation give \(16\cdot(2/5)\cdot(4/5)=128/25\), also reproduced by both enumerators.

## Verification

Run `python3 verify.py` (Python 3.10 or newer). Its assertions check \(630\) paired orders, \(396{,}900\) paired-order pairs, \(96\) exceptions, two disjoint orbits of size \(48\), and the exact strict-ranking incidence. It separately tests both representatives against all \(128\) complete allocations, not merely the sixteen known market-feasible ones.

For a distinct full-ranking census, run `g++ -O2 -std=c++17 independent_full.cpp -o independent_full` followed by `./independent_full`. This enumerates all \(25{,}401{,}600\) strict-ranking pairs, checks prefix discrepancies directly, and asserts \(6{,}144\) zero-solution pairs and \(130{,}056{,}192\) total compatible allocations counted with multiplicity. Both exact, deterministic programs were run on their included sources.

## Relationship to prior work

Barman, Ebadian, Latifian and Shah (arXiv:2410.23137, first posted October 30, 2024), Theorem 1, already give **Type I** as a seven-good impossibility example, and their Theorem 2 proves that two agents with at most six goods always admit simultaneous SD-EF1 with market values. Their Lemma 1 explains the common-ranking pair-block characterization used above. These results establish the seven-good boundary but do **not** state its complete two-type obstruction census, its exact uniform probability, or the distinct Type II profile.

Bu, Li, Liu, Song and Tao (arXiv:2310.03475, first posted October 5, 2023), study doubly fair allocations from agents' and an allocator's perspectives, giving EF1 (a weaker criterion) guarantees. Those guarantees neither prohibit nor classify simultaneous **SD-EF1** failures. The present result is an exact classification **inside** the known first impossibility layer, not an independent proof that seven goods are minimal and not a result for the weaker EF1 property.

## Limitations

The classification concerns exactly two agents, exactly seven goods, strict rankings, and complete allocations. Ties can change the SD constraints; the theorem makes no claim for ties, larger markets, or additional agents. The fraction assumes independently uniform **rankings**, not a particular distribution of cardinal values. Orbit equivalence preserves SD-EF1 feasibility rather than all cardinal utility ratios. The finite enumeration is exhaustive in its stated domain; it does not prove a general theorem for arbitrary item counts. Independent scientific validation has not been performed.

## References

1. S. Barman, S. Ebadian, M. Latifian and N. Shah, *Fair Division with Market Values*, arXiv:2410.23137, first public version October 30, 2024. https://arxiv.org/abs/2410.23137
2. X. Bu, Z. Li, S. Liu, J. Song and B. Tao, *Fair Division with Allocator's Preference*, arXiv:2310.03475, first public version October 5, 2023. https://arxiv.org/abs/2310.03475
