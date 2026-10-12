# Review

## Correctness

PASS. The first source step is evaluated exactly from the printed bias corrections, giving the corrected Nesterov numerator \((1+\beta_1)g_1\) and the belief denominator floor \(D\). The limiting two-state parameter/momentum matrix follows by first-order expansion at the minimizer, while the squared belief residual contributes only at second order and the second-moment perturbation has eigenvalue \(\beta_2\). The three Jury inequalities reduce to one sharp curvature ceiling, with root \(-1\) at equality.

Scientific risk: the tail statement is a limiting local spectral result, not a global convergence theorem.

## Originality

PASS. AdaBelief's belief denominator and the range-suppressing role of epsilon placement are prior and are explicitly excluded from the novelty claim. The defining AdaPlus paper supplies the combined recurrence but no startup or local Schur threshold, and FastAdaBelief studies a different strongly-convex regret construction. Focused indexed searches did not identify the exact two-threshold law or their closed-form ratio.

Residual risk: an unindexed optimizer-analysis note may contain the same scalar linearization.

## Value

PASS. The two thresholds differ by more than a factor of twelve at the published defaults. This exposes a practically interpretable transient-versus-tail robustness gap in the exact mechanism AdaPlus was designed to combine, and gives a sharp learning-rate/curvature diagnostic rather than a generic statement that adaptive methods can overshoot.

Self-review: passed. Independent audit: not yet performed.
