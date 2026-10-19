# Scientific review

## Correctness
**PASS.** The stationary law follows from a coupling and an absolutely convergent series of independent exponential differences. Its exact moment-generating function and domain follow by factoring the exponential-time Brownian innovation. Elementary independent exponential and gamma convolution identities give each density-tail equivalent, including the critical linear prefactor. The remaining series has a finite exponential moment in an open neighborhood of the relevant tail pole after dominant factors are removed. The seven coefficient/product normalizations and sample rates are consistent with exact moment and rational-pole checks in `verify.py`. The proof is not based on extrapolating a finite series.

## Originality
**PASS, with residual risk.** Pierce (2022) and Tal-Friedman, Roichman, and Reuveni (2022) address drifted motion with **positive** fractional resetting; Biroli and collaborators (2024) permit negative resetting for **zero** drift. Their examined primary texts do not give the competition between the direct negative excursion and the first negatively reflected positive excursion, nor the sharp critical linear factor in the combined drift-plus-reflection model. This is a comparison of hypotheses and implications, not merely title matching. Standard signed affine-perpetuity tail theory could contain a more general implication and warrants independent priority review.

## Value
**PASS.** The question is a motivated stationary rare-event diagnostic: how a positive microscopic drift and sign-reversing resets compete to generate large *negative* positions. The result gives a complete sharp parameter transition, an observable change in the left decay rate, and a nontrivial critical density factor caused by two degenerate microscopic excursion channels. The unrestricted right-tail rate supplies a contrasting asymmetry. This is more informative than a restatement of an existing moment product.

## Scope and uncertainties
All parameters satisfy \(\mu,D,r>0\), \(0<b<1\). Results concern the full stationary position density. They do not address stochastic resetting amplitudes, non-Poisson events, zero drift, or finite-time exit laws. The literature comparison does not establish unique priority against every possible general perpetuity theorem.

Self-review: passed. Independent audit: not yet performed.
