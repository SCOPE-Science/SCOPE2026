# Scientific review: four-cube Hamiltonian-path face switching

## Correctness — PASS

Both exhaustive implementations independently enumerate all 45,696 unoriented spanning paths in the labelled four-cube using different search normalizations. Every face switch is enumerated by toggling the four edges of each coordinate square and testing membership in the full path set. Both recompute 69,120 edges, 5,184 isolated vertices, 32 components of size 528 and 32 of size 738, and the exact nine-class degree census. Parity implies all endpoints lie in opposite cube bipartitions, so only distance one or three occurs. The primary implementation further partitions every configuration by endpoints, yielding the 672/756 and 144/18 fiber counts. Exhaustive proof scope is finite Q4 alone.

## Originality — PASS, with residual risk

Searching both 'Hamiltonian paths in Q4 face-switch' and alternate 'hypercube square-flip reconfiguration' formulations did not identify a covering finite theorem. The closest indexed research record treats four-cube Hamilton-path quadratic phases, not a face-switch adjacency. Earlier local literature on hypercube Hamiltonian cycles, matching-switch graphs, Hamiltonian reconfiguration generally, and rectangular-grid switching does not imply this strict endpoint-fiber census: those studies have different objects, use different moves, or only state counting/complexity. A complete exhaustive search of unpublished material is impossible. Takaoka's full text could not be retrieved owing to rate-limiting; its abstract does not claim this classification. Caution: unindexed computations may cover these small finite quantities.

## Value — PASS

Endpoint-preserving local switches are natural in Hamiltonian-path rerouting and cyclic Gray-code constructions. The sharp obstruction is structural and non-obvious: there is exactly one large connected mobile class *per pair of endpoints* but also isolated paths in every fiber, and the frozen count differs by factor eight between endpoint separations one and three. This is a complete finite cutoff for a canonical four-dimensional Boolean graph, not an arbitrary chosen statistic or mere count of Hamiltonian paths.

Self-review: passed. Independent audit: not yet performed.
