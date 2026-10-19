# Scientific review of the exact exchange-graph classification

## Correctness — PASS

The direct synchronous infection enumeration and the independent subcube-closure enumeration return identical sorted seed-list SHA-256 digests, not just matching totals. The former enumerates all subsets below the minimum size to establish the finite minimum, then constructs every legal one-for-one exchange. The latter independently builds exchange relations and examines all full cube-isometry orbits. Each computes breadth-first shortest paths from a complete set of symmetry representatives and agrees on 144 and 16960 optimal seeds, both graphs' edge totals, connectivity, the jump diameter four, and the slide radii/diameters six/six and nine/eleven. Both recorded outputs were reproduced from the packaged source files. Residual correctness risk is normal computational implementation risk, mitigated by the independent methods and complete orbit coverage.

## Originality — PASS with publication-overlap risk

Balogh–Bollobás–Morris (arXiv:0907.3097) concerns random thresholds on grids; Morrison–Noel (arXiv:1506.04686) determines weak-saturation and minimum-size bounds; Kang–Missethan–Schmid (arXiv:2406.13341) uses internally spanned projections and sequentially spanning configurations for random thresholds. Their examined results do not imply exact edges or graph distances between fixed-size optimal seed sets. Searches for the competing terms minimum contagious/percolating/spanning sets, exchange graphs, token jumping, token sliding and bootstrap reconfiguration, as well as mathematical-record comparisons, yielded no covering reconfiguration result. The 2006 Balogh–Bollobás primary paper could be read bibliographically and by abstract only; its unexamined body, other unindexed literature and potential independent rediscoveries remain residual risks. This review does not establish exhaustive world literature priority.

## Value — PASS

The minimum seed budget addresses a standard irreversible threshold-spread problem. Whether an optimum placement can be repaired by moving one seed to a neighbouring cube site without losing percolation is an additional operational question not answered by minimum-cardinality bounds. The results give complete reachability and exact worst-case relocation costs. The transition from a self-centered slide graph in dimension four to a radius-nine/diameter-eleven graph with a single central orbit in dimension five is a structural metric distinction, not an arbitrary single-state count. The theorem is restricted to two small but nontrivial natural cubes, and no general-dimensional conclusion is implied.

Self-review: passed. Independent audit: not yet performed.
