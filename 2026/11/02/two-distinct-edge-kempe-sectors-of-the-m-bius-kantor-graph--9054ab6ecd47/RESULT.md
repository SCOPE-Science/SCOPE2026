# Two distinct edge-Kempe sectors of the Möbius–Kantor graph

## Finding

Let \(M=GP(8,3)\) be the Möbius–Kantor graph. The graph \(\mathcal K(M)\) of proper edge-colourings in three **named** colours, with adjacency given by one colour interchange on one complete alternating bichromatic cycle, has \(120\) vertices and \(342\) edges. It has exactly two connected components, of orders \(24\) and \(96\), with respectively \(54\) and \(288\) edges.

The smaller component has \(18\) vertices of degree \(4\), six of degree \(6\), radius and diameter \(3\), and odd girth \(5\). From each degree-four vertex its distance-sphere sizes are \((1,4,15,4)\); from each degree-six vertex they are \((1,6,15,2)\). It is nonbipartite.

The larger component is bipartite and six-regular, has radius and diameter \(4\), and has distance-sphere sizes \((1,6,27,42,20)\) from **every** vertex. Moreover it is a Cayley graph of an explicitly constructed group of order \(96\) acting by automorphisms of \(M\), with six involutory generators.

An intrinsic distinction between the two sectors is the cycle-length signature of the three bichromatic spanning two-factors. Every colouring of the \(96\)-component has signature
\[
\bigl((6,10),(6,10),(6,10)\bigr).
\]
The \(24\)-component instead contains eighteen colourings with signature \(\bigl((8,8),(16),(16)\bigr)\) and six with signature \(\bigl((8,8),(8,8),(8,8)\bigr)\). Here a pair \((a,b)\) records the lengths of the alternating cycles in a two-colour spanning two-factor; \((16)\) means a single Hamiltonian alternating cycle. The signatures are unordered over the three colour-pairs, so they do not depend on naming the colours.

## Assumptions and scope

The graph has sixteen vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/8\mathbb Z\), and exactly the twenty-four undirected edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). It is cubic. A proper named three-edge-colouring is a function from its edges to \(\{0,1,2\}\) assigning three distinct colours at each vertex. A move chooses two colours, selects **one complete connected component** of the subgraph they induce, and interchanges those two colours on all edges of that component. The component is necessarily a simple alternating cycle because the graph is cubic with all three colours represented at every vertex. The two endpoints of a move are distinct; duplicate descriptions of the same undirected edge are counted once. No quotient by graph or colour automorphisms is taken in the \(120\)-state configuration graph.

## Proof

**Exhaustive state space.** For any cubic graph, each colour class in a proper three-edge-colouring is a perfect matching. Conversely, any ordered triple of pairwise disjoint perfect matchings covering all edges is a proper named colouring. Enumerate perfect matchings by selecting the least-index unmatched vertex and branching over its incident edges to unmatched neighbours. Every perfect matching appears exactly once, because its partner at that vertex determines the branch. The complete recursion produces exactly \(33\) perfect matchings. For each ordered disjoint pair, its complementary edge set is tested for membership in the matching set; this produces exactly \(120\) distinct ordered triples. This proves the state count without statistical sampling or relying on a precomputed catalogue.

**Complete move graph.** In each state, a pair of colour classes forms a spanning two-factor. Starting from each as-yet-unvisited edge of that two-factor and traversing incident two-factor edges enumerates exactly its connected components. At every vertex the two-factor degree is two, so each such component is a single alternating even cycle. Interchanging the chosen two colours on that cycle yields another enumerated state and gives **every** legal move. Enumerating all three pairs and all their cycles, and deduplicating undirected edges, yields \(342\) edges. Connected-component traversal gives exactly the \(24\)- and \(96\)-vertex components. Computing the three two-factor length partitions for every state establishes the signatures and multiplicities stated above; checking each complete move verifies that no exchange crosses between these two signature sectors. The signatures are *not* asserted to be invariant for arbitrary cubic graphs.

**Distances, parity, and small-sector structure.** Breadth-first search from each of the \(120\) states gives exactly the two distance-sphere distributions in the smaller component and the uniform distribution in the larger. Since each search visits every state in its own component, these are exact shortest-path metrics, proving both radii and diameters. A graph two-colouring of the larger component verifies bipartiteness. In the smaller component a directly enumerable simple five-cycle proves nonbipartiteness; exhaustive adjacency checks give no triangles, so its odd girth is five. Degree and edge totals follow directly from complete neighbour sets.

**Cayley structure of the large sector.** Define permutations of the sixteen graph vertices by \(r(u_i)=u_{i+1}\), \(r(v_i)=v_{i+1}\); \(s(u_i)=u_{-i}\), \(s(v_i)=v_{-i}\); \(t(u_i)=v_{3i}\), \(t(v_i)=u_{3i}\). Define a fourth permutation \(w\) on vertex labels \(u_0,\ldots,u_7,v_0,\ldots,v_7\) by the image list

`(0,1,9,12,4,5,13,8,7,2,14,15,3,6,10,11)`.

Direct comparison with the twenty-four edges verifies that all four maps are graph automorphisms. Closure under composition gives a group \(\Gamma=\langle r,s,t,w\rangle\) of exactly \(96\) elements. Acting by these graph automorphisms on any chosen colouring in the \(96\)-component produces \(96\) pairwise distinct colourings; by the already proved component count these are **all** its vertices. Automorphisms carry legal moves to legal moves, so the action is regular and the component is a Cayley graph of \(\Gamma\). Exactly six group elements send a reference colouring to one of its six neighbours, and direct composition checks show all six are involutions. This proves the asserted Cayley realization. The corresponding group action has four orbits of six named colourings on the smaller component, as a separate exact calculation; it does not imply transitivity there.

Both complete exhaustive algorithms are included in `verify_matchings.py` and `verify_edge_backtrack.py`. They use distinct state-generation methods and distinct move-generation routines, with no external packages or input files.

## Verification

Run `python3 verify_matchings.py` and `python3 verify_edge_backtrack.py` with Python 3. The first uses edge-bitmask perfect matchings and independently checks the explicit \(96\)-element permutation group. The second recursively assigns colours directly to edges subject to local vertex constraints, then reconstructs the alternating-cycle moves from edge incidence. Both assert all state, edge, component, signature, parity and distance data; the first additionally asserts Cayley transitivity and involutory generators, and the second independently constructs a five-cycle witness. Each ends by printing lines ending in `PASS` when all assertions succeed. Their loops traverse finite, explicitly specified complete search spaces; the programs do not use random seeds or numerical tolerances.

## Relationship to prior work

Belcastro and Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs* (first public 2012-09-08, arXiv:1209.1730v1), define this exact move and study component counts, including nonplanar bipartite cases. Their later *Edge-Kempe-equivalence graphs of class-1 regular graphs* (2017) develops global structural results and a detailed crossed-prism example, but not this Möbius–Kantor decomposition. Goedgebeur and Östergård, *Switching 3-Edge-Colorings of Cubic Graphs* (arXiv:2105.01363v1, 2021) computationally cover component counts for **all** cubic graphs through order thirty, including sixteen-vertex graphs in aggregate. Their order-wise tables and published propositions do not provide this named graph's two component sizes, the opposed bipartiteness, complete shortest-path distributions, cycle-factor signatures, or the Cayley action. In particular, a general algorithm capable of recomputing those quantities must not be mistaken for a published theorem stating them. The component *count alone* is not asserted to be new.

Related existing exact edge-Kempe classifications for the Desargues graph \(GP(10,3)\), the Pappus graph, the Petersen graph at four colours, and \(K_{3,5}\) at five colours concern different graphs and do not imply the present component geometry. Graph symmetry and basic parameters for the Möbius–Kantor graph are classical; the claim concerns the reconfiguration graph of its edge-colourings, not the construction or uniqueness of the base graph.

## Limitations

This is an exact finite-graph theorem, not a universal statement about all cubic graphs. A verification run checks the supplied mathematical enumeration and adjacency constructions but is not a formal proof assistant or independent scholarly review. Historical priority under alternative terminology (one-factorization exchange, Tait-colouring interchange, symmetric cubic graph catalogues) is not proven exhaustively. The 2021 broad enumeration is acknowledged as relevant coverage of component *counts*. No mixing-time bounds for any stochastic process or extension to a larger family are claimed.

## References

1. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730v1 (2012-09-08); *Discrete Mathematics* **325** (2014), 77–84. https://arxiv.org/pdf/1209.1730
2. S.-M. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, *Australasian Journal of Combinatorics* **69** (2017), 197–214. https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf
3. J. Goedgebeur and P. R. J. Östergård, *Switching 3-Edge-Colorings of Cubic Graphs*, arXiv:2105.01363v1 (2021). https://arxiv.org/abs/2105.01363
4. J. McDonald, B. Mohar, and D. Scheide, *Kempe equivalence of edge-colorings in subcubic and subquartic graphs*, *Journal of Graph Theory* **70** (2012), 226–239. https://doi.org/10.1002/jgt.20613
