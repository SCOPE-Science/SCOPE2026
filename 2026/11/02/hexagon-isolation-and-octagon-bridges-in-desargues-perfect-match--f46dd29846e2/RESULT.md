# Hexagon isolation and octagon bridges in Desargues perfect-matchings

## Finding

Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with vertex set the ten two-element subsets of \(\{0,1,2,3,4\}\) and edges between disjoint subsets. Let \(D\) be its bipartite double cover: \(V(D)=V(P)\times\{0,1\}\), with \((u,0)\) adjacent to \((v,1)\) exactly when \(uv\in E(P)\). This is the twenty-vertex Desargues graph, also denoted \(GP(10,3)\).

For an even integer \(L\), let \(F_{\leq L}(D)\) have as vertices all perfect matchings of \(D\). Two matchings are adjacent exactly when their symmetric difference is one simple alternating cycle of length at most \(L\). Write \(F_6\) for flips of length six only and \(F_8^{\mathrm{exact}}\) for flips of length eight only.

**Theorem.** There are exactly \(60\) perfect matchings of \(D\). Identifying a perfect matching with its Petersen-supported permutation on ten vertices, the cycle-type multiplicities are
\[
(2,2,2,2,2):6,\qquad(5,5):24,\qquad(8,2):30.
\]
These are precisely the three orbits under the natural \(S_5\)-action.

The hexagon graph \(F_6\) has \(120\) edges and seven connected components: one of size \(54\), containing all \(24\) configurations of type \((5,5)\) and all \(30\) of type \((8,2)\), and six isolated configurations of type \((2,2,2,2,2)\). The nontrivial component is bipartite with respective degrees \(5\) and \(4\).

The octagon-only graph \(F_8^{\mathrm{exact}}\) has \(60\) edges. It joins the six involutive configurations, each of degree \(10\), to the \(30\) configurations of type \((8,2)\), each of degree \(2\); the \(24\) configurations of type \((5,5)\) are isolated. Every pair of involutive configurations has exactly two common octagon neighbours. Equivalently, the nonisolated octagon-only subgraph is the subdivision of the complete graph \(K_6\) in which every edge is replaced by two internally disjoint paths of length two.

The graph \(F_{\leq8}(D)\), allowing hexagon and octagon flips, is connected and bipartite, with \(60\) vertices and \(180\) edges. Every vertex has eccentricity four, so
\[
\operatorname{rad}(F_{\leq8}(D))=\operatorname{diam}(F_{\leq8}(D))=4.
\]
The complete distance profiles at distances \(0,1,2,3,4\), by the three permutation types in the order above, are
\[
(1,10,25,20,4),\qquad(1,5,15,25,14),\qquad(1,6,21,24,8).
\]
The unordered-pair distance enumerator at positive distances is \((180,570,720,300)\). Consequently, eight is the least even cutoff for connected bounded-cycle reconfiguration.

## Assumptions and scope

All graphs are finite, simple and labelled by the explicit vertex sets above. Perfect matchings are unordered sets of edges, not oriented cycle covers. A legal flip means that the *whole* symmetric difference, and not just one component of it, is one simple alternating cycle. The connectedness threshold is among even cycle lengths in this fixed graph, not a universal assertion for arbitrary graphs or embeddings. The \(S_5\)-action permutes the five underlying labels simultaneously in both bipartite layers.

## Proof

**1. Exhaustive structural classification.** A perfect matching of \(D\) is a bijection \(\pi:V(P)\to V(P)\) with \(u\pi(u)\in E(P)\) for all ten vertices. Each cycle of \(\pi\) is a directed cycle in the undirected Petersen graph, except that a two-cycle traverses one edge both ways. The Petersen graph has no triangles or squares, has twelve pentagons, ten hexagons, fifteen octagons, no Hamilton cycle, and six perfect matchings. The complement of a six-cycle induces \(K_{1,3}\), so it cannot support the two transpositions that a \((6,2,2)\) cycle type would require. No other cycle-length partition of ten is feasible. The six Petersen perfect matchings give the six all-transposition permutations. The twelve pentagons occur as six complementary pairs, and independently choosing orientations on the pair gives \(6\cdot4=24\) configurations of type \((5,5)\). Every Petersen edge is the complement of exactly one octagon; independently orienting it gives \(15\cdot2=30\) configurations of type \((8,2)\). The count is \(6+24+30=60\).

The graph \(P\) is the disjointness graph on two-subsets of a five-element set. Every relabelling of those five elements acts on the configurations. A complete check of all \(120\) permutations shows that each of the three cycle-type classes is one orbit. This is independently checkable in the attached first program.

**2. Exact flip criterion.** For two supported permutations \(\pi,\rho\), their common matching edges correspond to fixed points of \(\pi^{-1}\rho\). Each nontrivial cycle of length \(k\) in this relative permutation corresponds to one alternating cycle of length \(2k\) in the symmetric difference. Thus the matching flip is legal at length six or eight precisely when \(\pi^{-1}\rho\) has one nontrivial cycle of length three or four, respectively, with every other point fixed. This also shows that hexagon flips preserve permutation sign and octagon flips reverse it. The all-transposition class has odd sign and the other two classes have even sign.

**3. The octagon incidence geometry.** Every pair of the six Petersen one-factors shares exactly one edge; every one of the fifteen Petersen edges belongs to exactly two one-factors. The complementary eight vertices induce one octagon. Its two orientations give two \((8,2)\) configurations, each having precisely the two corresponding involutive configurations as octagon-flip neighbours. No other octagon flips occur. Hence every pair of the six involutive states has two common octagon neighbours, giving the doubled-edge incidence subdivision of \(K_6\).

**4. Complete finite metric.** To verify the remaining connectivity and distance assertions exactly, enumerate supported permutations recursively by assigning an unused neighbour to each successive Petersen vertex; this examines the entire finite choice space, not a sample. For every unordered pair, apply the criterion in step 2, form both flip graphs, and run breadth-first search from *every* one of their \(60\) vertices. The first included checker performs precisely this labelled enumeration and verifies all asserted figures. The second checker independently constructs \(GP(10,3)\) from its \(30\) edges, recursively enumerates all perfect matchings as edge masks, and declares a flip only when the symmetric-difference subgraph is connected and two-regular. It verifies an explicit isomorphism to the Petersen double cover before comparing orbit classes. A direct Ryser inclusion–exclusion calculation of the ten-by-ten biadjacency permanent independently gives \(60\). The independently computed component sizes, degrees, incidence multiplicities and all \(\binom{60}{2}=1770\) pairwise distances agree. Because the graph has girth six, hexagons are the only allowed cycles for any cutoff strictly below eight; their disconnected graph and the connected octagon-augmented graph prove sharpness.

## Verification

Two standalone Python 3 standard-library programs are included: `verify_petersen_permutations.py` and `verify_generalized_petersen.py`. Each must terminate without assertion failure and print four named `PASS` markers. They compute the entire finite search space by different graph representations and different flip tests, independently check all \(60\) source distances and confirm the stated degree and orbit profiles. No random trials, numerical tolerances, cached data, external dependencies or unproved extrapolation are used. The checker code also verifies Petersen cycle counts and the double-cover isomorphism.

## Relationship to prior work

Classical Petersen graph and Desargues graph structure, including the six Petersen one-factors and the generalized Petersen representation, are background rather than new assertions. Csikvári's 2014 work on matchings in vertex-transitive bipartite graphs establishes general enumerative bounds, not the small-cycle exchange metric studied here. The resonance-graph theory of Tratnik and Ye (2017) restricts flips to selected *facial* cycles of an embedding; the present graph permits all simple alternating cycles of the specified lengths, whether facial or not. Ito and coauthors (2019) study unrestricted single-alternating-cycle matching reconfiguration in general graphs; their complexity results do not directly yield the exact Desargues graph metric. A later matching-polynomial study of the Desargues–Levi graph considers numerical matching counts, not the local six/eight-cycle reconfiguration structure. The specific flip graph and doubled-\(K_6\) incidence description were not located in the reviewed sources; this is evidence of a research gap, not proof of priority.

## Limitations

The theorem pertains to the explicit Desargues graph and the specified flip rule only. Generalizations to other generalized Petersen graphs or longer cycles are unproved. Historical novelty cannot be guaranteed: differently named resonance, dimers or one-factor exchange results might cover the same configuration space. A 2025 matching-polynomial article reports a perfect-matching count of \(120\) for a graph it calls the Desargues–Levi graph, while both explicit models and the structural count in this work give \(60\); the discrepancy in the published table was not resolved from the accessible material. It does not affect the internally exhaustive classification for the explicitly defined \(D\), but merits independent external reconciliation. No independent scholarly review has been performed.

## References

1. Péter Csikvári, *Matchings in vertex-transitive bipartite graphs* (first public version 2014-07-21), arXiv:1407.5409, https://arxiv.org/abs/1407.5409. Primary MSC2020 05C35.
2. Niko Tratnik and Dong Ye, *Resonance Graphs and Perfect Matchings of Graphs on Surfaces* (2017), arXiv:1710.00761, https://arxiv.org/abs/1710.00761.
3. Takehiro Ito, Naonori Kakimura, Naoyuki Kamiyama, Yusuke Kobayashi and Yoshio Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles* (2019), arXiv:1907.01700, https://arxiv.org/abs/1907.01700.
4. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry 17 (2025), article 133, https://www.mdpi.com/2073-8994/17/1/133 (matching count discrepancy noted above).
5. Wolfram MathWorld, *Desargues Graph*, https://mathworld.wolfram.com/DesarguesGraph.html (graph identification).
