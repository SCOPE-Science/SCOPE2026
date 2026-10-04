# Review

## Correctness

PASS. The exact two-step source recurrence closes only when the momentum values take the displayed form. The two strict sign constraints then give the stated interval and the necessary-and-sufficient condition \(2\beta_1<1+\beta_2\). The fixed-sign two-step Jacobian has multipliers \(1\) and \(\beta_2^2\), and the average-loss formula follows exactly.

Risk: the boundary convention for \(\operatorname{sign}(0)\) is excluded, and no global basin theorem is claimed.

## Originality

PASS. The defining Lion paper gives the sign-momentum rule and its two coefficients; the later Lyapunov paper develops broader convergence and constrained-optimization theory. The inspected full texts do not state a scalar constant-step period-two continuum, the exact chattering band, or the transverse multiplier. Focused published-record searches found no implication-equivalent Lion result.

Residual risk: a related calculation may appear in unindexed signed-momentum notes.

## Value

PASS. Constant-step sign methods inherently risk terminal chattering, but Lion's asymmetric momentum makes the geometry nontrivial. The exact band, default-parameter width, transverse contraction, and unavoidable average-loss floor give a concrete account of Lion's terminal behavior and explain why learning-rate decay is mathematically consequential.

Same-model review: passed. Independent audit: not yet performed.
