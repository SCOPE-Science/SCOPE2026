# Scientific review

## Correctness — PASS

The stationary convolution is defined because the response decays exponentially and each resetting Brownian input has a finite fourth moment. Conditioning on the entire reset clock makes every output a centered Gaussian with explicit clock-dependent variance; Itô isometry gives the displayed sum over independent excursions. The Poisson add-one identity and the exact change from splitting any reset-free interval prove that the mixing variance is nonconstant for every nonzero continuous response, including signed ones. Thus the fourth cumulant equals three times a strictly positive variance, and independent Gaussian bath contributions cannot change it. The OU covariance comparison holds at all time lags. The exact symbolic generator/perpetuity calculations independently test two normalizations and a signed two-mode instance.

## Originality — PASS (same-model, residual implicit-coverage risk)

Guéneau, Majumdar, and Schehr, arXiv:2306.09453, already obtain a scalar harmonic stationary distribution recursion and its low moments: the scalar example here is not novel. Sarkar and Roy, arXiv:2307.06127, already observe non-Gaussian finite-chain velocity distributions and measure positive kurtosis numerically. Their inspected §§2–4 do not establish the universal strict fourth-cumulant result for *every* coupled linear-system observable with sign-changing response, nor the all-time Gaussian covariance-matcher comparison. The proof is a nondegeneracy argument based on Poisson gap insertion, not a relabeling of a particular published scalar formula. A generic Gaussian-mixture theorem supplies the nonnegative cumulant identity, but it does not automatically prove that the mixing variance cannot be constant for an arbitrary signed response. Residual risk: general results on stochastic filters or Gaussian mixtures may implicitly cover the strictness statement, and full independent priority review is still necessary.

## Value — PASS

The finite-chain literature provides numerical evidence for non-Gaussianity but not a parameter-free all-observable sign certificate. The theorem upgrades this to a network-wide, arbitrary-impulse-response statement independent of response sign; this covers underdamped, oscillatory, and nonnormal finite dynamics without assuming cooperative coupling. Matching a Gaussian colored reservoir shows that even the entire second-order spatiotemporal output law cannot resolve these forcing mechanisms, whereas fourth-order statistics always can for any observable connected to a reset Brownian input. The result is motivated by finite active reservoir chains, is structurally reusable, and has exact, explicitly delimited finite-dimensional scope.

## Literature and limits

Closest primary sources: arXiv:2306.09453 §§2, 4, Appendix E and arXiv:2307.06127 §§2–4. The proof uses standard Gaussian conditioning and a Poisson point process identity, so any stronger published all-filter theorem could subsume it. The claim does not cover correlated clocks, infinite networks, or nonlinear dynamics. Independent audit is not yet performed.

Self-review: passed. Independent audit: not yet performed.
