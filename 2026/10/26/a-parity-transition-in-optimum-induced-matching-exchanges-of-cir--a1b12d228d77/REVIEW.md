# Self-review

## Correctness

**PASS.** The proof uses the universal two-column capacity bound to derive the sharp maximum induced-matching cardinality. In the equality cases, the column occupancies force all possible rung-only or alternating rail-and-rung patterns. The odd-order two-unit-defect argument gives an exhaustive parametrization; exact comparison of rail/rung edge sets gives every exchange edge, degree and component. The standalone verifier uses an independent maximum-independent-set search and confirms all complete configuration and adjacency families for every order from 4 through 19, without treating finite trials as infinite proof.

## Originality

**PASS, with residual literature risk.** Cameron–Sritharan–Tang (2003) address weakly chordal graph algorithms, Dabrowski–Demange–Lozin (2013) address complexity and hypercube strong matching sizes, and Joos (2014) proves general maximum-degree lower bounds. Nakahata (2025) supplies a component-reconfiguration framework with separate restricted-class results. Comparison of their accessible mathematical text reveals no exact theorem for maximum induced-matching edge exchanges of the circular prism. Previously available exact prism strong chromatic indices concern edge partitions, not the optimum matching exchange graph. Searches for the aliases strong matching, 2-separated matching and maximum stable sets of squared line graphs identified no covering result. The complete absence of a prior equivalent theorem has not been certified, particularly for unindexed ladder literature.

## Value

**PASS.** The exact parity-dependent transition from frozen to connected optimal edge packings, including the complete irregular odd-degree spectrum and constructive reconfiguration routes, is a structural problem about the geometry of optimal choices, not a routine reformulation of the strong matching size. The result is an infinite-family classification with a natural combinatorial explanation via local column-capacity defects.

## Limits and closest sources

The theorem is for labeled simple prisms with at least four columns and exchanges of one entire edge; it does not address the triangular prism, token motion of endpoints, or nonmaximum matchings. Source details: Cameron–Sritharan–Tang, Discrete Mathematics 266 (2003), DOI `10.1016/S0012-365X(02)00803-8`; Dabrowski–Demange–Lozin, Theoretical Computer Science 478 (2013), DOI `10.1016/j.tcs.2013.01.027`; Joos, arXiv:`1406.2440`; Nakahata, arXiv:`2505.07268`. The closest alternative formulation—maximum stable sets in the square of the line graph—remains a possible unindexed prior-literature route.

Self-review: passed. Independent audit: not yet performed.
