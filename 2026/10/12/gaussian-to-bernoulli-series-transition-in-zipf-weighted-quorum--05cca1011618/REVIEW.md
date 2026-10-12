# Scientific review — Gaussian-to-Bernoulli-series transition in Zipf-weighted quorum times

## Correctness: PASS

For homogeneous Poisson rates, rescaled first arrivals are iid standard exponentials. The associated weighted empirical distribution has exact mean \(1-e^{-x}\) and variance scale \(a_N^2=H_N^{(2s)}/(H_N^{(s)})^2\). The proof bounds increments of the centered empirical distribution over windows of length \(O(a_N)\) by \(O(a_N^3)\) in variance. Monotone-grid interpolation yields a local inverse expansion with derivative \(1-\theta>0\). The bounded-vector Lindeberg theorem applies exactly when \(s\le1/2\), whereas the coefficients converge in \(\ell^2\) to a nonzero sequence when \(s>1/2\). Explicit power-sum asymptotics give the stated normalization constants and covariance structure. The third (or, at the balanced level, fourth) cumulant proves the non-Gaussian limit. Finite exact-rational checks were successfully reproduced; they do not substitute for the analytical limit arguments.

## Originality: PASS, with qualification

The primary motivating paper [1, Theorem 4.1] proves the universal homogeneous-clock law of large numbers, not the three second-order distributions. Its Zipf sections analyze aligned arrival probabilities and weights, which are not the homogeneous-clock model under study. Withers–Nadarajah [2] derive cumulant/Edgeworth expansions for weighted empirical functionals with bounded rescaled weights; these conditions fail for all positive Zipf exponents here, and a non-Gaussian series cannot follow from their Gaussian expansions. Necir [3] treats approximation-error weights for ordinary uniform-weight empirical/quantile processes; Akinshin [4] treats weighted estimators, not this threshold-time phase classification. Related published mathematical-record searches did not reveal a covering statement, but indexing is not exhaustive and a general theorem might imply part of the result.

## Value: PASS

The sharp \(s=1/2\) boundary separates diffuse Gaussian quorum-time fluctuations from a persistent series of individual Bernoulli discoveries even though the leading quorum time is deterministic throughout \(0\le s<1\). This is a natural separation of *quorum influence weights* from *arrival activities*, addressing a second-order gap raised by the known first-order universality. The joint law for finitely many thresholds and precise Gaussian covariance constants give more information than a single variance comparison. No extension to the aligned-rate Zipf model or to process-tightness in the threshold is asserted.

## Closest literature and scientific risk

[1] S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1, Theorem 4.1 and Sections 5–7.

[2] C. S. Withers and S. Nadarajah, *The distribution and quantiles of functionals of weighted empirical distributions when observations have different distributions*, arXiv:1002.4338v1, especially Section 1 bounded-weight assumptions.

[3] A. Necir, *Weighted Gaussian Approximations for Increments of the Uniform Empirical and Quantile Processes*, arXiv:2606.28222v2.

[4] A. Akinshin, *Weighted quantile estimators*, arXiv:2304.07265v1.

An unindexed prior result formulated as a triangular-array weighted empirical-quantile limit theorem may cover part or all of the specific phase diagram. Priority remains subject to further independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
