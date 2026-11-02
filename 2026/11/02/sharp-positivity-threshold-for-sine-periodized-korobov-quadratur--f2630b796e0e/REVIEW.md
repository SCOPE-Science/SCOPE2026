# Self-review

## Correctness — PASS

The analytic proof fixes the exact periodic RKHS normalization, derives the unique minimal-norm spline on each cell, and recovers the original kernel cubature weights from its integral. The common correction has a strict monotone parameter dependence. The folded circle-convolution comparison identifies the minimum hat integral for all grid sizes, while Fourier expansions evaluate the bubble integral in both parity cases. This yields necessity, sufficiency, attained threshold and two-term asymptotics; finite independent-formula Gram checks supplement but do not prove the general result.

## Originality — PASS (subject to historical-priority uncertainty)

The 2026 Bartel–Gilbert–Griebel–Kuo–Sloan source establishes the method, kernel, density and optimal weight formula but does not give the necessary-and-sufficient univariate parameter interval. Oettershagen (2017) supplies the general minimal-spline/optimal-cubature framework, and its Section 6.1 considers periodic Sobolev spaces under uniform Lebesgue integration, not this sine-weighted gamma threshold. Sloan–Smith (1982) concerns polynomial product-integration asymptotic positivity rather than this periodic RKHS kernel. Searches for direct sine-density, periodic Sobolev, spline and gamma-threshold aliases found no equivalent formulation; absence from search is not a proof of novelty. The full text of Sloan–Smith was not available for direct inspection, and historical sources could conceivably dominate the claim.

## Mathematical value — PASS

The work settles a natural sign-stability design question for a recent unequal-weight quadrature method: exact positive weights for nonnegative inputs cannot be presumed from the positive density. The result is an all-size, all-parameter classification, not a numerical tabulation. The \(\gamma_N=N+\pi^2/3+O(N^{-1})\) law distinguishes fixed-parameter asymptotic positivity from growing-parameter sign failure. It does not transfer to multivariate or subsampled lattices and is not a floating-point backward-stability theorem.

Self-review: passed. Independent audit: not yet performed.
