# Minimum odd-neighborhood witnesses in line graphs of cyclically robust cubic graphs

## Finding
For a finite simple connected cubic graph \(H\) of girth at least five and cyclic edge-connectivity at least five, let \(G=L(H)\) be its line graph and define
\[
 f(G)=\min_{\varnothing\ne A\subseteq V(G)}|A\cup\operatorname{Odd}_G(A)|,
 \qquad\operatorname{Odd}_G(A)=\{x:|N_G(x)\cap A|\text{ is odd}\}.
\]
Then \(f(G)=5\), and **all** minimizing choices of \(A\), identified with subsets of \(E(H)\), are precisely:

1. the singleton edge sets \(\{e\}\) for \(e\in E(H)\);
2. the edge sets of all five-cycles in \(H\);
3. if \(|V(H)|=10\), the perfect matchings of \(H\).

There are no additional minimizing sets. In particular, if \(c_5(H)\) is the number of (unoriented) five-cycles and \(p(H)\) the number of perfect matchings, the number of minimum witnesses is
\[
 |E(H)|+c_5(H)+\mathbf1_{\{|V(H)|=10\}}p(H).
\]
The local minimum degree of \(L(H)\) is exactly four: \(\delta_{\mathrm{loc}}(L(H))=f(L(H))-1=4\). It equals the original line graph's minimum degree, so local complementation cannot lower that minimum degree.

**Fullerene corollary.** Every classical fullerene graph \(H\) (a cubic three-connected plane graph with only pentagonal and hexagonal faces) has exactly twelve five-cycles, has \(|V(H)|\ge20\), and is cyclically five-edge-connected. Therefore its line graph has exactly
\[
 \boxed{\tfrac32|V(H)|+12}
\]
minimum witnesses and local minimum degree four. Under the usual graph-state stabilizer construction, the witness count equals the number of minimum-weight nonidentity stabilizer elements, each of weight five. The excess of twelve over the edge count is supplied exactly by the twelve pentagons.

The Petersen graph provides a small boundary case with \(15+12+6=33\) minimum witnesses, whereas the Heawood graph has \(21\), all coming from singleton edges. These examples illustrate the same theorem, rather than separate findings.

## Assumptions and scope
All graphs are finite, undirected, simple, and connected. A cubic graph is three-regular. The girth is the length of a shortest cycle. Cyclic edge-connectivity at least five means that no cut with fewer than five edges separates the graph into shores both containing a cycle. The line graph \(L(H)\) has one vertex for each edge of \(H\), with adjacency for incident edges. A five-cycle refers to a five-edge simple cycle, not a five-edge closed walk.

For a graph \(G\), local complementation at a vertex toggles adjacencies among its neighbors. The local minimum degree is the least minimum degree of any graph obtainable by finitely many local complementations. The equality \(\delta_{\mathrm{loc}}(G)+1=\min_{\varnothing\ne A}|A\cup\operatorname{Odd}_G(A)|\) is an established theorem, not part of the novel claim.

A graph state on \(|V(G)|\) qubits has commuting stabilizer generators \(K_x=X_x\prod_{y\in N_G(x)}Z_y\). For \(A\subseteq V(G)\), the nonidentity product \(\prod_{x\in A}K_x\) has support exactly \(A\cup\operatorname{Odd}_G(A)\). Distinct nonempty \(A\) yield distinct stabilizer elements. Thus this theorem classifies minimum-weight stabilizer *elements*; it does not claim an independent quantum-error-correcting code distance.

## Proof
**1. Edge-cut parity identity.** Identify \(A\subseteq V(L(H))\) with an edge set of \(H\). Let \(S=S(A)\subseteq V(H)\) consist of vertices of odd degree in the spanning subgraph with selected edge set \(A\), and let \(\delta_H(S)\) denote the edges crossing the cut \((S,V(H)\setminus S)\). For any edge \(uv\) not in \(A\), its number of neighbors belonging to \(A\) in \(L(H)\) is \(\deg_A(u)+\deg_A(v)\), which is odd exactly when \(uv\in\delta_H(S)\). Consequently
\[
 |A\cup\operatorname{Odd}_{L(H)}(A)|
 =|A|+|\delta_H(S)\setminus A|
 =|\delta_H(S)|+|A\setminus\delta_H(S)|. \tag{1}
\]
This identity is valid for every finite simple graph \(H\), without cubicity assumptions.

**2. Small-cut lemma.** In a cubic graph, if one side \(R\) of a cut induces a forest with \(c\ge1\) components, the number of crossing edges is
\[
 3|R|-2(|R|-c)=|R|+2c.\tag{2}
\]
By cyclic edge-connectivity at least five, every cut of size at most four must have a forest side. It follows that no nonempty proper cut has size one or two; every four-edge cut isolates exactly two adjacent vertices on one of its shores. (A three-edge cut can isolate a singleton.) Since \(|S(A)|\) is even, cubicity gives \(|\delta_H(S(A))|\equiv 3|S(A)|\equiv0\pmod2\). Therefore, when \(\varnothing\subsetneq S(A)\subsetneq V(H)\), the cut has at least four edges; if it has four, \(S(A)\) is an adjacent pair or the complement of such a pair.

**3. Classification at weight at most five.** A singleton selected edge \(A=\{uv\}\) has \(S(A)=\{u,v\}\), four cut edges, and one selected edge outside the cut, so (1) yields weight five. Thus the minimum is at most five. Suppose conversely that a nonempty \(A\) has weight at most five. Consider its even-cardinality odd-degree set \(S=S(A)\).

If \(S=\varnothing\), all degrees in the selected spanning subgraph are even; every nonempty Eulerian edge set contains a cycle. Girth at least five implies \(|A|\ge5\), with equality exactly when \(A\) is a five-cycle.

If \(S=V(H)\), every vertex has positive odd selected degree, so \(|A|\ge |V(H)|/2\). The cubic girth-five Moore bound gives \(|V(H)|\ge10\). Thus weight at most five forces \(|V(H)|=10\) and \(A\) to be a perfect matching (weight five).

Finally let \(S\) be nonempty and proper. By (1) and the parity of the cut, weight at most five forces \(|\delta_H(S)|=4\) and \(|A\setminus\delta_H(S)|\le1\). By step 2, one shore of the cut is an adjacent pair \(\{u,v\}\). The four cut edges meet four *distinct* vertices on the other shore: an identification would create a triangle or violate simplicity.

If \(S=V(H)\setminus\{u,v\}\), at most four selected cut edges and one selected non-cut edge can make at most six vertices of \(S\) have odd selected degree. But the Moore bound gives \(|S|\ge8\), a contradiction.

Hence \(S=\{u,v\}\). With no selected non-cut edge, every selected cut edge would give a distinct outside vertex odd selected degree, contrary to the definition of \(S\). If the allowed one non-cut edge is \(uv\), the same observation forces all cut edges absent, giving \(A=\{uv\}\). The only remaining possibility is a non-cut edge \(wx\) on the other shore. To cancel the parity at its endpoints, the selected cut edges must be \(uw\) and \(vx\) (in either orientation), with one at each of \(u,v\). These selected edges together with the existing edge \(uv\) would form a four-cycle \(u,w,x,v,u\), contrary to girth at least five. Thus the singleton edge is the sole proper-cut minimizer. The three cases prove both exactness and the exhaustive list.

**4. Counts and local complementation.** Singleton edges, five-cycles and (where permitted) perfect matchings are distinct chosen edge sets, yielding the count. The known local-complementation identity converts \(f=5\) to \(\delta_{\mathrm{loc}}=4\), while cubicity makes every vertex in \(L(H)\) degree four. The standard fullerene properties of cyclic edge-connectivity five, twelve five-cycles, and at least twenty vertices specialize the count to \(3|V(H)|/2+12\).

## Verification
The two complete standalone Python programs `check_flip_linegraphs.py` and `check_cubic_cut_certificates.py` use only the Python standard library. Run each with Python 3 from the extracted package directory.

`check_flip_linegraphs.py` constructs the Petersen graph as the disjointness graph on two-subsets of five points, the Heawood graph as the seven-point Fano incidence graph, and the dodecahedral graph as a generalized Petersen graph. For each, it exhausts every nonempty selected edge set of size at most five, computes the odd neighbors directly in the corresponding line graph, and checks exact minimum-witness counts: \(33\), \(21\), and \(42\). Searching larger selected sets is unnecessary because such sets have support weight greater than five.

`check_cubic_cut_certificates.py` uses a different Petersen representation and a binary-vector Fano incidence construction. It enumerates all distinct cuts for these three examples, confirms that every three-edge cut isolates a vertex and every four-edge cut isolates an edge, and independently counts their five-cycles: \(12,0,12\). This verifies the principal hypotheses in each example; the unrestricted theorem follows from the proof, not extrapolation from a finite census.

## Relationship to prior work
Bohman, Dudek, Frieze and Pikhurko (first arXiv version March 12, 2009) defined and studied \(f(G)\), focusing on random graph asymptotics. Javelle, Mhalla and Perdrix and later Cattanéo and Perdrix developed the local-minimum-degree framework and its complexity. The identity relating local minimum degree to odd-neighborhood minimization is previously known and is used here.

Došlić's 2003 cyclic edge-connectivity theorem supplies the fact that all classical fullerenes satisfy the relevant cut hypothesis. The twelve pentagons, their identification with all five-cycles, and the Petersen and Heawood base-graph descriptions are also known facts. The claimed new statement is the **uniform exact classification of minimum odd-neighborhood witnesses in the specified cubic line-graph family**, including the fullerene stabilizer multiplicity formula; it is not a new theorem about fullerene cyclic connectivity or the number of pentagons.

## Limitations
The result requires cubicity, girth at least five and cyclic edge-connectivity at least five; no equivalence or necessity of these hypotheses is asserted. The graph-state interpretation counts nonidentity stabilizer elements, not all Pauli errors or the distance of an independently encoded quantum code. A historical result under graph-state, isotropic-system or binary-additive-code terminology might be equivalent; the accessible primary sources and research records did not establish such coverage. The two programs validate particular examples and the low-weight search cutoff, not every graph in the infinite class.

## References
1. T. Bohman, A. Dudek, A. Frieze and O. Pikhurko, *Flips in Graphs*, arXiv:0903.2201v1 (first public version 2009-03-12); SIAM J. Discrete Math. 24 (2010), 1046–1055, DOI: 10.1137/090752237.
2. J. Javelle, M. Mhalla and S. Perdrix, *On the Minimum Degree up to Local Complementation: Bounds and Complexity*, arXiv:1204.4564v1 (2012-04-20).
3. D. Cattanéo and S. Perdrix, *Minimum Degree up to Local Complementation: Bounds, Parameterized Complexity, and Exact Algorithms*, arXiv:1503.04702v1 (2015-03-16), especially the odd-neighborhood identity.
4. T. Došlić, *Cyclical edge-connectivity of fullerene graphs and (k,6)-cages*, Journal of Mathematical Chemistry 33 (2003), 103–112, DOI: 10.1023/A:1023299815308.
5. *Fullerene*, Wolfram MathWorld (the standard count of exactly twelve five-cycles), https://mathworld.wolfram.com/Fullerene.html.
