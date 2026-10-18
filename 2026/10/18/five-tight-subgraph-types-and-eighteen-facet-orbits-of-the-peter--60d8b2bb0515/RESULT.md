# Five tight-subgraph types and eighteen facet orbits of the Petersen transportation ball

## Finding
Let \(G=KG(5,2)\) be the Petersen graph. Its vertices are the ten two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent exactly when the corresponding subsets are disjoint. Give the vertex set the unit-edge shortest-path metric and write \(B\) for the unit ball of its real Lipschitz-free (transportation-cost) space. This ball is the nine-dimensional symmetric edge polytope
\[
B=\operatorname{conv}\{\pm(e_U-e_V):UV\in E(G)\}
\subset\{x\in\mathbb R^{10}:\sum_U x_U=0\}.
\]

The **complete tight-subgraph classification** comprises exactly **135** connected spanning maximal bipartite subgraphs. Under the full graph automorphism group \(\operatorname{Aut}(G)\cong S_5\), these subgraphs form precisely **five orbits**. Each subgraph supports a constant number of facets depending only on its orbit:

| Subgraph orbit size | Number of tight edges | Facets with exactly this subgraph | Representative edge mask |
|---:|---:|---:|---:|
| 10 | 9 | 10 | `4735` |
| 30 | 9 | 6 | `6005` |
| 60 | 10 | 10 | `5055` |
| 30 | 11 | 14 | `7615` |
| 5 | 12 | 22 | `4095` |

The mask is a fifteen-bit integer; bit \(k\), starting at zero, records the presence of edge \(k\) in the lexicographic edge ordering specified below. The table exhausts the subgraphs and gives \(10\cdot10+30\cdot6+60\cdot10+30\cdot14+5\cdot22=1410\) facets. The total **1410** was already independently recorded in [5]; it is included as a consistency check, not claimed as a new count.

The more refined **complete facet classification** gives exactly **18 orbits** under \(S_5\) together with global reflection. In the following table, each potential is the unique nonnegative integer translate with minimum zero. The coordinate order is
\[
(01,02,03,04,12,13,14,23,24,34),
\]
where, for example, `01` denotes \(\{0,1\}\). A word such as `0002110100` denotes ten coordinates, *not* a decimal integer.

| Facet orbit size | Representative potential | Tight edges |
|---:|:---:|---:|
| 20 | `0000000111` | 9 |
| 120 | `0000001111` | 10 |
| 60 | `0000011111` | 11 |
| 10 | `0000111111` | 12 |
| 60 | `0001010111` | 9 |
| 20 | `0002110100` | 9 |
| 120 | `0002110101` | 10 |
| 120 | `0002110111` | 11 |
| 40 | `0002111111` | 12 |
| 60 | `0011201011` | 11 |
| 120 | `0011201101` | 9 |
| 240 | `0011201111` | 10 |
| 60 | `0011211111` | 9 |
| 30 | `0012210101` | 12 |
| 120 | `0012210111` | 11 |
| 120 | `0012211111` | 10 |
| 60 | `0022111110` | 11 |
| 30 | `0022111111` | 12 |

In particular, 270 facets have two potential levels and 1140 have three. The numbers with respectively nine, ten, eleven, and twelve tight edges are **280, 600, 420, 110**. Every orbit representative and multiplicity is certified by the exact standalone checker `verify.py`.

## Assumptions and scope
The scalar field is real. The graph is the standard ten-vertex, fifteen-edge Petersen graph, not a generalized Petersen graph or a larger Kneser graph. Every graph edge has metric length one; nonedges have distance two. A facet *potential* is an integer-valued unit-Lipschitz function on vertices modulo additive constants; global sign changes give opposite facets. For a potential \(h\), its *tight subgraph* contains exactly the edges \(UV\) with \(|h(U)-h(V)|=1\). The first table acts on unoriented tight subgraphs with \(S_5\); the second table acts on individual facets with \(S_5\times C_2\), where the second factor changes the sign of the normal. Orbits and fibers are counted as distinct geometric facets, not distinct integer translates.

For reproducibility, define the vertex list as all increasing pairs from `range(5)` in lexicographic order. Enumerate all lexicographically ordered index pairs \((i,j)\) with \(0\le i<j<10\) whose associated two-subsets are disjoint. That gives the edge order
\[
(0,7),(0,8),(0,9),(1,5),(1,6),(1,9),(2,4),(2,6),
(2,8),(3,4),(3,5),(3,7),(4,9),(5,8),(6,7).
\]

## Proof
**1. The transportation ball and the tight-edge criterion.** Every molecule \((e_U-e_V)/d(U,V)\) for nonadjacent graph vertices decomposes along a shortest path into the average of its two unit-edge molecules; hence the transportation unit ball is exactly the edge-difference convex hull displayed above. Because the graph is connected, these differences span the nine-dimensional zero-sum subspace. The dual ball is
\[
Q=\{h\pmod{\mathbf1}:|h(U)-h(V)|\le1\text{ for all }UV\in E(G)\}.
\]
The equalities active at a potential \(h\) have coefficient vectors \(e_U-e_V\) for the edges of its tight subgraph. Such vectors span the nine-dimensional quotient exactly when the tight subgraph is connected and spanning. If they do not span, a sufficiently small perturbation in an unconstrained direction preserves all strict inactive inequalities, so \(h\) is not a vertex of \(Q\). If they do span, the active equalities isolate \(h\), so it is a vertex. Thus facets of \(B\) are in bijection with connected-spanning-tight potentials modulo constants. This is the established general facet criterion [1–3], reconstructed here to fix all normalizations.

A spanning tree of tight edges expresses every coordinate of \(h\) relative to a chosen coordinate as a sum of \(\pm1\); therefore all coordinate differences are integers. The Petersen graph has diameter two (intersecting two-subsets have a common disjoint two-subset, while disjoint ones are adjacent). All normalized facet potentials consequently belong to \(\{0,1,2\}^{10}\) and have minimum zero. These finitely many possibilities are **exhaustive**, not a sample.

**2. Tight subgraphs are precisely connected spanning complete cuts.** Along any tight edge, the integer labels have opposite parity. Thus every tight subgraph is bipartite. A non-tight graph edge cannot cross its parity bipartition, because an odd integer difference of absolute value at most one would have to equal one. The tight subgraph therefore contains *all* edges crossing that bipartition. Conversely, for any bipartition whose complete crossing-edge subgraph is connected, the \(\{0,1\}\)-valued indicator of one part is Lipschitz, and its tight graph is that connected complete cut. Such a cut is maximal bipartite: adding an internal edge closes an odd cycle along an even-length path in the connected cut graph. Every maximal connected spanning bipartite subgraph must be a complete cut, because an omitted crossing edge could otherwise be added while maintaining bipartiteness.

Fix the first vertex in the first part to remove swapping the two parts. There are exactly \(2^9-1=511\) nontrivial cuts to test. For every cut, form its complete crossing-edge subgraph and check spanning connectedness by breadth-first search. The exhaustive integer certificate `verify.py` finds exactly 135 qualifying masks. In a logically independent enumeration, it examines all \(2^{15}=32768\) edge subsets and retains exactly those that are connected, bipartite, and edge-maximal; the resulting **sets of masks agree exactly**.

**3. Full graph symmetry.** The independent sets of size four of \(KG(5,2)\) are precisely the five stars \(\mathcal S_a=\{\{a,b\}:b\ne a\}\). Indeed, a pairwise intersecting family of at least four edges of a complete graph has a common endpoint: without one, any three incident edges without a common endpoint form a triangle, which admits no fourth edge meeting all three. Thus an automorphism permutes these five distinguished stars. A vertex \(\{a,b\}\) is their unique intersection \(\mathcal S_a\cap\mathcal S_b\); hence its image is determined by the induced permutation of five stars. This injects \(\operatorname{Aut}(G)\) into \(S_5\). Conversely every permutation of the ground five-set preserves disjointness, giving all 120 automorphisms.

**4. Complete finite orbit certificate.** For every mask found in step 2, apply each of the 120 induced vertex permutations. The resulting five disjoint orbits have sizes \(10,30,60,30,5\) and the tight-edge counts shown in the first table. For the facet classification, enumerate all \(3^{10}=59049\) labelings in \(\{0,1,2\}^{10}\); retain precisely those with minimum zero, edge differences at most one, and connected spanning tight graph. This yields 1410 potentials. For each potential apply all 120 vertex permutations and both signs, renormalizing by subtracting the resulting minimum. This partitions the 1410 potentials into the 18 orbits represented above. The orbit computations verify explicit disjointness, closure under every group element, exact sizes, and exhaustion; thus no unspecified numerical extrapolation is used.

Assign each facet to its tight mask. The subgraph fibers have sizes 6 on each of 30 masks, 10 on each of 70 masks, 14 on each of 30 masks, and 22 on each of five masks, with the finer orbit allocation in the first table. The sum is 1410. As an independent symmetry check, fixed-point counting over all group elements gives \(600=120\cdot5\) fixed subgraph incidences and \(4320=240\cdot18\) fixed facet incidences, verifying the two orbit numbers by Burnside's lemma. Finally, direct counting of label levels and tight-edge sizes gives the stated histograms. All finite ranges, edge orders, complete group actions, and expected rows are explicit in `verify.py`.

## Verification
Run `python verify.py` using Python 3 and the standard library only. The program recomputes the Petersen vertices and edges without stored graph data; performs both independent connected-cut and all-edge-subset tests; enumerates the complete admissible ternary set; establishes the five maximum independent stars and all 120 induced graph automorphisms; checks the 135/1410 exhaustions, all orbit representatives and sizes, subgraph fiber multiplicities, Burnside fixed-point totals, and the two histograms. It prints `ALL EXACT CHECKS PASSED` only after every assertion holds. Its termination is finite by explicit iteration over 511 cuts, 32768 edge masks, 59049 potential assignments, and finite permutation groups; no SAT-solver trust, floating point, random sample, or unproved computational search completeness is involved.

## Relationship to prior work
The general facet criterion for symmetric edge polytopes is due to Higashitani, Jochemko and Michałek [1]; Chen, Davis and Korchevskaia [2] identify facet subgraphs as maximal bipartite subgraphs; Braun and Bruegge [3] give enumeration formulas for sparse families with few excess edges, especially theta-type graphs. D’Alì, Delucchi and Michałek [4] relate symmetric edge polytopes to Lipschitz-free transportation norms and investigate other graph families. These general results motivate the present special graph but **do not themselves enumerate its full \(S_5\)-orbit/fiber classification**.

A prior published Petersen-specific record [5] already states the aggregate number 1410, identifies thirty nearest facets, and proves the exact inradius and rigidity of its incenter. Its inspected result does not provide the 135 maximal bipartite subgraphs, their five orbits and fiber multiplicities, or the full eighteen-orbit facet decomposition. Those **finer classifications**, not the total number of facets or the nearest-facet theorem, are the present contribution.

## Limitations
The theorem treats one natural graph, not all generalized Petersen or pair-Kneser graphs, and it classifies facets rather than all faces or full face lattices. The total 1410 count is independently known [5], and the generic criterion is not new [1–3]. Completeness of the finite classification is exact, but the absence of an equivalent enumeration in every inaccessible or unindexed dataset is not established; see the accompanying originality review. No external independent scientific validation is asserted.

## References
1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first submitted 2018-07-20, especially Theorem 3.1. https://arxiv.org/abs/1807.07678
2. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first submitted 2021-07-26, especially Theorem 3 and Theorem 9. https://arxiv.org/abs/2107.12315
3. B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303, first submitted 2022-01-31, especially Theorem 2.3 and Section 4. https://arxiv.org/abs/2201.13303
4. A. D’Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first submitted 2019-10-11. https://arxiv.org/abs/1910.05193
5. *Exact inradius and contact-facet rigidity of the Petersen symmetric edge polytope*, publicly indexed mathematical research record (2026-10-11), in the published-finding corpus public 2026 repository, record identifier `af8a32ec1f59`.
