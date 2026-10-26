# Scientific review of the finite-budget beta product theorem

## Correctness — PASS

The singular-value reduction is exact: the Rayleigh quotient is a constant plus a positive multiple of squared projection onto a fixed spike direction. The optimizer in an augmented subspace is the normalized projection of that spike direction. Its gap ratio is the orthogonal complement of a Haar-subspace projection, yielding a conditional beta law independent of the current state; iteration gives true iid multipliers, not merely matching marginal distributions. The gamma moments, almost-sure logarithmic rate, strict budget-merging inequality and two high-dimensional limits are established without relying on simulation. The embedded script replayed 837 finite checks. Domain exclusions (exactly orthogonal starting vector, repeated lower singular space and full-block termination) are explicit.

## Originality — PASS, with priority risk

The central numerical method is *not* new: arXiv:2410.08297 supplies the one-direction randomized exact line search, while Section 8.6 of arXiv:2512.05520 already introduces and evaluates a multi-vector Rayleigh–Ritz version. Haar projection beta distributions and randomized subspace error laws are known. The claimed distinct result is the exact independent beta **trajectory** for an adaptive two-level operator problem, together with exact moment/lyapunov formulas and a strict optimizer over every allocation of a fixed forward-evaluation budget. The compared works give general almost-sure/sublinear theory, a block algorithm with experiments, or geometric projection distributions; the inspected portions do not state the entire implication. Targeted mathematical-record queries and comparisons with previously published mathematical claims did not surface a complete equivalent. Equivalent specialist randomized eigenmethod calculations remain possible, so publication priority is not independently established.

## Value — PASS

This is a complete, sharp stochastic-runtime benchmark on the natural rank-one spectral spike family, specifically motivated by adjoint-free operator norm search. It converts a broad convergence guarantee into the full finite-time law, exact expected residual, sample-path exponential rate and a quantitative forward-evaluation cost tradeoff. Near a full tangent budget the expected gap under one block is \(1/(d-1)\) of its initial value, versus asymptotic \(e^{-1}\) under the same count of sequential single-direction steps, a dimension-order separation. The comparison does not predict total computational runtime because Rayleigh–Ritz subproblems become more costly with block size.

Self-review: passed. Independent audit: not yet performed.
