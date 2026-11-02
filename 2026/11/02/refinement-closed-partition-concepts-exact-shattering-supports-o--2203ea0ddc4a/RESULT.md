# Refinement-closed partition concepts: exact shattering supports, online dimension, and coloring quotients

## Finding

Let \(V\) be a finite nonempty set and let \(\mathcal F\) be a nonempty family of partitions of \(V\), closed under refinement: if \(\pi\in\mathcal F\) and \(\rho\) refines \(\pi\), then \(\rho\in\mathcal F\). A concept \(h_\pi\) on unordered distinct pairs \(\{u,v\}\subseteq V\) outputs \(1\) when \(u,v\) belong to the same block of \(\pi\) and \(0\) otherwise.

**Support theorem.** A set \(S\) of such pairs is VC-shattered by \(\{h_\pi:\pi\in\mathcal F\}\) if and only if (i) the simple graph \((V,S)\) is a forest and (ii) the partition \(\pi_S\) into its connected components lies in \(\mathcal F\).

**Exact static/online dimension theorem.** Writing \(b(\pi)\) for the block count,
\[
\operatorname{VCdim}(\mathcal F)=\operatorname{Ldim}(\mathcal F)=|V|-\min_{\pi\in\mathcal F}b(\pi).
\]
Here Littlestone dimension refers to deterministic realizable online prediction for the **same pair-equality instance domain**, not the number of queries required to identify the entire hidden partition.

**Conditional theorem.** These results remain exact following any finite consistent sequence of labeled pair observations: contract every positive-observation connected component, retain the negative observations as nonmerger constraints, and apply the same results to the resulting nonempty refinement-closed family of partitions of the contracted vertices. Queries within already contracted components are constants, and pair queries between components have identical answer patterns whenever their quotient pair is the same.

**Graph-coloring specialization.** For a finite simple graph \(G=(V,E)\), let \(\mathcal C(G)\) be all partitions into independent sets of \(G\); these are proper color classes when unused color names are ignored. Then
\[
\operatorname{VCdim}(\mathcal C(G))=\operatorname{Ldim}(\mathcal C(G))=|V|-\chi(G).
\]
A pair-query set is shattered exactly when its graph is a forest whose connected components are independent in \(G\). After any consistent positive/negative transcript, construct a quotient constraint graph \(H\): identify positive-connected vertices and place an edge between two quotient vertices whenever an original edge of \(G\), or a negative observation, prohibits their merger. If \(m=|V(H)|\), both dimensions of the residual concept class equal \(m-\chi(H)\). These are *exact version-space identities*, not merely bounds.

## Assumptions and scope

All sets, graphs, partitions, and transcripts are finite; the partition family is explicitly **nonempty and closed under every refinement**. A partition \(\rho\) refines \(\pi\) when every block of \(\rho\) is contained in a block of \(\pi\). All queried pairs consist of distinct unordered vertices. Duplicate queries carry no extra coordinate information. VC dimension is the greatest cardinality of a fixed shattered subset of the instance domain; Littlestone dimension is the greatest depth of a full binary mistake/shattering tree with a common queried pair at each node, potentially dependent on preceding labels. A consistent transcript has at least one realizing partition. The graph-coloring specialization uses unbounded numbers of anonymous color classes, **not** a predetermined exact number of named colors.

## Proof

**1. Cycle obstruction.** Suppose the graph with edge set \(S\) has a cycle. Label all but one cycle edge \(1\) and the remaining edge \(0\). The positive cycle edges connect the endpoints of the negative edge, so equivalence-relation transitivity forbids that labeling. Consequently every shattered support is a forest.

**2. The component partition condition.** If \(S\) is shattered, some \(\pi\in\mathcal F\) realizes its all-ones labeling. Every connected component of \((V,S)\) is within one block of \(\pi\), so \(\pi_S\) refines \(\pi\); refinement closure gives \(\pi_S\in\mathcal F\). Conversely assume \(S\) is a forest and \(\pi_S\in\mathcal F\). For any assigned positive-edge subset \(T\subseteq S\), the connected-component partition \(\pi_T\) refines \(\pi_S\), so belongs to \(\mathcal F\). Every edge in \(T\) is within one block, and, because \(S\) is acyclic, every edge in \(S\setminus T\) joins distinct components of \((V,T)\). Thus \(\pi_T\) realizes precisely the designated labeling. This proves the iff characterization, including isolated vertices and the empty support.

**3. VC extremum.** Put \(r=|V|-\min_{\pi\in\mathcal F}b(\pi)\). For any shattered \(S\), its forest has exactly \(|V|-|S|\) components, and by Step 2 its component partition belongs to \(\mathcal F\). Therefore \(|S|\le r\). Choose a partition \(\pi_*\) realizing the minimum block count. A spanning tree in each block of \(\pi_*\), combined over blocks, is a forest \(S_*\) with \(\pi_{S_*}=\pi_*\) and exactly \(r\) edges, shattered by Step 2. Hence \(\operatorname{VCdim}=r\).

**4. Online upper bound.** Maintain the connected components of all positively labeled queried pairs so far. When asked about a pair already connected by positive observations, predict \(1\); for any other pair, predict \(0\). On any realizable sequence, positive-observation connectivity implies true equivalence in the fixed target partition, so the first kind of prediction never errs. Every error is a target-positive response joining two previously different maintained components. Thus each error strictly reduces the maintained component count. More strongly, if the target partition has \(k\) blocks, positive connections never merge different target blocks, so at most \(|V|-k\le r\) errors are possible. A depth-\(r+1\) shattered tree would force \(r+1\) mistakes against any deterministic predictor by following the opposite edge at each node, contradiction. Therefore \(\operatorname{Ldim}\le r\). Every VC-shattered set of size \(r\) yields a depth-\(r\) Littlestone tree by querying these coordinates in the same fixed order, so \(\operatorname{Ldim}\ge r\), completing equality. No assumption that an offline optimization algorithm knows \(r\) is used.

**5. Consistent histories.** Let \(P\) be the equivalence relation generated by positively observed pairs and let \(Q=V/P\), of size \(m\). Every partition still consistent with the observations must coarsen \(P\). Such partitions correspond bijectively to partitions \(\sigma\) of \(Q\) in which negatively observed quotient pairs lie in distinct blocks and whose pullback belongs to \(\mathcal F\). Call this nonempty family \(\mathcal F_Q\). If \(\sigma\in\mathcal F_Q\) and \(\tau\) refines \(\sigma\) on \(Q\), the pullback of \(\tau\) refines the pullback of \(\sigma\), and splitting cannot violate negative constraints. Hence \(\mathcal F_Q\) is refinement closed. Reapply Steps 1–4 on \(Q\). Each unordered pair of different quotient vertices is represented by an original pair and has the same label under each consistent hypothesis, so the true residual VC and Littlestone dimensions agree with those on \(Q\), with no loss from duplicated original queries.

**6. Coloring quotient.** Partitions into independent vertex sets of \(G\) form a nonempty refinement-closed family. The least block count of such a partition is the chromatic number \(\chi(G)\), yielding \(|V|-\chi(G)\). By Step 2, \(\pi_S\) is feasible exactly when each forest component is an independent set in \(G\). After contracting positives, two quotient blocks can be merged precisely when no forbidden original graph edge or observed negative pair crosses them; the family of permissible partitions is therefore exactly the family of independent-set partitions of the quotient graph \(H\). The conditional formula follows from Step 5 and the chromatic specialization.

**7. Further natural constraint.** If \(\mathcal F\) consists of partitions whose blocks have size at most a fixed integer \(b\ge1\), the minimum block count is \(\lceil |V|/b\rceil\). Therefore both dimensions are \(|V|-\lceil|V|/b\rceil\); the shattered supports are exactly forests whose components have at most \(b\) vertices. This holds for every finite \(V\).

## Verification

A standalone standard-library Python checker, `verify_partition_rank.py`, exhaustively constructs each of the \(1099\) labeled simple graphs on up to five vertices and the compatible partitions. It independently computes chromatic number by dynamic programming over independent blocks, VC dimension by enumerating projected label patterns on candidate coordinate subsets, and Littlestone dimension by recursion on both branches of each possible query. For each graph it checks both equalities with \(|V|-\chi(G)\). In addition it checks \(12070\) consistent graph/transcript combinations on four vertices against the contracted constraint graph identity. These finite checks are corroboration; the universal claims rest on the argument above. Reproduce with `python3 verify_partition_rank.py`. The exact recorded standard output is `verify_partition_rank_output.txt`.

## Relationship to prior work

Liu and Mukherjee study the number of same-component oracle queries required to *identify* a partition when its number of blocks is fixed, a different target from Littlestone mistake dimension; fixed-block-count families are not refinement closed. DePavia, Medrano Martín del Campo and Tani analyze error-tolerant partition recovery with same-cluster queries, again under an identification/noisy-oracle objective. Chase, Freitag and Reyzin develop general applications of Littlestone dimension to query learning and compression without the present refinement-closed partition support theorem or coloring-quotient formula. The classical equivalence-relation transitivity and graph chromatic number are used as standard mathematical ingredients. The present theorem concerns the equality-query concept class itself; it does not assert that the algorithm predicts a complete partition using only the stated number of *queries*.

## Limitations

Refinement closure is essential to the exact support characterization and the online equality. Arbitrary fixed-block-count partition classes are not covered. The conditional quotient theorem requires a consistent transcript; incompatible histories have an empty version space and no dimension is asserted. The chromatic formula is a structural identity but computing it from a general graph is NP-hard, while the mistake-bounded union-find predictor itself requires no chromatic computation. Exhaustive program checks reach only five graph vertices (and conditional checks four), not arbitrary cardinality. Historical publication priority could be affected by relevant work not indexed or inspected; no claim of independent certification or of uniqueness of the result in all literature is made.

## References

1. Xizhi Liu and Sayan Mukherjee, *Tight query complexity bounds for learning graph partitions*, arXiv:2112.07897v1, first posted 2021-12-15, https://arxiv.org/abs/2112.07897 .
2. DePavia, Medrano Martín del Campo, and Tani, *Error-Tolerant Exact Query Learning of Finite Set Partitions with Same-Cluster Oracle*, arXiv:2305.13402v1, https://arxiv.org/abs/2305.13402 .
3. Hunter Chase, James Freitag, and Lev Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812v1, https://arxiv.org/abs/2310.04812 .
