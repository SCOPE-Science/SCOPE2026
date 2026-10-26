# Review: Total-variation relaxation profile and Gaussian critical layer in nested stochastic resetting

## Correctness (PASS)
Published exact solution (Britton et al., 2026, eq. 2.10) gives Gaussian variance mixing with min(Gamma(n,r),t); equivalent Poisson-renewal expression is checked. The finite-n signed-density ratio is strictly decreasing in |y|, proving unique crossing. L1 concentration of Gamma(n,n) gives the closed TV normal-vs-normal profile. Gamma Chernoff gives postcritical exponential bound. CLT and UI, a uniform L1 bound on the second variance derivative of normal density for v>=1/2, and an exponentially small Gamma left tail yield the critical signed-L1 limit; the exact Gaussian derivative norm yields phi(1)[phi(s)-s(1-Phi(s))]. Replayed standalone program passed 84 deterministic numerical checks from the actual package path, including an independent finite-n Fourier integral identity. No finite computation is used to assert infinite-index proof.

## Originality (PASS)
The starting stochastic model, stationary law, exact transient density and local accumulation times are all credited to the 2025 and 2026 primary papers. Their inspected complete text does not state the global tagged-marginal total-variation profile, its \(n^{-1/2}\) critical window coefficient, or unique crossing theorem; actual published-finding corpus searches did not identify an equivalent claim. Unlike local accumulation times, the new profile takes a global L1 norm after scaling n and t together. The published formula implies the claimed results after additional analysis, so implicit broader coverage by Gaussian scale-mixture limit results is a material residual risk, not falsely excluded.

Closest inspected literature: Britton, Le Jeune, Alston, Bressloff and Bertrand (2026), arXiv:2609.25252, especially equation (2.10) and section 3; Alston, Britton and Bertrand (2025), arXiv:2502.03225; Bressloff (2021), arXiv:2104.09365. The formula supplying the Gaussian-Gamma clock is pre-existing. The distinction between existing local accumulation time and new full-distribution distance is a claim-to-prior implication comparison, not proof of universal novelty. Possible broader general variance-mixture coverage remains a risk.

## Value (PASS)
The physically natural question is how much of the tagged position law remains out of its nonequilibrium stationary distribution as depth n increases. The source provides local accumulation time but no quantitative global probability-metric profile. The exact F(theta) distinguishes substantial persistent precritical deviation from postcritical exponential convergence, while the critical coefficient quantifies finite-depth corrections at the wavefront. The single-crossing theorem provides an exact central-interval observational interpretation. These are nontrivial functional (TV) and critical-index statements rather than routine single-parameter substitution, although extension beyond this solvable model is not shown.

## Limitations
Only the tagged marginal is analyzed, not joint mixing. Equal Poisson rates, free Brownian evolution, all-zero initial data and fixed positive microscopic parameters are essential. Numerical verification is finite and not an infinite-index proof. Independently assessed correctness, value and novelty remain open.

Self-review: passed. Independent audit: not yet performed.
