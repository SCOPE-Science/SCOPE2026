# Mathematical audit — 2026-10-01

## Final claim

Unique Desargues-graph signing unfolding all base 6-cycles gives a 40-vertex bipartite cubic Ramanujan 2-lift of girth 8

## Correctness — PASS

PASS. The Desargues graph G(10,3) was rebuilt independently and its 20 base 6-cycles were enumerated. After fixing a spanning tree, the 20 odd-parity unfolding constraints on the 11 cotree sign variables have a unique solution over F2. For that signing, a fresh signed-adjacency computation gives characteristic polynomial x^8 (x^2-5)^6. The corresponding 40-vertex 2-lift has girth exactly 8; combining the inherited Desargues eigenvalues with new eigenvalues 0 and plus/minus sqrt(5) proves the cubic Ramanujan property. The audited cycle census also reproduces 60 eight-cycles.

## Originality — PASS

PASS. Bilu-Linial and Marcus-Spielman-Srivastava give general 2-lift spectral theory and existence of good Ramanujan lifts, while standard graph references give the Desargues spectrum and structure. Targeted searches did not locate this exact signing, the uniqueness statement under all-20-six-cycle unfolding, the signed characteristic polynomial, or this 40-vertex lift census. The general existence theorems do not determine this named finite lift.

## Scientific value — PASS

PASS. The Desargues graph is a canonical distance-regular cubic graph, and 2-lifts are a central construction in modern Ramanujan graph theory. Uniqueness of a signing simultaneously maximizing local girth by unfolding every base 6-cycle and meeting the Ramanujan spectral bound is a natural exact finite classification with reusable benchmark value.

## Sources inspected

- Y. Bilu, N. Linial, Lifts, discrepancy and nearly optimal spectral gap — https://doi.org/10.1007/s00493-006-0029-7: GENERAL_2_LIFT_FRAMEWORK. Primary abstract describing signed 2-lifts and their new eigenvalues.
- A. Marcus, D. Spielman, N. Srivastava, Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees — https://arxiv.org/abs/1304.4132: GENERAL_EXISTENCE_NOT_EXACT_LIFT. Primary abstract/theorem statement on existence of Ramanujan 2-lifts.
- Desargues graph reference data — https://www.math.mun.ca/distanceregular/graphs/desargues.html: BASE_GRAPH_REFERENCE. Standard graph entry giving 20 vertices, intersection array and spectrum.

## Residual risks

- No exhaustive search of every historical cubic-graph catalogue was possible; a graph isomorphic to the lift may occur under an unrelated name.
- The originality claim is specifically the signed-cover characterization and uniqueness under the stated base-cycle constraints, not that 40-vertex cubic girth-8 graphs in general are new.

## Disposition

**passed**
