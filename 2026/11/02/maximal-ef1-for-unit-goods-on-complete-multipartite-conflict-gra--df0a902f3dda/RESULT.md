# Maximal EF1 for unit goods on complete multipartite conflict graphs with arbitrarily many agents

## Finding

**Theorem.** Let \(G\) be any finite nonempty complete multipartite graph, with arbitrary positive part sizes, and let \(n\ge4\) be any integer. With \(n\) agents sharing the identical unit additive valuation \(v_i(S)=|S|\) for every bundle \(S\), there exists a feasible **maximal EF1 partial allocation**, computable deterministically in \(O(m+n+r\log r)\) time from the part partition, where \(m=|V(G)|\) and \(r\) is its number of nonempty parts. Equivalently, every such graph has a maximal equitable partial coloring with exactly \(n\) labeled color classes, some possibly empty.

The construction is valid for every \(n\ge1\), although the substantive additional agent range here is \(n\ge4\). When the largest part has fewer than \(n\) items and there are at least \(n\) items in total, all \(n\) resulting classes have size one or two and the algorithm colors at most \(2n-2\) items. The ability to leave items unassigned can be necessary: \(K_{3,3,3}\) with \(n=4\) admits such a maximal equitable partial coloring, but has no *complete* equitable four-coloring.

## Assumptions and scope

A complete multipartite graph is a graph whose nonempty vertex parts \(P_1,\dots,P_r\) induce no edges, with every pair of vertices in distinct parts adjacent. A feasible allocation is a family of pairwise-disjoint independent bundles \((A_1,\dots,A_n)\); goods outside their union may remain unassigned. It is maximal if for every unassigned vertex \(x\) and every agent \(j\), \(A_j\cup\{x\}\) is not independent. It is EF1 if for all agents \(i,j\), either \(A_j=\varnothing\), or some \(x\in A_j\) satisfies \(v_i(A_i)\ge v_i(A_j\setminus\{x\})\). For unit additive valuations this is exactly \(\max_j|A_j|-\min_j|A_j|\le1\).

Let part sizes, after sorting, be \(a_1\ge a_2\ge\dots\ge a_r\ge1\), and write \(m=\sum_i a_i\). All items are valued exactly one by all agents; heterogeneous positive item weights and general conflict graphs are not included.

## Proof

**Case 1: \(m\le n\).** Assign each of the \(m\) vertices to a different agent. Every bundle has size at most one, so EF1 holds; no item is unassigned, so maximality is automatic. Every singleton is independent.

**Case 2: \(m>n\) and \(a_1\ge n\).** Assign every vertex of the first part \(P_1\) among the \(n\) agents by round-robin, making all class sizes either \(\lfloor a_1/n\rfloor\) or \(\lceil a_1/n\rceil\). Each class is nonempty and contained in \(P_1\), hence independent. Any unassigned vertex lies in another part and is adjacent to every class. Therefore the partial allocation is maximal and equitable.

**Case 3: \(m>n\) and \(a_1<n\).** Let \(s\ge2\) be the smallest index such that \(\sum_{i=1}^s a_i\ge n\); put \(B=\sum_{i=1}^{s-1}a_i<n\) and \(t=a_s\le a_1\). Define integer lower quotas \(\ell_i=\lceil a_i/2\rceil\) for \(1\le i\le s\). Then

\[
\begin{aligned}
\sum_{i=1}^s\ell_i
&=B-\sum_{i=1}^{s-1}\lfloor a_i/2\rfloor+\lceil t/2\rceil\\
&\le B-\lfloor a_1/2\rfloor+\lceil t/2\rceil\\
&\le B+1\le n.
\end{aligned}
\]

The penultimate inequality uses \(t\le a_1\), hence \(\lceil t/2\rceil-\lfloor a_1/2\rfloor\le1\). Since \(\sum_{i=1}^s a_i\ge n\), choose integers \(q_i\) with \(\lceil a_i/2\rceil\le q_i\le a_i\) and \(\sum_{i=1}^s q_i=n\), by starting at the lower quotas and greedily increasing them within their respective upper bounds. Every \(P_i\), for \(i\le s\), can be partitioned into precisely \(q_i\) nonempty subsets of sizes one or two: use \(a_i-q_i\) pairs and \(2q_i-a_i\) singletons. Allocate these \(\sum_iq_i=n\) subsets bijectively to the agents, and leave the parts with index above \(s\) unassigned.

Every assigned bundle is independent and every agent receives one or two goods, proving EF1. Every unassigned vertex belongs to a part distinct from every assigned bundle's part, and hence conflicts with at least one item of every nonempty bundle; maximality follows. The number colored is \(\sum_{i=1}^s a_i=B+t\le(n-1)+(n-1)=2n-2\).

The cases exhaust all \(m,n\), proving existence. Constructing and sorting the parts, forming quotas, and writing all \(n\) bundles takes \(O(m+n+r\log r)\) time.

**Why partiality is genuinely needed.** For \(G=K_{3,3,3}\), a complete equitable four-coloring of nine vertices would have one class of size three and three classes of size two. Each class must lie wholly within one of the three parts, yet a part of size three cannot be assembled from size-two classes; consequently each of three parts would require its own size-three class, contradiction. For a maximal equitable partial coloring, select two parts and split each three-vertex part into one pair and one singleton. This produces four classes of sizes \(2,1,2,1\), leaving the third part uncolored; every left-out vertex conflicts with every class.

## Verification

The accompanying `verify_multipartite.py` independently constructs the bundles and checks (a) disjointness and graph independence, (b) unit-value EF1 via maximum-minus-minimum bundle size, (c) maximality by testing every unallocated vertex against each bundle, and (d) the case-three colored-vertex bound. Its deterministic exhaustive bounded families and seeded randomized families tested **7,517** graph/agent instances, of which **5,118** left some items unallocated. All checks passed. These finite checks supplement, but do not replace, the proof above.

## Relationship to prior work

Equbal et al., *Fair Allocation under Conflict Constraints* (arXiv:2605.09930, originally submitted 11 May 2026), Section 5.3, define maximal equitable partial coloring, prove existence for trees, and leave arbitrary graphs open. The present theorem proves an infinite non-tree family, covering all complete multipartite graphs and arbitrary numbers of agents with unit values, including parameters that do not admit complete equitable colorings.

Hummel and Hetland, *Fair allocation of conflicting items* (published online 23 December 2021), Proposition 5, establish complete equitable colorability when the number of agents exceeds the conflict graph's maximum degree; this does not imply the present case with fewer agents or the no-complete-coloring example. Their Example 1 and Proposition 3 show that replacing uniform values with heterogeneous common positive item weights can destroy EF1 even for complete bipartite graphs. Haviv, *Fair Allocation under Conflict Constraints via Strong Colorability* (arXiv:2607.01059, 1 July 2026), develops sufficient conditions for complete fair allocations through strong coloring; those conditions do not supply the required partial allocation where complete equitability fails. Earlier work separately covers the three-agent case for the same graph family under stronger identical monotone valuations; the new range highlighted here is four or more agents.

## Limitations

Only uniform positive goods and identical additive valuations are proved. The result makes no existence claim for heterogeneous item weights, mixed goods and chores, nonmultipartite conflict graphs, EFX, or Pareto-efficient allocations. An equitable complete coloring need not exist. The algorithm may leave goods unassigned and does not optimize the number assigned or social welfare. The elementary integer-quota argument may have equivalent antecedents in unindexed graph-coloring literature; publication priority is not independently certified.

## References

1. S. Equbal et al., *Fair Allocation under Conflict Constraints*, arXiv:2605.09930, v1 publicly submitted 11 May 2026, Section 5.3. https://arxiv.org/abs/2605.09930
2. H. Hummel and M. L. Hetland, *Fair allocation of conflicting items*, *Autonomous Agents and Multi-Agent Systems* 36 (2022), article 8; published online 23 December 2021. DOI:10.1007/s10458-021-09537-3. https://link.springer.com/article/10.1007/s10458-021-09537-3
3. I. Haviv, *Fair Allocation under Conflict Constraints via Strong Colorability*, arXiv:2607.01059, v1 publicly submitted 1 July 2026. https://arxiv.org/abs/2607.01059
