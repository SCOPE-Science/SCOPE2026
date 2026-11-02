# Self-review

## Correctness — PASS

The finite-dimensional diffusion with independent replacement jumps is contractive and admits a unique stationary state with finite second moments. Direct generator calculations for centered squares and distinct-coordinate products give a two-equation linear system with a strictly positive denominator. Conditional linear regression supplies the exact lagged covariance matrix, and elementary matrix spectral limits give the coupling–population scaling and the microscopic lag boundary layer. Independent exact-rational generator calculations cover 512 parameter tuples; the standalone checker also tests the lag and scaling formulas (531 total). The proof, not finite testing, establishes the all-size theorem.

## Originality — PASS (qualified)

The motivating 2024 paper establishes the local-reset Curie–Weiss model and its infinite-population stationary mean, while its explicit persistent correlations arise under *global* simultaneous resetting. The present claim instead gives the finite-population stationary off-diagonal and lagged covariance under genuinely independent local resetting, extends the replacement law beyond deterministic sites, and identifies a size-dependent coupling threshold and two-timescale boundary layer. An earlier review concerns different many-particle reset models, while exact one-particle moments under distributed resets do not determine interacting-particle correlations. Targeted searches disclosed no identical finite-\(N\) correlation formula plus crossover. General linear jump-process covariance theory might implicitly cover pieces, and the full literature has not been exhaustively classified.

## Mathematical value — PASS

The natural distinction between independent local resets and shared global resets motivates asking which finite-population correlations survive as normalized fluctuations. The exact model-independent Pearson law characterizes the critical coupling-to-size ratio rather than merely presenting a sample parameter value, and the time-lag formula separates macroscopic and microscopic relaxation. The finding is mathematically meaningful even though it is obtained from a closed second-moment system: it gives a sharp all-size criterion, universal under arbitrary finite-variance reset-location laws. It does not assert nonzero unscaled correlations or failure of weak propagation of chaos.

## Closest literature and limitations

Bressloff (arXiv:2401.03501v1): the exact local model and mean-field mean; global resetting correlations are a different stochastic mechanism. Nagar–Gupta (arXiv:2305.16955): review of related local/global models. Olsen (Phys. Rev. E 108, 044120): one-particle distributed-reset moments, not off-diagonal interacting correlations. Residual risks are generic affine jump-diffusion covariance results and uncatalogued finite-particle applications; the result is limited to positive harmonic confinement, symmetric attractive coupling, independent Poisson clocks and finite-variance replacement laws.

Self-review: passed. Independent audit: not yet performed.
