# Self-review

## Correctness — PASS

The Pappus incidence model is explicit and complete: the nine point and nine line vertices are given as finite coordinate lists with the three exact incidence equations. Every perfect matching corresponds uniquely to a nine-point bijection, and the recurrence for partial assignments reaches exactly 42. For two matchings the cycle structure of the relative permutation determines precisely whether their symmetric difference is one six- or eight-cycle, ruling out accidental union-of-cycles edges. All 861 unordered state pairs are checked, all adjacency components are traversed, and breadth-first search is run from every state. The six-cycle components' explicit three-hub/three-hexagon structure is verified vertex by vertex, not inferred from a degree sequence. A second independent Hamiltonian LCF construction verifies isomorphism and all graph and distance counts. Both supplied programs ran successfully. No infinite extrapolation is made.

## Originality — PASS, with identified risks

A targeted comparison looked for the same 42 matching states, hexagon/octagon flipping, parity sectors, stronger bounded-length connectivity theorems, and equivalent toroidal-honeycomb terminology. Lei–Yeh–Zhang (2014) is about anti-forcing and planar alternating-cycle packings, not flip graph connectivity for the nonplanar Pappus graph; Dyer–Jerrum–Müller (2015) uses only four-cycle switches, which cannot occur here. Bau–Henning (2003) concerns plane cubic bipartite graphs. Ito et al. (2019) treats unrestricted alternating-cycle reachability and complexity, which does not settle the sharp cutoff or explicit state-graph geometry. Published mathematical research records on Pappus matching complexes concern homotopy rather than matching swaps. Earlier exact hexagon/octic flip studies on different cubic graphs do not imply the Pappus result. No covering theorem or exact table was located. An equivalent calculation in unindexed or not fully accessible work remains possible, particularly under the toroidal-dimer name.

## Value — PASS

The bounded alternating-cycle flip length is an intrinsic question in perfect-matching reconfiguration, rather than an arbitrary numerical slice. The theorem identifies the *first* cycle size that permits movement across every matching, explains the shorter-cycle obstruction by a parity invariant, and classifies both obstructed sectors as a concrete 21-vertex graph. The sharp threshold, local structure and exact geodesic profiles together give a complete model of the smallest natural exchanges for a canonical cubic bipartite graph. The contribution is not predicated on priority for the raw perfect-matching count or a generic parity observation.

## Limitations and closest literature

The theorem is finite and graph-specific; no mixing-time or asymptotic property is claimed. An inaccessible full text from Bau–Henning (2003) remains a limited historical comparison risk, although its planar hypothesis excludes the Pappus graph. Pappus toroidal dimer literature and alternative exchange conventions could contain an equivalent graph. The full breadth-first-search certificates are reproducible but have not been independently audited by an external scholar.

Self-review: passed. Independent audit: not yet performed.
