# Self-review

**Correctness — PASS.** The proof reconstructs the 2023 model's exact four-person final-size recurrences, expected within-household outbreak sizes, and the normalized second-epidemic threshold difference. The common positive rational denominator and the factorization \(\ell^2\pi^2(1-\pi)H\) are recomputed symbolically. Exact Bernstein inversion verifies the degree-13, 14-row sign certificate: all 406 rational coefficients of the row polynomials are nonnegative, and each row is nonzero, giving strict positivity throughout the stated open domain. A separate finite-state Markov chain recurrence validates a rational test case. A finite sample alone would not suffice; the algebraic certificate covers the infinite continuum of parameters.

**Originality — PASS.** The primary 2023 paper's Theorem 4.11 proves the desired inequality only for household sizes two and three, and Conjecture 4.12 proposes all sizes. Corollary 4.10 treats only sufficiently small local rates, while Theorem 4.1 handles the infinite-rate limit. The full article and the 2026 multitype follow-up were materially inspected. Related network and vaccination studies do not establish the exact Markovian \(n=4\) all-finite-rate comparison. Public discovery searches yielded no covering proof, but priority cannot be conclusively certified; incompletely inspected older theory and unindexed work are residual risks.

**Value — PASS.** Household size four is the first explicitly unresolved natural case in the stated conjecture. Uniform validity over every positive finite local infection rate is a motivated structural result rather than a routine endpoint or perturbative consequence. The precise scope is the approximate disease-induced herd-immunity statistic, not the original unrestricted dynamic threshold.

**Limits.** Exponential infectious periods, four-member households and finite strictly positive local rates only. No proof is given for nonexponential durations, other household sizes, degenerate rates, or the exact unrestricted disease-induced threshold. Independent audit was not performed.

Self-review: passed. Independent audit: not yet performed.
