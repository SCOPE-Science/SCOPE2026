# The Heawood hexagon-flip graph is the 24-vertex Klein graph

## Finding
Let \(H\) denote the Heawood graph, the bipartite incidence graph of the Fano plane, and let \(\mathscr P(H)\) consist of its perfect matchings. Form a graph \(R(H)\) with vertex set \(\mathscr P(H)\), joining two perfect matchings exactly when their symmetric difference is the six edges of one cycle of length six in \(H\). Then **\(R(H)\) is isomorphic to the 24-vertex distance-regular Klein graph**. In particular,
\[
 |V(R(H))|=24,\qquad |E(R(H))|=84,
\]
and its intersection array is
\[
 \boxed{\{7,4,1;1,2,7\}}.
\]
Its diameter is three. There are exactly eight distance-three antipodal classes, each comprising three pairwise edge-disjoint perfect matchings. Each class is a partition of the 21 edges of \(H\) into three perfect matchings, and contracting the eight classes yields \(K_8\), with precisely one neighbour in each other class for every vertex. Thus \(R(H)\) is an antipodal threefold cover of \(K_8\).

For arbitrary perfect matchings \(M,N\) of \(H\), let \(t=|M\cap N|\). Their hexagon-flip distance has the exact rule
\[
 d_{R(H)}(M,N)=\begin{cases}
 0& t=7,\\
 1& t=4,\\
 2& t\in\{1,2\},\\
 3& t=0.
 \end{cases}
\]
No other intersection cardinalities occur. In particular, every two perfect matchings can be connected by at most three hexagon flips.

## Assumptions and scope
Represent the seven points by \(\mathbb Z/7\mathbb Z\) and the seven lines by
\[
 L_j=\{j,j+1,j+3\}\pmod{7},\qquad j\in\mathbb Z/7\mathbb Z.
\]
A perfect matching is uniquely represented by a permutation \(p\) of \(\{0,1,\ldots,6\}\) with \(i\in L_{p(i)}\) for every point \(i\). The graph operation is strictly a *single alternating hexagon switch*: remove the three matching edges on one six-cycle and insert the other three cycle edges; intermediate states must remain perfect matchings. The comparison Klein graph is the specific 24-vertex distance-regular graph with published binary adjacency matrix in Reference 3, not the distinct 56-vertex cubic Klein graph.

## Proof
**Exact finite classification of matchings and switches.** Every perfect matching gives precisely one admissible permutation of the seven lines. Enumerate all \(7!=5040\) permutations in lexicographic order, retaining just those with \(i\in L_{p(i)}\) for all seven \(i\). The executable `verify_flips.py` carries out this fully bounded search, proves that exactly 24 survive, and uses the same explicit incidence rule to enumerate every simple six-cycle: select three distinct points and three distinct lines and require all six cyclic consecutive incidences. The result contains exactly 28 unique undirected hexagons, stored as sets of six edges.

For each matching and each hexagon, the script checks whether exactly three of the hexagon's edges belong to the matching. Such three edges alternate because the matching has no repeated endpoints; replacing them by the complementary three yields another perfect matching. Conversely, two perfect matchings differ by a single hexagon switch if and only if their symmetric difference is one such six-cycle. The script constructs the entire adjacency matrix this way, obtaining degree seven at every vertex, 84 undirected edges, and three undirected switching edges per hexagon. These counts are exact finite enumeration, not statistical sampling.

**Explicit graph-identification certificate.** `MATCHINGS.txt` records the lexicographically ordered 24 admissible permutations. The reference adjacency matrix is reproduced *in full* in `KLEIN_ADJACENCY.txt` from Reference 3, one 24-bit row per vertex. `ISOMORPHISM.txt` gives the complete vertex bijection \(\phi\), indexing both matrices from zero: 
\[
(0,11,3,4,15,6,8,19,13,9,18,21,7,22,17,2,1,12,14,10,16,5,23,20).
\]
For **each** of the 576 ordered pairs \((u,v)\), `verify_flips.py` independently reconstructs the hexagon-switch adjacency and checks the exact equivalence
\[
 u\sim_{R(H)}v\quad\Longleftrightarrow\quad \phi(u)\sim_{K} \phi(v),
\]
using the 24-by-24 published matrix. The program additionally checks that \(\phi\) is a bijection and that the external matrix is symmetric, loopless and seven-regular. This finite exhaustive equality certifies the isomorphism without relying on a numerical similarity of graph invariants.

**Metric and antipodal classification.** Breadth-first searches from each of the 24 vertices give exactly \(1,7,14,2\) vertices at respective distances \(0,1,2,3\). For every rooted vertex and every vertex at distance \(i\), the number of neighbours at distance \(i-1\) is \((1,2,7)\) and the number at distance \(i+1\) is \((4,1,0)\), independent of the vertex. This proves the displayed distance-regular intersection array. For all 576 ordered pairs the code also compares the number of shared matching edges to the graph distance, obtaining exactly the piecewise distance rule above.

For each matching \(M\), its two distance-three partners are exactly the two other matchings sharing no Heawood edge with \(M\). The exhaustive pair check shows that adjoining these partners defines a three-element equivalence class. There are eight such classes. Because three pairwise disjoint perfect matchings use \(3\cdot7=21\) different edges, each class is an edge partition of \(H\). Finally, for each of the 24 matchings and each of the other seven classes, the script verifies exactly one switching neighbour therein. Thus the quotient graph is the complete graph \(K_8\), with the asserted antipodal-cover property.

## Verification
Two independently constructed executable Python programs provide complementary finite certificates. `verify_flips.py` works with the cyclic seven-line model and explicit six-edge cycles and checks the full published-matrix isomorphism. `verify_binary.py` reconstructs the incidence graph instead from nonzero vectors and nonzero binary linear forms in dimension three, uses recursive backtracking for perfect matchings, and generates flips by cyclically permuting the line partners of three points; it separately checks all-pairs distances, neighbour intersection numbers and antipodal classes. Both use only the Python standard library. Run them in the directory containing the accompanying data files using `python3 verify_flips.py` and `python3 verify_binary.py`; compare stdout with `VERIFY_FLIPS_OUTPUT.txt` and `VERIFY_BINARY_OUTPUT.txt`. All assertions succeed in the included run records. No floating point arithmetic or heuristic search enters either final verifier.

## Relationship to prior work
The Klein graph, with 24 vertices and intersection array \(\{7,4,1;1,2,7\}\), was already known; this result does not claim to discover its parameters. Dejter's 2010 paper constructs the Klein graphs geometrically starting from the Coxeter graph and the 28 hexagons of the Heawood graph (Reference 1). That construction concerns the Coxeter graph and the Klein maps, not the graph formed by *perfect matchings* of the Heawood graph under single-hexagon switches. Existing Heawood material also lists 24 perfect matchings and eight perfect three-edge-colourings (Reference 2). Those enumerations by themselves do not identify the 84-switch adjacency matrix with the Klein graph or establish shortest switching distances and the antipodal threefold covering structure. Reference 3 provides independently published labelled Klein adjacency, enabling an explicit structural identification rather than only agreement of parameters.

## Limitations
The theorem is an **exact finite** result about the Heawood graph, not a claim for all incidence graphs of projective planes. The exhaustive programs are transparent proof certificates for finite claims; they do not demonstrate any general infinite theorem. The matrix identification is relative to the published adjacency in Reference 3. The 24-vertex Klein graph must not be confused with the cubic 56-vertex Klein graph. Earlier work also studies subsets of hexagon switches supported by fixed toroidal embeddings; the present statement concerns **all** alternating hexagon switches, without an embedding restriction. A complete historical priority assessment is not proved by literature search. An equivalent graph identification in an unindexed source remains a residual originality risk.

## References
1. I. J. Dejter, *From the Coxeter graph to the Klein graph* (first arXiv release 9 February 2010), arXiv:1002.1960, https://arxiv.org/abs/1002.1960 . Full preprint inspected for graph constructions and comparison of the 24- and 56-vertex Klein graphs.
2. *Heawood Graph*, reference page with perfect-matching count and three-factorization count, https://jaanos.github.io/tables/graphs/Heawood.html .
3. Distance-Regular Graphs database, *Klein graph*, Memorial University, https://www.math.mun.ca/distanceregular/graphs/klein.html ; labelled adjacency matrix https://www.math.mun.ca/distanceregular/graphdata/klein.am .
4. R. Diestel, *Graph Theory*, standard definitions of perfect matching, graph distance and graph isomorphism (background terminology only).
