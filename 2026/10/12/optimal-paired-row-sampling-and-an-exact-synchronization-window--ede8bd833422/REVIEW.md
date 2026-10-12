# Scientific review: optimal paired-row RK–RK sampling

## Correctness — PASS

The update order is reconstructed from Ma–Needell–Ramdas, Algorithm 1: the second projection sees the first-stage **updated** intermediate coordinate. On nonzero diagonal factors this reduces to a two-event completion rule. Conditioning on the first occurrence of the first-stage row gives an exact coordinate failure probability; summing these probabilities with fixed squared target weights gives the stated mean-square law. Every admissible pairing is bounded by the Fréchet diagonal inequality, and the explicit leftover-mass transport realizes equality in all coordinates. The transition center and window follow by an elementary uniform logarithmic expansion. The actual embedded `verify.py` completes exhaustive exact-rational path comparisons and supplementary finite-asymptotic checks. Finite checks are not substituted for the analytic claims.

## Originality — PASS, with residual risk

The source algorithm [1] specifies two randomized row projections and develops convergence-rate bounds for the ordinary independent sampler. Du [2] studies a different regularized problem and explicitly identifies ordinary RK–RK as a special case. Neither inspected complete paper gives a sharp same-round coupling optimization across all right-hand sides and horizons or the exact balanced synchronization crossover. Indexed related results on randomized Gauss–Seidel delay, maximal-distance Kaczmarz residual spikes, and cyclic Kaczmarz order bias address different update mechanisms and do not imply the stated diagonal factorized two-stage result. The Fréchet coupling upper bound and ordinary coupon-collector ideas are known; the claim concerns their quantitative implication for these interlaced updates. A specialized unindexed derivation remains a possible priority risk.

## Value — PASS

The result addresses a natural design freedom in a published interlaced solver: whether factor-row choices should be sampled independently when each factor's importance-sampling marginal must remain unchanged. It gives an exact universally optimal stationary coupling on a nontrivial family of all nonsingular diagonal factorizations, not merely one parameter example. It also identifies an order-\(m\log\log m\) delay in a fixed absolute error target that disappears under synchronization, and quantifies the complete crossover at partial synchronization. This is a useful structural benchmark; it does not transfer automatically to coupled rows of general matrices.

## Scientific limitations

The proof does not establish optimality under changing marginals, correlations across iterations, or non-diagonal factors. It assumes zero initialization and exact arithmetic. The scaling window describes expected absolute squared error rather than the distribution of first exact termination. Indexed-only comparisons do not exclude unindexed priority.

Self-review: passed. Independent audit: not yet performed.
