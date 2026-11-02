# Exact cactus edge-deletion distance in complete bipartite graphs

## Finding
For integers \(p,q\ge1\), let \(K_{p,q}\) be the simple complete bipartite graph with parts of sizes \(p\) and \(q\). A **cactus** is a connected graph in which every edge belongs to at most one simple cycle. Define the unweighted cactus edge-deletion distance by
\[
\delta_{\mathrm{cact}}(G)=\min\{|F|:F\subseteq E(G),\ G-F\text{ is a connected spanning cactus}\}.
\]
Then, with
\[
\kappa(p,q)=\min\left\{p-1,\ q-1,\ \left\lfloor\frac{p+q-1}{3}\right\rfloor\right\},
\]
**the exact formula for every complete bipartite graph is**
\[
\boxed{\delta_{\mathrm{cact}}(K_{p,q})=(p-1)(q-1)-\kappa(p,q).}
\]
Equivalently, the maximum edge count of a connected spanning cactus subgraph is
\[
\boxed{p+q-1+\kappa(p,q).}
\]
Every optimum contains exactly \(\kappa(p,q)\) cycles, and a maximizer is constructible by a deterministic algorithm using \(O(p+q)\) edge additions (or \(O(pq)\) time to enumerate all deleted edges). The three competing bounds on \(\kappa\) represent the capacities of the two bipartition classes and the total vertex budget. The common general bound from four-cycle block counting is credited to prior work; sharp simultaneous attainment for all bipartition sizes and the resulting distance formula are the claimed result.

## Assumptions and scope
Graphs are finite, undirected, simple, and labelled only for construction and verification. A solution deletes edges, **never vertices**, and the surviving graph must remain connected. The two parts are nonempty; in particular \(K_{1,q}\) is a star and requires no deletions. A cycle in a bipartite graph has even length at least four. Optimality concerns the number of surviving edges, not minimum diameter, girth, weighted costs, or enumeration of all optimizers.

## Proof
**1. The cactus edge identity.** Suppose \(H\) is a connected cactus on \(N\) vertices with \(c\) cycles. Each cyclic block is precisely one simple cycle. Deleting one edge from each cyclic block produces a spanning tree. Hence
\[
|E(H)|=N-1+c.
\]
Thus maximizing retained edges in a spanning cactus is exactly maximizing its number of cycles.

**2. Three necessary cycle bounds.** A connected cactus has a block-cut tree: start at any vertex and traverse blocks away from that root, where each new block meets the previously explored graph in exactly one cut vertex. Every cyclic block in a bipartite cactus has at least two vertices on each side. When a new cyclic block is attached, it therefore introduces at least one new vertex of **each** part and at least three new vertices altogether. Rooting this traversal at a vertex of the first part gives \(p\ge1+c\), rooting at a vertex of the second part gives \(q\ge1+c\), and rooting at any vertex gives \(p+q\ge1+3c\). Consequently,
\[
c\le \min\left\{p-1,q-1,\left\lfloor\frac{p+q-1}{3}\right\rfloor\right\}=\kappa(p,q).
\]
The same bounds hold in the presence of bridge blocks, because bridges only consume additional vertices and create no cycles. This also covers a cactus with no cycles.

**3. Simultaneously sharp construction.** Put \(k=\kappa(p,q)\). If \(k=0\), at least one part has size one. The original \(K_{p,q}\) is then a spanning tree and already optimal. Assume \(k\ge1\). Begin with a four-cycle on two vertices of each part, choosing one distinguished vertex \(A_0\) in the first part and one \(B_0\) in the second.

Set
\[
x=\max\{0,2k-p\},\qquad y=k-1-x.
\]
The three inequalities defining \(k\) give
\[
0\le x\le k-1,\qquad x\le q-k-1.
\]
Indeed \(2k-p\le k-1\) is \(k\le p-1\), while \(2k-p\le q-k-1\) is \(3k+1\le p+q\); the inequalities \(k\le q-1\) handle \(x=0\). Thus \(x,y\) are nonnegative integers.

Attach \(x\) new four-cycles through the single distinguished vertex \(A_0\): each such cycle uses one new vertex of the first part and two new vertices of the second part. Attach \(y\) more four-cycles through \(B_0\): each uses two new vertices of the first part and one new vertex of the second. All introduced vertices are distinct; an attached four-cycle meets the existing graph only at its chosen distinguished vertex. The resulting graph is a cactus with \(1+x+y=k\) cycles and uses exactly
\[
2+x+2y=2k-x\quad\text{first-part vertices},\qquad
2+2x+y=k+1+x\quad\text{second-part vertices}.
\]
By the inequalities above, these quantities are at most \(p\) and \(q\), respectively. Attach every unused first-part vertex by a single edge to \(B_0\) and every unused second-part vertex by a single edge to \(A_0\). These bridge edges preserve the cactus property and make the graph span all \(p+q\) vertices. Every constructed edge is present in \(K_{p,q}\).

The final cactus has exactly \(k\) cycles, so its edge count is \(p+q-1+k\). This matches the bound from Step 2. Since \(K_{p,q}\) has \(pq\) edges, the exact number of deletions is
\[
pq-(p+q-1+k)=(p-1)(q-1)-k,
\]
proving the formula for all \(p,q\ge1\). The construction uses one fixed four-cycle, \(k-1\) attached four-cycles and the remaining vertices as leaves, so its running time is linear in the size of the output cactus.

## Verification
The standalone standard-library script `verify.py` constructs bipartite graphs and checks the cactus property directly using an independent biconnected-block decomposition. It exhaustively examines every edge subset for twenty parameter pairs: all \(1\le p,q\le4\), plus \((2,5)\), \((2,6)\), \((3,5)\), and \((2,7)\), totalling **129226** subset tests. Its exact optimum matches the theorem on every instance. Separately it constructs the proposed optimum for all **900** pairs \(1\le p,q\le30\), checks every edge, connectedness, the block structure, and the number of retained edges. The last lines of a successful run are:

```
CONSTRUCTIVE_CACTI_OK 900 PARAMETER_PAIRS
DIRECT_EXHAUSTIVE_CHECKS_OK 20 PARAMETER_PAIRS 129226 EDGE_SUBSETS
VERIFY_OK
```

Run with `python3 verify.py` on Python 3.8 or later. The independent finite checks corroborate the proof; neither the checks nor the absence of a counterexample establishes the infinite theorem, which follows from Steps 1–3.

## Relationship to prior work
Akhtar and Philip, *Exact Algorithms for Edge Deletion to Cactus* (arXiv:2603.27655, first posted 2026-03-29), formalize the same connected-spanning deletion problem and give exact algorithms for general graphs. Song, *Exact Algorithms for Edge Deletion to Cactus Graphs and Weighted Variants* (arXiv:2606.17578, first posted 2026-06-16), improves the unweighted general algorithm and handles weighted cases. Those algorithms can compute an instance's optimum but do not state an all-parameter closed formula for complete bipartite inputs.

Koch, Pardal, and dos Santos, *Edge deletion to tree-like graph classes* (arXiv:2210.03839; published in *Discrete Applied Mathematics* in 2024), prove hardness even for bipartite input graphs. Their cycle-count argument explicitly uses the general bound \(c\le(N-1)/3\) for bipartite cacti; **that bound is not new here**. The present theorem adds two bipartition-specific bottlenecks, proves their joint sufficiency for every complete bipartite input, and gives the exact deletion optimum and constructive witnesses. Searches of available records did not locate an equivalent explicit biclique specialization. This is a provisional priority assessment, not proof of uniqueness.

## Limitations
This is an unweighted result for complete bipartite input graphs only. It does not classify all optimal spanning cacti, generalize to arbitrary bipartite inputs, or solve weighted deletion. Historical priority may be affected by specialized literature not captured by the searches. The proof and finite verifier have received no independent external mathematical audit.

## References
1. S. S. Akhtar and G. Philip, *Exact Algorithms for Edge Deletion to Cactus*, arXiv:2603.27655, first version 2026-03-29. https://arxiv.org/abs/2603.27655
2. W. Song, *Exact Algorithms for Edge Deletion to Cactus Graphs and Weighted Variants*, arXiv:2606.17578, first version 2026-06-16. https://arxiv.org/abs/2606.17578
3. I. Koch, N. Pardal and V. F. dos Santos, *Edge deletion to tree-like graph classes*, arXiv:2210.03839, first version 2022-10-07; *Discrete Applied Mathematics* 348 (2024), 122–131. https://arxiv.org/abs/2210.03839
