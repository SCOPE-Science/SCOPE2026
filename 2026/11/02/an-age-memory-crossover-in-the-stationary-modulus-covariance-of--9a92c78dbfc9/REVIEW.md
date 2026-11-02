# Scientific review

## Correctness: PASS

The stationary Poisson construction supplies an exponential backward age independent of future resets. Conditioning on whether the interval contains a reset gives an exact factorization; the zero-reset bivariate Gaussian pair has a standard and explicitly stated absolute-value moment. A two-term law-of-total-covariance decomposition yields the formula. For the age covariance, concavity bounds its rescaled difference by an integrable multiple of the exponential age; for the within-excursion term, the ratio \(h(q)/q^2\) is bounded and a third fractional age moment dominates. These give the two exact gamma coefficients and the comparison of decay exponents. The strict sign and the critical \(1/4,3/4\) split are proved, not inferred from a finite simulation. The accompanying checker independently integrates the direct folded-normal expression and the decomposed expression, then examines large lags.

## Originality: PASS (preliminary)

The 2026 motivating paper examines the integrated absolute-area functional and ergodicity. The most relevant earlier full text, Taźbierski–Metzler–Magdziarz (2025), supplies two-time position distributions and signed-position covariance, including the scaled Brownian specialization, but not an explicit modulus covariance or the competition between two noninteger powers of lag. The new contribution is the exact age-versus-Gaussian decomposition **and its sharp three-regime asymptotic with constants**, not a claim to invent renewal or Gaussian-moment methods. The 2021/2022 ordinary-diffusion correlation treatment is less close. An older nonlinear-observable asymptotic or a direct specialization of a broad two-time formula remains a real priority risk. The accessible prior research record was compared by claims/parameters and showed no same mathematical model claim; search nonmatches do not establish uniqueness.

## Mathematical value: PASS

The model is the natural instantaneous integrand of the motivating absolute-area statistic. The result identifies which of two competing, physically distinct dependence mechanisms controls long-lag correlations on opposite sides of Brownian scaling. The exact prefactors and their transition, including a critical decomposition, supply benchmarks for covariance-based mixing estimates and future renewal-functional calculations. This is a genuinely motivated asymptotic classification rather than a parameter renaming or an arbitrary finite numerical slice.

## Residual risks and scope

Only stationary complete Poisson resetting with one-dimensional centered Gaussian excursions and \(0<\beta<2\) is proved; there is no general reset-time or vector extension. The broad two-time joint-distribution formula of Taźbierski–Metzler–Magdziarz is stronger as a distributional identity and can imply the exact covariance after integration; the novelty claim is confined to the additional explicit nonlinear and asymptotic analysis. Independent examination of historical priority remains necessary. Numerical quadrature is not independent validation of the theorem.

Self-review: passed. Independent audit: not yet performed.
