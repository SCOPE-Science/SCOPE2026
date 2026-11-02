# Scientific review: five-cube perfect-matching square switches

## Correctness — PASS

The state encoding bijects admissible sixteen-partner assignments with perfect matchings, and exhaustive recursion visits each exactly once. The swap predicate is equivalent to an alternating four-cycle; an independent edge-bitset implementation tests the eighty actual squares. The two implementations agree on all 589,185 states, 3,219,360 flip edges, 202 components and their orders; the independent implementation checks all 3,840 cube automorphisms for the stated orbit assertions. Connectivity is computed by exact disjoint-set closure, not guessed from sampling. The four-cycle type is justified by checked degree two at every vertex of each size-four component. Bipartiteness is proved by permutation-sign alternation.

## Originality — PASS (qualified)

The perfect-matching count was established by earlier authors and is excluded from the proposed novelty. General four-cycle flip reconfiguration was studied by Bonamy et al. (2019); their inspected treatment concerns computational complexity and certain graph classes, not the exact five-cube component census. The highly relevant full papers of Klivans–Saldanha (2022) and Hartarsky–Lichev–Toninelli (2023/2024) describe dimension-four examples, twist/stabilization, and ergodicity with longer alternating cycles, rather than the fixed five-cube square-only component census. Östergård and Pettersson (published online in 2012) discuss static counts and symmetry orbits; only metadata and abstract were accessible, so an equivalent result elsewhere in their full text cannot be ruled out. Results for four-cubes and for unrestricted alternating-cycle flips do not imply the square-only five-cube component split. Comparisons and residual risks are detailed in the structured review.

## Value — PASS

The five-cube is a natural first substantially larger case after four-cube computations. An exact decomposition into 120 frozen configurations, 80 four-state motion cycles and two large disconnected motion sectors distinguishes static enumeration from actual reconfiguration accessibility. In particular, a sampler restricted to local square switches is provably not irreducible. The orbit statements reveal that small exceptional components are systematic rather than arbitrary isolated examples. This is a natural exact finite connectivity benchmark, not a parameter chosen only for computation.

## Limits and sources

The two large connected graphs are not classified beyond their orders and edge totals, and no higher-dimensional formula or full literature uniqueness proof is asserted. Sources: Graham–Harary (1988); Östergård–Pettersson (2012/2013), DOI `10.1007/s11083-012-9279-8`; Bonamy et al. (2019), DOI `10.4230/LIPIcs.MFCS.2019.80`; Mütze's combinatorial Gray-code survey, matching section; Klivans–Saldanha, DOI `10.5802/alco.205`; Hartarsky–Lichev–Toninelli, `arXiv:2304.10930`; Fink, DOI `10.1137/070697288`. Relevant primary full text was consulted where open access allowed; the 2012 article remained inaccessible in full.

Self-review: passed. Independent audit: not yet performed.
