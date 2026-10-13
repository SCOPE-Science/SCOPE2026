# Review

## Correctness

PASS. The alternating first moment and centered residual are exact geometric sums. The squared residual converges geometrically, so its stable second-moment EMA converges to the same constant; the one-step asynchronous delay does not change that limit. The matched uncentered state is exactly solvable because the squared gradient is constant. The gain ratio and its monotonic dependence on \(\beta_1\) follow algebraically.

Risk: the theorem is an input-response statement and does not classify a fixed-objective training trajectory.

## Originality

PASS. The defining ACProp paper contains the architecture, asynchronous convergence results, and a different sparse periodic comparison between centered and uncentered denominators. The inspected source and implementation do not state the pure alternating-gradient centered-denominator floor or the exact high-frequency gain \((1+\beta_1)/(2\beta_1)\). Focused published-record and web searches found no implication-equivalent result.

Residual risk: an equivalent short frequency-response derivation may exist in unindexed notes.

## Value

PASS. Centering is a core ACProp design choice. The theorem shows exactly how it alters the most rapidly oscillating deterministic signal and exposes a sharp tuning tradeoff: smaller \(\beta_1\) makes the centered denominator increasingly underestimate the raw alternating scale, while changing \(\beta_2\) cannot alter the asymptotic gain. This is a direct structural diagnostic of the method rather than an arbitrary numerical case.

Self-review: passed. Independent audit: not yet performed.
