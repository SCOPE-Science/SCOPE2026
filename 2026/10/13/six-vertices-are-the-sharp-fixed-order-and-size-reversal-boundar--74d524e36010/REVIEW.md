# Self-review

## Correctness
**PASS.** The domain is connected finite simple undirected graphs compared at common order and common edge count. The verifier reconstructs every connected isomorphism class through five vertices, reproduces the standard counts \(1,2,6,21\), and checks all same-\((n,m)\) pairs. Adjacency Perron roots and nonbacktracking roots are certified with exact rational polynomial arithmetic and Sturm isolation. The six-vertex graphs are reconstructed from their edge sets and satisfy the claimed opposite strict inequalities. The packaged verifier returns `VERIFY_OK`.

Risk: interpreting inverse spectral radii as epidemic thresholds requires the modeling assumptions stated in the limitations; the graph-spectral reversal itself is exact.

## Originality
**PASS.** Wang et al. establish the adjacency-eigenvalue epidemic-threshold viewpoint. Karrer et al. establish the nonbacktracking/message-passing percolation threshold and compare it with adjacency-based bounds. Lin and Zhou study inequalities and extremal behavior linking the two graph spectral radii. None of the inspected sources states the sharp fixed-order-and-size six-vertex ranking reversal, and targeted searches by aliases, fixed-edge formulations, and exact witness structure did not locate it.

Risk: an unindexed small-graph computation could contain the same pair without presenting the minimal boundary.

## Value
**PASS.** Adjacency and nonbacktracking spectra are both used to summarize spreading or percolation vulnerability, but they encode different walk structure. Fixing both vertex count and edge count isolates a genuinely structural disagreement rather than a density effect. The exact minimal witness therefore gives a compact diagnostic for when the two common spectral surrogates can lead to opposite network comparisons.

Self-review: passed. Independent audit: not yet performed.
