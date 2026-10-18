# Scientific review: parity-complete Pappus edge-Kempe reconfiguration

## Correctness — PASS

The graph is precisely specified as the incidence graph of the nine points and nine nonvertical affine lines over \(\mathbb F_3\), and a concrete vertex bijection is verified against the standard Pappus LCF graph. A proper coloring modulo three color names is exactly an unordered triple of disjoint perfect matchings covering all 27 edges. An exhaustive nine-point matching recurrence generates exactly 42 matchings and 20 factorization triples. Cycling over all three pairs of color classes and over every connected two-colored cycle generates all 36 nontrivial switches, with no omitted move type. The complete adjacency list has two ten-state components, each a hub joined to three vertex-disjoint triangles; its signs distinguish the components. A separately written C++ program enumerates all 120 *labeled* edge-colorings without using the matching recurrence and reproduces the entire classification. The sign obstruction follows analytically because a switch on a \(2k\)-cycle multiplies both involved matching-permutation signs by \((-1)^{k-1}\).

The finite calculation proves exactly a finite configuration, not an infinite extension. The package contains both standalone programs and a complete 20-state, 36-edge certificate; the certificate is recomputed from the source-defined graph before acceptance. No computations, certificates or dependencies are drawn from a different configuration.

## Originality — PASS, with historical-priority risk

Belcastro–Haas (2012/2014, arXiv:1209.1730) introduced the relevant equivalence framework and studied its class counts; their inspected full text contains no Pappus-specific complete switching graph. Goedgebeur–Östergård (2021/2022, arXiv:2105.01363) give the exhaustive algorithm and aggregate census through this order, so the *number* of edge-Kempe classes is not asserted as novel. Their inspected article does not give the precise Pappus twenty-state adjacency, parity completeness, two-switch diameter, or windmill decomposition. Their public dataset and code may allow reconstruction and should be considered a priority risk. Dejter (arXiv:2102.06956) treats a distinct tight-coloring invariant and Pappus prisms, not the base graph's move graph.

Own earlier claims on the Pappus graph concern domination and resolving sets, and an earlier Möbius–Kantor switching claim has a different graph and nonisomorphic reconfiguration components; none implies this theorem. Direct published-finding corpus and literature searches under Pappus, switching, Tait/three-edge coloring, one-factorization, parity and windmill terminology found no stronger statement covering the exact theorem. Search absence is not independent proof of priority. The residual risk is an unindexed earlier tabulation or a derived supplementary computation, especially from the 2021 census software.

## Value — PASS

The question concerns an intrinsic reconfiguration graph on the full set of Tait colorings of a classical symmetric cubic bipartite graph. Beyond the aggregate class count, the theorem identifies an exact *if and only if* accessibility invariant: matching-sign parity is sufficient as well as necessary. Every reachable pair has a two-switch path, and each parity component consists of three tetrahedra sharing a vertex. This gives a complete finite state-space geometry and exact shortest-switch diameter for a meaningful named configuration. The claim is not merely a renaming of a classical graph parameter or a marginal improvement of a known bound. No general theorem about all cubic graphs is claimed; historical novelty is not independently certified.

Self-review: passed. Independent audit: not yet performed.
