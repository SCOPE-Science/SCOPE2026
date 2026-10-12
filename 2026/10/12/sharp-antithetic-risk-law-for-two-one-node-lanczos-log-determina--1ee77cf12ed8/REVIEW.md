# Review of the two-scalar-one-node log-determinant risk theorem

## Correctness — PASS

The relevant Lanczos operation is specified exactly: one unit-vector Rayleigh quotient per independent scalar Krylov construction. Diagonalization of a \(2\times2\) positive-definite matrix yields an elementary angular factorization; an absolutely uniformly convergent Fourier series gives the common bias and both dilogarithm variance identities. Complementary beta-distributed eigenbasis weights realize the strictly countermonotone minimizing coupling, justified by the exchange form of the rearrangement inequality. The Rayleigh-product identity independently gives the exact transformed-arcsine error distribution, including endpoints. Taylor series give both small-contrast error orders. Exact arithmetic and numerical quadrature supplement but do not replace the infinite proof.

## Originality — PASS, subject to residual priority risk

The 2022 Chen–Trogdon–Ubaru study (arXiv:2204.01941) constructs randomized quadrature by averaging independent probes and supplies general spectral-sum analysis; the 2021 Chen–Trogdon–Ubaru work (arXiv:2105.06595) treats spherical-probe spectral approximation. Neither inspected result establishes the fixed-two-probe Haar-coupling minimum together with the exact nonlinear one-node log-determinant error law. The 2025 Yeon–Ghosal–Anitescu BOLT analysis (arXiv:2505.12289) instead uses joint block Lanczos or exact \(v^{\mathsf T}f(A)v\) trace moments. In dimension two a full block can evaluate \(\log\det A\) exactly; that fact restricts the scope and utility but does not imply the present scalar one-node formulas. The comparison also considered Han–Li–Huang–Zhu (arXiv:2307.02152), whose accessible projection-cost-preserving and concentration analysis does not state this two-dimensional optimal coupling. Searches for antithetic probes, equivalent logarithmic Rayleigh quotients, beta/angular laws, and dilogarithm variance expressions did not identify a dominating theorem. Failure to locate a result is not proof of global priority, and specialized unindexed work remains a risk.

## Value — PASS

When two low-cost scalar one-node quadratures are mandated, iid directions exhibit a leading \(\Theta((\log\kappa)^2)\) mean-squared risk near equal eigenvalues, while an optimal antithetic pair has \(\Theta((\log\kappa)^4)\) risk. This eliminates first-order stochastic sampling error but leaves a precisely quantified positive quadrature bias. The exact law is a reusable benchmark for correlated-probe design and separates sampling variance from nonlinear quadrature truncation. No claim is made that this beats full-block, two-step, or explicitly available-matrix computations in dimension two.

## Boundaries and further validation

The result is confined to real two-dimensional matrices with strictly positive and unequal eigenvalues, Haar-uniform marginal directions, exact arithmetic, and the sum of two separately evaluated one-node scalar Lanczos quadratures. No larger-dimensional or floating-point robustness theorem is asserted. Independent review and exhaustive priority verification have not occurred.

Self-review: passed. Independent audit: not yet performed.
