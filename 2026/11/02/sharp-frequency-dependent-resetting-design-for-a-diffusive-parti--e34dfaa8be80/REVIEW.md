# Scientific review: sharp frequency-dependent resetting design

## Correctness — PASS

The stationary two-sided Brownian–Poisson convolution converges in mean square because the squared multiplier contracts at exponent \(r(1-a^2)\). This gives stationary variance \(2D/[r(1-a^2)]\). Conditional expectation across future jumps yields exponential covariance with relaxation rate \(r(1-a)\), and the Fourier transform yields the stated Lorentzian spectrum. Global optimization is proved by differentiating the cubic denominator and comparing its negative stationary root to both excluded endpoints. At \(|\omega|=r\) there is one interior optimum, whereas above this frequency the value at the excluded no-reset boundary is strictly better than every stationary admissible factor. The time-average CLT follows from the compensated-jump martingale, its ergodic predictable quadratic variation and the martingale Lindeberg condition. These arguments supply the infinite-dimensional and boundary portions that finite tests cannot prove.

The standalone standard-library checker returned PASS with 53,019 assertions, including exact rational computations, parameter and Fourier quadratures, independent covariance integration, and seeded stochastic simulation. Numerical checks support, rather than replace, the proof. The optimizer is unique for all frequencies below or at threshold; above it only an infimum exists.

## Originality — PASS, qualified

Biroli, Feld, Hartmann, Majumdar and Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension* (arXiv:2406.08387v1, 2024), introduce the signed-factor model and characterize one-time stationary statistics and first passage. Olsen and Löwen, *Partial stochastic resetting with refractory periods* (arXiv:2406.10039v1, 2024), derive Fourier–Laplace propagators and moments and investigate positive contraction factors with refractory periods. Their propagator could be used to derive particular correlations, so elementary covariance and spectral calculations are not asserted as novel by themselves. The compared works do not appear to establish the global frequency-by-frequency optimum over negative and positive reset factors, the sharp transition at the reset rate, nonattainment above it, or the connection to the optimal long-time averaging variance. Related broad stochastic-control and correlation results could nevertheless contain an equivalent classification, so publication priority remains qualified.

The compared claims differ by more than terminology: the new result optimizes the two-time spectral observable across a signed multiplier, not the one-time stationary law, kurtosis, mean-first-passage time, or a positive-factor refractory parameter. A negative multiplier is mathematically important, since the low-frequency optimizer equals \(-1/3\), strictly outside the positive-parameter family.

## Mathematical value — PASS

A stationary noise spectrum is a natural observable for fluctuation measurements. The result solves the model's complete fixed-rate, single-frequency parameter-design problem, and its attained-to-unattained threshold is a substantive boundary distinguishing strategies: at low frequencies the optimum deliberately reverses the particle's position, at the reset-rate frequency it becomes a full reset, and at high frequencies the best limiting design ceases to have a stationary position distribution. The cusp in the optimized spectrum and the exact \(5/32\) improvement in the long-time variance of time-averaged position are testable consequences. The quantitative problem is motivated by a natural physical spectral observable, not an arbitrary numerical slice.

## Scope and limits

The theorem holds only for one-dimensional Brownian diffusion, stationary statistics, an independent constant-rate Poisson reset clock, and a deterministic signed factor strictly between -1 and 1. Finite-horizon spectra, joint reset-rate optimization, random factors and refractory dynamics are not covered. An inaccessible or unindexed mathematically equivalent treatment could change the novelty assessment. There is no independent external audit.

Self-review: passed. Independent audit: not yet performed.
