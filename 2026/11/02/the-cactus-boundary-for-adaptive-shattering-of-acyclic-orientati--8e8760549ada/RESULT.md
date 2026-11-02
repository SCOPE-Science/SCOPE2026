# The cactus boundary for adaptive shattering of acyclic orientations

## Finding
Let \(G=(V,E)\) be any finite, simple, undirected graph, including disconnected graphs and isolated vertices. Let \(\mathcal A(G)\subseteq\{0,1\}^{E}\) be its family of **acyclic orientations**, with one binary query per edge specifying its direction. Write \(c(G)\) for the number of connected components, including isolated vertices, and \(r(G)=|V|-c(G)\) for the graphic-matroid rank.

**Theorem.** Every edge-query support is VC-shattered by \(\mathcal A(G)\) if and only if it is an undirected forest. Consequently,
\[
\operatorname{VCdim}(\mathcal A(G))=r(G).
\]
Moreover, the following are equivalent:

1. \(G\) is a cactus: each edge is contained in at most one simple undirected cycle.
2. \(\operatorname{Ldim}(\mathcal A(G))=\operatorname{VCdim}(\mathcal A(G))\).

If \(G\) is not a cactus, then the quantitative strict inequality holds:
\[
\operatorname{Ldim}(\mathcal A(G))\ge r(G)+1.
\]

This classification is valid without connectedness, planarity, maximum-degree, or size assumptions. In particular, the four-vertex diamond \(K_4-e\) satisfies \(\operatorname{VCdim}=3\) and \(\operatorname{Ldim}=4\). Subdividing its central edge gives the triangle-free graph \(K_{2,3}\), for which the dimensions are \(4\) and \(5\), respectively. The disjoint union of \(s\) diamonds has dimensions \(3s\) and \(4s\), for every integer \(s\ge1\), so the adaptive-minus-static gap is unbounded.

## Assumptions and scope
All graphs are finite, simple, and undirected before orienting. An orientation directs each edge exactly once; it is acyclic if the resulting digraph contains no directed cycle. An edge query reveals the direction of that edge relative to an arbitrary fixed reference direction. A support \(S\subseteq E\) is VC-shattered when every \(0/1\) labeling of \(S\) extends to a concept in \(\mathcal A(G)\). The Littlestone dimension is the largest integer \(d\) for which a complete binary depth-\(d\) tree of edge queries has a distinct compatible acyclic orientation at every leaf, agreeing with the entire answer path. The depth-zero case is allowed. A cactus is equivalently a graph in which any two distinct simple cycles have no common edge. A theta graph means three internally vertex-disjoint paths with the same two endpoints.

The theorem concerns the concept class of **all** acyclic orientations of the fixed underlying graph. It does not address arbitrary digraphs, partial orientations as final hypotheses, or query spaces containing nonedges.

## Proof
**1. Static shattering.** If \(S\) contains an undirected cycle, assign directions consistently around it. That labeling cannot extend to an acyclic orientation. Conversely, if \(S\) is a forest, every orientation of \(S\) is an acyclic partial orientation. Topologically order its directed edges (together with the isolated vertices) and direct all remaining graph edges forward along that order. The result is acyclic. Hence the shattered supports are exactly the forests, and the largest support has size \(r(G)\). This static fact was also established by Kozma and Moran; it is background rather than a novelty claim.

**2. Product lemma.** For two nonempty binary concept classes \(\mathcal C\) and \(\mathcal D\) on disjoint coordinate sets,
\[
\operatorname{Ldim}(\mathcal C\times\mathcal D)
=\operatorname{Ldim}(\mathcal C)+\operatorname{Ldim}(\mathcal D).
\]
The lower bound concatenates a complete shattered tree for \(\mathcal C\) and, below every leaf, a complete shattered tree for \(\mathcal D\). For the upper bound, induct on \(|\mathcal C||\mathcal D|\). The initial query of any putative shattered tree belongs to one factor, say \(\mathcal C\). Its two nonempty branches have the form \(\mathcal C_0\times\mathcal D\) and \(\mathcal C_1\times\mathcal D\), with strictly smaller products. The Littlestone recurrence and the inductive bounds give at most
\[
1+\min\{\operatorname{Ldim}(\mathcal C_0),\operatorname{Ldim}(\mathcal C_1)\}+\operatorname{Ldim}(\mathcal D)
\le \operatorname{Ldim}(\mathcal C)+\operatorname{Ldim}(\mathcal D).
\]
The same argument applies to queries from the other factor.

**3. The cactus case.** A cactus has edge-disjoint simple cycle blocks and bridge edges. An orientation is acyclic precisely when the orientation of each cycle block is not one of its two coherent directed cycles. Therefore its concept class is a Cartesian product of free one-edge bits (bridges) and classes of the form \(\{0,1\}^{\ell}\) with exactly the two coherently directed cycle assignments deleted, one factor per simple cycle of length \(\ell\). A cycle factor has VC dimension \(\ell-1\): any \(\ell-1\) edges form a forest, but its full edge set cannot be shattered. Its Littlestone dimension is also \(\ell-1\), since static shattering is bounded by adaptive shattering and its \(2^{\ell}-2\) members cannot realize the \(2^\ell\) leaves of a depth-\(\ell\) complete tree. Every bridge contributes one to each dimension. The product lemma gives
\[
\operatorname{Ldim}(\mathcal A(G))
=\sum_{\text{cycle blocks }C}(|E(C)|-1)+\#\{\text{bridges}\}
=|V|-c(G)=r(G).
\]
This includes forests and the edgeless graph.

**4. The diamond gadget.** Let \(D\) have vertices \(0,1,2,3\) and edges \((0,1),(0,2),(0,3),(1,2),(1,3)\) in that order. There are exactly 18 acyclic orientations. The file `certificates/diamond_tree.json` gives an explicit depth-four complete binary query tree, specifying all 15 query nodes and 16 leaf-orientation witnesses. The independent script `verify.py` checks that each witness is acyclic and realizes every answer along its root-to-leaf path. Thus \(\operatorname{Ldim}(\mathcal A(D))\ge4\). Since a depth-five tree needs at least 32 distinct hypotheses, 18 hypotheses give the reverse inequality. Hence
\[
\operatorname{VCdim}(\mathcal A(D))=3,
\qquad \operatorname{Ldim}(\mathcal A(D))=4.
\]

**5. Subdivision lift.** Let \(G'\) be obtained from a graph \(G\) by subdividing an edge \(uv\) with a new vertex \(w\). Choose the old reference direction \(u\to v\), and use the direction \(w\to v\) of the new edge \(wv\) to encode the old edge direction. The direction on the other new edge \(uw\) can then be chosen independently. Given any acyclic orientation of \(G\), if its old edge is \(u\to v\), choose \(w\to v\) and either \(u\to w\) or \(w\to u\). If the old edge is \(v\to u\), choose \(v\to w\) and either \(u\to w\) or \(w\to u\). In each case, \(w\) is either a new source or sink, or lies on a directed two-edge path replacing the old directed edge. All choices are acyclic. Keeping directions of the remaining edges unchanged embeds the entire product \(\mathcal A(G)\times\{0,1\}\) as a subclass of \(\mathcal A(G')\) after relabeling the coordinates. Therefore
\[
\operatorname{Ldim}(\mathcal A(G'))\ge\operatorname{Ldim}(\mathcal A(G))+1.
\]
Subdividing increases the graphic rank by exactly one.

**6. Every noncactus graph.** Every noncactus contains a theta subgraph \(H\): if two cycles share an edge, one cycle has an off-cycle path from the other joining two vertices of the first, producing three internally disjoint connecting paths. Every simple theta is obtainable from the diamond by subdividing edges, because its three paths between the two branch vertices have lengths at least \(1,2,2\) after reordering. Repeated use of Step 5 proves
\[
\operatorname{Ldim}(\mathcal A(H))\ge r(H)+1.
\]
Take a forest \(F\subseteq E(G)\setminus E(H)\) connecting each vertex outside \(H\) to the component of \(H\) when appropriate and spanning each other component of \(G\). Within the component containing \(H\), contract the connected subgraph \(H\) and choose a spanning tree of the resulting component; lift its edges to form the rooted attachments. Then \(|F|=r(G)-r(H)\), and **every** acyclic orientation of \(H\), combined with **every** orientation of \(F\), is acyclic on their union: attached branches have only one connection to the core, while other components are forests. Any such partial orientation extends to an acyclic orientation of \(G\) by topological sorting. Hence the projection of \(\mathcal A(G)\) onto \(E(H)\cup F\) contains \(\mathcal A(H)\times\{0,1\}^{F}\), and
\[
\operatorname{Ldim}(\mathcal A(G))
\ge\operatorname{Ldim}(\mathcal A(H))+|F|
\ge r(H)+1+r(G)-r(H)=r(G)+1.
\]
This completes the equivalence for all finite graphs.

**7. Sharp examples.** The graph \(K_{2,3}\) is the one-edge subdivision of the diamond, so its Littlestone dimension is at least five. It has exactly \(46\) acyclic orientations: each of its three degree-two vertices has four possible local direction patterns (source, sink, forward path, backward path), and the only forbidden global arrangements contain both a forward and a backward path. Inclusion-exclusion therefore gives \(3^3+3^3-2^3=46\). Since \(46<64\), the Littlestone dimension is at most five. It has five vertices and graphic rank four, proving its stated pair of dimensions. The disjoint union of \(s\) diamond components has product concept class; Steps 1, 2 and 4 give the stated \(3s,4s\) formulas.

## Verification
The standalone standard-library Python program `verify.py` reads `certificates/diamond_tree.json` and checks all 16 gadget leaf witnesses against the five edge coordinates, including acyclicity and the complete direction-answer path. It independently evaluates the exact Littlestone recurrence on the 18 diamond orientations, checks six small theta subdivisions, and exhaustively compares the structural cactus classification against computed Littlestone dimension for every labeled simple graph on four and five vertices (\(64+1024=1088\) graphs). The observed cactus/noncactus counts are \((57,7)\) and \((623,401)\), respectively. Its replayed stdout is stored in `verification_output.txt`. These finite computations certify the displayed gadget and corroborate boundary cases; the unrestricted conclusion is proved in Steps 1–7 above, not inferred from the finite census.

## Relationship to prior work
Kozma and Moran, *Shattering, Graph Orientations, and Connectivity* (first arXiv posting November 6, 2012, Section 3, Proposition 15), already proved the VC-dimension/graphic-rank relationship for acyclic orientations. That fact is explicitly treated as background. Chepoi, Knauer, and Philibert, *Labeled sample compression schemes for complexes of oriented matroids* (first arXiv posting October 28, 2021), include acyclic orientations of mixed graphs in their broader COM framework and prove VC-sized proper labeled sample compression; their compression theorem is not an equality of VC and Littlestone dimensions. The new result here isolates exactly which underlying graphs admit equality of the static and adaptive dimensions, and supplies a structural theta obstruction in the complementary class. The proof also distinguishes the query model from online strategies with graph-vertex, nonedge, or completion queries. No claim of exhaustive priority verification is made.

## Limitations
The strict inequality for noncacti is a lower bound, not a closed formula for their exact Littlestone dimensions. The result uses simple graphs; multigraphs with loops or parallel edges require modified statements. Scientific priority remains subject to independent comparison with the full historical literature on online learning of acyclic orientations and on partial-cube/topes complexity. The provided verification checks are reproducible finite corroboration, not an external independent scientific audit.

## References
1. L. Kozma and S. Moran, *Shattering, Graph Orientations, and Connectivity*, arXiv:1211.1319 (initial public posting 2012-11-06), especially Section 3 and Proposition 15. https://arxiv.org/abs/1211.1319
2. V. Chepoi, K. Knauer, and M. Philibert, *Labeled sample compression schemes for complexes of oriented matroids*, arXiv:2110.15168 (initial public posting 2021-10-28), Introduction and Theorem 3. https://arxiv.org/abs/2110.15168
3. H. Chase, J. Freitag, and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812 (initial public posting 2023-10-07), online-query-learning context. https://arxiv.org/abs/2310.04812
