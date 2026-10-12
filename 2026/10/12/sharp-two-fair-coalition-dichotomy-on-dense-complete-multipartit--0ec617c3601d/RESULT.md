# Sharp two-fair coalition dichotomy on dense complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge3\) and every \(n_i\ge3\). Put \(N=\sum_{i=1}^r n_i\). With the two-fair coalition definition below, we prove the complete formula
\[
C_{2f}(G)=\begin{cases}
N-3,&r=3,\\
2,&r\ge4.
\end{cases}
\]
When \(r=3\), the proper two-fair dominating sets are precisely the three-part transversals, selecting exactly one vertex per part. When all three parts have at least four vertices, every maximum coalition partition has exactly three two-vertex blocks, one of each cross-part type, and all other vertices singleton; conversely every such partition is maximum. The number of maximum (unordered) partitions is
\[
8\prod_{i=1}^{3}\binom{n_i}{2},
\]
and their coalition graphs are all isomorphic to
\[
K_{1,n_1-2}\sqcup K_{1,n_2-2}\sqcup K_{1,n_3-2}.
\]
For \(r\ge4\), every two-block partition is optimal and its coalition graph is \(K_2\).

## Assumptions and scope
All graphs are finite, simple and undirected. The parts of \(G\) are nonempty and all have cardinality at least three. A set \(S\subseteq V(G)\) is two-fair dominating if every vertex outside \(S\) has **exactly two neighbours** in \(S\). Under the standard vacuous convention, \(V(G)\) itself is two-fair dominating. Two disjoint sets form a two-fair coalition when neither is two-fair dominating but their union is. A two-fair coalition partition is a set partition where every block is either a two-fair dominating set of size exactly two or forms a two-fair coalition with another block; \(C_{2f}\) maximizes the number of blocks. The coalition graph has these blocks as vertices, with adjacency precisely when they form a coalition. No assertion here concerns multipartite graphs containing parts of size one or two. The structural and enumerative classification of all maximum partitions assumes \(r=3\) and each part has size at least four; the numeric formula holds when parts have size three.

## Proof
**Lemma (the exact eligible proper unions).** Let the multipartite parts be \(V_1,\ldots,V_r\). If \(S\ne V(G)\) is two-fair dominating and a part \(V_j\subseteq S\) is fully selected, then choose an outside vertex \(v\) in some other part. It sees every vertex of \(V_j\), hence at least three selected neighbours, contradiction. Thus every part contains an outside vertex. Put \(s_i=|S\cap V_i|\) and \(s=\sum_i s_i\). From every outside vertex in part \(i\), the condition reads \(s-s_i=2\). Subtracting two equations yields \(s_i=s_j=t\) for all parts; hence \((r-1)t=2\) with \(t\) a nonnegative integer. Because \(r\ge3\), the only solution is \(r=3\) and \(t=1\). Conversely, one selected vertex in each of three parts gives exactly two selected neighbours to every outside vertex. In particular, there is no proper two-fair dominating set for \(r\ge4\), and none of size two for any \(r\ge3\).

**Four or more parts.** By the lemma, if \(r\ge4\), a coalition of nonempty disjoint proper sets must have union equal to all vertices. Consequently a coalition partition cannot have more than two blocks. Splitting the vertex set arbitrarily into two nonempty blocks realizes two: neither block is two-fair dominating, while their union is by the vacuous convention. Its coalition graph is \(K_2\).

**Three parts, upper bound.** Write the three parts as \(A,B,C\), all of size at least three. Consider any coalition partition with at least three blocks. A union of two blocks is always proper, so every coalition union must be a three-vertex transversal by the lemma. There are no autonomous two-vertex two-fair blocks. Thus every partition block must be either a singleton or a pair whose vertices lie in distinct parts; a singleton of colour \(A\) can only partner with a pair of type \(BC\), and cyclically. If a partition of the \(N\) vertices had at least \(N-2\) blocks, its block-size excess \(\sum_B(|B|-1)\) would be at most two. Therefore at most two cross-part pairs could occur, so each of the three parts, each of size at least three, would contribute at least one singleton. Those three singleton types require partners of the three distinct types \(BC,AC,AB\), demanding at least three pair blocks, contradiction. Hence \(C_{2f}(G)\le N-3\).

**Three parts, attaining construction.** Choose two distinct vertices from each part. Pair one chosen vertex of \(A\) with one from \(B\), the other chosen \(A\) vertex with one from \(C\), and the remaining chosen \(B\) vertex with the remaining chosen \(C\) vertex. Keep all other vertices as singleton blocks; each part contains at least one singleton. Every pair block has a complementary singleton partner, and every singleton has a complementary pair block, so this is a coalition partition with exactly three nonsingleton pairs and \(N-3\) blocks.

**All optimum structures with part sizes at least four.** An optimal partition has \(N-3\) blocks and, as shown above, only singletons and cross-part pairs. Therefore it has exactly three pairs. Because every part has at least four vertices, at least one singleton of each part remains; all three complementary pair types must occur. There are three pairs in total, so precisely one of each type. This also proves sufficiency. To count labeled-vertex partitions, choose the two vertices that participate in pair blocks from each part and assign those two vertices to the two pair types incident with that part. This gives \(\prod_i\binom{n_i}{2}\) choices of vertex pairs and independently two assignments at each of the three parts, hence exactly \(8\prod_i\binom{n_i}{2}\) partitions. A pair block of type \(AB\) is adjacent in the coalition graph precisely to the \(n_C-2\) singleton blocks from \(C\), and similarly for the other two types. No other coalition edges are possible, giving the claimed disjoint union of stars. This proves every assertion.

## Verification
The supplied standalone Python 3 program independently constructs adjacency masks and tests the exact two-fair predicate for all vertex subsets of seven multipartite profiles, including the critical cases \((3,3,3)\), \((3,3,4)\), \((3,4,4)\), \((4,4,4)\), and profiles with four and five parts. It enumerates all \(21{,}147\), \(115{,}975\), and \(678{,}570\) set partitions at the first three profiles and verifies their exact optimum numbers. A separate enumeration checks all \(13{,}860\) choices of three disjoint pairs on twelve vertices and finds exactly \(1{,}728=8\binom42^3\) optimal partitions for \(K_{4,4,4}\), each with the canonical pair types. Run \(\texttt{python3 verify\_fair\_coalition.py}\) from the extracted package root; the output is included as \(\texttt{verification\_output.txt}\). These are independent finite checks, not a substitute for the unlimited-order proof.

## Relationship to prior work
Jafari and Alikhani, *\(k\)-Fair Coalitions in Graphs*, arXiv:2509.11358v1 (first public 14 September 2025), introduce this exact coalition rule and study complete and complete-bipartite graphs, paths, cycles, and selected other classes. They do not state the dense multipartite three-to-four-part dichotomy or the extremizer/coalition-graph count. The older and subsequent ordinary \(k\)-coalition theories (Brešar--Henning--Samadi, arXiv:2507.18306; Kaneshiro, arXiv:2608.05403) allow **at least** \(k\) neighbours and so do not impose the exact-neighbour requirement. In particular, a large ordinary two-coalition partition need not be two-fair. An independent classification of ordinary multipartite coalitions cannot, without additional argument, imply the four-part impossibility established here. Published two-fair coalition results for complete bipartite graphs concern two-part graphs only. A separate published result counts fair dominating sets of complete multipartite graphs, rather than coalition partitions.

## Limitations
The hypothesis that every part has at least three vertices is essential to the no-full-part lemma. The enumeration of all optimal partitions (and their coalition graphs) is asserted for three parts of sizes at least four; for three-vertex parts only the exact maximum number of blocks is asserted. The cited ordinary \(k\)-coalition paper by Kaneshiro has an accessible abstract and a third-party description but the complete primary text was unavailable to read here; overlap risk regarding related ordinary-coalition upper bounds remains. Exhaustive finite testing is supplemental; no independent external audit is claimed.

## References
1. A. Jafari and S. Alikhani, *\(k\)-Fair Coalitions in Graphs*, arXiv:2509.11358v1, first posted 2025-09-14, https://arxiv.org/html/2509.11358v1.
2. B. Brešar, M. A. Henning, and B. Samadi, *On \(k\)-coalition in graphs: bounds and exact values*, arXiv:2507.18306v1, 2025, https://arxiv.org/abs/2507.18306.
3. C. Kaneshiro, *On \(k\)-coalition partitions of graphs*, arXiv:2608.05403v1, 2026, https://arxiv.org/abs/2608.05403.
