# Review: Sharp endpoint Hodge stability on anisotropically weighted Boolean cubes

## Correctness — PASS

The definition uses \(P=D^{1/2}B(B^{\mathsf T}DB)^+B^{\mathsf T}D^{1/2}\). Walsh diagonalization gives the exact matrix coefficients, and a positive Laplace integral proves every parallel-edge entry is positive and every transverse-edge sign is determined by \((-1)^{z_j+x_i}\). Summing the absolute matrix entries direction by direction yields row masses \(1\) and \(\sqrt{c_ic_j}/(c_i+c_j)\); maximizing row sums proves the sharp norm. The universal interval and equality cases follow from a strict arithmetic--geometric mean bound and continuous geometric weighting. A grounded-Laplacian exact-rational checker passed 31,006 assertions in twelve cases, independently of the Walsh expression; the proof, not finite checks, establishes all positive real weights and dimensions.

## Originality — PASS within examined evidence

The weighted Hodge/transfer-current representation itself is classical, notably in Jiang et al. and Kassel--Wu. The significant comparison is not the operator's name but whether their formulas imply the exact signed row-mass separation and anisotropic sharp stability range without a fresh cube-specific computation. The inspected general sources do not supply those conclusions. Full published published-finding corpus results on Hamming Lipschitz-free Walsh projections, cactus basis coordinate projections, \(Q_3\) edge fourth moments and cyclic Riesz transforms were compared by their operator domains and targets; none covers this theorem. Bernardi's weighted cube spanning-tree enumeration is related geometry, but not an edge-space norm calculation. A prior equivalent product-electrical-network representation may exist outside the examined texts. Independent literature-priority verification has not occurred.

## Value — PASS

Energy-minimizing graph gradient projection is norm-one in its Hilbert geometry, yet bounded coordinate errors can be amplified by as much as \((d+1)/2\). The theorem exactly resolves a natural noise-amplification invariant on all anisotropically weighted Boolean cubes, shows every directional contribution is a simple harmonic pair weight, and classifies both the maximizers and the complete attainable range. Unlike a routine graph-matrix computation, it discovers rigid sign structure explaining why complete absolute row sums simplify at arbitrary dimension.

## Limitations and closest literature

The conductance must be constant across all edges in the same coordinate direction. The complete range does not apply to arbitrary graph weights, to an unnormalized edge representation or to projections other than the stated Hilbert-orthogonal map. Jiang et al., arXiv:0811.1067, and Kassel--Wu, arXiv:1312.2946, are the closest foundational operator sources. Bernardi, arXiv:1207.0896, is the closest older direction-weighted hypercube study examined. A pre-existing equivalent norm identity under Green's-function terminology remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
