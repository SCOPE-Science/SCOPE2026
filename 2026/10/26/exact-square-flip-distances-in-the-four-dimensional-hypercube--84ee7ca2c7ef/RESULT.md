# Exact square-flip distances in the four-dimensional hypercube

## Finding
Let \(Q_4\) have vertex set \(\{0,1\}^4\), with edges joining pairs of Hamming distance one. Let \(\mathcal F(Q_4)\) be the graph of its perfect matchings, where an edge represents a *square flip*: for some four-cycle, the matching contains one opposite edge pair, which is replaced by the other opposite edge pair.

**Theorem (exact geodesic profile).** The unique non-singleton connected component \(\mathcal C\) of \(\mathcal F(Q_4)\) has \(264\) vertices and
\[\operatorname{rad}(\mathcal C)=7,\qquad\operatorname{diam}(\mathcal C)=8.\]
For unordered *distinct* pairs \(\{M,N\}\subset\mathcal C\), the numbers at respective distances \(1,2,3,4,5,6,7,8\) are
\[(768,2640,6032,9360,9504,5296,1104,12).\]
The \(264\) eccentricities are \(252\) copies of \(7\) and \(12\) copies of \(8\). The graph whose edges are the twelve pairs at distance \(8\) is the disjoint union of three four-cycles, with all other vertices isolated. The maximum eccentricity is attained on one orbit of size \(12\) under \(\operatorname{Aut}(Q_4)\); that orbit has flip degree \(4\).

The previously known perfect-matching count \(272\), nine connected components, and eight frozen matchings are **not** part of the novelty claim; they are included to define the component and check the calculation.

## Assumptions and scope
All graphs are finite, simple and undirected. Interpret a binary vector as an integer from \(0\) to \(15\); the edges of \(Q_4\) are pairs \(\{v,v\oplus2^j\}\) for the four coordinates \(j=0,1,2,3\). A perfect matching comprises eight disjoint such edges and covers all sixteen vertices. Only elementary four-cycle/square flips are permitted. Distances between different connected components are undefined; the diameter and radius above concern only \(\mathcal C\), not the disconnected whole graph. Every four-cycle of \(Q_4\) is a coordinate square, so there are exactly \(\binom42\,2^2=24\) squares.

## Proof
**Exhaustive state enumeration.** Enumerate a matching by choosing the least uncovered vertex \(v\), pairing it with each currently uncovered neighbor, then recursing until no vertices remain. Each perfect matching occurs exactly once: its partner of \(v\) is unique and appears among the four possible neighbors. This yields \(272\) matchings. Independently, partition vertices by Hamming-weight parity and assign the eight even vertices, in increasing order, to distinct adjacent odd vertices; the second recursion yields the identical set of \(272\) edge masks.

**Exact adjacency.** Enumerate all six unordered pairs of coordinate directions and each of the four choices of the other two coordinates. For every matching and every resulting square, exchange the two opposite edges when present. This constructs the complete square-flip adjacency relation. Independently, compare each unordered pair of distinct matching masks: there is one flip precisely when their symmetric difference has four edges, since two perfect matchings on four affected vertices must form an alternating simple four-cycle. The two independently built neighbor arrays agree entry by entry.

**Complete distance certificate.** Traverse all connected components of this finite adjacency graph. There are eight singletons and exactly one component of size \(264\). Run an ordinary breadth-first search from every one of its \(264\) states. For each source, BFS gives the exact minimum number of flips to every other vertex: the BFS-layer induction provides both a path using that many flips and the impossibility of a shorter path. Count only pairs whose source index is smaller than the target index. The resulting distance tally is the eight-entry vector stated above, with sum \(\binom{264}{2}=34716\). The largest observed distance is \(8\), and the eccentricity tally is \(\{7:252,8:12\}\), so the radius and diameter follow.

**Antipodal structure and symmetries.** Record the pairs at BFS distance \(8\). They consist of \(12\) edges; the \(12\) incident vertices each have degree \(2\) in this distance-eight graph, and its three connected components each have four vertices. Consequently it is three disjoint four-cycles. Independently, enumerate all \(2^4\cdot4!=384\) affine cube isometries (coordinate permutations followed by binary translations), check they preserve flip neighbors, and compute the induced matching orbits. Their triples (orbit size, flip degree, eccentricity) are
\[(4,12,7),\ (48,8,7),\ (24,8,7),\ (48,6,7),\ (96,5,7),\ (12,4,8),\ (32,3,7),\ (8,0,0),\]
where eccentricity \(0\) is only a convention for frozen singleton components. Thus the twelve eccentricity-eight matchings form one natural automorphism orbit. Every assertion is a finite identity checked by the transparent algorithms above, implemented in the included `verify.py`.

## Verification
Execute `python3 verify.py` with Python 3.9 or later. The script uses only the standard library, reconstructs all graph states and transitions from first principles, and terminates with `VERIFY_OK` if every asserted equality holds. It also prints a concrete pair of perfect matchings at flip distance \(8\). The two separate enumerators and the two independent adjacency descriptions make the main finite calculation cross-checkable. All-pairs BFS exhaustively proves the shortest-move distances, not merely experimental lower bounds. The complete reconstructed component is independently invariant under all \(384\) cube automorphisms.

## Relationship to prior work
Fink (2009) studied a different matching graph on hypercubes, with transitions defined via alternating Hamiltonian cycles; his connectivity results do not supply square-flip distances. Klivans and Saldanha (2022, Example 2.2) explicitly counted the \(272\) perfect matchings, nine square-flip components, the \(264\)-element component, and the eight frozen matchings for the four-dimensional domino box. Those quantities are credited as prior results. Their full text does not report the present all-pairs distance distribution, eccentricity classes or antipodal four-cycle decomposition. Hartarsky, Lichev and Toninelli (2023, Theorem 6) bounded the diameter when longer alternating cycles are allowed; their larger move set makes their bound inapplicable as an exact square-flip diameter. The present theorem supplies the sharp metric refinement for the already known non-frozen component.

## Limitations
The theorem is a complete finite case, not a uniform result for arbitrary dimension. Its novelty assessment is based on accessible primary texts and targeted searches; unpublished code, overlooked older tables, or unindexed literature could contain the same distance profile. There has been no independent external validation. The eight isolated matchings are intentionally excluded from all finite-distance statistics.

## References
1. J. Fink, *Connectivity of Matching Graph of Hypercube*, SIAM Journal on Discrete Mathematics (2009), DOI: 10.1137/070697288. The graph's edge relation is different here.
2. C. J. Klivans and N. C. Saldanha, *Domino tilings and flips in dimensions 4 and higher*, Algebraic Combinatorics 5 (2022), 163–185, DOI: 10.5802/alco.205, especially Example 2.2.
3. I. Hartarsky, L. Lichev and F. L. Toninelli, *Local dimer dynamics in higher dimensions*, arXiv:2304.10930 (2023), especially Theorem 6.
