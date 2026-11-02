# Self-review

## Correctness — PASS

The exact scope is a stationary two-coordinate Markov process with positive harmonic decay, resetting-Brownian forcing and independent Poisson reset times. The generator recurrences fix all second- and fourth-degree moments. The explicit quadratic Poisson solution is checked coefficient-by-coefficient. Two independent evaluations of the asymptotic variance—stationary Green–Kubo/Poisson covariance and the martingale's continuous-plus-jump quadratic variation—give the same rational expression. Stationary Gaussian Wick integration gives the matched benchmark, including the coincident-rate limit. The excess has a strictly positive numerator, and the derivative's quartic polynomial has an all-positive-domain certificate. Standard stationary ergodic martingale CLT conditions follow from finite polynomial moments and the dissipative/reset coupling, not from finite experiments. Exact-rational replay of 150 independent parameter tuples passed with the packaged verifier.

## Originality — PASS, with publication-priority qualification

The closest primary source, Guéneau–Majumdar–Schehr, arXiv:2306.09453 (2023), provides the stochastic model, stationary position moments, the two-time position correlation, and one-time relaxation formulas. Its inspected equations (33)–(37), (59), (85), (189)–(191), (199)–(211), and (212)–(221) do not state the long-time time-integrated squared-position variance, the covariance-matched Gaussian comparison rate, or the strict dimensionless five-to-one monotonic law. Earlier non-Gaussian moment comparisons and asymmetric fourth-order temporal correlations do not imply the sign or exact integral of the symmetric squared-position two-time covariance. Related boundary-reset harmonic-chain work (Sarkar–Roy, arXiv:2307.06127) treats non-Gaussian stationary velocity statistics and two-time velocity correlations in a distinct many-body model; only its abstract could be materially inspected, and full-document noncoverage is not asserted. Searches for equivalent observables and phrases including quadratic additive functionals, Green–Kubo variance, reset-Brownian harmonic trap, and matched Ornstein–Uhlenbeck noise gave no identified covering theorem. An unindexed or more general additive-functional theorem might subsume the algebraic formula, so independent priority verification remains necessary.

## Mathematical value — PASS

The article's harmonic reset-noise model is explicitly motivated by the experimental ambiguity of active colored forcing whose two-time correlation resembles Gaussian OU forcing. The quadratic time-average is a natural observable of confinement energy and responds to four-time statistics, which equal-time kurtosis or the two-time covariance cannot determine. The proved excess is global for every positive rate, and its sharp monotone normalization is a parameter-inference law independent of diffusivity or coupling. The strict bounds and limit ratios of five and one make it a nontrivial structural classification, rather than a numerical parameter instance or simple restatement of a known stationary moment.

## Limitations and closest literature

The Gaussian comparator is covariantly equivalent only at order two; no full-process distributional equivalence is implied. The theorem is stationary, linear, one-dimensional, and Poissonian; no finite-time stochastic ordering or nonlinear trap claim is made. The source paper's stationary moments and two-time covariance are credited. Material inspection of the related harmonic-chain source was limited to the abstract, and broad unindexed literature remains a residual priority risk. Independent scientific review was not performed.

Self-review: passed. Independent audit: not yet performed.
