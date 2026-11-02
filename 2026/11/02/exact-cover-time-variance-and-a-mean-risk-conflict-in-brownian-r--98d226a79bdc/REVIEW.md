# Self-review

**Claim:** Exact cover-time variance and a mean–risk conflict in Brownian resetting.

## Correctness — PASS

The result defines a reflected diffusion with visits persisting across Poisson resetting, and uses inclusion–exclusion for the three hitting problems. The free hitting Laplace transforms solve the correct mixed/Dirichlet boundary-value problems, and the Poisson renewal quotient yields the first and second moments by differentiation. The global mean minimizer at scaled rate one follows from an explicit quadratic derivative sign after a hyperbolic substitution. The variance sign is independently certified through exact rational Taylor intervals (see `verify.py`, executed successfully with 1,998 checks). Boundary starting points, scaling in \(L,D\), derivative variable and the strictly positive resetting rate are explicit. The main inequalities are analytical, not extrapolations from finite grids.

## Originality — PASS (best-knowledge, qualified)

Ghosh–Sabhapandit, arXiv:2605.31207v1, derive the centered reset cover-time distribution and mean; Linn–Lawley, arXiv:2406.12154, already provide a full arbitrary-asymmetric-interval **mean** formula and high-frequency moment asymptotics. Those results are expressly credited and not included as original. The current final claim specifically supplies the all-location *finite-rate second-moment* expression and proves a strict cross-design conflict: sites globally minimizing the mean have larger variance than the center at one exact scaled rate. The inspected papers do not explicitly provide this joint result, and no equivalent published record was found by the actual semantic searches. There is nonzero residual priority risk: differentiating general renewal equations might make some parts implicit, and no complete literature-wide equivalence certification is possible.

## Value — PASS

The microscopic model is already motivated by target-coverage problems. Mean completion time and reliability are distinct practical objectives; the theorem proves, without heuristic optimization, that an overall mean-optimal spatial reset site does not even dominate the simple midpoint in variance. This is a natural two-moment tradeoff, not an arbitrary numerical slice, and the formula works across all positions and rates. It informs which additional calculations a complete mean–risk Pareto classification would require.

## Closest literature and scientific limits

- Ghosh and Sabhapandit (2026), arXiv:2605.31207v1: midpoint distribution, exact mean and optimal rate.
- Linn and Lawley (2024/2025), arXiv:2406.12154: general arbitrary-location mean formula and high-reset moments, including a potentially dominant general renewal method.
- Pal and Prasad (2018/2019), arXiv:1812.03009: interval resetting first-passage.

Only a strict variance comparison with the two globally mean-optimal endpoints is shown; midpoint variance optimality over all reset sites is **not** established. Stochastic reset locations, delayed resets, and erasure of search history are outside scope.

Self-review: passed. Independent audit: not yet performed.
