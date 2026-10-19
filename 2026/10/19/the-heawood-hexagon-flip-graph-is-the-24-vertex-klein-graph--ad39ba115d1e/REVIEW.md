# Scientific review: Heawood hexagon-flip graph and Klein identification

## Correctness — PASS
The claim is exact and finite. The cyclic Fano-line verifier tests all \(5040\) permutations, enumerates all \(28\) six-cycles, reconstructs all \(84\) legal flips on the \(24\) perfect matchings, and validates a specified bijection against **every** entry of an independently published \(24\)-by-\(24\) Klein adjacency matrix. The verifier checks all rooted distances, intersection numbers, shared-edge counts and eight antipodal triple classes. A second independent binary-incidence and partner-rotation implementation obtains the same full classification, without using the external matrix or the cyclic incidence description. There is no untested quantifier over larger graphs: only the stated finite Heawood graph is asserted. The programs and their inputs/outputs are included, all code checks were reproduced. The external matrix must be interpreted as the 24-vertex Klein graph, not the 56-vertex cubic graph.

## Originality — PASS, with residual historical-priority risk
Dejter's *From the Coxeter graph to the Klein graph* (arXiv:1002.1960, 2010) derives Klein graphs from a geometric construction that uses the Heawood hexagons; examination of its full text found no statement about perfect-matching vertices and their *six-cycle flips*, nor the required explicit adjacency equivalence. The published Heawood graph table gives \(24\) perfect matchings and eight perfect three-edge-colourings, but does not identify the graph of all \(84\) hexagon flips with Klein's graph, establish the distance function, or prove the antipodal triple-cover interpretation. The distance-regular graph reference gives the already known Klein adjacency matrix and parameters, but is not a matching-reconfiguration classification. General perfect-matching switching papers typically permit other alternating cycles or concentrate on length-four switches; the operation and graph are different.

Related embedding-specific analyses of Heawood hexagonal resonance may enumerate some or all of the same switches; merely knowing the 84 edges or their decomposition into embedding-restricted subgraphs does not determine their global adjacency-isomorphism type. The new claim therefore rests on the explicit, checked 24-vertex Klein isomorphism and exact distances, not the already known counts \(24\), \(28\), or \(84\). A published equivalent could remain unindexed, and the complete historical record has not been verified.

## Value — PASS
This is an identification between two distinguished and mathematically motivated configurations: six-cycle moves on the minimum incidence graph of a projective plane, and a classical exceptional distance-regular Klein graph. The explicit graph isomorphism explains the non-obvious intersection array, gives an optimal flip-distance formula for every matching pair, and supplies a threefold antipodal covering interpretation of the eight one-factorizations. These structural links are more informative than a count-only table or an arbitrary small-graph invariant.

## Key sources and limits
- I. J. Dejter, *From the Coxeter graph to the Klein graph*, https://arxiv.org/abs/1002.1960 ; source first posted 9 February 2010. Inspected complete open preprint; no full-graph perfect-matching flip statement found.
- Heawood graph reference table: https://jaanos.github.io/tables/graphs/Heawood.html ; known 24 matchings and eight factorizations.
- Memorial University 24-vertex Klein graph table: https://www.math.mun.ca/distanceregular/graphs/klein.html and full adjacency https://www.math.mun.ca/distanceregular/graphdata/klein.am .
- General constrained reconfiguration literature includes Dyer, Jerrum and Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725. Its 4-cycle-switch setup does not cover the Heawood hexagon-flip graph.

Residual scientific risks: incomplete worldwide indexing, possible equivalent formulation hidden in graph-transformation or map literature, and reliance on the referenced matrix as the standard Klein labelling. These risks are documented, not asserted eliminated.

Self-review: passed. Independent audit: not yet performed.
