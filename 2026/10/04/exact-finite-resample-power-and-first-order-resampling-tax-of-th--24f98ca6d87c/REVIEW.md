# Independent mathematical audit

## correctness

PASS

Conditioning on Y gives the observed standardized covariance score \(S=(\delta R+Z)/\sqrt{1+\delta^2}\), while each null-resampled standardized score is iid N(0,1). Conditional exceedance counts are therefore binomial and give the exact finite-n, finite-B power integral and exact null size. Under \(\delta=h/\sqrt n\), \(R/\sqrt n\to1\) yields the fixed-B local limit. On the exact-size subsequence the rejection threshold is a beta order statistic; a Taylor expansion at its mean yields the displayed negative \(1/B\) coefficient. Independent numerical evaluation reproduced the quoted h=2, alpha=.05 powers and coefficient.

## originality

PASS

The most directly relevant CRT power paper explicitly separates the empirical finite-resample cutoff from its analytical power calculation and states that its power results cover empirical resampling only when the number of resamples diverges. Generic Monte Carlo randomization-test literature establishes rank corrections and studies simulation budgets, but no inspected result supplied this Gaussian marginal-covariance finite-n power integral or the explicit local \(1/B\) loss coefficient. The final claim therefore resolves a concrete finite-resampling question not implied by the inspected CRT asymptotics.

## value

PASS

Finite resampling is a documented computational bottleneck in CRT practice. The theorem converts a concrete resampling budget into exact finite-sample power and a sharp local \(1/B\) penalty for a canonical Gaussian statistic, including the minimum feasible 5-percent budget. This is a motivated statistical design fact rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
