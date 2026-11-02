# Seven Kempe sectors of the Desargues graph: a mixed-parity decomposition

## Finding

Let \(D=GP(10,3)\) be the Desargues graph, and let \(\mathcal K(D)\) have one vertex for every proper edge-colouring of \(D\) by the three individually named colours \(0,1,2\). Two colourings are adjacent when one results from interchanging two colours on **one connected component** of their bichromatic edge subgraph (an edge-Kempe change). Multiple changes are not merged into one edge.

Then \(\mathcal K(D)\) has exactly \(192\) vertices, \(504\) edges, and **seven connected components** of two sharply different types:

* One component on \(120\) vertices is \(6\)-regular, bipartite, and has radius and diameter \(5\). Every vertex has distance-sphere sizes \((1,6,27,48,32,6)\). It contains exactly \(90\) four-cycles and no odd cycles.
* The other six components have \(12\) vertices and \(24\) edges each. Every such component is \(4\)-regular, has chromatic number \(3\), radius and diameter \(2\), and distance-sphere sizes \((1,4,7)\) at every vertex. Each has precisely \(15\) four-cycles and \(48\) five-cycles, hence odd girth \(5\).

Consequently, the same cubic bipartite graph has both bipartite and nonbipartite edge-Kempe equivalence sectors under its optimal palette. The \(32\) colourings modulo global colour-name permutations split into a class of \(20\) and six classes of \(2\); the above statistics concern the **fully labelled** colouring graph.

## Assumptions and scope

The generalized Petersen graph \(D=GP(10,3)\) has the twenty vertices \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), and the thirty undirected edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). Parallel edges and loops are absent. A proper three-edge-colouring assigns each edge a label in \(\{0,1,2\}\) so that the three edges incident with any vertex have distinct labels. A Kempe move switches two labels on exactly one alternating cycle of the two-colour spanning subgraph. Such subgraphs are unions of even cycles because \(D\) is cubic and properly three-edge-coloured.

The classification concerns no other graph, palette size, or move rule. The number of components refers to labelled colourings, although global palette permutations stay within each component. Statements about diameter and radius concern individual connected components, not the disconnected whole.

## Proof

This finite theorem has an exhaustive proof with two genuinely different state constructions.

**First construction (edge-by-edge exhaustive enumeration).** Number the vertices \(u_i=i\) and \(v_i=10+i\), and sort all edges as increasing integer pairs, using the lexicographic order in `certificate.json`. Recursively colour edge \(j\) with every colour unused at both endpoints, maintaining a three-bit used-colour mask at each endpoint. At the last edge, every assignment is proper. Conversely, an arbitrary proper colouring follows exactly one branch of this recursion at every edge. Hence this generates each and every labelled proper colouring exactly once. The complete recursion (in `verify_desargues_direct.py`) gives \(192\) distinct strings of length \(30\), listed explicitly in the certificate.

**Independent construction (perfect matchings).** The Desargues graph is the bipartite double cover of the Petersen graph \(KG(5,2)\). The second verifier forms this graph by joining a two-subset in the left part to a disjoint two-subset in the right part. It gives an explicit bijection of its twenty vertices to the above generalized Petersen presentation and checks equality of the two thirty-edge sets under this map. Recursive elimination of the least remaining vertex, pairing it in turn with each available neighbour, enumerates all \(60\) perfect matchings. The complement of such a matching is a disjoint union of even cycles. Choosing one of the two alternating assignments of colours \(1\) and \(2\) on each cycle, while colouring the selected matching \(0\), generates every three-edge-colouring; deduplication gives \(192\) labelled states. This construction does not use the first edge-colouring recursion.

**Exhaustive adjacency.** For each colouring and each of the three unordered pairs of colours, construct its bichromatic spanning subgraph; for each connected cycle, swap the two colours only on that cycle. The resulting assignment is again proper. Conversely, every allowed move is exactly one of the three-pair, cycle-by-cycle switches just enumerated. Checking these neighbours against the complete state set and symmetrizing establishes the full simple, undirected \(192\)-vertex adjacency relation. The first construction obtains \(504\) edges and a component decomposition \(120,12,12,12,12,12,12\). The independently constructed matching-based graph obtains the same statistics.

**Distances and parity.** Breadth-first search from **every** state in **each** component produces the two claimed distance-sphere profiles, and establishes their diameters and radii. An exhaustive two-colouring propagation succeeds in the large component. It fails in every small component; an explicit length-five odd cycle is given for each in the certificate. All small components have proper three-colourings, with explicit vertex-colour maps in the certificate. They are therefore exactly three-chromatic. Direct simple-cycle enumeration finds \(90\) quadrilaterals in the large component and \(15\) quadrilaterals plus \(48\) pentagons in each small component. In particular, there are no triangles and the smallest odd cycles in the small components have length five.

For a second arithmetic check of the short-cycle counts, the matching-based verifier computes the number of quadrilaterals by
\[
N_4=\frac12\sum_{\{a,b\}\subseteq V(\mathcal C)}\binom{|N(a)\cap N(b)|}{2},
\]
where \(\mathcal C\) denotes the component. Because the graph is loopless and triangle-free, every closed walk of length five is a five-cycle, up to choice of starting point and direction; thus \(N_5=\operatorname{tr}(A_{\mathcal C}^{5})/10\). These independently reproduce the direct simple-cycle counts, completing the exhaustive finite proof.

## Verification

`verify_desargues_direct.py` uses a self-contained colouring backtracker and outputs `DESARGUES_DIRECT_PASS 192 504 [120, 12, 12, 12, 12, 12, 12] C4 180 C5 288`. The command `python verify_desargues_direct.py --emit certificate.json` reproduces the entire canonical certificate byte for byte, including the edge order, all labelled colourings, complete adjacency, connected components, distance profiles, odd-cycle witnesses and three-colour witnesses.

`verify_desargues_matchings.py` uses the disjoint-two-subset double-cover construction, matchings and alternating cycles rather than the colouring backtracker. It explicitly verifies the isomorphism to \(GP(10,3)\), derives the complete switching graph, performs every-source breadth-first search, counts short cycles by closed-walk identities, tests bipartiteness, and checks three-colourability of each small component. Its successful completion marker is `DESARGUES_INDEPENDENT_PASS`.

Both verifiers use only the Python standard library. The attached `certificate.json` is optional for running them; it supplies directly inspectable finite witnesses. The second verifier does not read the first one's certificate.

## Relationship to prior work

Belcastro and Haas (initial arXiv submission 8 September 2012) formulated edge-Kempe equivalence classes of cubic three-edge-colourings and investigated their number. Belcastro and Haas (2017) subsequently defined the same labelled edge-Kempe graph and proved general structural facts, including triangle-freeness; they explicitly raised diameter questions. Goedgebeur and Östergård (first arXiv submission 4 May 2021) exhaustively tabulated possible **numbers** of classes across small cubic graphs, using unlabelled colourings. These works establish the setting and may already imply the component count through their data; the seven-class fact or general triangle-freeness is **not claimed as a new conceptual discovery**.

The contribution isolated here is the complete *component-level* metric and parity separation for the Desargues graph: the uniform distance spheres, one bipartite diameter-five sector versus six three-chromatic diameter-two sectors, and the exact short-cycle profiles. The cited general statements and tabulations do not state those component-wise conclusions for this graph. An equivalent unpublished or unindexed computation remains possible; literature searches alone cannot certify priority.

## Limitations

The result is an exact finite theorem for one named graph, not a characterization of all cubic bipartite graphs or a statement about four-edge-colouring reconfiguration. The proof is exhaustive and reproducible, rather than a short conceptual derivation of the seven sectors. The older literature contains powerful generic equivalence-count algorithms, and additional historical material could cover the same component graphs. No independent scholarly audit has been performed.

## References

1. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730, initially public 8 September 2012; subsequently *Discrete Mathematics* 325 (2014), 77–84. https://arxiv.org/abs/1209.1730
2. S.-M. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, *Australasian Journal of Combinatorics* 69 (2017), 197–214. https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf
3. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363, initially public 4 May 2021; subsequently *Discrete Mathematics* 345 (2022), 112963. https://arxiv.org/abs/2105.01363
