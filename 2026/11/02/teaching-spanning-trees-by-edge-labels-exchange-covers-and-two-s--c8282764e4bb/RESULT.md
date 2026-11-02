# Teaching spanning trees by edge labels: exchange covers and two sharp global thresholds

## Finding

Let \(G=(V,E)\) be any finite connected simple undirected graph with \(n=|V|\ge 2\), and let \(T\) be any spanning tree. The concept class \(\mathcal T(G)\) contains the edge-membership vectors of **all** spanning trees of \(G\). A basic (classical) labeled teaching set for \(T\) is a collection of edge membership answers that uniquely determines \(T\) within this class; write \(\operatorname{td}_G(T)\) for its minimum cardinality.

Construct the bipartite **fundamental-exchange graph** \(X(G,T)\) with parts \(T\) and \(E\setminus T\). Join \(e\in T\) to \(f\notin T\) when \(T-e+f\) is a spanning tree, equivalently when \(e\) lies on the unique \(T\)-path joining the endpoints of \(f\). Then a labeled sample \(S\subseteq E\) teaches \(T\) if and only if \(S\) is a vertex cover of \(X(G,T)\). In particular,

\[
\boxed{\operatorname{td}_G(T)=\tau(X(G,T))=\nu(X(G,T)),}
\]

where \(\tau\) and \(\nu\) denote minimum vertex-cover and maximum matching sizes. The optimal sample, including when each edge has an arbitrary nonnegative query cost, can be computed by bipartite matching or weighted minimum cut, respectively.

Put \(r=n-1\) and \(c=|E|-n+1\). The following global characterizations hold:

1. Every spanning tree satisfies \(\operatorname{td}_G(T)=r\) **if and only if** \(G\) has two edge-disjoint spanning trees.
2. Every spanning tree satisfies \(\operatorname{td}_G(T)=c\) **if and only if** \(E\) can be partitioned into two forests (equivalently, \(G\) has arboricity at most two).

For all positive integers \(p,q\) and all spanning trees \(T\) of the complete bipartite graph \(K_{p,q}\),

\[
\boxed{\operatorname{td}_{K_{p,q}}(T)=\min\{p+q-1,(p-1)(q-1)\}.}
\]

Thus every spanning tree of a given complete bipartite graph has the same basic teaching number. The transition to the tree-size value occurs precisely when both sides have at least three vertices and one side has at least four.

## Assumptions and scope

All graphs are finite, loopless, undirected and simple; connectivity and \(n\ge2\) are assumed. Distinct edges have distinct query coordinates. A teacher knows the target spanning tree and may provide both positive and negative membership labels; the learner must identify it uniquely among *all* spanning trees, not just prefer it over alternatives. This is basic/classical teaching dimension of a specified concept, **not** recursive, no-clash, preference-based, approximate, or online teaching. In the weighted variant the query cost depends only on the queried edge and is nonnegative. Graph edges are not uncertain numerical weights; no minimum-weight spanning-tree objective is involved.

The assertions about all target trees include the case where the graph itself is a tree, in which case the complement of a target is empty and the teaching number is zero.

## Proof

**1. Exchange-cover characterization.** If \(e\in T\), \(f\notin T\), and \(T-e+f\) is a spanning tree, this alternative hypothesis differs from \(T\) at precisely the coordinates \(e,f\). Therefore every teaching sample must contain \(e\) or \(f\): it is a vertex cover of \(X(G,T)\). Conversely, suppose \(S\) covers every exchange edge and a second tree \(T'\ne T\) agrees with \(T\) on \(S\). Choose \(e\in T\setminus T'\). The two components of \(T-e\) must be reconnected by some \(f\in T'\setminus T\), because the only \(T\)-edge crossing this cut is \(e\). Hence \(T-e+f\) is a tree. The disagreement on both \(e\) and \(f\) means neither is in \(S\), contradicting its cover property. This proves the equivalence and, by König's bipartite matching theorem, the minimum-cardinality formula. The same equivalence with nonnegative edge costs is precisely a minimum-weight bipartite vertex-cover problem, solvable as an \(s\)-\(t\) minimum cut with effectively infinite capacities on exchange edges.

**2. The tree-side extremum.** The bound \(\operatorname{td}_G(T)\le r\) follows by teaching all positive edges. By Hall's theorem it is attained precisely when for all \(F\subseteq T\), \(|N_X(F)|\ge |F|\). Removing \(F\) from \(T\) makes \(|F|+1\) connected components. Exactly \(|F|\) tree edges and \(|N_X(F)|\) non-tree edges cross the resulting partition. If \(G\) contains two edge-disjoint spanning trees, the Nash-Williams–Tutte partition criterion gives at least \(2|F|\) cross edges; Hall holds for every \(T\).

Conversely, suppose Hall holds on the tree side for every spanning tree. Given an arbitrary vertex partition, refine each part into connected components of its induced subgraph. This refinement changes neither the number of crossing edges between different original parts nor adds edges within original parts (no edges run between different induced components). For the refined partition, choose spanning trees within the connected parts and connect them by \(k-1\) edges to obtain a spanning tree \(T\) (possible because \(G\) is connected). Let \(F\) be these \(k-1\) connecting edges. Its exchange neighbors are exactly the non-tree edges crossing the refined partition, since every tree path between different parts crosses \(F\), whereas tree paths within a part do not. Hall implies at least \(2(k-1)\) crossing edges. Because the refined partition has at least as many parts as the original and the number of crossing edges is unchanged, the same lower bound holds for the original partition. The Nash-Williams–Tutte criterion yields two edge-disjoint spanning trees.

**3. The cotree-side extremum.** The bound \(\operatorname{td}_G(T)\le c\) follows by teaching all absent edges. Hall's theorem says this bound is attained exactly when \(|N_X(Y)|\ge |Y|\) for every \(Y\subseteq E\setminus T\). Write \(F=N_X(Y)\). Every edge \(f\in Y\) has its complete fundamental \(T\)-path contained in \(F\), so \((V,F\cup Y)\) has exactly the same connected components as \((V,F)\). The latter is a forest with \(|F|\) edges. If \(G\) can be partitioned into two forests, every subgraph with \(v\) vertices and \(k\) components has at most \(2(v-k)\) edges. Applied to \((V,F\cup Y)\), this gives \(|F|+|Y|\le2|F|\), proving Hall for every \(T\).

If \(G\) cannot be partitioned into two forests, the Nash-Williams arboricity criterion supplies a nonempty vertex set \(U\) with more than \(2(|U|-1)\) induced edges. We may take \(G[U]\) connected (one component still violates the bound). Extend a spanning tree of \(G[U]\) to a spanning tree \(T\) of \(G\). Set \(Y=E(G[U])\setminus T\). Then \(|Y|>|U|-1\), while every fundamental path of an edge of \(Y\) lies inside \(U\), and hence \(|N_X(Y)|\le|U|-1\). Hall fails and \(\operatorname{td}_G(T)<c\), as required.

**4. Complete bipartite graphs.** For \(\min(p,q)=1\) the graph is a tree, so \(c=0\) and the claim holds. If \(\min(p,q)=2\), partition edges into the two stars centered at the two vertices of the smaller side, each a forest. For \(K_{3,3}\), on the two sides \(\{0,1,2\}\) and \(\{3,4,5\}\), the five edges \(03,04,05,13,24\) form a spanning tree and the remaining four edges form a forest. Thus the cotree-side theorem applies whenever \(\min(p,q)=2\) or \((p,q)=(3,3)\).

For \(K_{3,4}\), with sides \(\{0,1,2\}\) and \(\{3,4,5,6\}\), the following disjoint spanning trees use all twelve edges: \(T_1=\{03,04,05,13,16,24\}\) and \(T_2=\{06,14,15,23,25,26\}\). For any larger complete bipartite graph having one side of size at least three and the other at least four, add its new vertices one by one, attaching each to two distinct previously present vertices on the opposite side: one new edge in each tree. Disjointness and connectivity persist. The tree-side theorem applies. Comparing \(r=p+q-1\) with \(c=(p-1)(q-1)\) completes the formula for all \(p,q\ge1\).

**5. Why both extremal alternatives are necessary.** Attach a single pendant edge to a vertex of \(K_5\). The pendant edge is a bridge and has no exchange neighbors. The \(K_5\) core admits two edge-disjoint spanning trees, so every target spanning tree has teaching number four, whereas its six-vertex graph has \(r=5\) and \(c=6\). Thus an intermediate teaching number occurs and neither global condition may be discarded.

## Verification

Run `python3 verify_spanning_tree_teaching.py` with any recent Python 3 supporting integer `bit_count`. The checker uses only the standard library. It enumerates every labeled connected simple graph on two through five vertices (771 graph instances, 8,135 target spanning trees), computes the maximum-matching number of every target's exchange graph, and tests both graph-wide extremal equivalences independently using the partition and subgraph-density criteria. For all connected graphs through four vertices, and separately for all spanning trees of \(K_5\) and \(K_{3,3}\), it directly minimizes labeled teaching samples against every competing tree, without consulting the exchange graph. It additionally tests all trees of \(K_{1,4}\), \(K_{2,4}\), \(K_{3,3}\), \(K_{3,4}\), \(K_{3,5}\), and \(K_{4,4}\), and the pendant-\(K_5\) example. The last complete-bipartite test includes 4,096 target trees. The checker ends with `ALL_SPANNING_TREE_TEACHING_CHECKS_PASS` if all assertions hold. No finite enumeration is used as an infinite proof.

## Relationship to prior work

Classical labeled teaching sets and no-clash teaching are different notions. Simon's *Tournaments, Johnson Graphs and NC-Teaching* (first public 2022) supplies a clear basic-teaching definition, but its graph-theoretic results address no-clash teaching and Johnson/tournament families rather than spanning-tree incidence hypotheses. Mansouri et al. (first public 2019) study general preference-based and sequential teaching models; these results do not give the present graph-specific exchange-cover formula. Merino and Soto (first public 2019) optimize queries revealing uncertain **numerical weights** to identify uniformly optimal matroid bases, rather than querying Boolean edge membership of an already fixed target spanning tree. Ordinary basis exchange, König/Hall matching duality, and the Nash-Williams–Tutte spanning-tree-packing and arboricity theorems are classical ingredients, not new claims here. Relevant graph-exchange literature describes elementary exchanges but does not by itself imply the two global teaching extremality characterizations.

## Limitations

The teaching model is **nonadaptive** and identifies a specified target among all spanning trees; this result does not determine online or recursive teaching dimensions, distinguish graphs under unknown topology, or answer uncertain-weight minimum spanning-tree questions. The all-parameter characterization is proved for simple connected graphs and the stated positive/negative membership query model. Weighted optimization is a minimum-cost algorithmic corollary, not a classification of weighted costs by closed formula. Historical priority for these combined graph-teaching statements has not been independently certified; searches cannot establish absolute novelty. This work has not received an independent scientific audit.

## References

- A. I. Merino and J. A. Soto, *The Minimum Cost Query Problem on Matroids with Uncertainty Areas* (first public 2019-04-26), arXiv:1904.11668, https://arxiv.org/abs/1904.11668.
- F. Mansouri, Y. Chen, A. Vartanian, X. Zhu and A. Singla, *Preference-Based Batch and Sequential Teaching: Towards a Unified View of Models* (first public 2019-10-24), arXiv:1910.10944, https://arxiv.org/abs/1910.10944.
- H. U. Simon, *Tournaments, Johnson Graphs and NC-Teaching* (first public 2022-05-05), arXiv:2205.02792, https://arxiv.org/abs/2205.02792.
- M. Mihail and M. Sudan, *Connectivity Properties of Matroids*, UCB/CSD-92-662 (1992), https://www2.eecs.berkeley.edu/Pubs/TechRpts/1992/6143.html.
- C. St. J. A. Nash-Williams, *Edge-Disjoint Spanning Trees of Finite Graphs*, Journal of the London Mathematical Society 36 (1961), 445–450, https://doi.org/10.1112/jlms/s1-36.1.445.
- W. T. Tutte, *On the Problem of Decomposing a Graph into n Connected Factors*, Journal of the London Mathematical Society 36 (1961), 221–230, https://doi.org/10.1112/jlms/s1-36.1.221.
- C. St. J. A. Nash-Williams, *Decomposition of Finite Graphs Into Forests*, Journal of the London Mathematical Society 39 (1964), 12, https://doi.org/10.1112/jlms/s1-39.1.12.
- P. Hall, classical matching criterion; D. König, classical matching–vertex-cover duality (used as standard background).
