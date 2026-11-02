# The Klein graph hidden in Heawood backbite dynamics

## Finding
Let \(H\) be the fourteen-vertex Heawood graph. Define \(\mathcal B(H)\) to have, as vertices, all undirected Hamiltonian paths of \(H\), with a path and its reversal identified. A *backbite* joins an endpoint of a Hamiltonian path to a nonconsecutive **interior** vertex and deletes the path edge incident to that interior vertex on the newly formed cycle. Two paths are adjacent precisely when one backbite changes one into the other.

Let \(K\) denote the cubic Klein graph, Foster census graph F056B, with 56 vertices and 84 edges. Form its *truncation* \(T(K)\) by replacing each vertex with a triangle, one triangle vertex (a *port*) for each incident edge, and joining the corresponding ports across each original edge. Double each of the 84 intertriangle edges, keeping the 168 intratriangle edges simple. Subdivide each edge of the resulting multigraph once, assigning distinct subdivision vertices to parallel edges. Denote the resulting simple graph by \(S(T_2(K))\).

**Theorem.** There is an isomorphism
\[
\mathcal B(H)\cong S(T_2(K)).
\]
Consequently \(\mathcal B(H)\) is connected and bipartite, has exactly 504 vertices and 672 edges, has 336 vertices of degree two and 168 of degree four, and has radius 24 and diameter 25. Its Heawood-induced automorphism action has exactly three path orbits of size 168. Their respective (degree, eccentricity) pairs are \((2,24)\), \((2,25)\), and \((4,25)\).

Equivalently, suppressing every degree-two vertex of \(\mathcal B(H)\) gives a 168-vertex multigraph. Its 168 multiplicity-one edges split into 56 disjoint triangles; its remaining 84 pairs of parallel edges form a doubled perfect matching. Collapsing those triangles and replacing each doubled pair with a single edge gives precisely \(K\). The quotient has girth 7, diameter 6, and distance shells \((1,3,6,12,15,18,1)\) from every vertex.

## Assumptions and scope
Use labels \(P_i,L_j\) for \(i,j\in\mathbb Z/7\mathbb Z\), with the Fano incidence rule \(P_i\sim L_j\) if and only if \(i-j\in\{0,1,3\}\) modulo seven. These are all the edges of \(H\). A Hamiltonian path visits each of its fourteen vertices exactly once; paths are not oriented, and a backbite may be performed at either endpoint, but **not** by joining the two endpoints. The latter operation closes a cycle and does not meet the stated endpoint-to-interior backbite definition. All counts refer to this finite, fixed graph, not a family of arbitrary cubic graphs.

## Proof
**1. Exhaustiveness of the state space.** An ordered depth-first recursion begins at every vertex and extends along each unused neighbor. Every Hamiltonian path has an ordering reached by this recursion, and identifying a path with its reversal removes exactly the double count. `verify_paths.py` exhaustively produces 504 distinct paths. Independently, the Heawood graph has 21 edges; the complement of the thirteen edges of any Hamiltonian path contains eight edges. For a prospective eight-edge complement, exactly two vertices must have complement degree two and the other twelve complement degree one. Of the \(\binom{21}{8}=203490\) possible complements, `verify_edges.py` tests this necessary degree condition and then checks that the retained thirteen edges form a connected graph. A connected graph with exactly two vertices of degree one and all other vertices of degree two is one spanning path. This second complete construction also gives exactly 504 states.

**2. Exact moves and the bipartition.** For an oriented path \(p=(v_0,\ldots,v_{13})\), every legal backbite from \(v_0\) is specified by a unique index \(2\le j\le12\) with \(v_0\sim v_j\). Its new path ordering is
\[
(v_{j-1},v_{j-2},\ldots,v_0,v_j,v_{j+1},\ldots,v_{13}).
\]
The same rule at the opposite endpoint enumerates every backbite. The exhaustive state-and-move table gives 672 undirected edges and degree distribution \((336\text{ of degree }2,168\text{ of degree }4)\). In a cubic graph each path endpoint has two unused incident edges. If the endpoints are adjacent, one unused edge joins them and is excluded; otherwise neither endpoint has such an excluded edge. Thus a Hamiltonian path here has degree two if its endpoints are adjacent and four otherwise, as verified for all 504 states. Each computed backbite goes between the two types, proving the stated bipartition.

**3. Suppression and triangles.** The neighbors of every degree-two state have degree four. Suppress the 336 degree-two states, replacing each by an edge between its two degree-four neighbors. Exactly 252 unordered pairs of degree-four states appear: 168 pairs once and 84 pairs twice. Every degree-four state meets two simple edges and one doubled pair. The subgraph of simple edges is exactly a disjoint union of 56 triangles, covering all 168 degree-four states. The doubled pairs form a perfect matching. On contracting the triangles, the 84 doubled pairs connect distinct triangles without duplicate quotient pairs, yielding a connected cubic simple graph \(Q\) on 56 vertices and 84 edges. The inverse of these reductions is exactly the construction \(S(T_2(Q))\).

**4. Recognition of the Klein graph.** Enumerate the 168 permutations of the seven Fano points that permute the seven line-triples, and compose them with the point-line duality \(P_i\mapsto L_{-i}\), \(L_j\mapsto P_{-j}\). These 336 distinct incidence automorphisms preserve all the above constructions. Their action on the 56 quotient vertices is transitive on all 168 **directed** quotient edges, as the verification checks explicitly. The quotient is cubic, connected, arc-transitive, and has girth seven; in particular it is nonbipartite. The exhaustive Foster census classification of cubic symmetric graphs identifies the unique nonbipartite order-56 symmetric graph as F056B, the cubic Klein graph (Conder--Dobcsányi; see also Dejter's introduction). Therefore \(Q\cong K\), giving the asserted structural isomorphism.

**5. Distances and orbits.** Breadth-first search from every one of the 504 paths gives eccentricity 24 for exactly 168 states and eccentricity 25 for the other 336, hence the claimed radius and diameter. The 336 incidence automorphisms have precisely three orbits, each containing 168 paths. The core states form one orbit, and the two degree-two orbits have the two different eccentricities stated above. All searches are finite and complete; no statistical extrapolation is used.

## Verification
Both scripts use only Python's standard library and contain all graph data and checks in their source files. Run:

```text
python3 verify_paths.py
python3 verify_edges.py
```

The first script generates all ordered Hamiltonian paths via vertex DFS, constructs their moves, computes all distances, suppresses degree-two states, and enumerates all 336 incidence automorphisms and their induced quotient arcs. The second script constructs the Fano incidence graph independently by orthogonality of nonzero three-bit binary vectors, directly enumerates all 203,490 candidate edge complements, and computes every endpoint rotation as an edge-set exchange. It independently reconstructs the counts, the suppressed graph, girth, and distances. Each script asserts the numerical statements and prints a PASS marker only on success.

## Relationship to prior work
Oberdorf, Ferguson, Jacobsen, and Kondev (first public version 2005-08-03) describe the backbite move for Hamiltonian walks on square lattices and analyze a different small state graph; they do not provide the Heawood reconfiguration or Klein quotient. The Heawood graph's 24 Hamiltonian cycles and its incidence symmetries are classical, not claimed as new. Conder and Dobcsányi classify small cubic symmetric graphs, and Dejter constructs the Klein graph from the Coxeter graph and notes the Coxeter graph's relation to Heawood six-cycles. These works establish the objects and the target graph but do not state the backbite-to-truncation isomorphism. Kazazi's 2026 Hamiltonian-path reconfiguration results include a sufficient condition involving a squared spanning path; it is inapplicable to the girth-six Heawood graph, which cannot contain a path square with fourteen vertices. The present result is a distinct, finite exact connection between the two classic graphs.

## Limitations
The new statement is restricted to the specified fourteen-vertex graph and the endpoint-to-interior move. The computation is an exact finite certificate, not a proof for all incidence graphs or arbitrary cubic graphs. The identification as F056B uses the published exhaustive Foster classification. An equivalent construction might occur under different terminology in historical work; the accessible literature comparisons do not certify absolute historical priority. The 2026 manuscript's full text was not accessible, so its abstract was the only material inspected.

## References
- R. Oberdorf, A. Ferguson, J. L. Jacobsen, and J. Kondev, *Secondary Structures in Long Compact Polymers*, arXiv:cond-mat/0508094v1, first public 2005-08-03, https://arxiv.org/pdf/cond-mat/0508094 .
- M. Conder and P. Dobcsányi, *Trivalent symmetric graphs on up to 768 vertices*, J. Combin. Math. Combin. Comput. 40 (2002), 41--63, https://www.math.auckland.ac.nz/~conder/preprints/cubic768.pdf .
- I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, first public 2010-02-09; Journal of Graph Theory 70 (2012), 1--9, https://arxiv.org/pdf/1002.1960 .
- A. Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*, arXiv:2610.05068, first public 2026-10-04, https://arxiv.org/abs/2610.05068 .
