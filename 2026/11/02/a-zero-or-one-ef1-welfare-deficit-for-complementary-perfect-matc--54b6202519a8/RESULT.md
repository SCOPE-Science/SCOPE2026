# A zero-or-one EF1 welfare deficit for complementary perfect-matchings

## Finding

For two agents whose utilities count completed complementary pairs from respective perfect matchings, the exact loss of maximum utilitarian welfare under envy-freeness up to one good (EF1) is always zero or one. Let the union of their matchings decompose into alternating connected components of sizes \(2k_1,\ldots,2k_r\), including double-edge components for shared pairs, and put \(K=\sum_j k_j\). The maximum welfare is \(K\), and the **complete-EF1** maximum is
\[
\operatorname{OPT}_{\mathrm{EF1}}=\begin{cases}K,&\text{if }\exists J\subseteq\{1,\ldots,r\},\ |2\sum_{j\in J}k_j-K|\le 1,\\K-1,&\text{otherwise.}\end{cases}
\]
An EF1 optimum can be constructed in \(O(K^2)\) time, including a balanced-subset-sum test. The welfare loss one is attained already by two distinct complementary matchings on four goods.

## Assumptions and scope

There are exactly two agents, \(A\) and \(B\), and a finite good set \(G\) of \(2K\ge 2\) goods. Each agent \(i\) supplies a perfect matching \(M_i\) on \(G\) and has valuation \(v_i(S)=|\{e\in M_i:e\subseteq S\}|\) for any good bundle \(S\subseteq G\). Goods are allocated completely and disjointly as \((X_A,X_B)\). Welfare is \(U=v_A(X_A)+v_B(X_B)\). EF1 means, for each ordered pair of different agents \(i,j\), that \(v_i(X_i)\ge v_i(X_j\setminus\{g\})\) for some \(g\in X_j\), with an empty bundle interpreted as non-envious automatically. Parallel matching edges are retained when the two perfect matchings contain the same pair. Each connected component of their edge-colored multigraph is an even alternating cycle, including two-vertex cycles. Define \(k_j\) as half its vertex count; then \(\sum_jk_j=K\).

## Proof

**Upper bound and equality structure.** Every pair counted in \(U\) uses two items owned by that pair's matching agent. The counted pairs are vertex-disjoint because the owned good bundles are disjoint and each matching itself has disjoint edges. Hence \(U\le K\). Allocating every good to \(A\) attains \(K\). If \(U=K\), its counted pairs cover every item and collectively form a perfect matching assembled from edges of \(M_A\) or \(M_B\), with each edge assigned to its matching's agent. On a connected alternating cycle the only possible edge-perfect-cover choices are the two alternating color classes (in a two-vertex double-edge component either colored edge is permissible). Therefore each component is awarded **entirely** to one agent. Conversely, assigning components whole to their corresponding agents yields welfare \(K\).

**EF1 at maximum welfare.** If whole components indexed by \(J\) go to \(A\), set \(s=\sum_{j\in J}k_j\). Since either perfect matching contributes exactly \(k_j\) edges on each whole component, the four valuations satisfy \(v_A(X_A)=v_B(X_A)=s\) and \(v_A(X_B)=v_B(X_B)=K-s\). Removing one item from a nonempty bundle with positive valuation reduces its value by exactly one for the evaluating agent: the valuation counts vertex-disjoint pairs. Thus the whole-component allocation is EF1 exactly when \(s\ge K-s-1\) and \(K-s\ge s-1\), equivalently \(|2s-K|\le1\). This proves the first case and rules out welfare \(K\) in the other case.

**Construction with one lost pair.** Suppose no subset of component weights achieves this balance. Put \(T=\lfloor K/2\rfloor\). List the components arbitrarily and find the first prefix with accumulated weight exceeding \(T\). Write \(s\) for the sum before its crossing component, whose weight is \(k\). Since equality \(s=T\) or a prefix with total \(T\) would already be balanced, \(s<T<s+k\), so \(a=T-s\) lies in \(\{1,\ldots,k-1\}\). Give earlier whole components to \(A\), later whole components to \(B\). Label crossing-cycle vertices cyclically \(0,1,\ldots,2k-1\) with \(M_A\)-edges \((0,1),(2,3),\ldots,(2k-2,2k-1)\) and \(M_B\)-edges \((1,2),(3,4),\ldots,(2k-1,0)\). Give vertices \(0,\ldots,2a\) to \(A\) and the remaining \(2a+1,\ldots,2k-1\) to \(B\).

On that split component the agent-owned pair utilities are \(a\) for \(A\) and \(k-a-1\) for \(B\); the values each attributes to the other bundle are respectively \(k-a-1\) and \(a\). These are obtained by explicitly enumerating the internal edges of each matching on the two intervals, not from an assumption of additivity across goods. The other components also have the property that each agent's valuation of a bundle equals its recipient's actual utility on that bundle. In the resulting complete allocation, therefore,
\[
 v_A(X_A)=v_B(X_A)=T,\qquad v_A(X_B)=v_B(X_B)=K-1-T.
\]
Its welfare is \(K-1\). The absolute difference \(|T-(K-1-T)|\) is at most one, so removing one endpoint of any pair valued in an envied bundle removes the entire possible envy, proving EF1. Together with the exclusion of welfare \(K\), this construction is optimal.

**Complexity.** Find the alternating components in linear time. A boolean subset-sum dynamic program on \(r\) positive integer weights totaling \(K\) determines whether a balanced subset exists, and gives an assigning witness, in \(O(rK)\subseteq O(K^2)\) time. If it does, award each component accordingly. Otherwise use the crossing-component construction. All allocations output are complete.

## Verification

The companion `verify.py` enumerates all labeled second-agent matchings against the canonical first-agent matching, and all \(2^{2K}\) allocations, up to \(K=5\). It directly tests EF1 from the four pair counts and compares the optimum with the component-subset-sum formula. The run passed for \(K=1,2,3,4,5\), testing \(1,3,15,105,945\) matching instances respectively and \(995572\) complete allocations total. This is finite corroboration; the proof above, not enumeration, establishes every \(K\).

For sharpness, take four goods \(\{1,2,3,4\}\), matching \(M_A=\{\{1,2\},\{3,4\}\}\) and \(M_B=\{\{1,3\},\{2,4\}\}\). Their union forms a single four-cycle, with weight \(k_1=2\). No subset weight balances \(K=2\), so the unrestricted maximum is \(2\) while the EF1 maximum is \(1\).

## Relationship to prior work

Pyne, Viswanathan, Yang and Zick (arXiv:2610.15801v1, 2026-10-11) introduce dichotomous item-complement valuations and exhibit the two-agent four-good cross-matching obstruction to simultaneous EF1 and Pareto optimality. Their general approximation and hardness results concern a wider class, while this result gives a complete all-size exact utilitarian welfare/EF1 frontier under the structural restriction that both agents' desired pairs form perfect matchings. The sharp four-good obstruction is already their prior work, not a claimed new example. The contribution here is the arbitrary-size classification by cycle weights and a constructive optimum with at most one lost completed pair. General EF1 existence results for additive **item** valuations do not apply directly because a single item has zero marginal value until its mate arrives.

## Limitations

The theorem is confined to two agents, unit-valued complements of size two, and perfect-matching complement collections. It does not assert EF1–Pareto-optimal compatibility when the deficit is one, nor extend to overlapping desired pairs, unequal pair weights, more agents, or stronger fairness notions. Subset-sum balancing is pseudo-polynomial in encoded cycle weights, but here \(K\) is itself the number of item pairs supplied explicitly, so the algorithm is polynomial in input size. Equivalent results might occur in literature using different graph-theoretic terminology; no publication-priority claim follows solely from search absence.

## References

1. Pyne, Viswanathan, Yang and Zick, *Fair Allocation with Dichotomous Preferences over Item Complements*, arXiv:2610.15801v1 (first public 2026-10-11). https://arxiv.org/abs/2610.15801.
2. Lipton, Markakis, Mossel and Saberi, *On Approximately Fair Allocations of Indivisible Goods*, EC 2004 (general EF1/approximate envy-freeness framework, not item complement welfare frontier).
