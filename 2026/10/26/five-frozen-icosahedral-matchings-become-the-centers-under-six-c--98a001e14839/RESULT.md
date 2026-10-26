# Five frozen icosahedral matchings become the centers under six-cycle flips

## Finding
Let \(I\) be the twelve-vertex icosahedral graph. For \(\ell\in\{4,6\}\), let \(R_\ell(I)\) have one vertex for every perfect matching of \(I\), with two distinct perfect matchings adjacent exactly when their symmetric difference is the edge set of a **single simple alternating cycle of length \(\ell\)**. Chords of the cycle in \(I\) are allowed; this is an edge-set condition, not a restriction to facial or induced cycles.

There are \(125\) perfect matchings (a count already available from the top-dimensional face number of the published icosahedral matching-complex calculation). The new exact reconfiguration conclusions are
\[
\begin{aligned}
|E(R_4(I))|&=300, &\operatorname{comp}(R_4(I))&=(120,1,1,1,1,1),\\
|E(R_6(I))|&=580, &\operatorname{comp}(R_6(I))&=(125),\\
\operatorname{rad}(R_6(I))&=3, &\operatorname{diam}(R_6(I))&=4.
\end{aligned}
\]
The nontrivial 120-vertex component of \(R_4(I)\) has radius \(5\) and diameter \(6\). **Precisely five matchings are isolated under four-cycle flips, and these same five are precisely the radius-three centers of the connected six-cycle flip graph.** Every other matching has six-flip eccentricity \(4\). Thus six is the sharp smallest permitted alternating-cycle length for connectivity if all flips have one fixed length; allowing cycles of lengths at most six also connects all perfect matchings.

## Assumptions and scope
The underlying graph is simple and undirected. Use vertices \(\{0,1,\ldots,11\}\); for \(i\in\mathbb Z/5\mathbb Z\), set \(u_i=1+i\) and \(v_i=6+i\). Its thirty edges are
\[
\{0u_i,\,11v_i,\,u_iu_{i+1},\,v_iv_{i+1},\,u_iv_i,\,u_iv_{i+1}:i\in\mathbb Z/5\mathbb Z\}.
\]
This is the familiar two pentagonal rings plus opposite apices realization of the icosahedron. The two program inputs use this exact labeling, and verify twelve vertices, thirty edges and degree five. A perfect matching is a six-edge subset covering each vertex exactly once. A legal flip replaces the three (respectively two) matched alternating edges on one six-cycle (respectively four-cycle) by the other three (respectively two) cycle edges, leaving all other matched edges unchanged. Cycles need not bound a face; indeed the icosahedron has triangular faces only. No assertion concerns embedding-dependent facial resonance.

## Proof
**Exhaustive matching-space lemma.** If \(U\) is the set of unmatched vertices, every perfect completion must match its least-labeled vertex \(u\) to exactly one neighbor \(v\in U\), then perfectly match \(U\setminus\{u,v\}\). Recursing from all twelve vertices is exhaustive and produces no duplicates after canonically sorting the six selected edges. The first supplied self-contained verifier implements this recurrence on the displayed thirty-edge graph and obtains exactly 125 matchings. This count also agrees with the independently published icosahedral matching-complex face number and is not asserted to be new.

**Exact flip lemma.** For two perfect matchings \(M,N\), each vertex has even degree in \(M\mathbin\triangle N\), so their symmetric difference is a vertex-disjoint union of even alternating cycles. They differ by exactly one legal length-\(\ell\) flip if and only if this symmetric difference contains exactly \(\ell\) edges, each of its \(\ell\) incident vertices has degree two, and the resulting edge-induced subgraph is connected. These are finite, exact integer and graph-connectivity tests; checking every unordered pair of the 125 matchings therefore determines all edges of each flip graph with neither false positives nor omissions. The first verifier checks all pairs and reports 300 length-four flip edges and 580 length-six flip edges.

**Reachability and distance lemma.** Breadth-first search from each of the 125 states computes its entire connected component and all shortest-path distances, because every legal move has unit cost. The first verifier checks that the four-cycle graph has component sizes \((120,1,1,1,1,1)\), that its main component has radius five and diameter six, and that the six-cycle graph is connected, with radius three and diameter four. It also checks that exactly five states have no four-cycle neighbor and that precisely those five states have six-cycle eccentricity three; the other 120 have eccentricity four. Since there is no simple alternating two-cycle in a simple graph, four is the only smaller candidate length, establishing the sharpness assertion.

**Independent reconstruction.** The second verifier has a separately hard-coded symmetric adjacency table, enumerates all \(\binom{30}{6}=593775\) six-edge subsets, retains exactly those covering all twelve vertices, and enumerates simple four- and six-cycles by vertex-path depth-first search. It tests both alternating edge parities on every enumerated cycle and toggles the corresponding edges of each compatible perfect matching. This generates exactly the same *individual* matchings and graph edges as the pairwise symmetric-difference construction: the independently calculated SHA-256 digests of the canonical `matchings.tsv`, `flip4.tsv`, and `flip6.tsv` match the first verifier's output, not merely the edge counts. An independent breadth-first traversal reproduces the component and eccentricity statements. This supplies a second exact finite exhaustive derivation with different search space and transition construction.

## Verification
Run the two standard-library Python 3 programs, from the package directory:

```bash
python3 verify_pairs.py --cert-dir .
python3 verify_cycles.py
```

Both print a compact JSON record containing all claimed numbers and the SHA-256 digests of the three canonical certificates, then an explicit PASS marker. The first command writes `matchings.tsv`, `flip4.tsv`, and `flip6.tsv`; their exact bytes accompany this finding. The reproduced matching digests are `eee0f9c4f1beafaf17343ea8a3072905acf29ff82ed897353fc2dfbd30257b1e`, `c2308f82bec9ac5ad90ba143a71df136c9b388b13f11bb9829f8698e6814ddc3`, and `ecf05ba814dc788cad4392da10f29c8714ec368b0bd10839434891fe03ec732e` in that order. The two programs were actually executed separately, and their numerical JSON records were compared byte-for-byte; complete recorded terminal outputs are included. The code has no third-party dependencies and enumerates the *complete* finite sample space specified above.

For an additional human-readable witness, the five frozen matchings are precisely the rows indexed \(21,39,61,75,120\) in `matchings.tsv`. The program checks that they are the only radius-three vertices of the six-flip graph. They form a five-element symmetry orbit under cyclic rotation of the two pentagonal rings.

## Relationship to prior work
Lei, Yeh and Zhang's 2014 publicly posted work develops the theory of alternating cycles and anti-forcing of perfect matchings. Its planar-bipartite minimax theorem does not apply to the nonbipartite icosahedron and does not classify these transformation graphs. Bonamy and coauthors' 2019 full-text study formalizes four-cycle perfect-matching reconfiguration and proves broad complexity and tractable-class theorems; neither the concrete icosahedral component structure nor six-cycle eccentricity is supplied by those theorems. Bošković's 2026 study develops cycle-length connectivity bounds for decorated graphs, but does not provide this exact finite icosahedral classification.

A publicly accessible study of the **ordinary icosahedral matching complex** already gives the number \(125\) of maximal-cardinality simplices (perfect matchings) and determines a topological invariant of the complex. That theorem is different: it has the original graph edges as simplicial vertices, and it does not provide the alternating-cycle transition relation on the set of perfect matchings. The known matching count is explicitly credited here. Other finite perfect-matching flip enumerations for the Heawood, Möbius–Kantor, Desargues, and dodecahedral graphs concern different underlying graphs and their specific short-cycle structures; none implies this icosahedral result by a stated reduction.

## Limitations
This is an **exact finite** theorem for the labeled icosahedral graph, with computationally exhaustive proofs backed by two standalone programs. It is not a theorem for all triangulations, five-regular graphs, or larger geodesic graphs. A six-cycle flip here may traverse triangles and is not a facial resonance move. The independent programs compare their entire canonical matching and flip-edge certificates, but they are not a formal proof assistant or independent external scientific audit. Publication priority remains subject to unindexed or inaccessible graph-specific results; unsuccessful searches are not proofs of novelty.

## References
1. H. Lei, Y.-N. Yeh and H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796v1, first public 2014-06-15, https://arxiv.org/abs/1406.3796 .
2. M. Bonamy et al., *The Perfect Matching Reconfiguration Problem*, arXiv:1904.06184v1 (2019), https://arxiv.org/abs/1904.06184 .
3. V. Bošković, *Flip dynamics on perfect matchings beyond bipartite and planar graphs*, arXiv:2607.16101v1 (2026), https://arxiv.org/abs/2607.16101 .
4. *Three-torsion in the icosahedral matching complex: a planar counterexample*, public mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-icosahedral-matching-complex-a-planar-count--28565ad1ea1a .
5. Z. Che and Z. Chen, *Forcing on Perfect Matchings — A Survey*, MATCH 66 (2011), 93–136, https://match.pmf.kg.ac.rs/electronic_versions/Match66/n1/match66n1_93-136.pdf .
