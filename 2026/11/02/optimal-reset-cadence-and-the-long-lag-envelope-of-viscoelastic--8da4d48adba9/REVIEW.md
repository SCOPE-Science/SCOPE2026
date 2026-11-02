# Review of optimal reset cadence and viscoelastic event-lag memory

## Correctness — PASS

In the stated linear Gaussian probe–bath process with independent Poisson probe-only resetting, the stationary generator gives an exact three-equation moment system. Its positive solution supplies the variance of the pre-reset probe position and the probe–bath cross-moment. State-independent Poisson hazard makes pre-reset event sampling unbiased. Starting from the post-reset position \(X=0\), the one-step exponential-clock mean propagators are \(b=1/(r+g+1)\) for the next pre-reset probe and \(a=(r+1)/(r+g+1)\) for the persistent bath coordinate. They give \(\rho_m=ba^{m-1}V/U\) for each integer \(m\ge1\), as claimed. A concave quadratic controls the rate derivative and has one positive root exactly in the claimed region. Its explicit root yields the sharp large-lag asymptotics. The supporting standard-library checker reproduces 2,748 exact-rational identities, 48 bounded asymptotic/critical tests and 12 independently sampled exact-transition tests. These finite checks do not substitute for the proof.

## Originality — PASS, with residual priority risk

Santra and Das, *Resetting in a viscoelastic bath: the bath remembers* (arXiv:2603.17027, public 2026-03-17), supply the identical physical model, stationary moment analysis and bath-memory mechanism, but the examined material does not state the pre-reset event-sequence covariance, its necessary-and-sufficient rate-maximization threshold, or the optimized large-lag algebraic envelope. Biswas and colleagues (arXiv:2412.09260) study a complete-renewal GLE reset protocol and physical-time correlations, not persistent-bath event-index correlations. Olsen and Löwen (arXiv:2401.12685) reset a velocity variable in a different process, while Maes and Thiery (arXiv:1705.07670) reset a bath rather than the probe. Generic marked-Markov and affine-recursion methods are prior knowledge. Exact-statement and stronger-implication searches did not identify the full event-lag bifurcation; a broader parameter-comparison result could still subsume portions, and not every related paper was accessible in full.

## Value — PASS

The correlation of successive *excursion endpoints* is a natural, experimentally accessible marker of residual bath memory, distinct from an ordinary physical-time autocorrelation. A sharp boundary \(g=3/[2(m-1)]\) determines when increasing reset frequency first enhances rather than suppresses event-index memory. The nontrivial asymptotic optimum \(r_m^*\sim gm\) identifies relaxation-time matching, and the optimal \(1/m\) envelope contrasts with exponential event-lag decay at any fixed rate. These specify a meaningful reset-protocol design tradeoff, rather than an arbitrary parametric slice or numerical table entry.

## Limits of assessment

The conclusions concern only the stated instantaneous probe-only linear model and stationary event series. Source comparisons are not an independent publication-priority certification; numerical checks are bounded. Independent validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
