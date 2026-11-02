# The Heawood hexagon-flip graph is the 24-vertex Klein graph

## Finding

Let \(H\) be the Heawood graph, the incidence graph of the Fano plane. Let \(\mathcal F(H)\) have one vertex for each perfect matching of \(H\), and join two matchings when their symmetric difference is exactly one alternating hexagon. Then \(\mathcal F(H)\) is isomorphic to the seven-regular Klein quartic graph on 24 vertices.

More precisely, \(\mathcal F(H)\) has \(24\) vertices, \(84\) edges, diameter \(3\), and is distance-regular with intersection array
\[
\{7,4,1;1,2,7\}.
\]
Its distance-three relation partitions the 24 matchings into eight triples, each comprising pairwise edge-disjoint perfect matchings. Collapsing these triples gives a complete graph on eight vertices, and each pair of triples is connected by a perfect matching in \(\mathcal F(H)\). Thus \(\mathcal F(H)\) is an antipodal three-cover of \(K_8\).

## Assumptions and scope

The seven points are \(0,\ldots,6\), and the seven lines are \(L_j=\{j,j+1,j+3\}\) with arithmetic modulo \(7\). The bipartite graph \(H\) has an edge from point \(i\) to line \(L_j\) exactly when \(i\in L_j\). These seven triples form the Fano plane: each point occurs on three lines and each pair of points lies on exactly one line.

A perfect matching \(M\) means a set of seven disjoint point-line edges covering all 14 vertices. A hexagon flip replaces the three edges of \(M\) on one alternating simple six-cycle by its three complementary edges. All matchings and flips are unlabelled as states but use the fixed graph labels just specified for computation. Only these six-edge alternating-cycle moves are allowed; longer alternating-cycle exchanges are not edges.

## Proof

**1. Exhaustive encoding.** A matching is uniquely described by a permutation \(p\) of \(\{0,\ldots,6\}\), with point \(i\) matched to \(L_{p(i)}\). It is valid exactly when \(i\in L_{p(i)}\) for every \(i\). Therefore examining the \(7!=5040\) permutations and applying seven explicit membership tests is an exhaustive test of all possible perfect matchings. The resulting 24 distinct permutations appear in `certificate.json` under `matchings`. `verify_fano_permanent.py` reconstructs the list independently of that certificate.

**2. Exact adjacency criterion.** The symmetric difference of two perfect matchings is a vertex-disjoint union of alternating even cycles. The Fano incidence graph has no four-cycle: a four-cycle would put two distinct points on two distinct common lines. Hence each nonempty alternating cycle has at least six edges. If two matchings differ on exactly three matched points, their symmetric difference has exactly six edges and must be a single alternating hexagon. Conversely, a hexagon flip changes the partners of exactly three points. Consequently, for two valid matching permutations \(p,q\), adjacency is equivalent to
\[
\#\{i:p(i)\ne q(i)\}=3.
\]
This is an exact finite decision rule, not a heuristic.

**3. Certified distance structure.** Apply that rule to every unordered pair of the 24 enumerated permutations. It produces 84 edges, with seven incident to each vertex. Run breadth-first search from each of the 24 roots in this explicitly determined adjacency graph. For every root, the respective distance layers have sizes \(1,7,14,2\). For a root \(r\) and vertex \(v\) at distance \(d\), the numbers of neighbors of \(v\) at distances \(d-1,d,d+1\) from \(r\) are the following, independent of the chosen pair:

| \(d\) | Previous layer | Same layer | Next layer |
| --- | ---: | ---: | ---: |
| 0 | 0 | 0 | 7 |
| 1 | 1 | 2 | 4 |
| 2 | 2 | 4 | 1 |
| 3 | 7 | 0 | 0 |

The complete adjacency lists and 24-by-24 distance matrix are given in `certificate.json`; the two standalone programs implement distinct exhaustive reconstructions. The table verifies the distance-regular intersection array \(\{7,4,1;1,2,7\}\). The standard uniqueness classification of distance-regular graphs with this intersection array identifies the graph as the 24-vertex Klein graph [2, pp. 386; 3]. This last identification uses the cited uniqueness result; all enumerated graph invariants above are verified without it.

**4. Antipodal interpretation.** Each root has precisely two vertices at distance three; the certificate checks that these three vertices are pairwise at distance three. Thus distance-three equivalence classes are eight triples. Such triples are edge-disjoint matching triples: a direct check over all 24 matching permutations confirms that every pair at distance three differs in all seven matched point-line edges. Conversely all 24 disjoint matching pairs have distance three. Since each vertex has seven neighbors and the certificate verifies one neighbor in each of the other seven triples, the quotient is \(K_8\) with each edge lifted to a matching of three edges.

For additional resolution, the 276 unordered pairs of matchings split exactly as follows: 84 pairs change three point partners (distance one), 84 change five (distance two), 84 change six (distance two), and 24 change all seven (distance three). Thus the allowed local hexagon moves suffice to transform every matching into every other in at most three steps.

## Verification

Reproduce with a standard Python 3 installation by running `python3 verify_fano_permanent.py certificate.json`. This verifies the full permutation census, the exact adjacency rule, all 24 distance rows, every intersection number, the antipodal triples, the pair distribution, and byte-independent agreement with the embedded JSON certificate.

Independently run `g++ -O2 -std=c++17 verify_fano_cycles.cpp -o verify_fano_cycles && ./verify_fano_cycles`. This code builds a different Fano incidence representation using nonzero vectors of \(\mathbb F_2^3\) and orthogonality, enumerates matchings by recursive backtracking rather than by permutations, explicitly enumerates all 28 six-cycles, flips only alternating hexagons, and recomputes every distance-layer intersection count. Both programs succeeded in complete runs. The proof is an exhaustive finite computation with stated finite bounds, not an empirical extrapolation or a claim about general incidence graphs.

## Relationship to prior work

The counts of 24 perfect matchings of the Heawood graph and the well-known eight factorizations into three perfect matchings are established background, not claimed as new. Dejter [1] constructs the Klein map through 24 Coxeter-graph heptagons and discusses the Heawood-to-Coxeter six-cycle construction. His paper also gives the Klein quartic graph's intersection array but does not formulate the Heawood *perfect-matching hexagon-flip* graph or prove that it realizes the Klein graph. Brouwer, Cohen and Neumaier [2] provide the classification used for the last identification; it does not, by itself, identify a perfect-matching reconfiguration graph. Abreu et al. [4] study properties of two-factors of cubic graphs rather than this local matching-exchange adjacency.

The contribution here is the explicit reconfiguration realization of an exceptional distance-regular graph, with its exact local-move metric and antipodal fibers, rather than a new enumeration of Fano matchings or a new construction of the abstract Klein graph.

## Limitations

The statement concerns the Fano incidence graph only. The proof does not assert a corresponding identification for projective planes of higher order, nor for flips along longer cycles. The Klein identification invokes a published uniqueness theorem; the finite adjacency and distance assertions can be checked without that theorem. An equivalent interpretation may occur in older literature under Hamiltonian-cycle, 1-factorization, Coxeter-graph, or Klein-map terminology, and a comprehensive survey of inaccessible historical materials has not been established. Independent mathematical audit has not been performed.

## References

1. I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960 (first posted 9 February 2010), Journal of Graph Theory **70** (2012), 1–9. https://arxiv.org/html/1002.1960v9
2. A. E. Brouwer, A. M. Cohen, and A. Neumaier, *Distance-Regular Graphs*, Springer, 1989, especially p. 386 (the Klein intersection array and uniqueness). ISBN 978-0-387-50619-7.
3. E. W. Weisstein, *Klein Graphs*, MathWorld, entry for the 24-vertex Klein graph and its intersection array. https://mathworld.wolfram.com/KleinGraphs.html
4. M. Abreu, R. E. L. Aldred, M. Funk, B. Jackson, D. Labbate, and J. Sheehan, *Graphs and digraphs with all 2-factors isomorphic*, Journal of Combinatorial Theory B **92** (2004), 395–404. DOI:10.1016/j.jctb.2004.09.004. See also the 2009 corrigendum for the scope of its statements.
