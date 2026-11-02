# Scientific review

## Correctness — PASS

The one-attempt absorption Laplace transform and reset-clock decomposition independently reproduce the motivating paper's Eq. (5.37). Differentiation reduces the rate derivative to the sign of \(A_n(q)-2\). Analytic endpoint bounds, monotonicity of the truncated-geometric index mean, and an exact-rational covering argument prove \(A_{21}(q)<2\) on all \(0<q<1\). The 80 accepted rational intervals jointly cover the entire middle parameter range; the verifier reproduces them from scratch using exact fractions. A strict rational lower witness proves \(A_{22}(6/7)>2\), and budget-monotonicity propagates this to every larger finite allowance. The proof does not rely on numerical root counts.

## Originality — PASS, qualified

The 2023 preprint *Truncated stochastically switching processes* explicitly gives the mean termination time in Eq. (5.37) and observes the qualitative monotonicity-to-nonmonotonicity change in Fig. 4. The new assertion is the sharp finite reset-budget cutoff (20 or fewer permitted resets versus 21 or more) uniformly over positive diffusion and starting-distance parameters; that integer threshold and its global proof are not given by the motivating work. The 2023 critical-number-of-walkers paper studies independent particle number with unlimited resetting until target hit and neither implies nor reproduces this cap on attempts. The checked mathematical research records and available previous claims reveal no equivalent result. There remains an unexcluded risk of an unindexed or differently formulated mathematical analysis of the same finite-budget curve.

## Mathematical value — PASS

The finite allowance is the controlling resource in the motivating model. The exact first allowance at which a metastable local optimum appears resolves its observed qualitative change as a natural, uniform discrete phase boundary, distinguishing a termination-time profile from an unbounded-reset first-passage profile. The proof gives a reproducible finite analytic certificate for a delicate near-threshold case. No broad theorem or numerical approximation is required to interpret the sharp cutoff.

## Closest literature and limitations

P. C. Bressloff, arXiv:2310.20502v1, Section V.B, Eq. (5.37), Fig. 4: established formula and qualitative examples; no all-budget sharp integer threshold. M. Biroli, S. N. Majumdar, G. Schehr, arXiv:2303.18012v1: critical *number of walkers* and target first-hit mean, a different control variable and stopping event. The certificate establishes presence but not uniqueness of local extrema at large budgets. The mean stopping time includes trajectories terminated by budget exhaustion, so it is not a performance guarantee for successful target detection. Publication priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
