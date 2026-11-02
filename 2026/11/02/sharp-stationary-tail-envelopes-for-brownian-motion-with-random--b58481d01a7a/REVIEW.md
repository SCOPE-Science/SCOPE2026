# Assessment of the stationary extreme-tail envelope

## Correctness — PASS

The stationary innovation is symmetric Laplace because a Brownian increment at an independent exponential waiting time has characteristic function \(\lambda/(\lambda+Dt^2)\). The contraction series converges absolutely under the strict factor cap. Isolating the most recent Laplace innovation and controlling the remaining series at a strictly higher exponential moment yields the coefficient \(T(R)\), not merely a logarithmic decay rate. Nonnegative geometric-series expansion, Jensen's inequality, the sharp bounded-moment inequality and a proved Euler product identity furnish the extremizers and strict equality cases. The standalone finite checker passes 319 assertions; it is not substituted for the infinite proof.

## Originality — PASS, with historical-priority risk

The closest primary literature includes Assefa–Keller-Ressel–Palmowski (arXiv:2610.01363v1), Di Bello et al. (arXiv:2305.13722v2 and arXiv:2501.01139v1), Grzywny et al. (arXiv:2412.15626v1), Dahlenburg et al. (arXiv:2104.14866v1), and Buraczewski et al. (arXiv:1703.02330). The generic Laplace/perpetuity tail-transfer mechanism and the deterministic-reset density are known or prior-implied. The assessed contribution is **only** the complete sharp fixed-mean *random multiplier* optimization, its unique endpoint laws, and the convex-order ordering of the leading stationary absolute-tail amplitude. Targeted mathematical research record, alias, and literature searches did not identify that complete implication. Existing general convex-order theory may still subsume the specialized comparison; independent priority review remains necessary.

## Mathematical value — PASS

Rare excursions of a stationary partially reset diffusion have a natural exponential tail, but the tail prefactor depends on the full distribution of reset factors. At fixed mean reset retention and an imposed physical upper cap, the exact worst and best designs, their uniqueness, and convex-order monotonicity answer a motivated extremal question and reveal a mechanism not visible from the mean contraction or the decay exponent alone. This is a precise rare-event design law, not a routine moment recomputation.

## Limits

The argument requires iid multipliers in \([0,\rho]\) with \(\rho<1\), independent Brownian motion and Poisson events, and is asymptotic at fixed parameters. Finite numerical tests do not establish infinite convergence; a direct analytic proof is supplied. Deterministic and generic light-tail parts are carefully credited. Historical priority and independent proof assessment remain open.

Self-review: passed. Independent audit: not yet performed.
