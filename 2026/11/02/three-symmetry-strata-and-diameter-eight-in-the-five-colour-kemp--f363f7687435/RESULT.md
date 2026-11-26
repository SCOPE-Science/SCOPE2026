# Exact distance profiles in the five-colour edge-Kempe graph of \(K_{3,5}\)

## Finding

Let \(\mathcal K\) be the simple graph on the proper five-edge-colourings of \(K_{3,5}\), with all vertices of \(K_{3,5}\) and all five colours individually labelled. A move interchanges two colours on one entire nonempty connected component of the subgraph formed by the edges of those colours. Then \(\mathcal K\) is connected, with **radius 7 and diameter 8**. Its BFS profiles are constant within each row/column/symbol isotopy class of the associated \(3\times5\) Latin rectangles. The three such classes are already tabulated by McKay [1]; the result here is the graph metric on them, not the existence or number of the isotopy classes.

The complete distance profiles in the **labelled** graph are as follows. Each profile gives the number of vertices at distances \(0,1,\ldots\) from a state in the indicated class. The class sizes are included to identify the rows and give their multiplicities, not as a new isotopy enumeration.

| Labelled size of isotopy class | Kempe degree | Eccentricity | Distance profile |
|---:|---:|---:|:---|
| 8,640 | 15 | 8 | \((1,15,180,1480,8302,27868,26713,1675,6)\) |
| 14,400 | 16 | 7 | \((1,16,182,1472,8243,27793,26899,1634)\) |
| 43,200 | 17 | 7 | \((1,17,191,1540,8609,28689,25974,1219)\) |

Thus the 8,640 states in the first class each have exactly six partners at distance eight, and no other state has a distance-eight partner. There are 25,920 unordered diametral pairs and 57,600 central states. For reference, the underlying state count is 66,240 and the degree census gives 547,200 undirected edges.

## Assumptions and scope

The bipartition has three vertices on the left and five on the right. The five named colours are \(\{0,1,2,3,4\}\). A proper colouring uses each colour once at each left vertex; incident edges at each right vertex also have distinct colours. Each switch uses exactly one whole bichromatic connected component, not a proper subpath, a union of several components, or a sequence through improper colourings. Graph adjacency is between distinct colourings. Row, column and colour permutations act as symmetries; none is used to identify states for adjacency or distance.

## Proof

1. **States and isotopy representatives.** Store the colours as three ordered rows, one for each left vertex, and five ordered columns, one for each right vertex. Every row is a permutation of the palette and the three values in each column are distinct, so the state encoding is exactly a Latin rectangle. Fix the first row to \((0,1,2,3,4)\) by a unique symbol relabelling. Enumerate the possible remaining rows from all \(5!\) permutations, rejecting repeated values in any column. This gives 552 normalized states: 20 second rows of cycle type \((2,3)\) with 12 extensions each, and 24 five-cycles with 13 extensions each. All 120 palette permutations of each normalized state recover distinct labelled states, giving 66,240. For a normalized state, permute the three rows and five columns in all possible ways and renormalize the first row after each permutation. The smallest resulting rectangle is a canonical representative: for any fixed row/column permutation, renormalization removes the effect of any prior symbol permutation. Thus two normalized states have equal representatives exactly when they are isotopic. The normalized class sizes obtained are 72, 120 and 360, used here to identify the three representatives for the distance calculation. Each size increases by a factor of 120 in the fully labelled space. As a graph action, isotopy preserves the definition of a switch, so graph distances and profiles are invariant under it.

2. **Adjacency.** For each state and each unordered colour pair, list the six edges of the two colours. Group them by connectivity, either by taking the transitive closure of incidence among these edges or by finding the components of their bipartite endpoint graph. Produce one neighbour per nonempty component by interchanging the pair on all of its edges at once. This preserves properness: all edges in the pair incident with a vertex of the component are switched together. Each allowed move is listed; the reverse switch uses the same component in the resulting state. Deduplicating neighbours yields degree counts \(15^{8640},16^{14400},17^{43200}\); the degree sum is 1,094,400.

3. **Labelled BFS.** For each of the three representatives, mark its distance zero and visit the full labelled adjacency graph in FIFO order, recording the first visit to each state. In every case this reaches 66,240 vertices and gives the complete histogram in the table. Thus the graph is connected. Since isotopy acts by graph automorphisms and every vertex is in one of the three classes, these searches determine every vertex's eccentricity. Their minimum is 7 and maximum is 8. Only vertices of eccentricity 8 can be endpoints of a diametral pair, and the distance-eight entry is 6 in their orbit, giving \(8640\cdot6/2=25{,}920\) pairs. The two remaining classes comprise the center.

## Verification

The accompanying `verify_primary.py` (Python 3.10+) exhaustively generates the labelled graph and tests every table row, including the full profiles. The check of all neighbours includes reciprocity. `verify_alt.cpp`, compiled with `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt` and run as `./verify_alt`, computes components on the eight endpoint vertices, checks the degree census, class sizes and eccentricities, and prints the full profiles for comparison with the table. These finite procedures require no external table or data to run. The isotopy reduction reduces the number of BFS sources, not the number of vertices searched by each BFS.

## Relationship to prior work and limitations

McKay's table explicitly supplies three isotopy classes at order \(5\times3\) [1], the dimensions here in the opposite notation. Classical Latin-rectangle counts concern states; the use of these prior strata in the table is to attach the graph-distance information to each class. The degree in the move graph differs among the classes, and their distance profiles distinguish a peripheral class from the two central classes. Thus the calculation gives more than Kempe equivalence or an unannotated state count.

McDonald, Mohar and Scheide [2] treat general edge-Kempe equivalence, including low-degree and surplus-colour cases, which do not give the metric at the chromatic index five for this graph. Belcastro and Haas [3] treat cubic graphs and three colours. Hong and Miklós [4] study recolouring of bipartite graphs and Latin rectangles. Their Theorem 3.1 gives a diameter bound in the chain \(M(G,k)\); a step of that chain may combine recolouring operations that create and correct temporary deficiencies and hence is not necessarily one strict edge-Kempe switch. Their Theorem 4.4 is for a regular bipartite graph, whereas \(K_{3,5}\) is not regular. These results do not supply the exact strict-switch profiles. The claim is specific to this labelled instance and does not give general connectivity of strict switches, unlabelled distances, or a mixing time. This comparison does not exclude equivalents in other literature.

## References

1. B. D. McKay, *Combinatorial Data: Latin Squares*, section “Isotopy classes of Latin rectangles,” row “order 5x3 (3),” https://users.cecs.anu.edu.au/~bdm/data/latin.html.
2. J. McDonald, B. Mohar and D. Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs*, arXiv:1005.2248v1.
3. S. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730v1.
4. J. Hong and I. Miklós, *A Markov chain on the solution space of edge-colorings of bipartite graphs*, arXiv:2103.11990v1.
