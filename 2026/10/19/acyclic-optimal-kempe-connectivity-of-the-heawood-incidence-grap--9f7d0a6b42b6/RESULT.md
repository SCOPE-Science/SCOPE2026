# Acyclic-optimal Kempe connectivity of the Heawood incidence graph

## Finding
Let \(H\) be the Heawood graph. The acyclic four-edge-colorings of \(H\), modulo permutations of the four color names, form exactly \(119{,}784\) configurations. If a permitted reconfiguration interchanges two colors on **one entire maximal alternating path**, but is accepted only when the resulting coloring remains acyclic, the resulting reconfiguration graph \(\mathcal A(H)\) has exactly \(832{,}440\) edges and is **connected**.

Its full degree distribution is:

| Degree | Number of configurations |
| ---: | ---: |
| 8 | 672 |
| 9 | 2,688 |
| 10 | 6,384 |
| 11 | 8,904 |
| 12 | 17,584 |
| 13 | 15,624 |
| 14 | 16,968 |
| 15 | 16,632 |
| 16 | 18,480 |
| 17 | 10,752 |
| 18 | 3,472 |
| 19 | 1,176 |
| 20 | 336 |
| 21 | 112 |

There are exactly \(2{,}874{,}816\) labeled acyclic proper four-edge-colorings with the four color names distinguished. Their minimum palette size of four is previously known, not part of the novelty claim.

## Assumptions and scope
The finite simple graph \(H\) has seven point vertices indexed \(0,\dots,6\) and seven line vertices indexed \(0,\dots,6\). A point \(i\) meets line \(j\) precisely when \(i-j\pmod 7\in\{0,1,3\}\). There are \(14\) vertices, \(21\) edges and all degrees equal three. Fix point \(0\), and order its three incident edges by the line index. Use the palette \(\{0,1,2,3\}\).

A coloring is **proper** when three incident edges at every vertex have distinct colors, and **acyclic** when, for each unordered pair of colors, their union forms a forest (contains no alternating cycle). Two acyclic colorings count as the same configuration if one is a global permutation of the four colors of the other. Each class has a unique representative in which the three root-incident edges have colors \(0,1,2\) in order: the remaining color is \(3\). Every acyclic coloring uses all four colors, because a proper three-edge-coloring of a cubic graph has a bichromatic 2-factor with cycles.

For each unordered pair of palette colors, form the maximal connected components of edges having those two colors. Every nonempty component is an alternating path under acyclicity. Interchange its two colors. An undirected reconfiguration edge joins the original and modified colorings only when the latter is still acyclic and distinct modulo global color permutation. Ignore identity moves and repeated descriptions of the same pair. The graph has labeled original graph vertices, but unordered color names.

## Proof
**Exhaustive finite certificate with complete search.** Both included standalone C++17 programs reconstruct \(H\) and systematically enumerate all four-edge assignments satisfying the fixed root normalization.

In `verify_a.cpp`, depth-first search chooses an uncolored edge with minimum available palette, assigns each locally compatible color, and prunes a candidate if its insertion creates a bichromatic cycle. The pruning condition is exhaustive: inserting color \(c\) on edge \(uv\) creates a two-color cycle only if for some other color \(d\) there already exists a \(c,d\)-alternating path joining \(u\) and \(v\). Since an incomplete state has only already colored edges, this test detects every newly formed alternating cycle, and a rejected partial state cannot extend to an acyclic complete coloring. This search yields \(119{,}784\) normalized valid states, with no duplicates.

In `verify_b.cpp`, a distinct realization of the Fano plane uses nonzero vectors in \(\mathbb F_2^3\), with a point \(a\) incident to a line \(b\) precisely if their scalar product is zero. It independently enumerates **all** \(230{,}336\) proper normalized four-edge-colorings without acyclicity pruning, and tests all six bichromatic edge subgraphs using disjoint-set cycle detection. Exactly \(119{,}784\) states survive. Both incidence models realize the unique projective plane of order two and hence the same labeled-isomorphism type.

Every nonempty bichromatic component in each accepted coloring is found by exhaustive graph traversal; switching its colors preserves properness. The programs independently check the forest condition on the modified coloring, normalize the root colors, and deduplicate destination states. They obtain the same degree histogram above. Its degree sum is \(1{,}664{,}880\), and the edge count is half that sum, \(832{,}440\). Both independently verify reciprocal adjacency, zero missing destinations, and a breadth-first traversal visiting **all** \(119{,}784\) states from one configuration. Connectivity follows.

These exhaustive certificates prove the claims for this particular finite graph; they are not extrapolations to arbitrary cubic graphs.

## Verification
Compile and run with a standard C++17 compiler:

```sh
g++ -std=c++17 -O2 verify_a.cpp -o verify_a
./verify_a
g++ -std=c++17 -O2 verify_b.cpp -o verify_b
./verify_b
```

The two source files are self-contained, use different descriptions of \(H\), independent enumeration paths and transition implementations. The accompanying `check_a.log` and `check_b.log` give the actual outputs. The first program includes a non-deterministic elapsed-time field; mathematical integers and histograms are reproducible exactly. The second also checks the number of ordinary proper colorings. Each calculation completed with reciprocal edges and a single connected component.

## Relationship to prior work
McDonald, Mohar and Scheide (2010) prove that **all** proper four-edge-colorings of any subcubic graph are Kempe equivalent. Their theorem does not require the intermediate states to be acyclic; it therefore does not imply connectivity of the induced acyclic-only exchange graph. Andersen, Máčajová and Mazák (first online 2011) prove the existence of an acyclic four-edge-coloring for cubic graphs apart from two exceptions. The optimal color count and general existence are not claimed as new. Neither known statement supplies the exact enumerator, degree spectrum or the preservation-constrained reachability classification here. Comparisons included searches for color-relabeling equivalents, stronger coverage and existing enumerations.

## Limitations
The result is an exact finite computation for the Heawood graph, not a theorem for all cubic graphs, nor a diameter or mixing-time calculation. Correctness is backed by two exhaustive programs with finite search spaces, but there has been no independent external audit. Bibliographic coverage is incomplete: full text of some plausible color-theory sources, especially the Andersen–Máčajová–Mazák journal paper and related conference paper, could not be inspected through an accessible route. Equivalent unpublished or unindexed computational data may exist; priority is not independently established.

## References
1. Jessica McDonald, Bojan Mohar, Diego Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs*, arXiv:1005.2248 (public 2010-05-13), https://arxiv.org/abs/1005.2248.
2. Lars Døvling Andersen, Edita Máčajová, Ján Mazák, *Optimal acyclic edge-coloring of cubic graphs*, Journal of Graph Theory 71 (2012), 353–364 (first online 2011-12-06), https://doi.org/10.1002/jgt.20650.
3. Edita Máčajová, Ján Mazák, *An Algorithm for Optimal Acyclic Edge-Colouring of Cubic Graphs*, FAW-AAIM (2011), https://doi.org/10.1007/978-3-642-21204-8_17.
4. Noga Alon, Benny Sudakov, Ayal Zaks, *Acyclic edge-colorings of graphs*, Journal of Graph Theory 37 (2001), 157–167, https://doi.org/10.1002/jgt.1010.
