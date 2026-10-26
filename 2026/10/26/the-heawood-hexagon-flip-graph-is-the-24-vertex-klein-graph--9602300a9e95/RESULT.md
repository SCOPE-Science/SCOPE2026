# The Heawood hexagon-flip graph is the 24-vertex Klein graph

## Finding
Let \(H\) be the point–line incidence graph of the Fano plane. Form \(\mathcal F_6(H)\), whose vertices are perfect matchings of \(H\), joining two matchings precisely when one results from replacing the three matched edges of an alternating six-cycle with its other three edges. Then
\[
\mathcal F_6(H)\cong K_{24}^{\mathrm{Klein}},
\]
where \(K_{24}^{\mathrm{Klein}}\) is the standard seven-regular, 24-vertex Klein graph. More precisely, \(\mathcal F_6(H)\) has 24 vertices, 84 edges, diameter three, 56 triangles, and distance-regular intersection array
\[
\{7,4,1;1,2,7\}.
\]
Its antipodal classes are the eight triples of perfect matchings that individually partition the 21 edges of \(H\) into three one-factors. Every vertex has exactly one flip-neighbor in each of the seven other classes. Hence the flip graph is an antipodal threefold cover of \(K_8\).

## Assumptions and scope
Write the point and line labels of the Fano plane as \(\mathbb Z/7\mathbb Z\). Point \(i\) is incident with line \(j\) exactly when
\[
(i-j)\bmod7\in D=\{0,1,3\}.
\]
The six nonzero ordered differences of the three elements of \(D\) are all distinct, so these incidences define the order-two projective plane. Its incidence graph is the Heawood graph \(H\). A perfect matching contains seven point–line edges, one incident to each point and each line. An alternating six-cycle has three matching edges and three other edges. Only such six-cycle flips are allowed (not longer alternating-cycle replacements). Matchings and lines are labelled as above; the resulting flip graph is independent of that presentation up to isomorphism.

## Proof
**Permutation encoding.** Every perfect matching corresponds bijectively to a permutation \(\pi=(\pi_0,\ldots,\pi_6)\) of \(\{0,\ldots,6\}\) satisfying \((i-\pi_i)\bmod7\in D\) for every \(i\). This follows because the edge at point \(i\) ends at line \(\pi_i\), and the permutation condition is precisely the requirement that each line occurs once. Thus enumerating all \(7!=5040\) permutations and filtering by these seven tests is exhaustive, not sampling.

**Flip equivalence.** For two perfect matchings \(M_\pi,M_\sigma\), their symmetric difference is a union of alternating even cycles. The incidence graph has girth six. If the permutations disagree at exactly three point labels, their difference consists of three removed edges and three added edges, forming a single alternating six-cycle: the nontrivial permutation induced on those three line labels is a three-cycle, so the six involved vertices form one cycle. Conversely, a six-cycle flip changes exactly three point-to-line assignments. Therefore
\[
M_\pi\sim M_\sigma\quad\Longleftrightarrow\quad
|\{i:\pi_i\ne\sigma_i\}|=3.
\]
This is an exact equivalence, with no unlisted candidate edges.

**Finite exhaustive calculation.** `verify_permutations.py` applies the permutation characterization and exact Hamming-three test to all 276 unordered pairs of the 24 passing permutations. It checks exactly 84 undirected flip edges, degree seven at each vertex, and a connected graph. For every ordered pair of its vertices \((u,v)\), it computes the graph distance \(d=d(u,v)\) by finite breadth-first search and counts the neighbors of \(v\) at distances \(d-1,d,d+1\) from \(u\). All 576 ordered pairs satisfy the same values by distance:

| \(d\) | at \(d-1\) | at \(d\) | at \(d+1\) |
| --- | ---: | ---: | ---: |
| 0 | 0 | 0 | 7 |
| 1 | 1 | 2 | 4 |
| 2 | 2 | 4 | 1 |
| 3 | 7 | 0 | 0 |

Consequently, the graph has diameter three and intersection array \(\{7,4,1;1,2,7\}\). Counting triangles directly gives 56. These finite steps are exact, exhaustive proofs for this fixed graph, not extrapolations from smaller graphs.

**Identification with the Klein graph.** The accompanying `klein_reference.am` is the complete 24-by-24 adjacency matrix published for the Klein graph in the DistanceRegular.org graph database, with rows and columns indexed from zero. Let \(M_0,\ldots,M_{23}\) denote the perfect matchings in the lexicographic order of the valid permutation tuples. Define the map \(\phi\) by the consecutive images
\[
(0,11,3,4,15,6,8,19,13,9,18,21,7,22,17,2,1,12,14,10,16,5,23,20).
\]
The certificate verifies that this is a permutation of \(\{0,\ldots,23\}\), and for every ordered pair \(a,b\) it checks exactly
\[
(a\sim b\text{ in }\mathcal F_6(H))\quad\Longleftrightarrow\quad
\text{KleinMatrix}[\phi(a),\phi(b)]=1.
\]
All 576 comparisons pass. Thus the claimed isomorphism follows by an explicit adjacency-preserving bijection, without relying on a uniqueness classification inferred from the shared intersection array.

**The antipodal classes.** For each triple of indices \(a<b<c\), the certificate tests whether the three corresponding perfect matchings cover all 21 edges of \(H\), equivalently whether their three seven-edge sets are pairwise disjoint. Exactly eight triples pass, and they partition the 24 matchings. The other two members of any triple are precisely the two vertices at flip distance three from a member; hence the triples are the distance-three antipodal classes. Directly enumerating each vertex's seven neighbors shows exactly one neighbor in each other class. There are therefore three edges between each unordered pair of classes, yielding an antipodal threefold cover of the eight-vertex complete graph.

## Verification
`verify_permutations.py` uses only Python's standard library and checks permutation completeness, every flip edge, every distance-intersection count, the eight one-factorizations, the triangle count, and all 576 entries of the explicit Klein-graph isomorphism against `klein_reference.am`. `verify_cycles.py` independently generates perfect matchings by recursive incidence assignment and generates all 28 six-cycles from the 14-vertex graph, then constructs legal flips by symmetric difference with cycles, independently checks the full intersection array and factorization structure. The two codes calculate the same canonical SHA-256 fingerprint of the lexicographically indexed matchings and flip edges. Their actual standard output files are `verify_permutations.out` and `verify_cycles.out`. Run both scripts in the directory containing `klein_reference.am` using a standard Python 3 interpreter. No third-party Python packages are necessary.

## Relationship to prior work
The fact that the Heawood graph has 24 perfect matchings partitioned into eight one-factorizations is recorded in established graph-reference material. Dejter's *From the Coxeter graph to the Klein graph* (initial arXiv public version, 9 February 2010) constructs the 56-vertex Klein cubic graph from cycles of the Coxeter graph, notes the Coxeter graph's construction from Heawood six-cycles, and describes the 24-vertex Klein dual graph. The published 24-Klein adjacency matrix fixes the comparison target. Those sources do not state that the *perfect-matching hexagon-switch graph* of the Heawood graph is that Klein graph, and do not supply the explicit permutation-to-Klein adjacency isomorphism above. General results on alternating-cycle-flip dynamics study other graph families or connectivity bounds rather than this exact isomorphism. The novel content claimed here is the structure-preserving identification of these two configuration graphs, not previously known independent counts or the existence of the Klein graph itself.

## Limitations
This is a theorem about a specific 14-vertex incidence graph and six-cycle flips; it does not classify longer-cycle flip graphs, arbitrary incidence graphs, or all cubic bipartite graphs. Exact finite enumeration is a valid proof here because all 5040 potential perfect-matching assignments and all 576 relevant ordered state pairs are covered. The identifying adjacency file reproduces published numeric graph data, not a new graph-theoretic construction of the Klein map. A literature search cannot exclude equivalent descriptions in unindexed or inaccessible older sources; publication priority has not been independently established.

## References
1. Italo J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, first submitted 9 February 2010; accessible full text https://arxiv.org/html/1002.1960v9 (particularly Sections 1–4).
2. DistanceRegular.org, *Klein graph*, https://www.math.mun.ca/distanceregular/graphs/klein.html ; exact adjacency data https://www.math.mun.ca/distanceregular/graphdata/klein.am (24 rows, last graph-page update 7 February 2019).
3. A. E. Brouwer and collaborators, graph reference notes on the Heawood graph, including its eight one-factorizations, https://jaanos.github.io/tables/graphs/Heawood.html .
4. Vladimir Bošković, *Flip dynamics on perfect matchings beyond bipartite and planar graphs*, arXiv:2607.16101 (17 July 2026), https://arxiv.org/abs/2607.16101 ; contextual, not a source for the theorem proved here.
5. Eric W. Weisstein, *Klein Graphs*, MathWorld, https://mathworld.wolfram.com/KleinGraphs.html ; independent graph-parameter reference.
