# Two move regimes for optimal decycling sets of the Möbius–Kantor graph

## Finding
Let \(G=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph. Its vertices are \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\); its edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). A feedback vertex set, or decycling set, is a set \(S\subseteq V(G)\) such that the induced graph \(G-S\) is a forest. The known minimum size is \(\nabla(G)=5\).

Define \(J\) and \(T\) on **all minimum** decycling sets. In \(J\), two distinct sets are adjacent if one deleted vertex can be exchanged with one nondeleted vertex (token jumping), with the result again a minimum decycling set. In \(T\), that exchange must additionally be along an edge of \(G\) (token sliding). There are exactly \(672\) vertices in each graph, split into \(192\) independent deleted sets and \(480\) deleted sets inducing exactly one edge. Both reconfiguration graphs are connected.

The jump graph has \(5664\) edges and is self-centered: every vertex has eccentricity \(5\), so its radius and diameter both equal \(5\). Its degree distribution (degree: frequency) is \((13:96,15:336,17:48,19:96,25:96)\).

The slide graph has \(1848\) edges, radius \(7\), diameter \(9\), and eccentricity distribution \((7:96,8:560,9:16)\). Its degree distribution is \((4:288,5:144,6:96,7:48,9:48,10:48)\). Thus strengthening a single optimal exchange by the adjacency restriction preserves global reachability but changes self-centeredness into a nontrivial center/periphery structure. These are exact statements about this finite graph, not assertions for other generalized Petersen graphs.

## Assumptions and scope
All graphs are finite, undirected, simple, and vertex-labelled as above. Index arithmetic is modulo eight. To match the checkers, label \(u_i\) by integer \(i\) and \(v_i\) by \(8+i\), so a set is encoded as the integer bit mask \(\sum_{x\in S}2^{\operatorname{label}(x)}\). Reconfiguration is undirected; deleted sets retain cardinality five at every step. There is no permission to temporarily use a larger deletion set. A token jump can go to any vacant vertex; a token slide can only cross an edge of \(G\).

For every minimum set \(S\), the forest \(G-S\) has eleven vertices. If \(S\) is independent, the remaining forest has two components; if \(G[S]\) has one edge, the forest is a tree. Exactly those two deletion types occur. The previously established scalar decycling number is background, not the claimed contribution.

## Proof
**Extremal cardinality and two types.** The Möbius–Kantor graph is cubic on sixteen vertices, with twenty-four edges. For a deletion set \(S\) of size \(k\), let \(e(S)=|E(G[S])|\). Counting the deleted incidences with multiplicity gives
\[
|E(G-S)|=24-3k+e(S).
\]
If \(G-S\) is a forest, then \(|E(G-S)|\le15-k\); hence \(2k-e(S)\ge9\), proving \(k\ge5\). The set \(S=\{u_0,u_2,u_4,u_6,v_0\}\) has cardinality five and its complement is a tree, giving the upper bound. For \(k=5\), write \(c\) for the number of forest components. The forest identity \(|E(G-S)|=11-c\) yields \(c=2-e(S)\). As \(c\ge1\), necessarily \(e(S)\in\{0,1\}\), and the two claims about component structure follow.

**Exhaustive state determination.** Each five-element vertex subset occurs exactly once in the \(\binom{16}{5}=4368\) lexicographic combinations of the sixteen labels. `verify_masks.py` uses a disjoint-set cycle test on its eleven retained vertices. A distinct implementation, `verify_forests.py`, enumerates eleven-element retained sets, counts induced edges and connected components by depth-first search, and applies the identity \(|E|=|V|-c\) for forests. Both enumerate exactly \(672\) valid five-sets, with \(192\) of internal-edge count zero and \(480\) of count one. The complete sorted list of their bit masks is in `certificate.json`; no symmetry quotient, heuristic search, or sampling is used.

**Exhaustive exchange determination.** For every valid set and each ordered choice of a currently deleted vertex and a currently retained vertex, the checkers test whether the exchanged five-set is in the exact valid-state list. The slide checker additionally tests whether the changed pair is an edge of \(G\). As a five-set exchange has a unique removed and inserted vertex, this procedure examines every possible legal jump or slide exactly once in each direction. Each resulting undirected edge is stored once in the two edge lists in `certificate.json`. The lists contain respectively \(5664\) jump edges and \(1848\) slide edges. Their complete degree spectra are those stated above.

**Exact distances and connectedness.** Breadth-first search from each of the \(672\) enumerated vertices in each complete adjacency graph visits all \(672\) vertices. Consequently both exchange graphs are connected. Each breadth-first search gives all shortest-path distances from its root, not merely a lower or upper bound. Taking every root's maximum yields the stated eccentricity spectra. In the jump graph, all \(672\) maxima equal five; in the slide graph, exactly \(96\) equal seven, \(560\) equal eight, and \(16\) equal nine. The diameter witnesses in `certificate.json` comprise a five-move jump path between masks \(341\) and \(682\), and a nine-move slide path between masks \(1448\) and \(10772\). The exhaustive all-roots BFS also certifies that no shorter paths join those endpoints. This establishes the reported radii and diameters.

## Verification
The two standalone standard-library programs `verify_masks.py` and `verify_forests.py` use different acyclicity tests, complementary enumeration variables, and independent graph builders. They print the same canonical result and finish with `VERIFY_OK`. The recorded outputs are `verify_masks.out` and `verify_forests.out`. The independently reconstructed vertex/edge fingerprints, computed as SHA-256 of compact JSON arrays of sorted vertex masks and sorted undirected edge pairs, are:

- Jump graph: `0a3f428c5d7735ef01016b8506b3dc31301630b8d4449d6943c211d5491afc6f`.
- Slide graph: `7f3db4a352eb46e816c26dd38fd324b0fa242e2c21a00097bc5a7cd25b3cd56d`.

The whole-graph, unordered-pair distance multiplicities are respectively \((5664,29952,75744,83472,30624)\) at distances one through five for jumping, and \((1848,7968,25456,54528,69976,48752,15600,1312,16)\) at distances one through nine for sliding. Each multiplicity sequence sums to \(\binom{672}{2}\). In the included certificate, vertices are literal integers and an edge is a length-two ordered integer array.

## Relationship to prior work
Wei and Li (2013) and Gao et al. (2015) studied the decycling number of generalized Petersen graphs; the scalar value \(\nabla(G)=5\) is not new. Agrawal et al. (2015) established algorithmic properties of the simultaneous feedback-vertex-set problem; their result does not classify this fixed graph's reconfiguration states. Hertz (2021) uses fixed-cardinality swaps of induced forests within bipartition sides for a heuristic search of large forests, but supplies neither the all-optimum transition graphs on \(\operatorname{GP}(8,3)\) nor their exact metrics; moreover its neighborhood is not the same as unrestricted jumping or edge-constrained sliding here. Work on independent-set token reconfiguration concerns different feasible sets. Graph-specific work on matching and independence complexes of the Möbius–Kantor graph likewise concerns different combinatorial objects.

The paper of Gao et al. was not available in full text during comparison; a hidden exact optimum-set census is a residual overlap risk. Available descriptions emphasize the scalar number rather than optimal-solution distances. No publication-priority certification is claimed.

## Limitations
This is a complete finite computation with a transparent exhaustive proof, not a general formula for all cubic, bipartite, or generalized Petersen graphs. The finite searches prove the exact properties of \(\operatorname{GP}(8,3)\) only. Results for relaxed cardinality constraints, simultaneous multi-token moves, or weighted deletion sets are not established. Related unindexed or inaccessible work may contain an equivalent metric classification.

## References
1. E. Wei and Y. Li, *Decycling Number and Upper-Embeddibility of Generalized Petersen Graphs*, Acta Mathematica Sinica (Chinese Series) 56 (2013), 211–216. DOI:10.12386/A2013sxxb0022 (publisher page lists public date 2013-03-15).
2. L. Gao, X. Xu, J. Wang, D. Zhu, and Y. Yang, *The decycling number of generalized Petersen graphs*, Discrete Applied Mathematics 181 (2015), 297–300. DOI:10.1016/j.dam.2014.09.005.
3. A. Agrawal, D. Lokshtanov, A. E. Mouawad, and S. Saurabh, *Simultaneous Feedback Vertex Set: A Parameterized Perspective*, arXiv:1510.01557 (first submitted 2015-10-06).
4. A. Hertz, *Decycling Bipartite Graphs*, Journal of Graph Algorithms and Applications 25 (2021), 461–480. DOI:10.7155/jgaa.00567.
5. T. Ito, M. Kamiński, and H. Ono, *Fixed-Parameter Tractability of Token Jumping on Planar Graphs*, arXiv:1406.6567 (first submitted 2014-06-25).
