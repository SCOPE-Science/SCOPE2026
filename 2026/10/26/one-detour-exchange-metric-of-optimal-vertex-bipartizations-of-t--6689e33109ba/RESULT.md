# One-detour exchange metric of optimal vertex bipartizations of the dodecahedral graph

## Finding
Let \(D\) be the dodecahedral graph and \(\mathcal B\) its family of *minimum vertex odd-cycle transversals* (sets whose deletion leaves a bipartite graph). Direct exhaustive finite certification gives \(|\mathcal B|=3240\) and a minimum cardinality of six. Form the one-replacement graph \(R\) on \(\mathcal B\), with an edge precisely when the two six-element sets have five common vertices. Then \(R\) is connected with exactly 31,800 edges, and both radius and diameter equal six. Every vertex of \(R\) has eccentricity six.

For all \(S,T\in\mathcal B\), put \(h(S,T)=6-|S\cap T|\), their distance in the ambient Johnson graph \(J(20,6)\). The exact **one-detour law** is
\[
h(S,T)\le d_R(S,T)\le h(S,T)+1.
\]
Both possibilities occur. Of the \(10,497,600\) ordered pairs, precisely 67,480 need the extra step (33,740 unordered pairs); all other pairs realize their ambient Johnson distance.

The complete metric enumerator is specified by the following \((h,d_R):\mathrm{count}\) triples, **counting ordered pairs**:

| Johnson distance \(h\) | Exchange distance \(d_R\) | Ordered pairs |
|---:|---:|---:|
| 0 | 0 | 3,240 |
| 1 | 1 | 63,600 |
| 2 | 2 | 503,160 |
| 2 | 3 | 15,360 |
| 3 | 3 | 1,923,080 |
| 3 | 4 | 36,520 |
| 4 | 4 | 3,678,840 |
| 4 | 5 | 15,600 |
| 5 | 5 | 3,216,480 |
| 6 | 6 | 1,041,720 |

The vertex-degree distribution of \(R\), expressed as degree:frequency, is 12:150, 14:480, 15:240, 16:30, 17:240, 18:120, 19:120, 20:240, 21:480, 22:120, 23:240, 24:260, 25:360, 26:120, 27:40. In particular the graph is nonregular despite being self-centered.

## Assumptions and scope
We use a fully specified simple graph: \(V(D)=\{u_i,v_i: i\in\mathbb Z/10\mathbb Z\}\) and
\[
E(D)=\{u_i u_{i+1},u_i v_i,v_i v_{i+2}:i\in\mathbb Z/10\mathbb Z\}.
\]
There are 20 vertices and 30 edges. In `verify_a.py`, vertex label \(i\) denotes \(u_i\), and \(10+i\) denotes \(v_i\), for \(0\le i<10\). A vertex odd-cycle transversal \(S\) means that the **induced** subgraph on \(V(D)\setminus S\) is bipartite. Each move removes one member from \(S\) and inserts one former nonmember; intermediate sets must remain minimum-cardinality vertex transversals. This is neither an edge odd-cycle transversal nor a free-size reconfiguration relation.

## Proof
This is an exact finite exhaustive proof implemented by two independent standalone standard-library algorithms. It does not infer a universal theorem from finitely many samples.

1. Exhaustive cardinality argument. `verify_a.py` generates every subset of the 20 graph vertices of cardinalities zero through six, once each by `itertools.combinations`. It tests bipartiteness of the remaining induced graph by a complete BFS two-coloring of **every connected component**, rejecting an edge between same-colored vertices. Thus no size-zero-through-five set succeeds, and exactly 3,240 size-six sets succeed. The construction explicitly tests all \(\sum_{j=0}^6\binom{20}{j}\) relevant vertex subsets, not a sample.
2. Exhaustive move argument. For every successful size-six mask, `verify_a.py` examines every selected vertex and every unselected vertex, performs that replacement, and adds the edge precisely if the resulting mask lies in the full computed family. These are all and only the allowed moves, by the adjacency definition. Reciprocity and absence of duplicate neighbors are asserted. The degree sum proves 31,800 undirected edges.
3. Exhaustive metric argument. BFS beginning at **each** of the 3,240 state vertices traverses all exchange edges. Because the edge lengths are one and BFS explores by nondecreasing path length, the first-arrival depth is the exact shortest-path distance. Every BFS reaches every state; the computed eccentricity histogram is exclusively 6:3240. The program evaluates \(h(S,T)\) by six minus bitwise overlap for **every** of the \(3240^2\) ordered pairs, accumulating the table above. The table contains no pair with \(d_R>h+1\), and contains strict-excess pairs, proving the sharp two-sided inequality. The lower bound \(d_R\ge h\) also follows directly: a single replacement can increase intersection with a target by at most one.
4. Independent replication. `verify_b.py` constructs the same abstract graph through a distinct Hamilton-cycle-plus-chords LCF encoding, `LCF[10,7,4,-4,-7,10,-4,7,-7,4]^2`. It checks an explicit isomorphism from the displayed \(GP(10,2)\) graph. It enumerates bitmasks instead of combinations, employs a different stack-based bipartite test, builds reconfiguration adjacency by comparing every unordered pair of successful state masks rather than generating moves, then independently BFS-traverses all source states. Both exact integer computations agree in all core invariant and distance outputs.

The one-detour bound is sharp: in the \(GP(10,2)\) labeling, the certified pair \(S=\{0,1,3,5,16,19\}\), \(T=\{0,1,3,8,14,15\}\) has \(h=3\) but \(d_R=4\). The feasible family also fails the matroid basis-exchange axiom: both \(S=\{1,5,7,9,11,14\}\) and \(T=\{6,9,10,12,13,15\}\) are size-six vertex transversals, yet exchanging vertex 5 of \(S\) for *any* of the five vertices of \(T\setminus S\) fails to preserve bipartiteness. These examples are finite witnesses within the same exact graph, not separate general claims.

## Verification
Run from a directory containing the four named artifacts:

`python verify_a.py > check_a.json`

`python verify_b.py > check_b.json`

The deterministic UTF-8 outputs including newline must match `verify_a.json` and `verify_b.json`, respectively. Both programs use only the Python standard library and assert the numerical claims internally. Their different vertex labelings produce different `first_excess_witness` lists, as expected, but all nine common scientific invariant fields coincide. A separate comparison verifies each common field and the \(\sum_{h,d}\) table total \(3240^2\). The independent LCF-to-Petersen-notation isomorphism is explicitly asserted in the second program. Exhaustive execution of both programs was successful prior to packaging. This is exact finite checking, without any claim of a formal theorem prover or independent external audit.

## Relationship to prior work
The scalar bipartization number is **not claimed as new**. Zhu's research on induced bipartite subgraphs of triangle-free subcubic graphs explicitly singles out the dodecahedral graph in the sharp-boundary discussion; our focus is the entire family of optimum vertex deletion sets and their one-exchange metric. Král', Sereni and Stacho study general minimum–maximum relations for vertex odd-cycle transversals in planar graphs, not an exact optimum-state metric for this graph. Faria, Klein and Stehlík's accessible arXiv paper studies **edge-deletion** odd-cycle transversals of fullerene graphs and independent-set bounds, not exchange on minimum **vertex** transversals; its relevant first page and text were inspected. Křišťan and Svoboda study generalized token-jumping rules for other graph parameters, a relevant but different reconfiguration setting. Related mathematical-record searches concerned dodecahedral independence/matching complexes and Johnson-hypersimplex graph distances; these do not entail the constrained optimum-transversal adjacency or distances here.

## Limitations
The statement is about exactly this twenty-vertex graph. The proof is a reproducible exhaustive finite certificate, not an analytic characterization for all fullerenes, and makes no assertion of a new scalar bipartization bound. An accessible abstract of Zhu's paper was available, but full text could not be inspected; equivalently formulated or unindexed earlier exchange tables remain possible. Search failures cannot establish global novelty. Independent external validation has not been performed.

## References
1. X. Zhu, “Bipartite subgraphs of triangle-free subcubic graphs,” *Journal of Combinatorial Theory, Series B*, DOI: 10.1016/j.jctb.2008.04.005 (historical induced-bipartite bounds).
2. L. Faria, S. Klein, and M. Stehlík, “Odd Cycle Transversals and Independent Sets in Fullerene Graphs,” arXiv:1203.3912; DOI: 10.1137/120870463 (edge-deletion transversal results).
3. D. Král', J.-S. Sereni, and L. Stacho, “Min-Max Relations for Odd Cycles in Planar Graphs,” DOI: 10.1137/110845835 (vertex transversals in planar graphs).
4. J. M. Křišťan and J. Svoboda, “Reconfiguration Using Generalized Token Jumping,” arXiv:2411.12582 (broader reconfiguration setting).
