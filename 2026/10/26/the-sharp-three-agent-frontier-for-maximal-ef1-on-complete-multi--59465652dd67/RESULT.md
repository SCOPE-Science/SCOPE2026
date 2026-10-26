# The sharp three-agent frontier for maximal EF1 on complete multipartite conflict graphs

## Finding

Let a finite collection of indivisible goods be the vertices of a **complete multipartite** conflict graph, with any number of nonempty parts and arbitrary part sizes. Three agents have the **same normalized monotone valuation** \(v:2^M\to\mathbb R_{\geq0}\); neither additivity nor strict monotonicity is assumed. Every such instance admits a feasible, maximal, envy-free-up-to-one-good (EF1) partial allocation. Given the multipartite partition, an allocation can be constructed using \(O(|M|)\) queries to the common valuation function.

The number of agents is sharp for this class: four agents can fail even with identical strictly positive additive valuations on \(K_{3,3}\), using singleton values \(2\) on one side and \(3\) on the other. This four-agent obstruction was established previously; the new assertion is universal three-agent existence for arbitrary common monotone set valuations on all complete multipartite conflict graphs.

## Assumptions and scope

Let \(M\) be a finite set partitioned into nonempty parts \(P_1,\dots,P_r\), where \(r\geq1\). The conflict graph has an edge between two distinct goods exactly when they lie in different parts. Thus an independent bundle can contain goods from only one part. Let \(v(\varnothing)=0\) and \(v(S)\leq v(T)\) whenever \(S\subseteq T\subseteq M\). Every agent uses this same set function, and \(v\) is accessed by a value oracle when discussing query complexity.

A feasible allocation consists of pairwise disjoint independent bundles \(A_1,A_2,A_3\), which need not exhaust \(M\). It is **maximal** if every unallocated good conflicts with at least one good in **each** agent's bundle. It is **EF1** if for every ordered pair of agents \((i,j)\), either \(A_j=\varnothing\) or there is \(g\in A_j\) with \(v(A_i)\geq v(A_j\setminus\{g\})\). For a graph with no goods, the all-empty allocation has both properties.

## Proof

**Lemma (last-received-item).** Allocate a finite set of goods in any order among three agents; each incoming good is given to an agent of minimum **current common bundle value**. Break ties in favor of agents with empty bundles. The resulting allocation is EF1, and if at least three goods are allocated then all three bundles are nonempty. Indeed, the first three goods go to distinct agents: an empty bundle has value zero, the minimum by nonnegativity, and wins any tie with a nonempty bundle. For any recipient \(j\) with nonempty final bundle, let \(g\) be the last good given to \(j\). Immediately before assigning \(g\), the algorithm chose \(j\) so \(v(A_j^{\mathrm{before}})\leq v(A_i^{\mathrm{before}})\) for every \(i\). Monotonicity gives \(v(A_i^{\mathrm{final}})\geq v(A_i^{\mathrm{before}})\), and because \(g\) was last for \(j\), \(A_j^{\mathrm{final}}\setminus\{g\}=A_j^{\mathrm{before}}\). This is exactly the required EF1 inequality for all \(i\). The lemma needs neither additivity nor positive singleton values.

**Case 1: a part contains at least three goods.** Select one such part \(P\), distribute *all* its goods by the last-received-item rule, and leave every other part unallocated. Bundles are independent and nonempty; the lemma gives EF1. Each omitted good belongs to a different part and hence conflicts with a good in every bundle, establishing maximality.

**Case 2: every part has size at most two, and there is a doubleton.** If this doubleton is the only part, allocate its goods to two distinct agents and nothing to the third; the allocation is complete and EF1. Otherwise choose a doubleton \(P=\{a,a'\}\) maximizing \(\min\{v(\{a\}),v(\{a'\})\}\) among all doubleton parts. Choose any other part \(Q\), containing one or two goods. Give \(a\) to agent 1, \(a'\) to agent 2, and all of \(Q\) to agent 3; omit the remaining parts. Every bundle is a nonempty independent set, and each unallocated good conflicts with a good in every bundle, so maximality holds.

To verify EF1, comparison against either singleton bundle is automatic: remove that singleton to leave value zero. If \(|Q|=1\), comparison against the third bundle is automatic too. If \(Q=\{b,b'\}\), removing the better of its two singleton goods leaves a bundle of value \(\min\{v(\{b\}),v(\{b'\})\}\). The choice of \(P\) ensures that each of \(v(\{a\})\) and \(v(\{a'\})\) is at least this number. Thus neither singleton recipient envies agent 3 up to one good. All comparisons satisfy EF1.

**Case 3: all parts are singletons.** Allocate one good from each of up to three different parts, one per agent. If fewer than three parts exist, all goods are allocated, so maximality is immediate. Otherwise all three agents have singleton bundles, so any omitted good conflicts with an item in every bundle. In either situation EF1 holds because every nonempty bundle contains just one good and removing it leaves the empty bundle. This includes all remaining cases.

Each construction scans the partition only a constant number of times, with at most three bundle-value queries per good in Case 1. Therefore it uses \(O(|M|)\) valuation-oracle calls, assuming the parts are supplied explicitly.

**Sharpness (previously known four-agent example).** Let the conflict graph be \(K_{3,3}\), with three goods of singleton value \(2\) on one side and three of value \(3\) on the other, with the same additive valuation for four agents. Every maximal allocation is complete: an unallocated good has exactly three neighbors, so among four agents some agent has no conflicting assigned neighbor and could accept it. In any complete feasible allocation, let \(t\) be the number of agents receiving at least one value-\(3\) good. Because both sides must be assigned, \(1\leq t\leq3\). For \(t=1\), one agent receives all three value-\(3\) goods, while one of the other three agents has value at most \(2\); removing one good from that triple leaves \(6\). For \(t=2\), one of the two agents receives at least two value-\(3\) goods, while one of the other two agents has value at most \(2\); removing one leaves at least \(3\). For \(t=3\), the sole agent without a value-\(3\) good receives all three value-\(2\) goods, leaving \(4\) after removing one, whereas each other agent has value \(3\). Each case violates EF1. Hence four agents do not have a universal guarantee even for positive additive valuations.

## Verification

The standalone script `verify.py` implements the construction, an independently expressed feasibility/maximality/EF1 checker, and the four-agent contrast. It was executed from the supplied package and reported:

```text
PASS exhaustive 187375 instances; branch counts {'large': 141858, 'doubleton': 35676, 'singleton': 9841}
PASS randomized 6000 instances
PASS common monotone set valuation 4885 instances
PASS four-agent K(3,3) contrast; 420 maximal allocations, none EF1
```

The exhaustive additive test covers every integer partition of up to eight goods into unlabeled part sizes and every singleton-value vector in \(\{0,1,2\}^{|M|}\). The monotone test includes all \(167\) normalized monotone Boolean set functions on four goods over the five unordered part-size profiles, plus random normalized monotone functions obtained as upward envelopes of arbitrary set scores, on up to eight goods. These finite tests support the construction; the unbounded theorem follows from the preceding proof rather than enumeration.

## Relationship to prior work

Igarashi, Manurangsi and Yoneda (2025, arXiv:2506.14149) established a two-agent maximal-EF1 theorem on arbitrary conflict graphs, found a three-agent nonexistence instance for general identical monotone valuations, and explicitly left the three-agent identical **additive** case open. Equbal et al. (2026, arXiv:2605.09930) consolidated that framework and obtained further results for paths, trees, and hardness. Neither paper's arbitrary-graph two-agent guarantee or path/tree results entails three-agent maximal EF1 for arbitrarily large complete multipartite graphs with nonuniform, nonadditive common valuations. The published three-agent counterexample has a conflict graph that is not complete multipartite.

Hummel and Hetland (2021/2022) showed the four-agent \(K_{3,3}\) obstruction for **complete** EF1 allocations, which also rules out maximal EF1 in that example because maximality forces completeness. The negative half of the sharp agent boundary is therefore prior art, and is included solely to contextualize the positive theorem. These references and available mathematical-results records did not identify a stronger theorem implying the complete-multipartite three-agent statement; the absence of a hit is not a proof of publication priority.

## Limitations

The theorem assumes three agents with **identical**, normalized, monotone set valuations and a **complete** multipartite conflict graph. It does not assert completeness of the constructed allocation, efficiency beyond maximality, EFX, or any guarantee for heterogeneous valuations, general conflict graphs, or nonmonotone valuations. The broader three-agent additive existence question on arbitrary conflict graphs remains open in the motivating sources. The known four-agent negative example is not independently original. Value-oracle complexity ignores the cost of evaluating an oracle or recognizing a multipartite decomposition when not supplied.

## References

1. A. Igarashi, P. Manurangsi, and H. Yoneda, *Dividing Conflicting Items Fairly*, arXiv:2506.14149v1, public 17 June 2025. https://arxiv.org/abs/2506.14149
2. S. Equbal et al., *Fair Allocation under Conflict Constraints*, arXiv:2605.09930v1, public 11 May 2026. https://arxiv.org/abs/2605.09930
3. H. Hummel and M. L. Hetland, *Fair allocation of conflicting items*, published 23 December 2021, Autonomous Agents and Multi-Agent Systems 36:8 (2022), DOI 10.1007/s10458-021-09537-3. https://doi.org/10.1007/s10458-021-09537-3
