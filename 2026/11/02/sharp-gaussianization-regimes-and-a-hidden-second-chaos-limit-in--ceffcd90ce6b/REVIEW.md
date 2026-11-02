# Scientific assessment

## Correctness — PASS

The conditional Gaussian computation fixes normalization exactly: the mean-square displacement is \(2\mu t^{2H}\), and the non-Gaussian parameter equals the normalized covariance double integral. The three regimes follow from a scaled dominated-convergence calculation, an integrable-kernel monotone limit, and a logarithmic Tauberian boundary comparison, respectively. The positive Gaussian-square diffusivity is admissible because its Gaussian covariance is a mixture of OU covariances. Its subcritical weighted quadratic fluctuations converge in \(L^2\) to a nonzero second-Wiener-chaos element, rigorously non-Gaussian by the positive fourth cumulant. Thirteen deterministic numerical checks passed across quadrature normalizations and all regimes. No finite computation is used as a substitute for the analytical proof.

## Originality — PASS, with residual risks

Pacheco-Pozo and Krapf (arXiv:2405.03836) provide the stochastic integral model and second-order theory, so these are prior work. Balcerek et al. (arXiv:2501.10472), especially Eq. (13), already give the general kurtosis covariance integral; that identity is **not** claimed as new. Their evaluated analyses concern Markovian exponential switching and nonstationary, infinite-mean renewal switching, not the stationary algebraic-covariance asymptotic coefficient trichotomy or the non-Gaussian magnified conditional-variance limit. A subsequent broad heterogeneous-medium framework (arXiv:2603.12775) was also compared: it discusses general non-Gaussian parameters without providing these evaluated Hurst/memory boundaries. Published mathematical-record searches under aliases including fluctuating diffusivity, long-memory covariance, Gaussianization, and second Wiener chaos did not reveal equivalent indexed coverage. This is a best-knowledge priority assessment: general regular-variation and Wiener-chaos limit theory may subsume techniques or partial statements; publication priority is not definitively certified.

## Mathematical value — PASS

The exact transition at \(H=\eta/4\) identifies which physical memory scale controls the rate at which a heterogeneous fractional displacement loses non-Gaussianity. The borderline logarithm and all three explicit amplitudes are meaningful predictions for anomalous transport with slowly relaxing environments. The distributional second-chaos limit shows that experimentally invisible Gaussianized displacement can coexist with non-Gaussian fluctuations in its latent conditional variance; this distinction is not an arbitrary parameter slice or mere restatement of the previously known fourth-moment integral.

## Scope and evidence limits

The asymptotic trichotomy assumes a stationary diffusivity with nonnegative, regularly varying covariance and finite second moment; it is not a theorem about nonstationary heavy-tailed renewal switching or sign-changing covariance. The non-Gaussian fluctuation limit is for a particular strictly positive Gaussian-square environment and only in the subcritical Hurst range. Independent expert assessment and exhaustive publication-priority checking have not been performed.

Self-review: passed. Independent audit: not yet performed.
