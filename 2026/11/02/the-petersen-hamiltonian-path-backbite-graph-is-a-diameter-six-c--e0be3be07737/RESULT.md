# The Petersen Hamiltonian-path backbite graph is a diameter-six Cayley graph of \(S_5\)

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, and let \(\mathcal R(P)\) have as vertices its undirected Hamiltonian paths, with a path identified with its reversal. Two such paths are adjacent when a single Pósa endpoint rotation (also called a *backbite*) transforms one into the other. Then \(\mathcal R(P)\) has exactly \(120\) vertices and \(240\) edges, is connected and \(4\)-regular, and has radius and diameter both equal to \(6\).

More structurally, the natural \(S_5\)-action on Hamiltonian paths is regular. Choose the reference path
\[
B=(01,23,04,12,34,02,13,24,03,14),
\]
where \(ab\) denotes the two-element subset \(\{a,b\}\) of \(\{0,1,2,3,4\}\). Under the identification \(g\leftrightarrow gB\), the backbite graph is the undirected right Cayley graph
\[
\mathcal R(P)\cong\operatorname{Cay}\bigl(S_5,\{(0\,3\,2\,4),(0\,4\,2\,3),(0\,1)(2\,3),(0\,3)\}\bigr).
\]
The exact numbers of paths at distances \(0,1,\ldots,6\) from *every* path are
\[
(1,4,11,25,39,29,11).
\]
In particular the Petersen graph itself is not a Cayley graph, but its Hamiltonian-path backbite reconfiguration graph is a Cayley graph.

## Assumptions and scope
The underlying graph is exactly \(\operatorname{KG}(5,2)\), with ten vertices the two-element subsets of \(\{0,1,2,3,4\}\); two subsets are adjacent precisely when disjoint. A Hamiltonian path visits all ten vertices exactly once. Reversal is not a new state; the two possible endpoints may both be used as pivots for rotations. For an oriented presentation \(v_0,\ldots,v_9\), a legal rotation at the last endpoint chooses \(i\in\{0,\ldots,7\}\) with \(\{v_i,v_9\}\in E(P)\), replaces edge \(v_iv_{i+1}\) by \(v_iv_9\), and yields
\[
(v_0,\ldots,v_i,v_9,v_8,\ldots,v_{i+1}).
\]
The same operation is permitted at the other endpoint, by reversing the presented path. No extra move (such as arbitrary independent edge swaps or intermediate non-Hamiltonian states) is allowed. Permutations are composed right-to-left; the displayed generators use standard cycle notation on \(\{0,1,2,3,4\}\).

## Proof
**Exhaustive path count.** The graph has \(10\) vertices, each of degree \(3\). Enumerate oriented simple walks with a bitmask of visited vertices, starting at each possible vertex and extending only along graph edges to previously unvisited vertices. Retain walks of length ten and identify each with its reversal using the lexicographically smaller presentation. This finite recursion visits every Hamiltonian path and no others. It gives \(120\) undirected Hamiltonian paths. As an independent count, the graph has \(30\) unordered nonedges; the same complete enumeration finds exactly four Hamiltonian paths with each prescribed nonadjacent endpoint pair (and none with adjacent endpoints). The latter is consistent with \(30\cdot4=120\) and is also checked in the independent implementation.

**Free transitive symmetry.** Relabelling the five elements acts on all two-subsets, preserves disjointness, and therefore acts on the Hamiltonian-path set and preserves rotations. Enumerating the \(5!=120\) permutations and applying each to the reference path \(B\), again taking paths modulo reversal, gives \(120\) distinct images. Since there are exactly \(120\) paths, the action is free and transitive, identifying all paths with \(S_5\).

**Edges and generators.** From either oriented end of \(B\), check all eight eligible pivot positions with the adjacency criterion in the definition. Exactly four *distinct* rotations occur. Under the free \(S_5\)-identification, their images are those of
\[
a=(0\,3\,2\,4),\quad a^{-1}=(0\,4\,2\,3),\quad b=(0\,1)(2\,3),\quad c=(0\,3).
\]
Every permutation preserves the operation, so the four rotations from \(gB\) lead precisely to \(gaB\), \(ga^{-1}B\), \(gbB\), and \(gcB\). This proves the asserted Cayley model and gives \(120\cdot4/2=240\) edges. Connectivity follows already algebraically: \(a,c\) generate the full symmetric group on \(\{0,2,3,4\}\), as the transposition \(c\) and its conjugates along the four-cycle generate adjacent transpositions; multiplying \(b=(0\,1)(2\,3)\) by \((2\,3)\) gives \((0\,1)\), which extends the generated group to all of \(S_5\).

**Exact metric.** Breadth-first search on the \(120\) permutations from the identity, applying each of the four explicitly displayed right generators, obtains the seven shells \((1,4,11,25,39,29,11)\), exhausting the group. Thus the maximum word length is \(6\), and there are \(11\) elements of length \(6\) (for example the one-line permutation \((0,2,4,3,1)\)). Regular left multiplication acts by graph isometries, so every vertex has eccentricity exactly \(6\); the radius and diameter are both \(6\). Both the exhaustive group calculation and its independent direct path-graph check are implemented in the attached programs.

**Independent edge criterion.** For this non-Hamiltonian graph, the endpoint vertices of a Hamiltonian path are nonadjacent. If another Hamiltonian path differs by removing exactly one path edge and adding exactly one graph edge, the added edge must run from an old endpoint to an interior vertex: connecting two interior vertices leaves two degree-three vertices, and connecting the two endpoints is impossible. To recover a path, the edge removed must be the edge from that interior vertex toward the original endpoint, exactly a backbite. Conversely every backbite changes one edge each way. Hence the alternative edge-mask verifier enumerates the same graph without implementing the rotation operation.

## Verification
Run `python3 verify.py` with Python 3.9+ and no external packages. It constructs the Kneser adjacency directly, enumerates all paths, applies endpoint rotations, checks the \(120\)-element regular action and all Cayley edges, and verifies distances from every state. It ends with `PRIMARY_CERTIFICATE_OK`.

Independently run `c++ -std=c++17 -O2 verify_alt.cpp -o verify_alt && ./verify_alt`. It constructs the isomorphic generalized Petersen graph \(GP(5,2)\) from pentagon, pentagram, and spokes, enumerates spanning paths, encodes each as a \(15\)-bit edge mask, compares every pair of paths for one-edge exchanges, and checks the complete all-sources distance distribution. It ends with `ALTERNATE_CERTIFICATE_OK`. For clarity, one explicit isomorphism sends outer vertices \(u_0,\ldots,u_4\) of \(GP(5,2)\) to \((01,23,04,12,34)\) and inner vertices \(v_0,\ldots,v_4\) to \((24,14,13,03,02)\).

Both programs were executed successfully, then independently rerun after extraction from the final embedded-file package. These are finite exhaustive calculations, not inferences about arbitrary cubic graphs.

## Relationship to prior work
Pósa's classical 1976 rotation-extension method introduces endpoint rotations of paths. Ferber, Kronenberg and Long's archival 2015 paper discusses that method in connection with Hamiltonian counting and packing; its publicly dated first version is 2015-06-01. Neither specifies the Petersen path-reconfiguration Cayley graph or exact diameter.

Kazazi's 2026 paper develops the backbite reconfiguration graph systematically and proves connectivity under a spanning squared-Hamiltonian-path hypothesis. Its theorem does not cover the Petersen graph, which is \(3\)-regular and cannot contain the square of a spanning ten-vertex path (that square has internal vertices of degree \(4\)); its detailed statements and constructions do not compute this case. An accessible earlier finite result on Hamiltonian-path rotations concerns the *Herschel* graph (\(222\) paths, a different underlying graph) and does not imply this Petersen classification. Basic Petersen Hamiltonicity and the \(S_5\)-automorphism action are background, not novelty claims.

## Limitations
This is an exact theorem about the ten-vertex Petersen graph only. It gives no general Hamiltonian-path reconfiguration theorem for all cubic, vertex-transitive, or non-Hamiltonian graphs. The Cayley generating set depends on the explicit reference path and indexing, although the isomorphism type does not. No independent scholarly audit has been performed. Unindexed or otherwise inaccessible prior work may contain an equivalent special-case classification; absence of a database hit does not prove uniqueness.

## References
1. L. Pósa, *Hamiltonian Circuits in Random Graphs*, Discrete Mathematics 14 (1976), 359–364. DOI: 10.1016/0012-365X(76)90068-6.
2. A. Ferber, G. Kronenberg, E. Long, *Packing, Counting and Covering Hamilton cycles in random directed graphs*, arXiv:1506.00618 (first posted 2015-06-01), https://arxiv.org/abs/1506.00618 .
3. A. Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*, arXiv:2610.05068 (first posted 2026-10-04), https://arxiv.org/abs/2610.05068 .
4. E. W. Weisstein, *Pósa Rotation*, MathWorld, https://mathworld.wolfram.com/PosaRotation.html .
