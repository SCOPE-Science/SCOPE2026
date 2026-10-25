# The first global geodesic-subpath maximizers beyond six vertices

## Finding

Let \(\operatorname{gpn}(G)\) count every unoriented shortest path between distinct vertices of a connected simple graph \(G\), once per undirected path, together with one zero-length path at each vertex. Equivalently, writing \(\sigma_G(u,v)\) for the number of shortest \(u\)-to-\(v\) paths,
\[
\operatorname{gpn}(G)=|V(G)|+\sum_{\{u,v\}\subseteq V(G)}\sigma_G(u,v).
\]
The sum ranges over unordered *distinct* vertex pairs. For \(n\in\{7,8\}\), let \(M(n)\) be the maximum of this invariant over all connected simple graphs with \(n\) vertices. Then
\[
M(7)=49,\qquad M(8)=74.
\]
More precisely, the seven-vertex equality graphs, up to isomorphism, are exactly \(K_{3,4}\) and \(K_{3,4}\) with one edge deleted. The eight-vertex equality graphs are exactly \(K_{4,4}\) with one edge deleted and \(K_{4,4}\) with two independent edges deleted. No other isomorphism classes attain equality. Since \(\operatorname{gpn}(K_{4,4})=72<74\), eight is the first graph order at which a balanced complete bipartite graph is not an unrestricted maximizer (the cases through six are known and order seven is resolved here).

## Assumptions and scope

Graphs are finite, undirected, simple and connected; parallel edges and disconnected graphs are excluded. All shortest paths are unoriented, so reversing a path does not give a second geodesic. Zero-length paths at vertices are counted. The assertion is **only** for seven and eight vertices, not a general upper bound at larger orders. A complete computational enumeration, rather than a short analytic extremal inequality, certifies its upper bounds and equality classifications. Its eight-vertex completeness uses the standard complete seven-vertex Graph Atlas of Read and Wilson; the complete list of its 1,044 graph masks is embedded as a reproducibility dependency.

## Proof

**Explicit equality values.** In \(K_{a,b}\), cross-part pairs contribute \(ab\) edges, same-part pairs contribute \(b\binom a2+a\binom b2\) geodesics, and singleton paths contribute \(a+b\). Thus
\[
\operatorname{gpn}(K_{a,b})=a+b+\frac{ab(a+b)}2.
\]
If a matching of \(t\) edges is removed, counting all shortest paths by endpoint type gives
\[
\operatorname{gpn}(K_{a,b}-M_t)=a+b+\frac{ab(a+b)}2+t(ab-2a-2b+3)-t^2.
\]
This matching-deletion expression is an earlier published result and is used here only to identify candidate equality values; it is **not** claimed as a new formula. Substitution yields
\[
\operatorname{gpn}(K_{3,4})=49,\qquad
\operatorname{gpn}(K_{3,4}-M_1)=49,
\]
\[
\operatorname{gpn}(K_{4,4})=72,\quad
\operatorname{gpn}(K_{4,4}-M_1)=\operatorname{gpn}(K_{4,4}-M_2)=74.
\]

**Exact counting routine.** For each vertex \(s\), run breadth-first search on the adjacency bit masks. At the start set \(\mathrm{dist}(s)=0\) and \(\mathrm{ways}(s)=1\). Whenever an edge \(uv\) satisfies \(\mathrm{dist}(v)=\mathrm{dist}(u)+1\), add \(\mathrm{ways}(u)\) to \(\mathrm{ways}(v)\); upon first discovery initialize the distance and contribution. BFS processes vertices in nondecreasing distance, so induction on distance shows that \(\mathrm{ways}(v)=\sigma_G(s,v)\). Count only \(v>s\) to avoid orientation duplicates, then add \(|V(G)|\). A disconnected graph is rejected when a BFS does not reach all vertices. This exact integer routine appears independently in `verify.cpp` and `verify8.cpp`.

**Complete seven-vertex search.** A labeled simple seven-vertex graph is one of the \(2^{21}=2,097,152\) subsets of the 21 possible edges. `verify.cpp` enumerates each mask. Of these, 1,866,256 are connected; the greatest calculated invariant is 49. The maximizers consist of precisely 35 labeled graphs with 12 edges and 420 with 11 edges. The code forms the full orbits, under all \(7!\) vertex permutations, of the two displayed exemplar graphs, and verifies **equality of the actual mask sets** with the two maximizer classes. The 12-edge exemplar is \(K_{3,4}\); the 11-edge exemplar is \(K_{3,4}-M_1\). A second implementation using Graph Atlas graphs and independent NetworkX shortest-path enumeration finds exactly two maximizing classes among the 853 connected seven-vertex representatives; this independently checks the seven-vertex classification.

**Complete eight-vertex search.** Every eight-vertex graph can be relabeled so that deleting vertex 7 leaves one of the 1,044 isomorphism representatives of seven-vertex graphs in Read and Wilson's Graph Atlas. Given any such representative, an eighth vertex is specified by exactly one of its \(2^7=128\) possible neighborhoods. Therefore *every eight-vertex isomorphism class occurs among these extensions*. `verify8.cpp` enumerates all \(1,044\cdot128=133,632\) representatives-with-extension (not necessarily distinct), including 119,980 connected extensions. The exact greatest value is 74, attained by just nine extension records: four having 14 edges and five having 15 edges. The program forms the complete labeled-permutation orbits of \(K_{4,4}-M_2\) and \(K_{4,4}-M_1\), with 2,520 and 560 distinct labeled masks respectively, and verifies that **every one** of the nine maximizing extensions is in the appropriate orbit. Since both candidate graphs have invariant 74, these two are exactly all eight-vertex maximizing isomorphism types.

The exhaustive reductions show no unseen seven- or eight-vertex graph can exceed the recorded maximum. Combined with explicit equality graphs they complete the two statements. The graph atlas is a standard published complete enumeration, not a random sample; its 1,044 stored representatives are required input and bundled with the verifier.

## Verification

The package includes `verify.cpp` and `verify8.cpp` (C++17, standard library only), `atlas7_masks.txt` (the required 1,044 seven-vertex representatives), `generate_atlas7.py` (regenerates the atlas from NetworkX 3.6.1), `verify_atlas.py` (an independent seven-vertex implementation), `requirements.txt`, and the actual outputs `verification_output.txt`, `verification8_output.txt`, `atlas_output.txt`.

From the extracted package, compile with `g++ -O3 -std=c++17 verify.cpp -o verify7` and `g++ -O3 -std=c++17 verify8.cpp -o verify8`. In that same directory run `./verify7`, `./verify8 atlas7_masks.txt`, and `python verify_atlas.py` after installing the pinned NetworkX version. The source and compiled checkers have no nonstandard C++ dependencies. To regenerate the atlas input, run `python generate_atlas7.py` and compare its output file bytewise with the bundled atlas masks.

Expected seven-vertex results: 2,097,152 labeled graphs, 1,866,256 connected, maximum 49, exactly 455 labeled maximizers split as 420 with 11 edges and 35 with 12 edges, and a full orbit comparison PASS. Expected eight-vertex results: 133,632 extensions, 119,980 connected, maximum 74, nine maximizing extensions, and a full orbit comparison PASS. The independent seven-vertex implementation reports 853 connected atlas isomorphism classes, two maximizers, and PASS. All these outcomes were observed in the embedded outputs.

## Relationship to prior work

Knor, Sedlar, Škrekovski and Zhang introduced the geodesic subpath number in 2026. Their complete published text states the extremal types for graph orders at most six, gives an all-order upper bound rather than sharp maxima beyond six, and explicitly leaves unrestricted extremal improvements and bipartite extremizers as open problems.

An earlier result, *Geodesic subpath numbers of bicliques with a deleted matching* (public research record dated 2026-10-04), already gives the exact formula for the candidate graph family and its optimum for fixed bipartition sizes. Thus it implies the displayed witness values but **not** global upper bounds or uniqueness among arbitrary connected graphs. Another result, *Balanced complete bipartite graphs uniquely maximize geodesic subpaths at diameter two* (2026-09-17), covers only diameter-two graphs. The eight-vertex maximizers here have diameter three and therefore lie outside it. A separate tapered-path-blowup construction concerns a larger-order family and supplies no global eight-vertex classification.

The contribution is the complete global seven- and eight-vertex extremal theorem, the full list of attaining isomorphism classes, and the first order at which balanced biclique extremality ceases. Targeted semantic and literature searches did not reveal a broader covering statement, but absence from searched records is not a proof of absolute bibliographic novelty.

## Limitations

This is a finite, computer-assisted extremal classification; no claim is made for nine or more vertices. The proof relies on published completeness of the seven-vertex Graph Atlas and on correctly executing the self-contained exact enumeration. Only the seven-vertex counts have an independent implementation with a separate shortest-path enumeration library. The two programs and the supplied full atlas masks permit reproducing all eight-vertex certificates. The classification does not settle unrestricted or bipartite extremal graphs at arbitrary order. A differently titled earlier global small-order census remains a bibliographic-priority risk; no independent mathematical audit has been performed.

## References

1. M. Knor, J. Sedlar, R. Škrekovski and X.-D. Zhang, *Counting Geodesic Paths in Graphs*, arXiv:2604.04907, first public 2026-04-06; *Mediterranean Journal of Mathematics* **23**, article 171 (2026), DOI 10.1007/s00009-026-03159-3.
2. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998. The seven-vertex atlas is distributed by NetworkX `graph_atlas_g`; see https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html.
3. *Geodesic subpath numbers of bicliques with a deleted matching*, public mathematical result, 2026-10-04.
4. *Balanced complete bipartite graphs uniquely maximize geodesic subpaths at diameter two*, public mathematical result, 2026-09-17.
5. *Boundary-tapered path blow-ups improve the geodesic-subpath lower bound*, public mathematical result, 2026-09-20.
