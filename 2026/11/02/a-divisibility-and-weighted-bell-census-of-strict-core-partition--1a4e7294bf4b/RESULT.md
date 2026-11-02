# A divisibility and weighted-Bell census of strict-core partitions on degree-two friendship networks

## Finding

Let \(G=(V,E)\) be a finite simple graph of maximum degree at most two, and let \(k\ge 1\) be an integer coalition-capacity bound. Agents in a coalition receive one unit of utility for each of their graph neighbors in that coalition. Both groups in a partition and potential deviating coalitions must have at most \(k\) members. A deviating coalition *weakly blocks* if none of its members loses utility and at least one gains utility; the *strict core* consists of partitions with no weakly blocking coalition.

**Complete classification.** The strict core is nonempty if and only if **every connected component of order greater than \(k\) has order divisible by \(k\)**. When this condition holds, every strict-core partition has the following form, and every partition of this form is strict-core stable:

1. Each path component of order greater than \(k\) is divided into its unique consecutive tiling by \(k\)-vertex blocks.
2. Each cycle component of order greater than \(k\) is divided into one of exactly \(k\) consecutive tilings by \(k\)-vertex blocks.
3. Each component of order at most \(k\) is kept intact. Several such components may share one coalition if and only if their total number of vertices does not exceed \(k\). No other mergers occur.

Consequently, strict-core existence and a witness partition can be found in \(O(|V|+|E|)\) time. For a connected path \(P_n\) the strict-core cardinality is \(1\) if \(n\le k\) or \(k\mid n\), and \(0\) otherwise. For a connected simple cycle \(C_n\), \(n\ge3\), it is \(1\) if \(n\le k\), \(k\) if \(n>k\) and \(k\mid n\), and \(0\) otherwise.

**Exact census for disconnected networks.** Assume the existence condition holds. Let \(c\) be the number of cycle components having more than \(k\) vertices and let \(a_j\) count components of order \(j\), for \(1\le j\le k\). With \(\mathbf a=(a_1,\ldots,a_k)\), define the weighted restricted Bell count

\[
B_k(\mathbf a)=\left(\prod_{j=1}^{k}a_j!\right)
[z_1^{a_1}\cdots z_k^{a_k}]
\exp\!\left(\sum_{\substack{b_1,\ldots,b_k\ge0\\1\le\sum_{j=1}^{k}j b_j\le k}}
\prod_{j=1}^{k}\frac{z_j^{b_j}}{b_j!}\right).
\]

Then the **exact number of strict-core partitions** is

\[
\boxed{|\operatorname{SC}(G,k)|=k^c B_k(\mathbf a).}
\]

When the existence condition fails this number is zero. Equivalently, \(B_k(\mathbf a)\) counts set partitions of the *labeled small components* into coalitions whose total vertex weights do not exceed \(k\). The formula includes isolated vertices and the case \(k=1\).

## Assumptions and scope

The graph is undirected, simple, finite, and has maximum degree at most two; it is therefore a disjoint union of paths and cycles. An isolated vertex is a path of order one. Every edge has symmetric weight one; nonedges have weight zero. There are no negative or heterogeneous values. No minimum group size is imposed.

For an allowed partition \(\Pi\), write \(\Pi(v)\) for the coalition containing \(v\), and set \(u_v(\Pi)=|N_G(v)\cap\Pi(v)|\). An allowed set \(S\subseteq V\), \(1\le |S|\le k\), is a weak blocker exactly when \(u_v(S)\ge u_v(\Pi)\) for every \(v\in S\) and the inequality is strict for at least one of them. This is the usual *strict-core* blocking convention, as opposed to ordinary core stability, which requires every deviator to improve strictly.

The proof permits arbitrary, possibly disconnected coalitions in the initial partition and arbitrary, possibly disconnected blocking sets. The connectedness of blocks in a large component is a **conclusion**, not an imposed rule.

## Proof

**1. Reduction to connected sets.** For any group \(Q\) in an allowed partition, splitting \(Q\) into the connected components of the induced graph \(G[Q]\) leaves every agent's utility unchanged: an agent has no graph neighbors in a different component of \(G[Q]\). Therefore the strict-core status, which depends only on the current utility vector and the allowed deviating sets, is unchanged by this splitting. Likewise, a weakly blocking set may be replaced by one of the connected components of its induced graph: all members of that component retain their prospective utilities, and at least one such component contains a strictly improving member.

**2. A connected component of order at most \(k\) is indivisible.** Suppose a connected graph component \(H\) has at most \(k\) vertices but its vertices do not all share one group. Taking the entire vertex set of \(H\) as a deviating coalition weakly improves every member, because all neighbors inside \(H\) are now together. At least one edge of \(H\) crossed the previous groups, so its endpoints strictly improve. This contradicts strict-core stability. Conversely, a component kept intact gives all its agents their maximum possible degree utility.

**3. All blocks within a larger path or cycle have size exactly \(k\).** Let \(H\) be a path or cycle of order \(n>k\), and split every group into induced connected components. This yields consecutive path blocks, each of size at most \(k\). Suppose one such block \(B\) has size \(\ell<k\). It has a neighboring vertex \(w\) outside \(B\) that is at an end of an adjacent consecutive block. The coalition \(B\cup\{w\}\) is allowed. Every member of \(B\) retains its old internal neighbors; its endpoint adjacent to \(w\) gains an additional neighbor. The vertex \(w\) previously had at most one neighbor in its own consecutive block and now has at least one neighbor in \(B\). Thus nobody loses and somebody gains, a weak block. This contradiction proves that all consecutive blocks have exactly \(k\) vertices. Hence \(k\mid n\).

The same argument applies to every component of a disconnected graph after restricting the partition to that component: a local weak blocker is also a global weak blocker. A group containing one full \(k\)-vertex block cannot contain vertices from any other component, by capacity.

**4. Full consecutive tilings are strict-core stable.** If \(k=1\), no allowed singleton can strictly improve. If \(k=2\), every agent in a full two-vertex block has utility one, the maximum attainable in any group of size at most two. For \(k\ge3\), a full consecutive \(k\)-vertex block of a path or a proper arc of a cycle has internal vertices of utility two and endpoints of utility one. Any strict improvement must occur at an endpoint of such a block whose graph degree is two. A deviating set that improves this endpoint must contain both of its neighbors, including the adjacent internal vertex of utility two. To avoid reducing that internal vertex's utility, the set must contain its other neighbor. Repeating this along the entire original block forces the set to contain all \(k\) block vertices **and** at least one neighboring vertex outside the block, requiring at least \(k+1\) agents. This violates the capacity. Agents in intact small components already have degree utility and cannot improve. By Step 1 it is enough to consider connected deviations, so mixed-component deviations do not invalidate stability.

**5. Exact enumeration.** A path of order \(n>k\) divisible by \(k\) has one consecutive \(k\)-tiling; a cycle of order \(n>k\) divisible by \(k\) has exactly \(k\), classified by the starting offset modulo \(k\). Step 2 forces each small graph component to remain intact, but several can be placed in a single group precisely when their combined order does not exceed \(k\). A large block is full and cannot be merged. Therefore the large cycles contribute the factor \(k^c\). For small components, a coalition containing \(b_j\) components of order \(j\) has size \(\sum_j j b_j\), and is allowed precisely when this sum lies between one and \(k\). The exponential formula for labeled set partitions with these permitted block types is the displayed multivariate generating function. Extracting its coefficient and multiplying by the factorials of the component multiplicities yields \(B_k(\mathbf a)\). The claimed formula follows.

## Verification

The accompanying standalone standard-library script `verify_degree_two.py` constructs every isomorphism type of simple graph of maximum degree at most two on one through eight vertices and checks every coalition capacity from one through the lesser of five and the vertex count. It enumerates **all allowed set partitions**, including groups disconnected in the friendship graph, and all weakly blocking sets. Across 570 graph/capacity instances and 614,381 partition checks, its directly evaluated strict-core counts agree exactly with the proposed formula.

For capacity three, the path on four vertices has zero strict-core partitions, the path on six vertices has one, and the cycle on six vertices has three. A graph consisting of a two-vertex path and two isolated vertices has four partitions in the strict core. These examples test both the arithmetic obstruction and the nontrivial component-grouping count. The exhaustive tests cover only finite orders and do not replace Steps 1–5.

## Relationship to prior work

Levinger, Hazon, Simola, and Azaria's bounded-coalition formulation supplies the exact utility and weak-blocking definitions used here. Their strict-core section proves hardness and exhibits an empty strict core on a clique with one more vertex than the coalition limit, but does not state the degree-two existence criterion or exact census. In the present theorem, already a **path** with \(k+1\) vertices lacks a strict-core partition for \(k\ge2\), showing that high graph density is unnecessary.

Igarashi and Elkind study graph-restricted communication, including strict-core counterexamples and complexity results on trees, but impose a *connected-coalition feasibility rule* rather than the cardinality-restricted positive-friendship domain of this theorem. Their path example and general hardness statements do not determine this capacity divisibility law. Hanaka, Köhler, and Lampis investigate the **ordinary** core and its bounded-*deviation* variant; those notions use strictly improving blockers and do not bound all groups, so their results do not imply a strict-core census.

## Limitations

The unit positive edge assumption is essential to the stated classification; arbitrary heterogeneous edge weights, negative values, graph degree greater than two, or alternative blocking conventions are not covered. The weighted Bell expression is an exact count, not a claim of polynomial-time counting with \(k\) variable. No general classification of strict-core partitions on trees of higher maximum degree is asserted. Literature priority is conditional on the inspected sources and searches; an earlier equivalent classification under different hedonic-game terminology remains possible. No external independent audit has been performed.

## References

1. C. Levinger, N. Hazon, S. Simola, A. Azaria, *Socially Aware Coalition Formation with Bounded Coalition Size*, arXiv:2306.01378, initial public submission 2 June 2023, https://arxiv.org/abs/2306.01378 . Sections 3, 5.2, and Appendix A.5.
2. A. Igarashi and E. Elkind, *Hedonic Games with Graph-restricted Communication*, AAMAS 2016, pp. 242–250, https://www.ifaamas.org/Proceedings/aamas2016/pdfs/p242.pdf . Sections 2, 3, and 5.2.
3. T. Hanaka, N. Köhler, M. Lampis, *Core Stability in Additively Separable Hedonic Games of Low Treewidth*, arXiv:2402.10815v1, 16 February 2024, https://arxiv.org/html/2402.10815v1 . Sections 2 and 5.
