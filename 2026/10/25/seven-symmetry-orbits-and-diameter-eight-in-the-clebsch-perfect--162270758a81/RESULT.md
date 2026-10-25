# Seven symmetry orbits and diameter eight in the Clebsch perfect-matching flip graph

## Finding
Let \(C\) be the degree-five Clebsch graph, presented on \(\mathbb F_2^4\) by joining \(x\) and \(x+s\) for each \(s\) in \(S=\{1,2,4,8,15\}\), where integers are four-bit vectors and addition is bitwise XOR. Let \(\mathcal F(C)\) have one vertex for every perfect matching of \(C\), with two matchings adjacent when their symmetric difference is one alternating four-cycle.

The graph \(\mathcal F(C)\) has 705 vertices, 2160 edges, and **one connected component**. Its radius is \(7\) and its diameter is \(8\). Exactly five matchings have eccentricity \(7\), namely the five *direction-parallel matchings* \(M_s=\{\{x,x+s\}:x\in\mathbb F_2^4\}\) for \(s\in S\); the other 700 matchings have eccentricity \(8\). Exactly 8840 unordered pairs of matchings are at distance eight.

Under the full automorphism group of the Clebsch graph, the perfect matchings form exactly seven orbits. The table gives each orbit's size, the sorted multiplicities of its nonzero edge directions, its flip degree, and its eccentricity:

| Orbit size | Direction multiplicity pattern | Flip degree | Eccentricity |
| ---: | :---: | ---: | ---: |
| 5 | \((8)\) | 16 | 7 |
| 80 | \((6,2)\) | 10 | 8 |
| 60 | \((4,4)\) | 8 | 8 |
| 120 | \((4,2,2)\) | 6 | 8 |
| 240 | \((4,2,2)\) | 6 | 8 |
| 160 | \((2,2,2,2)\) | 4 | 8 |
| 40 | \((2,2,2,2)\) | 4 | 8 |

In particular, the flip-degree distribution is \(200\) at degree \(4\), \(360\) at degree \(6\), \(60\) at degree \(8\), \(80\) at degree \(10\), and \(5\) at degree \(16\).

The matching count of 705 is **previously known** from the complete matching polynomial of the Clebsch graph. The original result asserted here is the exact four-cycle-flip geometry, its radius and diameter, its five distinguished centers, and its seven full-automorphism orbits.

## Assumptions and scope
The integer encoding \(\mathbb F_2^4\cong\{0,\ldots,15\}\) uses four binary coordinates, with addition given by XOR. The generator set \(S\) is exactly \(\{1,2,4,8,15\}\). A perfect matching consists of eight *unordered* disjoint edges covering all 16 vertices. A flip removes two matching edges on an alternating four-cycle and inserts the two other cycle edges. Longer alternating cycles are not allowed as a single move. Matchings are not identified modulo graph automorphisms when constructing \(\mathcal F(C)\).

For a direction \(s\in S\), its multiplicity in a matching is the number of matching edges \(\{x,x+s\}\). The direction multiplicity pattern is the nonincreasing sequence of the positive multiplicities, disregarding the labels of the five generators. The seven orbits are under **all** automorphisms of \(C\), not under graph automorphisms of the flip graph.

## Proof
**Graph and moves.** The five generators satisfy the sole nonzero linear dependence that their XOR is zero. Any four of them form a basis of \(\mathbb F_2^4\). Hence \(C\) has 16 vertices and 40 edges; each vertex has five neighbors, adjacent vertices have no common neighbor, and nonadjacent vertices have two common neighbors. This gives strongly regular parameters \((16,5,0,2)\) and identifies the intended five-regular Clebsch graph.

Every four-cycle in this Cayley graph uses two distinct generators twice each. Indeed, XORing its four successive edge differences gives zero, and the only relation among distinct generators has length five. Because the graph is triangle-free, these alternating squares have no diagonals. Every permitted flip therefore replaces two edges of one direction by two edges of another. Conversely, for any perfect matching, a pair of its selected edges and either of the two cross-pairings gives a permitted flip exactly when both proposed cross edges belong to the 40-edge graph.

**Complete matching enumeration.** For a subset \(U\subseteq\mathbb F_2^4\) of uncovered vertices, define \(f(\varnothing)=1\). If \(u\) is the least vertex in nonempty \(U\), set
\[
f(U)=\sum_{v\in N(u)\cap U} f(U\setminus\{u,v\}).
\]
This is an exact recurrence: every perfect matching on \(U\) contains a unique edge incident to \(u\), and the summands partition all such matchings without repetition. Exact evaluation gives \(f(\mathbb F_2^4)=705\). The accompanying `verify.py` also constructs all 705 matchings themselves with the same exhaustive branch invariant, whereas `verify_alt.cpp` independently enumerates them with 16-bit uncovered-vertex masks and 40-bit matching-edge masks.

**The full flip adjacency.** Each matching has eight edges, so the explicit construction checks all \(\binom{8}{2}\) pairs of selected edges and both cross-pairings, rejecting pairings that are not edges of \(C\). This produces the complete undirected flip graph. A separate verification checks all \(\binom{705}{2}\) unordered matching pairs using the criterion \(|M\triangle M'|=4\), equivalent for perfect matchings to one alternating four-cycle. Both constructions agree edge for edge. They give 2160 flip edges and the stated degree distribution.

**Distances.** From each of the 705 vertices, breadth-first search visits all 705 states; these are exhaustive shortest-path calculations, not partial sampling. The unordered-pair distance histogram is
\[
\begin{array}{c|rrrrrrrr}
\text{distance}&1&2&3&4&5&6&7&8\\\hline
\text{pairs}&2160&8040&22360&45160&64800&61920&34880&8840.
\end{array}
\]
The counts sum to \(\binom{705}{2}=248160\). Exactly five breadth-first searches have maximum distance seven, and 700 have maximum distance eight. An explicit comparison of these five centers with the five direction-parallel matchings gives equality, proving the radius, diameter, and center characterization. The complete graph of 705 matchings is connected because every search visits all states.

**Full automorphism orbits.** Translation by any vector is an automorphism. Any permutation of the five generator directions extends uniquely to an invertible linear map of \(\mathbb F_2^4\), because every four directions form a basis and their five-term sum is zero. Thus the 16 translations and 120 such linear maps yield \(16\cdot120=1920\) distinct automorphisms. Conversely, an automorphism fixing zero can permute its five neighbors in at most 120 ways; every remaining nonzero vertex is the unique common neighbor, other than zero, of a particular pair of these neighbors. Thus fixing those five neighbors fixes every vertex, giving an upper bound of 1920 automorphisms. The constructed group is therefore the full automorphism group.

For each not-yet-assigned matching in lexicographic order, the verifier applies all 1920 explicit automorphisms, forms its entire orbit, and removes that orbit before proceeding. The seven disjoint orbit sizes are \(5,80,60,120,240,160,40\), summing to 705. Each orbit's degree, eccentricity, and direction multiplicities are computed directly from one representative and cross-checked against all matchings. These give the complete table above and exclude any omitted symmetry type.

For additional structure, XORing the eight selected edge differences of any perfect matching gives zero (every graph vertex occurs exactly once). Since the only nontrivial linear relation among the five generators involves all five, their five multiplicities have the same parity. Their sum is eight, so all are even. This forces exactly the five direction patterns appearing in the table, although the two patterns \((4,2,2)\) and \((2,2,2,2)\) split into two distinct symmetry orbits each.

The finite algorithms thus constitute an exhaustive proof of every stated count and metric; no assertion about arbitrary folded cubes is inferred from these calculations.

## Verification
Run `python3 verify.py` (Python 3.8 or later). It verifies the strongly regular graph parameters, exhaustively constructs 705 matchings, independently checks their count by memoized vertex-subset recurrence, constructs the flips by cross-pairings, independently checks adjacency by all-pairs symmetric differences, performs breadth-first search from every state, and computes every orbit under all 1920 automorphisms. It terminates with `ALL_VERIFY_OK`.

Independently compile and run `verify_alt.cpp` using `c++ -std=c++17 -O2 -Wall -Wextra verify_alt.cpp -o verify_alt` and `./verify_alt`. This verifier independently enumerates the matchings, builds adjacency solely from 40-bit symmetric-difference masks, and recomputes the degree spectrum and all-pairs distance histogram. Both verifiers were run from the complete, locally checked versions of the packaged source.

## Relationship to prior work
Alon and Friedland give a general perfect-matching bound in terms of graph degrees; their theorem does not determine individual perfect matchings or their transition geometry. The 16-vertex Clebsch graph and its five-dimensional folded-cube description are classical.

The published *Mod-\(2\) homology of the Clebsch matching complex* supplies the complete matching-number sequence, with 705 perfect matchings. The published *Complete prescribed-difference matching multiplicity spectrum in dimension four* goes further, supplying exact numbers of matchings for prescribed XOR-difference profiles. The scalar count and profile multiplicity facts are treated here as prior knowledge; neither theorem determines flip adjacency, shortest-path distances, orbit splits, or the five geodesic centers.

Dyer and Müller study perfect-matching switch chains and characterize hereditary graph classes with connected switch dynamics. Bonamy and collaborators study four-cycle-flip reconfiguration and complexity across several graph classes. The present exact 705-state geometry is not a corollary of their general results: for example, the usual odd-chordal diameter bound is \(|V(C)|/2-1=7\), whereas the computed diameter here is eight. The later work of Brenner and collaborators addresses complete graphs, complete bipartite graphs, and geometric matching settings, not this sparse strongly regular graph. The recent decorated-graph flip theorem of Bošković treats another graph construction and also does not supply these exact invariants.

Searches included the graph aliases *Clebsch*, *Greenwood–Gleason*, *folded five-cube*, and *projective cube*, and the move aliases *four-cycle flip*, *switch*, and *two-edge exchange*. Direct comparison of accessible published claims found no theorem implying the seven orbits, the exact distances, or the center classification.

## Limitations
The result is a finite exact classification of one canonical graph. It is proved by transparent exhaustive recurrences, finite automorphism action, and full shortest-path searches rather than by a uniform closed-form theory of higher-dimensional folded cubes. It does not establish a mixing-time bound or Hamiltonicity of the 705-state flip graph. The previously published count of 705 is not new. Equivalent calculations in unindexed sources may exist, and no independent audit of this finding is asserted.

## References
1. N. Alon and S. Friedland, *The maximum number of perfect matchings in graphs with a given degree sequence*, arXiv:0803.2578v1, first posted 2008-03-18; Electronic Journal of Combinatorics 15 (2008), N13; MSC 05C70 among stated classifications.
2. M. Dyer and H. Müller, *Counting perfect matchings and the switch chain*, arXiv:1705.05790, first posted 2017-05-16.
3. M. Bonamy, N. Bousquet, M. Heinrich, T. Ito, Y. Kobayashi, A. Mary, M. Mühlenthaler and K. Wasa, *The Perfect Matching Reconfiguration Problem*, arXiv:1904.06184, first posted 2019-04-12.
4. S. Brenner, J. Dallant, L. Kleist, R. Lauff and T. Mütze, *Hamilton paths and cycles in flip graphs of (almost-)perfect matchings*, arXiv:2607.04687, 2026.
5. V. Bošković, *Flip dynamics on perfect matchings beyond bipartite and planar graphs*, arXiv:2607.16101, 2026.
6. *Mod-\(2\) homology of the Clebsch matching complex*, publicly accessible mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mod-2-homology-of-the-clebsch-matching-complex--7e53e4d18ed4.
7. *Complete prescribed-difference matching multiplicity spectrum in dimension four*, publicly accessible mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-complete-prescribed-difference-matching-multiplicity-spectrum-in--d86ded899098.
8. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html.
