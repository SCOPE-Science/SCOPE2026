# The shortest-cycle perfect-matching flip graph of the Tutte–Coxeter cage

## Finding

Let \(T\) be the 30-vertex Tutte–Coxeter graph, the incidence graph of the 15 duads and 15 synthemes on six symbols. Let \(\mathcal F_8(T)\) have one vertex per perfect matching of \(T\); join two matchings when their symmetric difference is **one eight-edge alternating cycle**. Then \(\mathcal F_8(T)\) is connected, bipartite, and 10-regular, with 288 vertices, 1,440 edges, radius five, and diameter six. It has 4,320 four-cycles. The eight-edge bound is sharp for connectivity: permitting only shorter even alternating cycles produces no edges.

The bipartition consists of 144 even and 144 odd incidence-preserving bijections between the ordered duads and synthemes. The natural \(S_6\)-action has exactly these two orbits, but the reconfiguration graph is **not vertex-transitive**: the even class has eccentricity six, whereas the odd class has eccentricity five. Its exact distance-sphere vectors (including the origin) are, respectively,

\[
(1,10,45,97,96,37,2),\qquad (1,10,42,97,101,37).
\]

The original graph has exactly 90 eight-cycles. Every such cycle alternates in 32 of its 288 perfect matchings; every matching permits exactly ten eight-cycle flips.

## Assumptions and scope

The underlying graph \(T\) is simple, undirected, and labelled by the duad–syntheme incidence construction. A *duad* is an unordered two-element subset of \(\{0,1,2,3,4,5\}\). A *syntheme* is a partition of the six symbols into three duads. A duad is incident with a syntheme precisely when it belongs to that partition. A perfect matching means a 15-edge set meeting every vertex exactly once. A flip replaces the four matching edges on one simple alternating eight-cycle by the other four edges. There is no restriction to planar faces, and longer alternating cycles are **not** allowed in \(\mathcal F_8(T)\).

To define matching parity, order the 15 duads lexicographically; order the 15 synthemes by the recursive lexicographic enumeration supplied by `verify_duads.py`. A perfect matching is an incidence-preserving bijection from the ordered duads to the ordered synthemes, represented by a permutation \(\pi\in S_{15}\). Even and odd refer to the sign of \(\pi\). Parity names depend on the chosen orders; the intrinsic metric distinction does not.

## Proof

**Exact finite enumeration lemma.** Both of the following fully specified procedures terminate and cover the entire finite state space; complete executable implementations occur in the files named below.

First, construct the list of 15 duads by the combinations of six symbols, and the list of 15 synthemes by recursively pairing the least remaining symbol with each larger remaining symbol. For each duad \(i\), compute the three synthemes containing it. Recursively assign to duad \(i\) one of its three allowed synthemes not already used. Every leaf at depth 15 is a perfect matching, and every perfect matching has exactly one root-to-leaf encoding, since its 15 edges prescribe all 15 assignments. The program asserts that the exhaustive set has 288 distinct members.

**Adjacency lemma.** Any two perfect matchings of a bipartite graph have symmetric difference a disjoint union of alternating cycles. The duad–syntheme graph has no four-cycle: distinct synthemes share at most one duad. Thus two perfect matchings differ on exactly four duads if and only if their symmetric difference is one alternating eight-cycle; two disjoint four-cycles cannot occur. The first program tests this criterion on each of the \(\binom{288}{2}\) pairs and obtains 1,440 edges, exactly ten at each vertex.

**Bipartition and natural orbits.** Changing four assignments along an alternating eight-cycle applies a four-cycle to the syntheme permutation; a four-cycle has odd sign. Therefore every flip reverses parity. The exhaustive census contains 144 states of each sign. Relabelling the six symbols induces five adjacent-transposition generators of an \(S_6\)-action on the matching states. Closure under these generators gives precisely two orbits of size 144, which coincide with the two parity classes. The graph is bipartite, with no triangles.

**Metric and four-cycle lemma.** Breadth-first search from every one of the 288 states traverses the complete 288-vertex graph and produces exactly the two distance-sphere vectors displayed in the Finding section, with 144 origins of each type. The first vector has maximum distance six; the second has maximum distance five. This proves connectivity, diameter six, radius five, and the eccentricity disparity, hence failure of vertex-transitivity. Every quadrilateral corresponds to a pair of opposite vertices and a two-element subset of their common neighbors. Summing \(\binom{|N(u)\cap N(v)|}{2}\) over all unordered vertex pairs and dividing by two counts 4,320 quadrilaterals exactly once.

**Independent incidence and cycle check.** Independently construct the 15 nonzero vectors of \(\mathbb F_2^4\). Regard the 15 totally isotropic two-dimensional vector subspaces under the nondegenerate alternating form \(\langle x,y\rangle=x_0y_1+x_1y_0+x_2y_3+x_3y_2\pmod2\) as lines, with incidence given by containment of the three nonzero vectors. The resulting 30-vertex incidence graph is the classical generalized quadrangle \(W(2)\), isomorphic to the Cremona–Richmond configuration and hence to \(T\). The second program enumerates all 30-vertex perfect matchings by recursively pairing the least uncovered vertex with a neighbor. It independently enumerates every simple cycle of lengths four, six and eight, obtaining counts zero, zero and 90. For each perfect matching and eight-cycle, checking whether exactly four cycle edges are in the matching is equivalent to checking alternation; symmetric difference with the cycle then yields the unique neighboring matching. This independent construction again obtains 288 matchings, ten flips per matching, both distance-sphere vectors, connectedness, radius five, diameter six and 4,320 quadrilaterals. Each of the 90 eight-cycles is alternating in 32 matchings.

**Sharpness.** Because the underlying Tutte–Coxeter graph has girth eight, every alternating cycle has at least eight edges. Consequently, before length eight no perfect matching has a permitted move. At length eight the graph is connected by the exact BFS above, so eight is the first possible connectivity threshold.

Every computational assertion is finite and exhaustive: the two different recursive encodings each visit every perfect matching, the adjacency test considers all possible neighbors, and the BFS visits every state from every origin. No random experiments or numerical approximations enter the proof.

## Verification

Run `python3 verify_duads.py` and `python3 verify_symplectic.py` using Python 3 and only the standard library. Both terminate with explicit success markers. The first verifies duad/syntheme bijection enumeration, parity, the induced \(S_6\)-orbits, all flip edges and all eccentricities. The second independently constructs the symplectic incidence graph, enumerates all perfect matchings and short cycles, and calculates the same exchange geometry. `certificate.json` contains the complete 288-state duad encoding and the full flip adjacency list for independent inspection; the two verifiers do not depend on this certificate.

## Relationship to prior work

The Tutte–Coxeter graph, the Cremona–Richmond configuration, and its duad/syntheme and generalized-quadrangle descriptions are classical. The 2014 preprint by M. Prażmowska and K. Prażmowski develops generalized Cremona–Richmond incidence structures and their automorphisms; it does not discuss perfect-matching flip geometry. The 2015 explanatory article by J. Baez gives the duad/syntheme description and girth-eight property. The exact count of 288 perfect matchings is already reported in K. Balasubramanian's 2025 matching-polynomial paper and **is not itself claimed as new**.

Ito, Kakimura, Kamiyama, Kobayashi and Okamoto (2019) study perfect-matching reconfiguration by unrestricted alternating-cycle flips, corresponding to edges of the perfect-matching polytope. Their general reachability observation does not establish reachability with only shortest eight-cycles, or the metric, orbit, and incidence counts computed here. The proposed contribution is this specific shortest-cycle restricted reconfiguration classification, not the general alternating-cycle model. Searches did not identify a covering theorem, but absence from indexed searches does not prove novelty.

## Limitations

This is an exact result for the single, naturally distinguished 30-vertex cage, not an assertion for every generalized quadrangle or cubic girth-eight graph. It is supported by exhaustive integer/combinatorial algorithms rather than a short closed-form hand derivation of the metrics. The published perfect-matching count and base-graph properties are prior facts. A mathematically equivalent formulation under older one-factorization, resonance, or generalized-quadrangle terminology remains a literature risk. The 2025 matching-polynomial article was accessible for its reported count and description through indexed text, but direct retrieval of its full publisher text was blocked; no whole-document exclusion is claimed from that restricted access.

## References

1. M. Prażmowska and K. Prażmowski, *The Cremona-Richmond Configuration revisited and generalized*, arXiv:1404.7166, first submitted 2014-04-28. https://arxiv.org/abs/1404.7166
2. J. Baez, *Tutte–Coxeter Graph*, Visual Insight, American Mathematical Society, 2015-08-15. https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/
3. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi and Y. Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, arXiv:1907.01700, first submitted 2019-07-03. https://arxiv.org/abs/1907.01700
4. K. Balasubramanian, *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry 17 (2025), article 133. https://doi.org/10.3390/sym17010133
5. H. Zhang and S. Liu, *2-resonance of plane bipartite graphs and its applications to boron–nitrogen fullerenes*, Discrete Applied Mathematics 158 (2010), 1559–1569. https://doi.org/10.1016/j.dam.2010.05.012
