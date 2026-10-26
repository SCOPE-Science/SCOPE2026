# Scientific review: complete split-graph cycle projections

## Correctness
**PASS.** The claimed minimum is over *all* real-linear projections onto the cycle-flow space. Signed-coordinate permutation averaging is norm nonincreasing, and representation decomposition identifies the complete one-dimensional family of equivariant corrections. Each candidate is verified to fix every cycle and have cyclic image. Its two column-orbit sums are derived exactly from the Laplacian spectral decomposition, including all absolute values and boundary cases. The global minimizer follows from the opposing slopes for independent-set sizes one through three, and from the cross-column kink for sizes at least four. An exact-rational standard-library checker passed 56 parameter pairs, 1932 columns and 1754 idempotence entries; finite instances are corroboration, not an infinite proof.

## Originality
**PASS under currently accessible evidence, with bibliographic risk.** The closest primary predecessor, Dilworth--Kutzarova--Ostrovskii (arXiv:2305.12582; initial submission 2023-05-21), gives the general averaging framework and works out tori and Hamming graphs, but not the graph family and exact minimax theorem here. Nearby published research records concern cactus-basis suppression projections, clustered finite-metric fluctuation projections, and distinct bipartite-family calculations; their conclusions do not logically imply the split-graph saturation law. Searches under graph joins, complete split graphs, invariant cycle projections and the plateau value did not identify covering literature, but incomplete indexing can never prove novelty. The complete-graph boundary is acknowledged as known.

## Mathematical value
**PASS.** The invariant is the globally optimal relative projection norm in a natural two-parameter graph family, rather than the norm of a preselected operator. Its unexpectedly stable value after four independent vertices and its fixed positive separation from the canonical orthogonal norm disclose a structural optimization phenomenon. The sharp threshold and all-parameter closed formula make the result reusable as a benchmark for Banach-space graph quotients, without claiming consequences for unrelated graph classes.

## Residual limits
Only real, unweighted edge-\(\ell_1\) operators are treated; no general weighted or \(\ell_p\) analogue is established. A potentially equivalent unindexed minimal-projection argument cannot be excluded. The standard-library computations are not a substitute for the general proof.

Self-review: passed. Independent audit: not yet performed.
