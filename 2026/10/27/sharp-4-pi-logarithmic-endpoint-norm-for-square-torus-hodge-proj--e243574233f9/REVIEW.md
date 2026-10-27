# Scientific review: square-torus endpoint Hodge norms

## Correctness — PASS

The claim is for all integers \(n\ge3\), real edge-\(\ell_1\)/\(\ell_\infty\) norms and the canonical Euclidean-orthogonal projections. Fourier diagonalization yields the two-component transfer-current kernel. Its infinite-lattice multiplier has a homogeneous order-zero singularity: the inverse Fourier transform has a second-angular-harmonic \(r^{-2}\) leading term and an absolutely summable \(O(r^{-3})\) error. Square-symmetric cancellation in a Gaussian-Abel periodization gives a uniform \(O(n^{-2})\) discrepancy between centered finite-torus and infinite-lattice coefficients. Summing \(n^2\) discrepancies costs only \(O(1)\); the lattice polar integral of the absolute angular modes has angular mass eight, giving \((4/\pi)\log n\). Trace and edge transitivity give the already-known exact complementary norm gap \(n^{-2}\). A separate standalone incidence-matrix computation checked all 172 edge columns for \(n=3,4,5,6\), and discrete Fourier computations gave additional confirmations for \(n=8,12,16,24,32\). These finite checks are corroboration, not an infinite proof.

## Originality — PASS, with specified literature uncertainty

The closest primary full text is Dilworth–Kutzarova–Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, especially Section 2.4.3, Proposition 27, the small-torus table and Question 32. Their exact cut/cycle trace relation is included only as a **known identity**, and their finite computations cannot imply the new leading constant. Their question explicitly seeks sharper large-torus asymptotics. Gurevich, *Asymptotics of the heat kernels on 2D lattices*, arXiv:1809.04850v1, treats lattice Green-function expansions, which give relevant kernel ingredients but not a finite-torus absolute-column-sum asymptotic with the sharp coefficient. Searches of graph Hodge kernels, discrete Helmholtz/Leray projections, transfer-current norms, Riesz transforms and related research records found no statement covering the asserted norm asymptotic. This is a bounded best-knowledge novelty judgment, not a worldwide uniqueness certificate.

## Mathematical value — PASS

The object is a standard two-dimensional discrete torus and a canonical Banach-space projection invariant, central to a published question about cycle projections. Identifying the exact coefficient rather than merely a logarithmic order reveals the angular contribution of the discrete two-dimensional Leray kernel; the bounded additive remainder is stronger than a leading-order equivalence. The result concerns orthogonal projection, and does **not** resolve the stronger optimization problem for arbitrary projections.

## Sources and residual risks

Primary: https://arxiv.org/abs/2305.12582, posted May 21, 2023. Supporting lattice analysis: https://arxiv.org/abs/1809.04850, posted September 13, 2018. Residual risk: an unindexed harmonic-analysis or transfer-current calculation may have this precise coefficient under different notation. The Gaussian-Abel periodization and kernel-remainder argument are the critical nontrivial proof steps requiring eventual independent inspection.

Self-review: passed. Independent audit: not yet performed.
