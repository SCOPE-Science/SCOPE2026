# The 240-pair six-cycle geodesic defect in the Clebsch zero-forcing exchange graph

## Finding

Let \(C\) be the five-regular Clebsch graph on the sixteen vertices \(V=\{0,1,\ldots,15\}\), with \(u\sim v\) exactly when the bitwise XOR \(u\oplus v\) lies in \(\{1,2,4,8,15\}\). Let \(\mathcal Z(C)\) have the minimum ordinary zero-forcing sets as vertices; two such sets are adjacent when exactly one chosen vertex is exchanged for one unchosen vertex.

The known zero-forcing number is \(Z(C)=10\), and the previously determined minimum-set census has \(3{,}872\) configurations and seven symmetry types. **The minimum size, total count, and orbit classification are prior results used as context, not new contributions.** For context, the six-vertex white complement \(W=V\setminus B\) of a minimum set \(B\) induces *exactly one* of these seven graphs, and every six-subset inducing one of them is the complement of a minimum set:

| Induced graph on \(W\) | Number of sets | Degree in \(\mathcal Z(C)\) |
| --- | ---: | ---: |
| A four-cycle with two leaves on the same cycle vertex | 480 | 37 |
| A four-cycle with leaves on adjacent cycle vertices | 960 | 34 |
| \(\Theta_{2,2,3}\), three internally disjoint terminal paths of lengths \(2,2,3\) | 480 | 34 |
| \(K_{1,4}\) with one edge subdivided | 320 | 37 |
| \(K_{1,3}\) with one edge subdivided, plus an isolated vertex | 960 | 32 |
| \(C_5\sqcup K_1\) | 192 | 30 |
| \(P_4\sqcup 2K_1\) | 480 | 30 |

These seven types are also precisely the seven orbits under the natural order-\(1{,}920\) folded-cube automorphism group. The exchange graph is connected, has \(64{,}720\) edges, and is self-centered:
\[
\operatorname{rad}(\mathcal Z(C))=\operatorname{diam}(\mathcal Z(C))=6.
\]
The numbers of unordered pairs at exchange distances \(1,2,3,4,5,6\), respectively, are
\[
(64{,}720,625{,}440,2{,}214{,}640,2{,}986{,}160,1{,}412{,}976,190{,}320).
\]

For every pair of distinct minimum sets \(A,B\), the shortest-path distance satisfies
\[
d_{\mathcal Z(C)}(A,B)\in\{|A\setminus B|,\ |A\setminus B|+1\}.
\]
Precisely \(240\) unordered pairs require the additional move. Every one has \(|A\setminus B|=2\) and distance \(3\). These exceptional pairs form a perfect matching on the \(480\) configurations whose white complements induce \(P_4\sqcup2K_1\), and no other configuration belongs to such a pair.

There is an intrinsic geometric characterization of all \(240\) exceptions. Exactly \(80\) eight-vertex subsets of \(C\) induce \(C_6\sqcup2K_1\). For each such subset, choose one of the three pairs of opposite vertices of its six-cycle. Take the two isolated vertices and those two opposite vertices, and supplement them alternately with the two internal vertices of one of the two length-three paths between the chosen opposite vertices. The resulting two six-vertex white sets are the complements of an exceptional pair, and **every** exceptional pair arises in exactly this way. Hence the exact count is \(80\cdot3=240\).

## Assumptions and scope

All graphs are finite, simple, and undirected. The specified sixteen-vertex model is the folded five-dimensional cube, rather than the ten-regular complementary graph that is sometimes also called the Clebsch graph. A blue vertex may turn its unique white neighbor blue, and the process repeats until no legal force remains. Zero forcing means that all sixteen vertices ultimately become blue. Configurations are *labelled subsets of the specified vertex set*, not isomorphism classes. Every reconfiguration move swaps exactly one chosen vertex. The Johnson lower bound on exchange distance is \(|A\setminus B|\).

## Proof

**Lemma 1 (exact forcing test).** Fix a blue set \(B\). Starting with \(S=B\), repeatedly add every white vertex that is the unique white neighbor of some vertex of \(S\). The terminal set is independent of the order of legal forces: a force legal before any other legal force either remains legal or has its target already blue afterward. Thus the terminal set equals the closure under any sequential legal-force schedule, and equals \(V\) precisely when \(B\) is zero forcing. A superset of a zero-forcing set is zero forcing. These facts justify both implementations below.

**Lemma 2 (recomputed input classification, not a new result).** There are \(\binom{16}{9}=11{,}440\) nine-element blue sets; none is zero forcing under Lemma 1. Monotonicity excludes every smaller set. Among the \(\binom{16}{10}=8{,}008\) ten-element blue sets, precisely \(3{,}872\) force all vertices. The following exhaustive integer certificate both proves this count and classifies their six-vertex complements: for each six-subset \(W\subseteq V\), form the degrees of the six vertices inside \(C[W]\) and apply Lemma 1 to \(V\setminus W\). The successful degree sequences are
\[
(1,1,2,2,2,4),\ (1,1,2,2,3,3),\ (2,2,2,2,3,3),\ (1,1,1,1,2,4),\ (0,1,1,1,2,3),\ (0,2,2,2,2,2),\ (0,0,1,1,2,2).
\]
For the sequence \((1,1,2,2,3,3)\), forcing holds exactly when its two degree-three vertices are adjacent. For \((2,2,2,2,3,3)\), forcing holds exactly when the two degree-three vertices are nonadjacent. The remaining five sequences need no further condition. Reading their induced edges identifies exactly the seven displayed graph types. The embedded Python checker independently loops over all \(8{,}008\) white sets and asserts both implications, not merely the successful count. It verifies the type multiplicities in the table. The separate C++ checker checks zero forcing with a sequential procedure on the antipodal quotient of the five-cube, independently of the XOR-neighborhood implementation.

**Lemma 3 (recomputed symmetry input, not a new result).** Regard \(V\) as the antipodal equivalence classes of five-bit words, represented by words whose fifth bit is zero. Every permutation of the five coordinates descends to a graph automorphism, and so does translation by any of the sixteen four-bit words. The \(120\cdot16=1{,}920\) resulting permutations are distinct and preserve every graph edge. The embedded symmetry checker constructs all of them and applies them to the minimum sets. Their seven orbits have sizes \(480,960,480,320,960,192,480\), with one distinct induced-white type per orbit. Hence exchange degree and eccentricity are constant on each type.

**Lemma 4 (complete exchange metric).** Index the \(3{,}872\) successful blue masks. Exchange neighbors are exactly the successful masks of the form \(B\oplus2^u\oplus2^v\) with \(u\in B\), \(v\notin B\). Construct the complete adjacency list by these \(10\cdot6\) tests per state. Breadth-first search computes shortest-path distances in any unweighted finite graph. The embedded C++ certificate runs an actual breadth-first search from **every one** of the \(3{,}872\) source states, and compares all \(\binom{3{,}872}{2}=7{,}494{,}256\) unordered pair distances to their Johnson lower bounds. It proves the distance histogram, connectedness, eccentricity six everywhere, and exactly \(240\) one-move excess pairs, all with Johnson distance two. Independently, the Python implementation performs breadth-first searches from all seven orbit representatives and weights each resulting distance row by its orbit size. Exact agreement gives the stated metric and edge counts. In particular, the exchanged-edge degree distribution, derived from the orbit degrees, is \(30:672,\ 32:960,\ 34:1{,}440,\ 37:800\).

**Lemma 5 (geometry of all exceptions).** The Python checker constructs all \(\binom{16}{8}=12{,}870\) eight-subsets, tests induced degrees and connectivity, and finds exactly \(80\) induced copies of \(C_6\sqcup2K_1\). For each, it explicitly constructs its three opposite-vertex/path-splitting pairs. Every resulting six-vertex white set passes the forcing test. Separately, it produces the full exceptional-pair orbit by applying all \(1{,}920\) automorphisms to one certified exceptional pair, obtaining \(240\) distinct pairs. It tests equality of these two **sets of labelled unordered pairs**, rather than merely equality of their sizes. The source/target type and exchange distance are independently verified in Lemma 4. This proves the bijection and the exceptional perfect matching: the exceptional source orbit contains exactly \(480\) configurations and each source has exactly one exceptional partner.

Together these five lemmas prove every assertion. The code is an executable finite proof using complete enumerations of fixed, explicitly bounded domains; no random sampling or unproved infinite extrapolation occurs.

## Verification

Two mutually independent constructions and search strategies are provided, requiring only a C++17 compiler and Python 3 standard library:

```text
c++ -O2 -std=c++17 checks/clebsch_full.cpp -o clebsch_full
./clebsch_full
python3 checks/clebsch_orbits.py
```

The C++ code constructs the antipodal quotient of the five-cube, performs sequential individual forcing, tests all relevant masks, builds all reconfiguration neighbors, and runs all-source shortest paths without symmetry reduction. Its success marker is `ALL_SOURCE_FOLDED_CUBE_EXHAUSTIVE_PASS`.

The Python code constructs the XOR Cayley graph, performs simultaneous forcing, examines every one of its \(65{,}536\) blue subsets, builds all \(1{,}920\) indicated automorphisms, verifies seven orbits and the complete distance spectrum, checks each induced-white type over all \(8{,}008\) six-white subsets, and verifies the geometrical identification of the \(240\) exceptional pairs. Its success markers are `SYMMETRY_REDUCED_CLEBSCH_CERTIFICATE_PASS` and `SEVEN_INDUCED_TYPES_AND_80_C6_PLUS_TWO_ISOLATES_PASS`.

The independent all-source and orbit-reduced breadth-first searches have the same unordered pair-distance histogram. Both verify \(7{,}494{,}016\) pairs with zero Johnson-distance excess and \(240\) with excess one. All array sizes and ranges are explicit in the source, making the exhaustive character independently reproducible.

## Relationship to prior work

The 2008 AIM Minimum Rank--Special Graphs Work Group paper introduced ordinary zero forcing. Hogben and collaborators' 2014 arXiv submission concerns forcing propagation time, rather than exchange distances. Boyer and coauthors' 2018 preprint introduced the zero-forcing polynomial, which counts forcing sets by cardinality but does not determine transitions between them. Geneson, Haas, and Hogben's 2020 preprint introduced the minimum-zero-forcing-set reconfiguration graph; its inspected introduction, examples, main constructions, and concluding computational questions do not determine the Clebsch-specific spectrum. It explicitly asks about shortest-path computation between minimum sets. The graph identification as the folded five-cube is classical. None of these concepts or general theorems is claimed as new here.

The minimum-set polynomial, its \(3{,}872\) coefficient, and its seven group-orbit sizes were determined previously and are not new findings here. The new claim is exclusively the **complete exchange-graph shortest-path metric**, including its self-centered diameter, degree and distance histograms, its sharp at-most-one-step Johnson defect, and the \(80\)-by-\(3\) six-cycle characterization of all defective pairs. A complete count or orbit classification of configurations alone does **not** imply edges, shortest paths, or this exceptional-pair geometry. Published research-record searches for the Clebsch/folded-five-cube aliases found no statement implying these claims, but nonappearance in searches is not a proof of historical priority.

## Limitations

The results concern the sixteen-vertex five-regular Clebsch graph only, not all folded cubes or its ten-regular complement. The finite proof is exact for this domain but does not supply a symbolic general-family theorem. The 2008 foundational paper's full PDF was not accessible in the inspected sources, and older unindexed or unpublished computations could conceivably include equivalent enumerations. The 2018 and 2020 primary preprints were accessible and materially inspected; absence of an indexed match is reported only as qualified originality evidence. No independent scholarly audit has been performed.

## References

1. AIM Minimum Rank--Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications **428** (2008), 1628--1648, DOI: https://doi.org/10.1016/j.laa.2007.10.009. The cited issue is dated 2008; no claim about its earliest preprint date is made.
2. L. Hogben et al., *Propagation time for zero forcing on a graph*, arXiv:1410.4191v1, first publicly posted 2014-10-15. https://arxiv.org/abs/1410.4191.
3. K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910, first posted 2018-01-26. https://arxiv.org/pdf/1801.08910.
4. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first posted 2020-09-01. https://arxiv.org/pdf/2009.00220.
5. Clebsch graph description, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html (graph construction reference, not a novelty claim).
