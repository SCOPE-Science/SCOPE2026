# Review: Petersen transportation-ball facet symmetry classification

## Correctness — PASS

The polar Lipschitz ball has a vertex exactly when tight edges connect all ten vertices; active-edge rank proves both directions. A connected tight spanning tree forces integer coordinate differences; diameter two bounds the normalized levels by zero, one and two. Each tight graph is the complete crossing-edge cut of the parity bipartition and is a maximal connected spanning bipartite subgraph. The full symmetry is the 120-element group induced by all five-point permutations, as the five four-vertex independent stars distinguish all automorphisms. The standard-library `verify.py` independently exhausts 511 cuts and all 32768 edge subsets, then all 59049 ternary potentials and the complete symmetry actions. It confirms the 135 tight masks, their five orbits and exact fibers, the 1410 facets and eighteen orbits, disjointness, completeness, Burnside sums, representatives, and histograms. The finite certificate is exhaustive and rerunnable, not a sample or an infinite-proof surrogate.

## Originality — PASS, with residual bibliographic risk

The core prior facet criterion is in Higashitani–Jochemko–Michałek (arXiv:1807.07678) and the maximal-bipartite formulation in Chen–Davis–Korchevskaia (arXiv:2107.12315). Braun–Bruegge (arXiv:2201.13303) treat other sparse graph families; D’Alì–Delucchi–Michałek (arXiv:1910.05193) give broader symmetric-edge-polytope context. The closest Petersen-specific public result, “Exact inradius and contact-facet rigidity of the Petersen symmetric edge polytope” (public record af8a32ec1f59), ALREADY states the aggregate 1410 facets and computes thirty nearest facets. Its full result text was compared. **Neither the total 1410 nor the thirty nearest facets is claimed new**. The new claim is the exact 135 maximal tight subgraphs with five orbits and fiber sizes, together with all eighteen facet orbits. Targeted record and literature searches did not find equivalent or dominating coverage; incomplete code-search results are not evidence of absence. Relevant primary PDFs were materially inspected in their pertinent theorem sections and the closest public Petersen result was read in full. An unindexed equivalent census remains possible.

## Value — PASS

The Petersen graph is a canonical highly symmetric metric, and its transportation unit ball is a natural nine-dimensional Banach polytope. Knowing 1410 facets does not determine their geometry. The sharp 135-subgraph, five-type and eighteen-facet-orbit classification reveals differing fiber multiplicities and tight-edge spectra, an exact substantive combinatorial invariant useful as a benchmark. No all-graph generalization is claimed, and the work does not resolve the full face lattice. Correctness and novelty alone are not the value rationale; the nontrivial natural complete classification is.

## Limitations and risk

The exhaustive certificate covers only the real Petersen metric, with automorphism and sign acting as specified; outside datasets can contain equivalent orbit tables. Finite computation is accompanied by its completeness proof and all code. The self-review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
