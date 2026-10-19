# Two recoloring components and one Kempe class for the Grötzsch graph

## Finding

**Theorem (exact finite reconfiguration classification).** Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, and let \(\Omega\) be the set of all proper vertex colorings \(c:V(G)\to\{0,1,2,3\}\) with four *named* colors. Two distinct members of \(\Omega\) are adjacent in \(R_4(G)\) when they differ at exactly one vertex. They are adjacent in \(K_4(G)\) when one arises from the other by swapping colors \(a,b\) on exactly one connected component of the subgraph induced by the vertices colored \(a\) or \(b\); singleton components are permitted.

There are \(12{,}480\) states in \(\Omega\) (a previously published static count). The two reconfiguration structures have the following exact properties:

1. \(R_4(G)\) has \(45{,}240\) edges and exactly two connected components of \(6{,}240\) states each, both with radius \(15\) and diameter \(17\). Across both components, exactly \(2{,}160\), \(10{,}200\), and \(120\) states have eccentricity \(15\), \(16\), and \(17\), respectively. Every state has degree at least \(5\); the failure of connectivity is not caused by frozen states.
2. A global permutation of the four color names preserves each of the two components of \(R_4(G)\) if and only if it is even; every odd color permutation interchanges them.
3. \(K_4(G)\) has \(87{,}120\) edges and is connected, and each of its \(12{,}480\) states has eccentricity exactly \(7\). Consequently its radius and diameter both equal \(7\). Exactly \(37{,}440\) Kempe edges connect different components of \(R_4(G)\).

Thus permitting connected two-color switches, rather than only one-vertex moves, joins two otherwise separated spaces of optimal four-colorings and sharply reduces the maximum transformation distance.

## Assumptions and scope

All graphs are finite, undirected, and simple. The graph \(G\) has vertices \(0,1,\ldots,10\). The original cycle vertices are \(0,\ldots,4\); their shadows are \(5,\ldots,9\); the apex is vertex \(10\). Indices \(i\) on the cycle are interpreted modulo \(5\). For each \(i\), the edges are \(\{i,i+1\}\), \(\{5+i,i-1\}\), \(\{5+i,i+1\}\), and \(\{5+i,10\}\). This gives exactly \(20\) edges, and the degree multiset comprises five vertices of degree \(3\), five of degree \(4\), and one of degree \(5\).

All four color labels are retained. No quotient by permutations of color names is taken in either reconfiguration graph. An eccentricity is the maximum finite distance from a state within its connected component. Radii and diameters for \(R_4(G)\) are reported separately for its connected components. All numerical assertions concern this graph and this fixed palette; no assertion is made for other members of the Mycielski family.

## Proof

The claim is an exact, reproducible computer-assisted finite theorem. Its exhaustive proof is implemented in `verify_recolorings.py`, using only the Python standard library; `checker_output.txt` records its successful execution. The finite search domain and the exhaustiveness reductions are given below.

**All colorings are enumerated.** The checker constructs the 20 edges explicitly. First, descending-degree constraint backtracking visits every admissible assignment for each of the 11 vertices. Independently, it enumerates all proper colorings of the initial five-cycle, each of four apex colors, and the direct Cartesian product of the five shadow-vertex palettes (each shadow's constraints depend only on the apex and its two neighboring original vertices). Because no two shadows are adjacent, this layer decomposition is exhaustive. Both methods give the *same set* of exactly 12,480 proper four-colorings. Both give zero proper three-colorings. Thus all four colors necessarily appear in every state. Color-label normalization yields exactly 520 partitions (the last count is already known in published expository material and is not an originality claim).

**Both adjacency sets are exact.** For every enumerated coloring and vertex \(v\), the recoloring generator tests each other palette color absent from \(v\)'s neighbors; this condition is necessary and sufficient for a legal one-vertex move. It records the resulting state by exact lookup. Separately, for each of six unordered color pairs, the Kempe generator performs a complete connected-component traversal on the two-color induced subgraph and swaps the labels on each component. This is exactly the definition of a Kempe edge. Every generated edge is checked for symmetry, and every Kempe edge is rechecked by recovering the vertex-difference set and an exact two-color component in its source. The corresponding double-counted degree sums yield 45,240 and 87,120 edges respectively.

**Connectivity and signs.** Breadth-first search from each hitherto unvisited state yields two recoloring components of 6,240 states each, and one Kempe component of 12,480 states. Independent union–find processing of every edge agrees with the component-size multiset. Global permutation of the four color labels is an automorphism of both adjacency relations. For one explicit state the checker tests each of the 24 color permutations, computing its inversion parity and recording whether the image lies in the other recoloring component. The test agrees with sign for all permutations. Because label permutations preserve the full recoloring graph and carry connected components to connected components, the permutation action on the two components is determined by the action on this one reference state, giving the claimed global sign rule. The two component IDs also classify each Kempe edge; exactly 37,440 are crossing edges.

**Metric completeness via symmetry.** The dihedral group of the five-cycle acts as graph automorphisms on both original vertices and their corresponding shadows, fixing the apex. This action has 10 elements, checked directly on all 20 edges. Global permutation of color names gives a commuting \(S_4\)-action. Since all proper four-colorings use all four labels, each color-label orbit has 24 states. Reducing the 520 color partitions under the dihedral action gives exactly 56 orbits: 8 of size 5 and 48 of size 10. Thus the \(D_5\times S_4\) orbits cover all 12,480 labeled colorings; both reconfiguration graphs are invariant under this group. The checker performs full breadth-first shortest-path searches from one state in each orbit, independently verifying the number of reachable states (6,240 or 12,480). Eccentricity is invariant on a graph-automorphism orbit, so weighting the 56 recorded eccentricities by 24 times their normalized orbit sizes establishes the entire eccentricity census and all radii/diameters asserted.

An explicit witness for a Kempe edge crossing the recoloring split is the pair of color vectors, in vertex order \(0,\ldots,10\),

\[
(0,1,0,1,2,3,1,2,1,2,0)\quad\longrightarrow\quad(1,0,1,0,2,3,0,2,0,2,1).
\]

It exchanges colors 0 and 1 on the connected two-color component with vertex set \(\{0,1,2,3,6,8,10\}\), and the two endpoints belong to different components of \(R_4(G)\), as verified by exact lookup.

## Verification

Run `python3 verify_recolorings.py` from the extracted package directory. The program requires Python 3 with the standard library only, uses deterministic canonical orderings, and terminates with `VERIFY_OK` only after all census, adjacency, orbit, connectivity, sign, and shortest-path assertions succeed. The exact output is embedded as `checker_output.txt`. The checker is short enough to permit an independent code audit. The proof is exhaustive for the finite stated vertex and palette domains, not a statistical sample or an extrapolation.

## Relationship to prior work

The standard single-vertex recoloring problem and its graph are developed by Johnson, Kratsch, Kratsch, Patel and Paulusma [1]; their theorems address general algorithms and complexity rather than this graph's exact component and metric census. Bonamy, Bousquet, Feghali and Johnson [2] distinguish single-vertex moves and Kempe changes and prove Kempe equivalence in connected noncomplete regular graphs with the matching palette size. Those hypotheses do not apply here: the Grötzsch graph is irregular and has maximum degree five while the palette has size four. Their theorem consequently does not imply the present Kempe connectivity or its exact distances. The survey [3] addresses reconfiguration and its mixing significance more generally. The 12,480 labeled colorings and 520 unlabeled partitions are expressly *known* from [4] and are reproduced only to define the exact dynamic state space. The potentially new content is the separation of single-vertex versus Kempe dynamics, the sign action, the exact edge cross-count, and the component metrics.

## Limitations

The computational conclusions depend on the validity of the explicitly packaged exhaustive verifier and its interpretation; the two coloring enumerations, independent connectivity method, full adjacency checking, and symmetry-reduced metric searches mitigate but do not remove implementation risk. No independently authored mathematical audit has been performed. An unindexed prior enumeration, an alternative presentation of the same recoloring graph, or a stronger yet-unrecognized theorem might subsume these exact conclusions. The finite result does not establish a general parity invariant for other graphs or a general bound for arbitrary Mycielskian graphs.

## References

[1] M. Johnson, D. Kratsch, S. Kratsch, V. Patel, D. Paulusma, *Finding Shortest Paths between Graph Colourings*, arXiv:1403.6347, first posted 2014-03-25, https://arxiv.org/abs/1403.6347 .

[2] M. Bonamy, N. Bousquet, C. Feghali, M. Johnson, *On a conjecture of Mohar concerning Kempe equivalence of regular graphs*, arXiv:1510.06964, first posted 2015-10-23, https://arxiv.org/abs/1510.06964 .

[3] C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956, https://arxiv.org/abs/2003.05956 .

[4] *No triangle, and four colours*, Matpic, https://www.matpic.com/essays/no-triangle-and-four-colours/ , section “Eleven vertices, no triangle, four colours” (published/static count).
