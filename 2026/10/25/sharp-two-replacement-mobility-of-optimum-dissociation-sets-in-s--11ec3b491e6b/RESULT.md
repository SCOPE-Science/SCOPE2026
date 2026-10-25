# Sharp two-replacement mobility of optimum dissociation sets in square rook graphs

## Finding
For every integer \(k\ge1\), set \(n=3k\) and let \(R_n=K_n\square K_n\), the graph on \([n]\times[n]\) with adjacency when exactly one coordinate agrees. A dissociation set is a vertex subset whose induced graph has maximum degree at most one. Let \(\mathcal D_n\) consist of the *maximum-cardinality* dissociation sets. For distinct \(S,T\in\mathcal D_n\), define \(S\sim_j T\) when \(|S\setminus T|=|T\setminus S|=j\), and write \(X_j(n)\) for the resulting exchange graph.

Then \(\operatorname{diss}(R_n)=4k\). Every member of \(\mathcal D_n\), regarded as edges of \(K_{n,n}\), is a spanning vertex-disjoint union of exactly \(k\) two-edge stars centered in each bipartition class. There are exactly
\[
N_k=\binom{3k}{k}^{2}\left(\frac{(2k)!}{2^{k}}\right)^2
\]
such sets. The new exchange conclusions are that \(X_1(n)\) has no edges, whereas \(X_2(n)\) is connected and regular of degree
\[
4k^2+8\binom{k}{2}=8k^2-4k.
\]
In particular, two simultaneous replacements are necessary and sufficient for universal optimum-preserving reconfiguration for every \(k\ge1\). The maximum size and the count are included for exact scope, but the count follows from earlier induced-matching packing enumerations and is not claimed as a new independent result.

## Assumptions and scope
All graphs are finite, simple, and labeled. The two sides of \(K_{n,n}\) are the labeled row and column sets. The graph \(R_n\) is its line graph: a chosen rook-graph vertex is an edge between one row and one column. A two-replacement operation exchanges two selected rook-graph vertices with two unselected ones in a single step; it need not pass through an optimum configuration after only one of the two individual replacements. No claim is made for rectangles with unequal dimensions or for \(n\not\equiv0\pmod3\).

## Proof
**Structure and optimum.** A selected edge family in \(K_{n,n}\) represents a dissociation set of \(R_n\) precisely when every connected component containing selected edges is either a one-edge component or a two-edge path (a two-edge star). Indeed, an edge in a longer selected-edge component would have at least two neighboring selected edges in the line graph. A two-edge star contributes two selected edges using three original vertices, whereas a one-edge component contributes one edge using two. On the \(6k\) original vertices, the number of selected edges is therefore at most \(\frac23(6k)=4k\). Equality requires all original vertices covered by two-edge stars, without isolated selected edges or uncovered original vertices. Such a spanning packing exists: take \(k\) row-centered stars and \(k\) column-centered stars on disjoint groups of three original vertices. To see the counts of each orientation must both be \(k\), let \(a\) be the number of row-centered stars and \(b\) the number of column-centered stars. Row usage is \(a+2b=3k\), column usage \(2a+b=3k\), so \(a=b=k\). Choosing the \(k\) centers on each side and partitioning the remaining \(2k\) labeled leaves into unordered pairs assigned to labeled centers gives the formula for \(N_k\).

**One-replacement rigidity.** Removing one selected edge from an optimum star leaves its center incident with one selected edge and frees one leaf. To cover this freed leaf in another optimum, the replacement must attach it to a vertex on the opposite side. An unaffected two-edge-star center already has degree two. An unaffected leaf is incident with an edge whose center is incident with a second edge; attaching there would give that preexisting selected edge two line-graph neighbors. The only available opposite-side vertex is the original center, so the sole feasible replacement restores the removed edge. Hence \(X_1(n)\) is edgeless.

**Two-replacement classification and degree.** Any changed edge is in one of the selected two-edge stars. Unaffected stars cannot receive additional selected edges, by the same saturation argument. If two removed edges lie in the same star, the only way to repartition its three now-free vertices into a two-edge star is the original pair, so there is no distinct optimum. If they come from two stars of the same orientation, the only nontrivial transformation swaps their removed leaves; for each unordered pair of row-centered stars there are four choices of leaf pair, and likewise for column-centered stars. This gives \(8\binom{k}{2}\) neighbors.

For opposite orientations, write the two selected stars, using distinct row vertices \(a,d,e\) and distinct column vertices \(r,s,b\), as
\[
\{(a,r),(a,s)\},\qquad\{(d,b),(e,b)\}.
\]
Removing \((a,s)\) and \((e,b)\) leaves \((a,r)\) and \((d,b)\). Among the six involved original vertices the unique *different* spanning pair of two-edge stars containing these retained edges is
\[
\{(d,s),(d,b)\},\qquad\{(a,r),(e,r)\}.
\]
Thus one simultaneously changes the row center from \(a\) to \(d\) and the column center from \(b\) to \(r\). Selecting the row star, column star, one of their two leaves for each new center gives \(4k^2\) distinct neighbors. These cases exhaust two-replacement possibilities and prove the degree formula.

**Connectivity.** Fix the sets \(A\) and \(B\) of row- and column-centered vertices, respectively, each of size \(k\). The configurations in this fiber are obtained by partitioning the other \(2k\) rows into unordered pairs assigned to column centers and the other \(2k\) columns into unordered pairs assigned to row centers. Same-orientation leaf exchanges above generate all permutations of these leaves, so each fiber is connected under two-replacement moves (trivial when \(k=1\)).

Now choose any row center \(a\in A\), a different row \(d\notin A\), any column center \(b\in B\), and a different column \(r\notin B\). By exchanges within the current fiber, we may arrange that \(d\) is a leaf of \(b\) and \(r\) a leaf of \(a\). The opposite-orientation transformation then reaches a fiber with centers \((A\setminus\{a\})\cup\{d\}\) and \((B\setminus\{b\})\cup\{r\}\). Thus the graph of center-set fibers contains the direct (tensor) product \(J(3k,k)\times J(3k,k)\), where \(J(n,k)\) denotes the Johnson graph on \(k\)-subsets with one-element replacements. Each Johnson factor is connected and has a triangle: fix \(k-1\) elements and vary the remaining element among three available choices. Two connected nonbipartite graphs have connected tensor product: between any pair of vertices one can choose walks of the same parity (an odd closed walk reverses parity) and pad the shorter by two-step backtracks. The product is therefore connected. Every fiber is connected and every edge of this center-set product can be realized after preparatory moves within a fiber, proving that \(X_2(n)\) is connected.

## Verification
Two complete standalone programs accompany this document. The first enumerates every optimum configuration by assigning row/column centers and unordered leaf pairs, identifies all two-replacement adjacencies through common size-\((4k-2)\) subsets, and checks connectedness and degrees for \(k=1,2\). The second independently uses exact-cover enumeration by original-graph two-edge-star blocks, reconstructs all two-replacement neighbors using the explicit local moves, and performs graph traversal for \(k=1,2\). It also tests every subset of the \(3\times3\) and \(4\times4\) rook graphs directly for the maximum dissociation number. Both programs give \(9\) optimum sets of degree \(4\) for \(k=1\), and \(8100\) optimum sets of degree \(24\) for \(k=2\), with a connected two-replacement graph and no one-replacement transitions. The general theorem follows from the proof, not extrapolation from these checks.

## Relationship to prior work
Orlovich, Dolgui, Finke, Gordon, and Werner developed the dissociation-set/three-vertex-path packing correspondence for line graphs and used it in hardness proofs. Earlier enumerative work on induced matchings of rectangular rook graphs already yields the optimum count as a specialization, so neither that correspondence nor the count is claimed as new. Bonsma, Kamiński, and Wrochna analyze *independent* set reconfiguration in claw-free graphs: their states have no adjacent selected vertices and do not include the size-\(4k\) dissociation states here, whose induced graphs are unions of edges. The new statement characterizes optimal dissociation-set exchange geometry at simultaneous-replacement budgets one and two.

## Limitations
Only sizes divisible by three are treated. A two-replacement step is simultaneous, not a path of feasible one-replacement steps. Direct computations check only the specified small instances; no computational experiment substitutes for the all-\(k\) proof. Literature equivalences under alternate path-packing language cannot be ruled out completely; independent external mathematical evaluation remains outstanding.

## References
1. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366, DOI: 10.1016/j.dam.2011.04.023; earlier author preprint *On the Complexity and Inapproximability of Dissociation Set Problems in Graphs* (2010), publicly readable at https://www.academia.edu/12908075/On_the_Complexity_and_Inapproximability_of_Dissociation_Set_Problems_in_Graphs.
2. P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (first posted 2014-03-03), https://arxiv.org/html/1403.0359v1.
3. Earlier exact rook-graph induced-matching packing enumeration, scientific reference identifier 58c2e820-445f-484a-a3b6-035a5291db15; its count formula is explicitly treated as prior knowledge.
