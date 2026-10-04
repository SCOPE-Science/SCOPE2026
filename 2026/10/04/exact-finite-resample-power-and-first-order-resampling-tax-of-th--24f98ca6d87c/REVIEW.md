# Review

## Correctness
PASS. Gaussian conditioning gives the observed standardized score exactly as \((\delta R+Z)/\sqrt{1+\delta^2}\), while every null-resampled standardized score is iid standard normal. This makes the exceedance count conditionally binomial and yields the finite-\(n\), finite-\(B\) power formula directly. The null-size statement follows independently from uniform rank. In the local regime, \(R/\sqrt n\to1\); the beta-order-statistic reduction on exact-size budgets is exact, and Taylor expansion about its mean gives the displayed strictly negative \(1/B\) coefficient. The embedded verifier reproduces the numerical benchmarks and coefficient convergence.

## Originality
PASS. Wang and Janson explicitly study the analytical-cutoff CRT and state that their empirical-cutoff results agree when the resample count tends to infinity; their marginal-covariance theorem gives asymptotic power but does not analyze fixed finite resampling. Candès et al. discuss the Monte Carlo burden and binomial uncertainty of randomization p-values, but not this exact Gaussian power law or resampling-power coefficient. Katsevich and Ramdas analyze optimal CRT statistics and local asymptotic power, not the finite-resampling effect. Searches over finite-resample, Monte Carlo rank, beta-order-statistic, Gaussian CRT, and resampling-budget aliases found no equivalent result. Residual risk remains from generic historical randomization-test literature.

## Value
PASS. The CRT's computational burden is a documented practical limitation, so an exact relation between resampling budget and statistical power answers a motivated design question. The result quantifies a persistent loss at fixed \(B\) under local alternatives and gives an explicit first-order budget correction: at the common \(5\%\) level with local effect \(h=2\), the minimum feasible budget \(B=19\) loses about 0.081 power relative to the exact-quantile CRT. The formula also separates Monte Carlo power loss from the underlying statistic's ideal-resampling power.

## Closest literature and limitations
Candès et al., *Panning for Gold* (arXiv:1610.02351), defines the CRT and emphasizes its resampling cost. Wang and Janson, *A High-Dimensional Power Analysis of the Conditional Randomization Test and Knockoffs* (arXiv:2010.02304), gives asymptotic power for the marginal-covariance CRT while taking the empirical resample count to infinity. Katsevich and Ramdas (arXiv:2005.05506) studies most-powerful CRT statistics and local asymptotic power. The present result is limited to the Gaussian one-predictor model and does not claim a universal finite-resampling law for arbitrary CRT statistics.

Same-model review: passed. Independent audit: not yet performed.
