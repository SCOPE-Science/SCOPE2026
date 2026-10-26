# Exact counts of optimal full-degree coalition partitions in regular graphs

## Finding
Let \(G\) be a finite simple \(k\)-regular graph, where \(k\ge2\). Let \(C_k(G)\) be its \(k\)-coalition number (defined below), and let \(F_4(G)\) count its unordered four-block \(k\)-coalition partitions. Then
\[
C_k(G)=\begin{cases}4,&G\text{ is bipartite},\3,&G\text{ is not bipartite}.
\end{cases}
\]
For bipartite \(G\), let \(c\ge1\) be the number of connected components and \(|V(G)|=2m\). Then
\[
F_4(G)=\begin{cases}
(2^{m-1}-1)^2,&c=1,\
2^{c-1}(2^{m-1}-1)^2-2^{c-2}(2^{c-1}-1),&c\ge2.
\end{cases}
\]
For nonbipartite \(G\), \(F_4(G)=0\). In particular, the full optimal-four-block partition count in the bipartite case depends only on graph order and the number of components, not on the edge arrangement or degree.

## Assumptions and scope
All graphs are finite, simple and undirected; disconnected graphs are permitted. The fixed integer \(k\ge2\) equals the degree of every vertex. A set \(D\subseteq V(G)\) is \(k\)-dominating if each vertex outside \(D\) has at least \(k\) neighbors inside \(D\). Two disjoint non-\(k\)-dominating sets form a \(k\)-coalition if their union is \(k\)-dominating. A \(k\)-coalition partition is a partition into nonempty blocks, each either a \(k\)-dominating set of cardinality exactly \(k\), or a non-\(k\)-dominating block with a coalition partner elsewhere in the partition. The maximum number of blocks is \(C_k(G)\). The number \(F_4(G)\) counts **unlabeled** four-block partitions, not permutations of their blocks.

## Proof
**Step 1 (vertex covers and partner degree).** Since every vertex has degree \(k\), a set is \(k\)-dominating exactly when it is a vertex cover: an outside vertex must have all its neighbors inside. In a maximum-cardinality coalition partition there can be no individually \(k\)-dominating block of size \(k\): split such a block into two nonempty proper subsets, each of size less than \(k\) and hence non-\(k\)-dominating, whose union remains \(k\)-dominating. Other coalition partners remain intact, contradicting maximality. Therefore all blocks in a maximum partition are noncovers. For each noncover block \(B\), choose an edge \(uv\) with neither endpoint in \(B\). Every partner \(B'\) must contain \(u\) or \(v\) for \(B\cup B'\) to cover that edge. Disjointness of blocks implies \(B\) has at most two partners.

**Step 2 (the four-block ceiling and bipartite obstruction).** Form the partner graph \(H\) on the blocks, joining two blocks when their union covers all edges. Every vertex of \(H\) has degree at least one, and Step 1 gives degree at most two. Any finite graph with minimum degree one, maximum degree two and at least four vertices has a matching of size at least two. Take disjoint partner edges \(AB\) and \(CD\). The unions \(A\cup B\) and \(C\cup D\) are disjoint vertex covers. There can be no fifth block: a vertex outside both covers would have all its \(k>0\) neighbors simultaneously in the two disjoint covers, which is impossible. Thus \(C_k(G)\le4\). If four blocks occur, the two covers partition all vertices and each is the complement of a vertex cover, so each is independent. Consequently \(G\) is bipartite.

**Step 3 (existence of three and four blocks).** Fix any edge \(uv\). The partition \(\{V(G)\setminus\{u,v\},\{u\},\{v\}\}\) is a valid three-block coalition partition: the first block misses edge \(uv\); neither singleton is a vertex cover because \(k\ge2\); and adjoining either singleton to the first block leaves only one vertex outside, hence covers all edges. If \(G\) is bipartite with color classes \(X,Y\), regularity forces equal sizes \(|X|=|Y|=m\ge k\ge2\). Splitting each of \(X,Y\) into two nonempty sets yields four noncover blocks, with a coalition between the two blocks from each color class. This proves the displayed formula for \(C_k(G)\).

**Step 4 (parametrization of every maximum four-block partition).** By Step 2, every four-block partition admits two disjoint partner pairs; their two vertex-cover unions are the independent color classes of a bipartition. Conversely, splitting both classes of any bipartition gives a valid four-block partition. Each connected bipartite component has two color orientations, and the whole graph has \(2^{c-1}\) unordered bipartitions. Every component is balanced by \(k\)-regularity, so each global color class has size \(m\). A set of size \(m\) has \(s=2^{m-1}-1\) unlabeled splits into two nonempty subsets. Thus these constructions produce \(2^{c-1}s^2\) candidate partitions, counted with multiplicity.

**Step 5 (duplicate correction).** A fixed four-block partition has exactly three possible pairings of its four blocks into two unordered pairs. Two such pairings produce graph bipartitions precisely if graph edges occur only across both pairings. Relabeling the four blocks \(A,B,C,D\), assume the pairings are \(AB\mid CD\) and \(AC\mid BD\). Then all graph edges run between \(A,D\) or between \(B,C\). Since the graph has positive degree, its connected components split into **two nonempty groups**, one supported on \(A\cup D\) and one on \(B\cup C\); within each group its two blocks are exactly the two color classes of a bipartition. The third pairing cannot also represent a graph bipartition, since every possible edge joining two distinct blocks is internal to one of the three pairings. Consequently each duplicate construction is counted **exactly twice**.

There are \(2^{c-1}-1\) unordered ways to split the \(c\) connected components into two nonempty groups. For any group split with group sizes \(a\) and \(c-a\), its two induced graphs have \(2^{a-1}\) and \(2^{c-a-1}\) unordered bipartitions respectively, so it defines \(2^{c-2}\) duplicated partitions. The duplicate count is thus \(2^{c-2}(2^{c-1}-1)\) for \(c\ge2\), and zero for \(c=1\). Subtracting once per duplicate from the construction total proves the formula for \(F_4(G)\). All arguments hold for every integer \(k\ge2\) and every finite number of components.

## Verification
The accompanying standalone `verify.py` directly checks the original neighbor-count definition of \(k\)-domination and enumerates every unlabeled set partition of 174 labeled regular graphs on three through six vertices. It also checks both the maximum block count and the exact number of four-block partitions in specified larger graphs through eight vertices, including the cube, complete bipartite graphs and a disconnected two-cycle union. A separate independent orientation-and-splitting enumerator checks the disconnected duplicate correction on three or four cycle components and on two complete bipartite components. All recorded tests return `VERIFY_OK` in `verification_output.txt`. The infinite theorem is proved by Steps 1–5 rather than inferred from finite tests.

## Relationship to prior work
Jafari, Alikhani and Bakhshesh (2024, arXiv:2407.09332) introduced \(k\)-coalitions and their general regular-graph bounds. Brešar, Henning and Samadi (2025, arXiv:2507.18306, Theorem 4.2) had already determined the **numerical** value for cubic graphs, including its bipartite criterion; their Lemma 2.3 establishes a general partner-degree bound. Kaneshiro (2026, arXiv:2608.05403, Theorem 3.7) records the general \(3\)-to-\(4\) bound for regular graphs, among wider coalition-partition results. These results are acknowledged as prior, especially the cubic case and the existing general upper/lower bounds. The assessed additional result is the full all-degree numerical classification together with the **exact enumeration** of all optimal four-block partitions for connected and disconnected regular bipartite graphs, including the overcount correction for alternative component orientations. The inspected primary works do not give this enumeration. An equivalent unindexed counting theorem is a residual priority risk.

## Limitations
The theorem assumes \(k\ge2\) and exact \(k\)-regularity; it neither handles irregular graphs nor enumerates optimal three-block partitions in nonbipartite graphs. Its count concerns unlabeled set partitions of a graph's fixed vertex set; it is not a count up to graph automorphisms. No independent external mathematical audit has been performed.

## References
1. A. Jafari, S. Alikhani, D. Bakhshesh, *k-Coalitions in Graphs*, arXiv:2407.09332, first posted 2024-07-12, https://arxiv.org/abs/2407.09332.
2. B. Brešar, M. A. Henning, B. Samadi, *On k-coalition in graphs: bounds and exact values*, arXiv:2507.18306, first posted 2025-07-24, https://arxiv.org/html/2507.18306v1.
3. C. Kaneshiro, *On k-coalition partitions of graphs*, arXiv:2608.05403, first posted 2026-08-05, https://arxiv.org/abs/2608.05403.
