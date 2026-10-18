# Scientific review

## Correctness — PASS

The proof explicitly fixes the left empirical order statistic, tie treatment, sampling independence, Wasserstein space, and stepsize quantifiers. The key lemma is a finite piecewise-affine derivative count: at least \(k\) residuals are unclipped and contribute slope \(1\), and the remaining \(m-k\) contribute at least \(-1\). This yields both the exact drift monotonicity and the sharp synchronous mean-square bound. A contraction on the complete Wasserstein space gives existence, uniqueness, and the limiting rate, without an unproved stochastic-stability assertion. Two-location distributions attain the sharp factor in optimal monotone transport and exhibit two absorbing states below the threshold. A binary-affine invariant-law example rigorously establishes the total-variation obstruction. The standalone checker confirmed 282876 exact-rational slope/endpoint tests, 272 sharp-factor witnesses, and 289 absorbing-state witnesses. Tests support, but do not replace, the general proof.

## Originality — PASS, with bibliographic risk

The strongest relevant primary comparison is Merad–Gaïffas (arXiv:2309.17316), which proves quantile-clipped SGD ergodicity under a diffuse noise assumption, not a sharp exact-order-statistic contraction criterion for potentially atomic fixed data. The later Shulgin–Richtárik paper (arXiv:2412.19916) derives bias/descent bounds and a scalar quadratic bias illustration but not the asserted global \(W_2\) coefficient, median-rank transition, or finite-time total-variation obstruction. Andrew et al. develop privately estimated clipping quantiles, whereas this construction uses an exact empirical quantile. General iterated random-function contraction and one-dimensional transport principles are acknowledged as standard. Targeted mathematical-record and primary-literature searches revealed no implication covering the joint theorem. Search coverage is non-exhaustive; unindexed equivalent statements remain a risk.

## Value — PASS

The exact rank threshold describes a real design choice for finite-data adaptive clipping, especially the difference between a chosen median convention and strict majority order statistics. It yields a dimension- and scale-free quantitative stability guarantee and a sharp stepsize boundary for an empirically defined stochastic optimizer. The Bernoulli example distinguishes the useful geometry of Wasserstein convergence from total-variation guarantees that require extra mixing hypotheses; it is relevant to interpreting stochastic-optimization convergence theorems on discrete datasets. The result does not claim optimizer recovery, robust private training, or a high-dimensional generalization.

Self-review: passed. Independent audit: not yet performed.
