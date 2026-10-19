# Hexagon resonance fragmentation and octagonal reconnection in the Nauru graph

## Finding

Let \(G=\operatorname{GP}(12,5)\) be the Nauru graph. For an even integer \(L\geq 6\), let \(R_{\leq L}(G)\) have one vertex for each perfect matching of \(G\), with distinct matchings adjacent if their symmetric difference is the edge set of a **single simple alternating cycle of length at most \(L\)**. In particular, \(R_{\leq6}(G)\) is the hexagon resonance graph of the standard toroidal hexagon embedding.

**Exact result.** There are \(120\) perfect matchings. The hexagon resonance graph has \(192\) edges and exactly thirteen connected components, of orders
\[
57,\quad18,\quad18,\quad18,\quad1,1,1,1,1,1,1,1,1.
\]
The four nontrivial components all have radius and diameter \(6\), and the other nine matchings are isolated. Its complete vertex-degree distribution (degree : multiplicity) is
\[
0:9,\quad 2:48,\quad 4:36,\quad 5:24,\quad 8:3.
\]

Allowing all alternating octagonal flips as well gives a **connected** graph \(R_{\leq8}(G)\) on the same \(120\) matchings, with \(606\) edges, radius \(4\), and diameter \(6\). Its eccentricity distribution is
\[
4:96,\qquad 5:18,\qquad 6:6,
\]
and its vertex-degree distribution is
\[
3:6,\quad8:12,\quad9:36,\quad11:42,\quad12:18,\quad14:3,\quad18:3.
\]
Precisely \(414\) previously absent adjacencies are contributed by octagonal flips. Thus the **minimum allowed cycle length giving connectivity is eight**: every allowed cycle shorter than eight is a hexagon, and hexagon flips alone do not connect the matchings.

## Assumptions and scope

All graphs are finite, undirected, loopless, and simple. The Nauru graph has vertices \(u_i,v_i\) for \(i\in\mathbb Z/12\mathbb Z\), and edges
\[
\{u_i,u_{i+1}\},\qquad\{u_i,v_i\},\qquad\{v_i,v_{i+5}\}
\quad (i\in\mathbb Z/12\mathbb Z).
\]
There are \(24\) vertices and \(36\) edges. A perfect matching covers every vertex with exactly one edge; it consequently contains \(12\) edges. If \(M\) and \(M'\) are perfect matchings, a legal \(\ell\)-flip means that \(M\triangle M'\) consists of the \(\ell\) edges of one simple cycle, rather than a disjoint union of two or more cycles. The cycle is then automatically alternating between \(M\) and \(M'\).

In the toroidal hexagon embedding described by Eppstein, there are twelve hexagonal faces. The enumerated graph has exactly twelve simple six-cycles, so the hexagonal flip graph here agrees with the face-flip resonance graph, without an extra choice of face set. The result concerns this one explicitly defined graph, not all toroidal polyhexes or all generalized Petersen graphs.

## Proof

**Lemma 1 (exhaustive matching enumeration).** Let \(U\) be the subset of graph vertices not yet covered by a partial matching. Choose the least labelled \(x\in U\), and branch once for every neighbor \(y\in U\), adding the edge \(xy\) and recursing on \(U\setminus\{x,y\}\). When \(U\) is empty, record the resulting matching. Every perfect matching contains exactly one incident edge at \(x\), so exactly one branch corresponds to it; inductively all perfect matchings, and no duplicates, are produced. The independently executable procedure in `verify_gp.py` yields \(120\) distinct length-\(12\) edge masks. The independent procedure in `verify_cayley.py`, with a distinct \(24\)-permutation graph model, likewise yields \(120\). This establishes completeness of the configuration space.

**Lemma 2 (exact adjacency test).** If \(M\) and \(M'\) are perfect matchings, every nontrivial connected component of \(M\triangle M'\) is an even cycle: at every vertex used by the difference, one incident edge belongs to each matching. Hence the two matchings are adjacent by a single cycle of length \(\ell\) if and only if their symmetric difference contains \(\ell\) edges and these edges induce a connected degree-two subgraph. This equivalence checks both necessity and sufficiency and excludes a disjoint union of shorter cycles with the same total size.

**Lemma 3 (finite exact computations).** Give the \(36\) edges of the displayed graph lexicographic indices. The accompanying certificate `nauru_certificate.json` contains all \(120\) matching masks, all \(12\) hexagonal and \(54\) octagonal simple-cycle masks, and complete lists of reconfiguration pairs for lengths six and eight. For each matching mask \(m\) and a listed even-cycle mask \(c\), the toggled mask \(m\oplus c\) is a perfect matching exactly when the selected edges alternate on that cycle; the program tests membership in the exhaustively enumerated set of matchings. Independently, it checks **all \(\binom{120}{2}=7140\) unordered matching pairs** using Lemma 2 and agrees with these cycle-toggle adjacencies. This yields precisely \(192\) six-flip edges and \(414\) distinct eight-flip edges.

**Lemma 4 (graph invariants).** For each of the two exact adjacency lists, breadth-first search visits each reachable vertex and assigns its minimum number of flips from the starting matching, by the standard queue invariant. Applying this search at every matching computes each connected component and the eccentricity of every vertex in that component. The complete computations in `verify_gp.py` obtain the component orders and degree, radius, diameter, and eccentricity distributions stated in the Finding. The independent implementation in `verify_cayley.py` separately obtains the same statistics from all matching pairs, including that the four nontrivial hexagon-flip components each have radius and diameter six.

The source programs have no nonstandard dependencies. Running them separately and comparing their finite outputs, including the pairwise symmetric-difference cross-check in the first, verifies the enumeration premises of Lemmas 3 and 4. Combining the four lemmas proves every numerical claim above. Finally, the graph has no cycle shorter than six (the verifiers' bipartite cubic construction, together with the simple-cycle check, confirms this for the graph); since the six-flip graph is disconnected while the six-or-eight-flip graph is connected, the connectivity threshold is sharp. \(\square\)

## Verification

From the directory containing the provided artifacts run:

```sh
python3 verify_gp.py
python3 verify_cayley.py
```

The first program writes `nauru_certificate.json`. Its exact generated bytes are supplied as a separate artifact, so the deterministic certificate can be compared directly, in addition to the reported counts. The two stdout transcripts `verify_gp.stdout` and `verify_cayley.stdout` reproduce the checked results.

The first program independently enumerates simple cycles and also checks all matching pairs by a connected symmetric-difference criterion; the second enumerates matchings from the Cayley graph of the symmetric group on four symbols generated by three star transpositions, and checks pairwise differences without using a cycle-mask catalogue. Eppstein describes the isomorphism of this Cayley model with the Nauru graph. Both programs contain explicit assertions for the core quantities and finished successfully.

## Relationship to prior work

Eppstein's 2007 account identifies the Nauru graph as \(\operatorname{GP}(12,5)\), gives its Cayley model, and describes the symmetric toroidal embedding with hexagonal faces. These descriptions fix the natural graph and face-flip operation but do not count or classify its perfect-matching flip components.

The reconfiguration papers of Bonamy et al. (2019) and Ito et al. (2019 preprint; published 2022) respectively study alternating **four-cycle** flips and **unrestricted** single alternating-cycle flips. Neither inspected work provides the exact six-versus-eight restricted-cycle transition or the component and distance census here. In particular, unrestricted alternating-cycle reachability does not imply reachability under the bound eight.

Liang and Zhang (2026) establish a general connectivity criterion for the face-resonance graphs of toroidal polyhexes, using fluxes and ladders. Their work also counts trivial perfect matchings for a parameterized polyhex family. Accordingly, the existence of isolated face-flip matchings and general component criteria are **not claimed new**. The retained result here is the explicit Nauru-graph reconfiguration census, distances, and the first cycle-length enlargement that reconnects all optimal configurations. The inspected article neither specifies the Nauru graph nor supplies this octagonal-reconnection threshold or its distance distribution.

## Limitations

This is an exact finite classification, not an infinite-family theorem. The proof relies on exhaustive, transparent enumeration and separately replayable programs; the output transcripts alone are not proof without inspecting the enumeration logic and actually executing it. Other polyhexes could have different connectivity thresholds. A wider or unindexed computational dataset might encode some or all of these values, and independent publication-priority review has not occurred. The current result gives no general formula for the diameter of resonance graphs or for the minimal cycle-length threshold of arbitrary toroidal graphs.

## References

1. D. Eppstein, "The many faces of the Nauru graph," 12 December 2007. https://11011110.github.io/blog/2007/12/12/many-faces-of.html
2. M. Bonamy, N. Bousquet, M. Heinrich, T. Ito, Y. Kobayashi, A. Mary, M. Mühlenthaler and K. Wasa, "The Perfect Matching Reconfiguration Problem," MFCS 2019, article 80, DOI: 10.4230/LIPIcs.MFCS.2019.80. https://arxiv.org/abs/1904.06184
3. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi and Y. Okamoto, "Shortest Reconfiguration of Perfect Matchings via Alternating Cycles," arXiv:1907.01700 (2019); SIAM J. Discrete Math. 36 (2022), 1102–1123. https://arxiv.org/abs/1907.01700
4. L. Liang and H. Zhang, "The resonance graphs of nanotubes and toroidal polyhexes," arXiv:2609.19766, 17 September 2026. https://arxiv.org/abs/2609.19766
