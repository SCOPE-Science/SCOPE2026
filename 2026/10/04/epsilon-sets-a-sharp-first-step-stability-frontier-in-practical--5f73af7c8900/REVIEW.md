# Review

## Correctness

PASS. The first practical MADGRAD update is reconstructed exactly from zero accumulators. On a diagonal quadratic it is coordinate-separable, and each coordinate multiplier is \(1-q_i\). The monotonicity frontier follows from the exact supremum of \(q_i\); the spike radius follows by solving \(q_i=2\), and the exact worst objective factor follows by optimizing \((1-q)^2\) over the attainable interval.

Risk: later MADGRAD states retain accumulated history and are outside this theorem.

## Originality

PASS. The defining paper gives the cube-root practical recurrence and a separately safeguarded denominator for its convergence analysis, but does not state the sharp practical first-step frontier. A later comparative study reports MADGRAD explosions and hyperparameter sensitivity without an implication-equivalent calculation. Focused published-record searches found no exact epsilon-curvature threshold, spike radius, or amplification law.

Residual risk: an equivalent short derivation may exist in unindexed implementation notes.

## Value

PASS. The result identifies which mechanism actually controls startup stability near a zero gradient: not the adaptive accumulator, whose cube root vanishes as \(|x|^{2/3}\), but epsilon. The exact frontier \(c\gamma L\le2\varepsilon\) and exact near-minimizer amplification provide a direct parameter diagnostic and a precise local counterpart to broader empirical reports of MADGRAD sensitivity.

Same-model review: passed. Independent audit: not yet performed.
