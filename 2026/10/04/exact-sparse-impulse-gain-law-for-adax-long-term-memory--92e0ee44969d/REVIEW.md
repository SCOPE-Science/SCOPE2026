# Review

## Correctness

PASS. The one-impulse recurrence is solved exactly. The second-moment floor and response kernel are closed form; strict gain monotonicity follows from stochastic ordering of geometric indices, and the sharp ceiling follows from the bounded kernel limit. Adam's threshold is an exact ratio-test consequence.

Risk: this is a sparse gradient-input theorem, not a fixed-objective global convergence result.

## Originality

PASS. The defining AdaX paper gives the long-term-memory recurrence and sparse-gradient motivation, but the inspected full text does not state the isolated-gradient cumulative response or its sharp gain ceiling. Nearby local adaptive-optimizer analysis studies fixed points rather than this source-specific input response. Focused published-record searches found no implication-equivalent result.

Residual risk: an equivalent short derivation may exist in unindexed notes.

## Value

PASS. The result directly measures what AdaX's two memory parameters do after fresh gradient information disappears. It proves finite impulse motion for every \(\beta_1<1\), in contrast with Adam's \(\beta_1<\sqrt{\beta_2}\) requirement, while quantifying the exact finite-gain cost as the long-memory parameter becomes small.

Same-model review: passed. Independent audit: not yet performed.
