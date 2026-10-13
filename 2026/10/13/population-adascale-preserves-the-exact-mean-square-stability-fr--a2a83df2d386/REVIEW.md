# Review

## Correctness

PASS. The source population gain and the batched stochastic gradient can both be written exactly from the first two curvature moments. Conditioning on the current iterate gives a scalar second-moment recursion whose multiplier factors explicitly. The factorization proves the scale-independent if-and-only-if stability boundary, and differentiation gives the unique optimal base rate and exact optimal contraction.

Scientific risk: the result concerns the population gain; practical moving-average gain estimates introduce extra state and estimation noise.

## Originality

PASS. The defining AdaScale paper was inspected at its algorithm, gain equation, and scaling theorems. It proves scale-robust sufficient bounds under different assumptions but does not state the exact random-curvature mean-square multiplier, the sharp scale-independent frontier, or the optimal factor. Focused published-record searches and current/prior owned-ledger checks found no implication-equivalent AdaScale result.

Residual risk: the fixed-map scalar mean-square calculation is elementary multiplicative-noise theory, although the AdaScale-specific gain cancellation appears not to be recorded in the inspected literature.

## Value

PASS. The result directly quantifies AdaScale's defining variance-adaptive scaling mechanism and explains, on an exact stochastic quadratic, how the method can preserve a base-rate safety margin while linear scaling loses it. The sharp comparator and scale-dependent optimal factor make the statement a tuning and mechanism result rather than a generic stability exercise.

Self-review: passed. Independent audit: not yet performed.
