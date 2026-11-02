# Exact backbite distances among Hamiltonian paths of the Herschel graph

## Finding

Let \(H\) be the eleven-vertex Herschel graph, the smallest non-Hamiltonian polyhedral graph. Let \(\mathcal B(H)\) have as vertices the **unoriented spanning Hamiltonian paths** of \(H\), each path identified with its reversal. Two different paths are adjacent when one is obtained from the other by a single endpoint backbite (Pósa rotation), as defined below.

**Theorem.** The graph \(\mathcal B(H)\) is connected and four-regular, with exactly \(222\) vertices and \(444\) edges. Its radius is \(8\) and its diameter is \(9\). Exactly \(198\) of its vertices have eccentricity \(8\), and exactly \(24\) have eccentricity \(9\). Its \(12\) unordered diameter-nine pairs form a matching on those \(24\) exceptional vertices: each exceptional path has a unique distance-nine partner.

More precisely, the six degree-three vertices in the larger side of the bipartition of \(H\) split naturally into three matched pairs and two pole layers. For any two distinct such vertices, the number of Hamiltonian paths with those endpoints is \(14\) when they belong to the same matched pair, \(12\) when they belong to different matched pairs but the same pole layer, and \(18\) when they belong to different matched pairs and opposite pole layers. All \(15\) endpoint pairs occur. Every eccentricity-nine path has endpoints of the last type; exactly four of the eighteen paths for each of these six endpoint pairs have eccentricity nine.

The numbers of **unordered distinct pairs of paths** at exact backbite distances \(1,2,\ldots,9\) are, respectively,
\[
(444,1152,2436,4326,6348,6189,3078,546,12).
\]
They sum to \(\binom{222}{2}=24531\). In particular, nine backbites are sometimes necessary and always sufficient.

## Assumptions and scope

A concrete construction removes dependence on a diagram. Take three *core* vertices \(c_0,c_1,c_2\), two *pole* vertices \(p_0,p_1\), and six vertices \(b_{ij}^{\varepsilon}\), for \(0\le i<j\le2\) and \(\varepsilon\in\{0,1\}\). Join \(b_{ij}^{\varepsilon}\) to exactly \(c_i,c_j,p_\varepsilon\), and add no other edges. This is the standard Herschel graph: it is the bipartite graph with parts of sizes \(5\) and \(6\), three degree-four core vertices, and eight degree-three vertices. In the verification programs the core vertices are \(0,1,2\), poles \(3,4\), and the six \(b\)-vertices \(5,\ldots,10\), ordered by \((01,0),(01,1),(02,0),(02,1),(12,0),(12,1)\).

Write an oriented representative of an unoriented Hamiltonian path as \((v_0,v_1,\ldots,v_{10})\). If \(2\le k\le10\) and \(v_0v_k\) is an edge of \(H\), the **backbite at \(v_0\)** changes this sequence to
\[
(v_{k-1},v_{k-2},\ldots,v_0,v_k,v_{k+1},\ldots,v_{10}).
\]
The symmetric operation at the other endpoint is allowed. The states are complete spanning paths, not partial paths; vertex labels are fixed, and path reversal is not a new state. The source graph \(H\) is non-Hamiltonian because every cycle in a bipartite graph is even whereas \(H\) has eleven vertices.

## Proof

**Endpoint structure and local degree.** A spanning path of a bipartite graph with bipartition sizes \(5\) and \(6\) alternates between the parts, so both endpoints lie among the six \(b\)-vertices. Each such vertex has degree three in \(H\), of which exactly one incident edge belongs to a given spanning path. Its other two neighbors lie in the interior of the path, since both endpoints are in the same bipartition class and are therefore nonadjacent. Either unused edge supplies one valid backbite. Distinct choices, and the two opposite endpoints, produce four distinct neighboring spanning paths. Thus \(\mathcal B(H)\), once its states are established, is four-regular.

**Complete state enumeration.** In `verify_dfs.py`, a recursion beginning at each of the eleven vertices extends a sequence only along an unused adjacent vertex. At length eleven it stores the lexicographically smaller of the sequence and its reversal. Every Hamiltonian path has a unique oriented starting sequence in this recursion up to reversal, and no non-Hamiltonian sequence can enter the state set. The resulting set has exactly \(222\) members. The endpoints have exactly the three stated orbit types. The aggregate numbers of paths of these types are, respectively, \(3\cdot14=42\), \(6\cdot12=72\), and \(6\cdot18=108\), totalling \(222\).

**Complete legal moves and distances.** The explicit backbite formula generates each legal edge; it yields exactly \(444\) unordered edges, and every state has four neighbors. Breadth-first search from each of the \(222\) states reaches every state, proving connectivity, and constructs the complete distance histogram above. The maximum eccentricities are \(8\) and \(9\) with multiplicities \(198\) and \(24\). Exactly twelve unordered pairs are at distance nine, and each of their twenty-four endpoints occurs in exactly one such pair. The six cross-pole/different-matched-pair endpoint classes each contain four of these exceptional states.

For an explicit sharpness witness, use the labelled vertex convention above and the two paths
\[
(5,0,6,4,8,2,7,3,9,1,10), \quad
(6,1,5,3,7,0,8,4,10,2,9).
\]
Breadth-first search from the first has consecutive distance-sphere sizes \((1,4,12,28,45,55,49,21,6,1)\); the second is in the last sphere. This proves the lower bound of nine, while the complete all-source census proves the upper bound.

**Second exhaustive formulation.** In `verify_edges.py`, rather than growing paths, all \(\binom{18}{10}=43758\) ten-edge subsets of \(H\) are inspected. Exactly \(222\) yield connected spanning graphs with degree multiset \((1,1,2,2,2,2,2,2,2,2,2)\), hence unoriented Hamiltonian paths. Two resulting paths form a backbite pair precisely when their edge sets differ by one deleted and one added edge, and the added edge is incident to an endpoint of the original path. Indeed, adding that edge creates a unique cycle; preservation of a connected spanning path forces deletion of the cycle edge on the way toward the original endpoint. This algorithm independently reconstructs all \(444\) edges and repeats every shortest-path check. A separate subset dynamic-programming recurrence independently verifies all fifteen endpoint-pair counts. Thus both the state enumeration and the local-move construction have distinct exhaustive implementations.

## Verification

Run `python verify_dfs.py` and `python verify_edges.py` from the directory containing the two included scripts. Both use only Python's standard library, create their own copy of the explicitly defined eleven-vertex graph, and abort on any failed assertion. Their checks include state counts, backbite edge counts, connectedness, complete all-pairs distance histograms, endpoint classes, and matching of the diameter pairs. The second script also exhausts all \(43758\) ten-edge candidates, and the first checks the explicit distance-nine witness.

The finite enumeration is exact and exhaustive: it does not extrapolate from random samples or impose a search timeout. The verifiers operate on the precise graph construction and fixed vertex labels stated above.

## Relationship to prior work

The backbite move and its role in compact polymer sampling are established work; Oberdorf, Ferguson, Jacobsen and Kondev gave an accessible 2005 preprint with a small square-lattice transition graph. Kazazi subsequently studied Hamiltonian-path backbite connectivity on general graphs. The sufficient spanning-squared-path hypothesis in Kazazi's theorem cannot apply to the Herschel graph, because any squared path on at least three vertices contains a triangle, whereas the Herschel graph is bipartite. The general results do not supply this graph's complete state count, metric, endpoint profiles or diameter-pair matching. The classical definition and non-Hamiltonicity of the Herschel graph themselves are also prior knowledge. The contribution here is the stated exact, reproducible reconfiguration classification for that graph.

## Limitations

The claim is specific to the eleven-vertex Herschel graph and the precise endpoint backbite rule. It does not provide a general theorem for all polyhedral or non-Hamiltonian graphs, or bounds on random-walk mixing times. Mathematical correctness rests on two exhaustive finite computations as explained above, not on an independent human audit. Historical priority remains qualified: an equivalent graph-specific tabulation may exist in an unindexed source.

## References

1. R. Oberdorf, A. Ferguson, J. L. Jacobsen and J. Kondev, *Secondary Structures in Long Compact Polymers*, arXiv:cond-mat/0508094, first submitted 2005-08-03; subsequently *Physical Review E* **74** (2006), 051801. https://arxiv.org/abs/cond-mat/0508094
2. A. Kazazi, *Connectivity of the Reconfiguration Graph of Hamiltonian Paths*, arXiv:2610.05068, first submitted 2026-10-04. https://arxiv.org/abs/2610.05068
3. E. W. Weisstein, *Herschel Graph*, MathWorld, Wolfram Research. https://mathworld.wolfram.com/HerschelGraph.html
4. H. S. M. Coxeter, *Regular Polytopes*, 1948, p. 8; cited as a historical source for the graph, not for the present reconfiguration classification.
