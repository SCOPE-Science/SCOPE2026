# Review of the three-row perfect-matching boundary comparison

## Correctness — PASS

All eight graph instances are defined by explicit vertex and edge lists. An exhaustive perfect-matching recursion, followed by downward closure, gives the complete face set. Every face is used at most once in an explicitly specified codimension-one toggle matching. The actual matched Hasse graph was independently oriented and subjected to a complete topological sort: all 1,161,740 faces across the eight cases were visited, with no directed cycle. Critical cells are absent for both two-column cases, occur only in degree one with ranks 1 and 3 for four columns, only in degree two with ranks 1 and 3 for six columns, and only in degree three with ranks 2 and 12 for eight columns. The empty face is paired in every case. Discrete Morse theory therefore gives the claimed CW homotopy types, not just rational Betti numbers. No infinite-length generalization is inferred.

## Originality — PASS against inspected evidence

The closest publicly available source, Chandrakar–Singh, arXiv:2407.05809, proves the two-row open-grid result and states a broader rectangular-grid wedge conjecture. Its complete theorem descriptions and polygonal-tiling sections do not include the eight-column, three-row comparison or its periodic transverse closure. Bayer–Jelić Milutinović–Vega, arXiv:2209.02803, concerns hexagonal honeycomb graphs; Agarwal–Basak, arXiv:2608.30601, concerns cubic Möbius ladders. Neither family is isomorphic to the eight-column triangular cylinder. Existing calculations of narrower or shorter graph instances cannot imply the new exact third-homology rank jump. A mathematical search does not establish global uniqueness, and independently unindexed or unpublished computations remain a residual risk.

## Value — PASS

The comparison makes the role of boundary conditions quantitative in the simplest three-row rectangular strip and its nonbipartite triangular-cylinder closure. The first three nontrivial heights exhibit open-versus-periodic wedge ranks \((1,3)\), \((1,3)\), and \((2,12)\), making the eight-column case the first verified failure of constant rank amplification within the natural cutoff. The exact integral homotopy types answer a finite case of a published square-grid conjecture and provide concrete benchmark instances for boundary-sensitive discrete Morse constructions. This is not merely a recalculation of a known table or a claim about all lengths.

## Limits and literature risk

All proofs are finite exact calculations and rely on the standard discrete Morse theorem. No universal recurrence or classification for larger lengths is claimed. The nearest papers were inspected in their readable preprint texts; additional equivalent calculations could exist in less accessible literature. Independent validation remains open.

Self-review: passed. Independent audit: not yet performed.
