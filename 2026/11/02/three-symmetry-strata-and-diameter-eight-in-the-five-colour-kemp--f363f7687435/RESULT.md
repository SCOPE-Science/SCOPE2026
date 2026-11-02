# Three symmetry strata and diameter eight in the five-colour Kempe graph of \(K_{3,5}\)

## Finding
Let \(G=K_{3,5}\), with three individually labelled left vertices, five individually labelled right vertices, and five individually labelled colours \(\{0,1,2,3,4\}\). Let \(\mathcal K\) have as vertices all proper five-edge-colourings of \(G\). Two **distinct** vertices are adjacent precisely when interchanging a pair of colours on **one entire nonempty connected component** of their two-colour subgraph transforms one colouring into the other. Then
\[
|V(\mathcal K)|=66{,}240,\qquad |E(\mathcal K)|=547{,}200,
\quad \operatorname{rad}(\mathcal K)=7,\qquad
\operatorname{diam}(\mathcal K)=8.
\]
The graph is connected. The natural symmetry group \(S_3\times S_5\times S_5\), acting by left-vertex, right-vertex and colour permutations, has precisely three orbits on these colourings. Their (orbit size, graph degree, eccentricity) are
\[
(8{,}640,15,8),\quad(14{,}400,16,7),\quad(43{,}200,17,7).
\]
The corresponding distance profiles (number of configurations at distances \(0,1,\dots\) from any representative of the orbit) are, respectively,
\[
(1,15,180,1480,8302,27868,26713,1675,6),
\]
\[
(1,16,182,1472,8243,27793,26899,1634),
\]
\[
(1,17,191,1540,8609,28689,25974,1219).
\]

## Assumptions and scope
All graphs are finite and simple. Every edge is assigned one of five named colours, and incident edges must have distinct colours. Every colour is used on the three left-vertex edges, so each colour occurs exactly three times. A move switches only one **connected component** of the graph induced by edges of two chosen colours, not an arbitrary proper subpath, and self-loops are discarded. Colour permutations are treated as symmetries only for analyzing orbits; **they are not identified when counting states or constructing moves**. Thus the 66,240 states are fully labelled. The graph has degree five on the left and degree three on the right.

## Proof
Encode a proper colouring as three ordered rows of length five; every row is a permutation of the five colours and the three entries in every column are pairwise distinct. This correspondence between colourings and \(3\times5\) Latin rectangles is bijective. With the first row fixed to \((0,1,2,3,4)\), the second row is a derangement: exactly twenty permutations of cycle type \((2,3)\), each permitting twelve third rows, and twenty-four five-cycles, each permitting thirteen third rows. Hence the normalized count is \(20\cdot12+24\cdot13=552\), and undoing the first-row colour normalization gives \(5!\cdot552=66{,}240\) labelled colourings. The two third-row extension counts are also verified by the full enumeration, and may be checked by directly testing the remaining \(5!\) permutations per second row.

For every encoded colouring and unordered pair of colours, list all six edges bearing these colours. Regard two listed edges as connected when they share a graph endpoint; take the transitive closure of this relation. For each resulting component, swap the two colours at all its edges. The result is again a proper colouring because each vertex incident with the component has its incident edges of the chosen colours switched together. The procedure finds **all** and only legal edge-Kempe neighbours by definition. Deduplicating transformed states and pairing reciprocal adjacencies gives \(1{,}094{,}400\) directed adjacency incidences, hence \(547{,}200\) undirected edges; the degree multiset is \(15^{8{,}640},16^{14{,}400},17^{43{,}200}\).

To check the full orbit decomposition, apply every permutation of the three rows and five columns to each normalized state and then uniquely relabel colours to restore its first row to identity. Lexicographically minimizing these images partitions the 552 normalized states into classes of sizes \(72\), \(120\), \(360\); unnormalizing colours gives the three orbit sizes in the claim. The operations used in canonicalization are invertible, and every allowed independent row, column, and colour symmetry is represented. Because the symmetry group acts by graph automorphisms, degrees and distance profiles are constant on each orbit.

Run breadth-first search in the fully labelled \(66{,}240\)-vertex adjacency graph from one orbit representative in each class. In all three searches every vertex is reached, establishing connectedness. The exact distance profiles are listed in the finding; the largest distances for the three orbits are \(8,7,7\). Since every vertex belongs to one of the three orbits, these three searches determine the eccentricity of **every** vertex. The minimum eccentricity is seven and the maximum is eight, proving the asserted radius and diameter. This is an exhaustive finite proof, not an extrapolation from sample graphs.

## Verification
Run `python3 verify_primary.py` (Python 3.10+) and compile the independently constructed verifier using `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt`, followed by `./verify_alt`. Both standalone programs enumerate all proper Latin rectangles, build whole-bichromatic-component Kempe edges, compute complete adjacency and symmetry orbit classes, and run shortest-path calculations from each orbit representative. The Python implementation uses an edge-connectivity closure; the C++ implementation uses connectedness of the eight-vertex bichromatic incidence graph. In particular, the latter computes components without reusing the former's construction. The asserted numerical invariants are embedded as explicit checks rather than trusted output constants alone. No third-party datasets, downloaded files, or external solvers are required. The proof's exhaustive bound derives from the exact finite state encoding.

## Relationship to prior work
Kempe equivalence of edge-colourings is classical. McDonald, Mohar and Scheide [1] prove broad edge-Kempe equivalence theorems, but their low-degree and surplus-colour cases do not yield this sharp five-colour graph metric for \(K_{3,5}\), whose maximum degree and chromatic index are both five. Belcastro and Haas [2] classify edge-Kempe behaviour in 3-edge-coloured cubic graphs, a different degree/colour regime. Hong and Miklós [3] establish ergodic recolouring Markov chains on bipartite graphs, including transitions with altered intermediate properness or additional colours; their more permissive perturbation rules and general bound do not imply connectivity under a **single whole bichromatic-component** swap, much less this diameter or orbit stratification. Classical Latin-rectangle counts concern the state set, not this reconfiguration metric. Our claim is the exact strict-Kempe reconfiguration classification at the natural three-row, five-symbol finite case, not a claim to the general definition or Latin-rectangle enumeration.

## Limitations
This is a complete finite classification for the specified labelled \(K_{3,5}\) model, not an assertion about all \(K_{m,n}\), arbitrary recolouring operations, unlabelled counting, or Markov mixing time. The exact counts depend on requiring **whole** bichromatic components and retaining labels. Equivalent results could exist in incompletely indexed or inaccessible older Kempe/Latin-rectangle literature. The two code implementations corroborate the same finite assertion but do not constitute external independent scholarly validation.

## References
[1] J. McDonald, B. Mohar and D. Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs* (2010), arXiv:1005.2248v1, https://arxiv.org/abs/1005.2248 .
[2] S. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs* (2012), arXiv:1209.1730v1, https://arxiv.org/abs/1209.1730 .
[3] J. Hong and D. Miklós, *A Markov chain on the solution space of edge-colorings of bipartite graphs* (2021), arXiv:2103.11990v1, https://arxiv.org/abs/2103.11990 .
