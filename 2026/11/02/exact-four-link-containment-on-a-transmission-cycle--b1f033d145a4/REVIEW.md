# Scientific review

## Correctness

PASS. For distinct arcs, the two edge-disjoint transmission routes produce connection probability \(q^d+q^{4-d}-q^4\); uniform initial seeding turns its pairwise connectivity sum into the mean final outbreak. The displayed four-by-four circulant matrix has eigenvalues \(\lambda_0\), twice \(\lambda_1\), and \(\lambda_2\) as stated. The exact identity \(\lambda_1-\lambda_2=2q(1-q)^2>0\) resolves the only competing parity minima. Positive integer arc sizes and all four residues of \(n\) are accounted for. Direct independent sixteen-state rational checks and a complete finite optimizer comparison reproduce the formulas. A finite checker alone cannot establish universal correctness; the given general algebraic proof does.

## Originality

PASS provisionally against the inspected accessible sources. The closest underlying stochastic models are Deijfen's weighted Reed–Frost epidemic on configuration-model graphs [1] and Mann et al.'s formula for homogeneous cyclic percolation motifs [3]. Neither inspected work gives the arrangement minimizer for four designated equal-probability imperfect edges in an otherwise certain finite cycle. Russo et al. [2] motivates the spatial intervention question but treats heterogeneous wildfire simulation and network centrality. Published mathematical-result searches for edge placement, susceptibility, inhomogeneous percolation, and cyclic four-gap arrangements did not identify an equivalent risk optimizer. A superficially similar cyclic four-frequency sampling theorem optimizes a Fourier determinant, not epidemic connectivity risk, and neither statement implies the other without an unestablished rearrangement reduction. Priority remains provisional in view of the general network-reliability literature; absence in search results is not proof of originality.

## Value

PASS. A complete parameter-wide optimizer for the uniform-seed mean outbreak supplies an interpretable benchmark for stochastic intervention-placement algorithms. Exactly four barriers are the first cyclic barrier count for which two longer balanced gaps can be adjacent or opposite in genuinely inequivalent ways; three barriers cannot distinguish those patterns up to rotation and reflection. The strict gap \(2q(1-q)^2/n\) shows that a nonzero barrier failure probability resolves an otherwise degenerate layout choice. This is a natural exact classification and not a numerical demonstration for selected parameter values. Its applicability is limited by the one-dimensional perfect-intra-arc transmission idealization.

## References and residual risk

[1] Deijfen (2011), arXiv:1101.4154v1. [2] Russo et al. (2015), arXiv:1509.04065v1. [3] Mann et al. (2021), arXiv:2102.09261v1. The candidate remains vulnerable to a stronger general rearrangement theorem on edge-weighted ring susceptibility; no assertion of exhaustive literature access is made. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
