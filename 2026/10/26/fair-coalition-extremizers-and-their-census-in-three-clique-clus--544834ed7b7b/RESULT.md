# Fair-coalition extremizers and their census in three-clique cluster graphs

## Finding

Let \(G=K_{n_1}\sqcup K_{n_2}\sqcup K_{n_3}\) be the disjoint union of three labelled complete-graph components, with integers \(n_1,n_2,n_3\ge 3\). Set \(N=n_1+n_2+n_3\). Its 1-fair coalition number is

\[
\mathcal C_f(G)=N-3.
\]

All unordered optimal partitions have exactly three doubleton blocks and \(N-6\) singleton blocks. Each doubleton meets two different components. Their component-pair types are precisely one of: (i) one of each of the three pairs, (ii) two of one pair and one of an adjacent pair, possible only if the common component has size three, or (iii) three of one pair, possible only when both components of that pair have size three.

The exact number \(T(n_1,n_2,n_3)\) of unordered optimal partitions of the labelled vertex set is

\[
T=\prod_{i=1}^3 n_i(n_i-1)
+3\sum_{i=1}^3 \mathbf 1_{\{n_i=3\}}
 \left(\prod_{j\ne i}n_j\right)
 \left(\sum_{j\ne i}n_j-2\right)
+6\sum_{1\le i<j\le3}\mathbf 1_{\{n_i=n_j=3\}}.
\]

In particular, for all three component orders at least four, only type (i) occurs and the count simplifies to \(\prod_i n_i(n_i-1)\). For three triangles the count is \(558\), whereas for three four-cliques it is \(1728\).

## Assumptions and scope

Graphs are finite, simple, undirected and labelled. A set \(S\subseteq V(G)\) is **1-fair dominating** if each vertex outside \(S\) has *exactly one* neighbour in \(S\). A **1-fair coalition** consists of two disjoint sets that are individually not 1-fair dominating but whose union is 1-fair dominating. A **fair-coalition partition** partitions the vertex set into nonempty blocks, each of which is either a singleton that is itself 1-fair dominating or has a coalition partner among the other blocks. We use the definition from [1]. Here no singleton dominates all three components, so every block must have a coalition partner. An unordered partition does not order its blocks; vertices remain individually labelled.

## Proof

**1. Small fair-dominating sets.** A set is 1-fair dominating in \(G\) precisely when, within each component \(K_{n_i}\), it selects either one vertex or the entire component. Indeed, an unselected vertex in that clique sees exactly the selected vertices of its component, and other components have no effect. The complete-selection case is vacuous. Since all \(n_i\ge3\), every 1-fair dominating set of cardinality at most four has exactly one vertex from each of the three components, hence exactly three vertices. In particular, no set of two or four vertices is 1-fair dominating; a singleton can partner with a doubleton to form such a set only if the doubleton selects one vertex from each of the *other* two components. Two disjoint doubletons cannot form a coalition, since their union has four vertices.

**2. Sharp upper bound.** Write \(d=N-|\mathcal P|=\sum_{B\in\mathcal P}(|B|-1)\) for the excess of a partition above singletons. Suppose \(d\le2\). At most \(2d\le4\) vertices lie in nonsingleton blocks, so at least two clique components have singleton blocks: otherwise all vertices in two components, at least six, would lie in nonsingleton blocks. A singleton from each of those two components needs a *different* doubleton partner consisting of one vertex from each of the other two components, by step 1 and the bound \(|B|\le3\). These two doubletons consume only two vertices of the third component, so that component, of size at least three, also has a singleton. This third singleton requires a third doubleton partner. Three doubletons have excess three, contradicting \(d\le2\). Hence every fair-coalition partition has at most \(N-3\) blocks.

**3. Attainment.** Choose two distinct vertices in each component. Use these six vertices to make three doubletons of component types \((1,2)\), \((1,3)\), and \((2,3)\), with each of the two chosen vertices of a component used in a different doubleton. Leave all other vertices singleton. Every doubleton pairs with any remaining singleton of the complementary component to give a three-vertex 1-fair dominating transversal. All three components retain at least one singleton because \(n_i\ge3\). Every singleton pairs with the complementary doubleton. Thus a valid partition has \(N-3\) blocks.

**4. Structure of equality.** If \(d=3\), the nonsingleton block sizes are one four-block, or a triple and a double, or three doubles. There are at most six vertices in nonsingleton blocks. Since \(N\ge9\), at least one component has a singleton. If only one component had singletons, the other two components would contribute at least six vertices to nonsingleton blocks, so necessarily there are exactly three doubles and the other components are triangles. If at least two components have singletons, then a triple cannot partner a singleton (their union has four vertices, never 1-fair dominating). A lone four-block could partner a singleton only by selecting two vertices from that singleton's three-vertex component and one from each other component; therefore it cannot serve singleton blocks in two different components. Thus neither the one-four-block nor the triple-and-double shape can serve two singleton components. We conclude that *all* equality partitions consist of three doubles and all remaining vertices singleton.

Each double must have a singleton coalition partner, since two doubles cannot form a coalition. Accordingly, it must meet two different components. Let the multiplicities of the three component-pair types be \(x_{12},x_{13},x_{23}\), with sum three. If they are \((1,1,1)\), each component uses two vertices and retains a singleton. If they are a permutation of \((2,1,0)\), the common component of the two occurring pair types uses all three doubleton vertices; since there is no complementary doubleton for a singleton there, it must have exactly three vertices. Conversely, that condition suffices; singleton vertices in the other two components each have a complementary doubleton, and every doubleton has a complementary singleton. If the multiplicities are \((3,0,0)\), the two used components must both have exactly three vertices; singleton blocks lie in the third, and each double has a coalition partner there. These are precisely the stated cases.

**5. Enumerating equality.** In type (i), select and assign two distinct vertices of each component to its two incident pair types. This yields \(\prod_i n_i(n_i-1)\) unordered partitions because the doubletons have different component-pair types. In type (ii), fix the common size-three component \(i\), choose which of its three vertices belongs to the singly occurring pair, choose a vertex from that pair's other component, and inject the remaining two vertices into distinct vertices of the repeated-pair's other component. Summing the two possible repeated-pair choices gives \(3n_jn_k(n_j+n_k-2)\) for each \(i\) of size three. In type (iii), for each unordered pair of three-vertex components there are \(3!=6\) bijections producing its three doubletons. The three types are disjoint and exhaust equality, proving the formula.

## Verification

Run `python3 verify_three_cliques.py`. The program builds ordinary adjacency masks of the disjoint cliques and checks the 1-fair condition vertex by vertex, not through the preceding occupancy classification. It exhaustively checks all \(21{,}147\) set partitions for component sizes \((3,3,3)\) and all \(115{,}975\) set partitions for \((3,3,4)\). It also enumerates *every* partition with excess at most three in nine component-size profiles, comparing exact optimizer counts with the formula. The recorded output is `verification_output.txt` and ends with `VERIFY_OK`. These are finite checks; the proof above supplies the universal argument.

## Relationship to prior work

Alikhani, Jafari and Safazadeh [1] introduced the 1-fair coalition parameter, established general bounds and exact results for paths, cycles and cubic graphs of small order; their general \(N-\gamma_f+2\) upper bound gives only \(N-1\) here because the minimum 1-fair dominating set has size three. Jafari and Alikhani [2] study \(k\)-fair coalitions, principally for \(k\ge2\); their statements do not provide the three-clique 1-fair optimum census. Kaneshiro [3] studies ordinary \(k\)-coalitions for \(k\ge2\), including disjoint unions, with a different domination inequality. The result here instead uses *exactly one* selected neighbour at each unselected vertex and determines every optimum partition and its count. No claim is made that absence from the searched literature establishes priority.

## Limitations

The claim concerns exactly three components, each a clique of size at least three. It does not determine fair-coalition partitions for arbitrary cluster graphs, smaller clique components, or other values of \(k\). The enumerator counts partitions, not choices of coalition-partner witnesses. As always for a recently introduced invariant, unindexed equivalent results could affect publication priority; no independent mathematical audit has been performed.

## References

[1] S. Alikhani, A. Jafari and M. Safazadeh, *Fair coalition in graphs*, arXiv:2507.15080, initially publicly submitted 20 July 2025; https://arxiv.org/abs/2507.15080.

[2] A. Jafari and S. Alikhani, *\(k\)-Fair Coalitions in Graphs*, arXiv:2509.11358, 2025; https://arxiv.org/abs/2509.11358.

[3] C. Kaneshiro, *On \(k\)-coalition partitions of graphs*, arXiv:2608.05403, 2026; https://arxiv.org/abs/2608.05403.
