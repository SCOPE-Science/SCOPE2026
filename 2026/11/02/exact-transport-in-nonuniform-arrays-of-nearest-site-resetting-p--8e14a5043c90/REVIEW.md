# Scientific review: Exact transport in nonuniform arrays of nearest-site resetting points

## Correctness — PASS

The stochastic generator and assumptions are explicitly fixed in `RESULT.md`. The invariant density is verified by normalization, the forward ODE on each gap and site-source derivative jumps. The lifted harmonic coordinate is continuously differentiable at all Voronoi midpoints and solves the generator equation pointwise between boundaries. Martingale bracket integration yields the exact all-gap coefficient and the martingale central limit theorem; a bounded corrector transfers the result to physical position. The small-rate cubic-gap expansion and strict Jensen comparison prove the fixed-rate reversal. The largest-gap high-rate law follows from leading hyperbolic terms. The separately constructed tilted-reset-time Markov chain checks 235 finite identities and numerical comparisons, but is not used to infer the infinite theorem.

## Originality — PASS, qualified

Alston and Bertrand's arXiv:2401.12772v1 (January 23, 2024) is the direct model source. Its regular-array formula, generic weak-reset enhancement, and globally optimized regular-array ceiling are prior results and not claimed here. The full accessible preprint main text and supplement IV were inspected; they explicitly discuss the obstacle for arbitrary-array site-exit weights and do not give this all-gap product formula or fixed-rate reversal. The later 2025 journal abstract and accessible indexed excerpts were also checked. Seven actual published-record semantic queries, corresponding web literature searches and the earlier scientific claim records showed no directly covering irregular-array result; the closest own entries 88701ce9 and ddd1dd42 concern the uniform lattice's higher cumulants. A general unindexed homogenization result or later journal appendix could still cover the calculation; novelty is therefore qualified, not externally certified.

## Mathematical value — PASS

The theorem gives an explicit, natural macroscopic transport invariant for the motivating model for **every** finite positive gap vector, with its stationary spatial law and reset-site probabilities. It resolves an arbitrary-array calculation otherwise handled numerically, uncovers a rate-dependent disorder advantage and gives a sharp largest-gap bottleneck law. Both are useful for selecting spatial binding-site arrangements; they are not an arbitrary slice or minor numerical improvement.

## Scientific limits

Only one-dimensional homogeneous Brownian diffusion and instantaneous nearest-site Poisson resets on a fixed periodic array are proved. Arbitrary renewal clocks, higher dimensions, finite-rate inference from short data, and nonperiodic sites remain untreated. The pre-existing optimized-rate ceiling is clearly separated. The same review does not replace independent publication-priority or mathematical validation.

Self-review: passed. Independent audit: not yet performed.
