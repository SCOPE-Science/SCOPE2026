# Scientific review

## Correctness — PASS

The matrix identity \(\mathcal E(\omega)=\det(A^\top A)\|\omega\|_2^2/(\omega^\top A^\top A\omega)\) follows samplewise by a two-by-two Cayley–Hamilton calculation. Isotropic Gaussian directions yield an explicit convergent circle integral, while the four Rademacher vectors collapse to two Rayleigh denominators, making the orientation bounds and equality cases exact. The crossover and its angular measure follow from a strictly monotone rational function. The independent expanded-projector verifier performed 7,904 exact-rational and 1,123 numerical checks, but the proof is analytic and exhaustive for the stated domain.

## Originality — PASS, qualified

The principal source [Saibaba–Międlar, arXiv:2308.05814, sections 2–3 and Appendix C] develops non-Gaussian matrix-sketch bounds and explicitly includes Rademacher probes, but Theorem 5 gives high-probability bounds under sample-size requirements rather than an exact one-probe orientation law. [Diouane et al., arXiv:2206.08793, section 4] considers Gaussian randomized SVD error bounds requiring more than two sketch columns, not the two-dimensional one-column equality. [Halko–Martinsson–Tropp, arXiv:0909.4061, sections 4 and 9–10] provides the underlying projection method and oversampled analysis. Relevant published mathematical records for adaptive randomized pivoting and random ellipsoid sections use different sampling objects and do not imply the signed-probe versus Gaussian range-projection law.

The comparison considered exact aliases, the two eigenvalues of the Gram matrix, and both squared residual and projection error formulations. There is no claim that keyword absence certifies novelty. An equivalent earlier specialized finite-dimensional derivation remains a priority risk; independent scientific priority validation is not performed.

## Value — PASS

For the same pair of singular values, the sign sketch's worst expected error grows as \(\kappa^2/2\) times optimal while its best expected error remains below twice optimal; Gaussian's factor is exactly \(\kappa\). The theorem identifies not merely a degenerate example but a sharp orientation-dependent selection frontier and the exact fraction of adverse orientations under random rotations. These facts make the small-sample comparison between two ubiquitous randomized range-finder probes mathematically consequential, without claiming general high-dimensional guarantees.

## Boundaries and closest literature

The theorem applies to the squared Frobenius norm, one sketch column, real matrices with two full-rank columns, and exact arithmetic. It is not a statement about the expected unsquared norm, other distributions, iterative power sketches, or arbitrary rank-two subspaces of many-column matrices. Literature: https://arxiv.org/html/2308.05814v1 ; https://arxiv.org/abs/2206.08793 ; https://arxiv.org/html/0909.4061v2 .

Self-review: passed. Independent audit: not yet performed.
