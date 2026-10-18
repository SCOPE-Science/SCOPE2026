# Scientific assessment: one-round delayed Jacobi communication

## Correctness — PASS

The theorem's universal quantifier is over all real initial histories for the exactly defined synchronous-round recurrences, not arbitrary asynchronous executions. The three companion polynomials are derived from the update rules. The one-directional case has only one positive real root when \(\beta>1\); its other roots are complex conjugates whose exact modulus is the positive root plus \(\beta-1\). The strict unit-circle test reduces to \(\beta^2r^2+\beta<2\). The two-directional delayed modes split into two quadratic Schur polynomials, restoring the ordinary ceiling. The global \(9/8\) ratio bound follows from an explicit perfect-square inequality with unique equality at \(r=2/7\). The completed independent checker passed 104 exact identities and finite matrix comparisons. These calculations corroborate but do not replace the analytic proof.

## Originality — PASS, with residual risk

The precise comparative claim has been checked against the motivating 2026 paper, original asynchronous-Jacobi stability literature, a 2018 propagation-matrix analysis, and a 1995 delay-state modeling paper. In particular, the 1995 work **already contains the relevant three-state companion-matrix form**, and the 2018 paper **already states the qualitative convergence advantage of asynchronous schedules**. Neither ingredient is claimed as new. The narrower asserted novelty is the complete sharp three-protocol SPD overrelaxation classification, including reversal when both edges are delayed and the unique universal nine-eighths maximum. Published mathematics-record searches for delay aliases, relaxed Jacobi, spectral-radius boundaries, and the exact constant did not identify a corresponding theorem. This absence is not a uniqueness proof. A closely relevant 2025 semi-iterative/Chebyshev paper was only inspectable at abstract level, so overlap risk persists and independent literature verification is worthwhile.

## Mathematical value — PASS

The two-node comparison separates a design variable (which directed message is stale) from the coarse delay bound (zero versus one round). It proves that two schedules sharing the same maximal lag can have different exact stability domains, and that the best overrelaxation expansion is bounded by an attained universal number. The equality example supplies a reproducible numerical boundary for communication-aware splitting, while the standard-relaxation spectral factors explicitly prevent confusing a stability gain with a runtime advantage. The statement is a natural complete classification for the smallest coupled SPD communication graph, not an arbitrary choice of numerical parameters.

## Scope and residual limitations

Only fixed one-round cross-coordinate ages and synchronous commits are covered; time-varying schedules and end-to-end parallel speed are unresolved. The older three-state matrix makes equivalent prior analyses plausible. The 2025 semi-iterative reference was not fully inspected because the accessible full text was blocked; its exact implications are uncertain. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
