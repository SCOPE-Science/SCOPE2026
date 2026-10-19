# Scientific review: Stationary resetting Brownian current

## Correctness — PASS

The stationary displacement density is normalized and obtained directly from the reset-age mixture. The two-time no-reset decomposition is exact; Campbell integration gives both environment-averaged and thermal-only connected correlations. The two Gaussian/exponential integrals evaluate to the complementary-error-function form stated in the result. Positivity and strict decay follow from a direct threshold-separated comparison of Gaussian cdfs. Conditional ergodicity under independent resetting and integrability of the infinite particle sum give almost-sure time-average convergence. The Poisson Laplace functional and the independent first-anchor decomposition prove its generalized Dickman distribution. The packaged checker passed 145 assertions on the actual formulas; this finite check supplements and does not replace the proof.

## Originality — PASS (self-review)

Di Bello et al. (arxiv:2302.06696) already establish the stationary one-time annealed Poisson law and the single-time quenched-variance constant. Dean et al. (arxiv:2303.08961) already establish the general bivariate-Poisson two-time effusion structure and a generic propagator-integral reduction. Bhattacharjee and Goldstein (arxiv:1706.08192) describe the classical generalized Dickman distribution; the distribution itself is not new. The assessed contribution lies in the full **evaluated** stationary covariance for independently resetting Brownian paths, its exact one-quarter temporal plateau, and the identification and cumulants of the nonergodic physical-time average. Those formulas and identifications were not located in the relevant inspected primary full texts. Searches of published mathematical findings and relevant primary literature did not locate a directly equivalent specialization. Search absence is not a proof of uniqueness.

## Value — PASS

The same established gas has Poisson stationary one-time measurements but a non-Poisson, sample-dependent infinite temporal average; this is a substantive mathematical distinction between ensemble and temporal measurement. The exact complementary-error-function decay identifies the time scale of dynamical decorrelation while the plateau and generalized Dickman law quantify persistent frozen-environment variation. Both observables arise directly from the original statistical mechanics model rather than an artificial slice.

## Closest literature and limitations

The full two-time joint-law **form** is implied by Dean et al.'s general theorem, but the new evaluated coefficient and stochastic-time-average distribution are not given there. More general or unpublished specialized calculations might preempt the claim. The result is limited to fixed Poisson anchors, stationary independent Brownian resetting and annealed/averaged-quenched correlation; finite-sample inference, synchronized resets, non-Poisson anchors and other particle dynamics are not established. No external priority validation was performed.

Self-review: passed. Independent audit: not yet performed.
