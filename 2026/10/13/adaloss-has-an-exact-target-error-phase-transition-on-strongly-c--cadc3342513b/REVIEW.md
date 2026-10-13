# Review

## Correctness

PASS. Specializing the published AdaLoss accumulator to a deterministic shifted SPD quadratic gives the exact eigenmode update. Initial scale exceeding learning rate times largest curvature makes all active modes contract without sign changes. A summability argument yields bounded accumulated excess under exact centering and linear squared-accumulator drift under a fixed target offset. Expanding the convergent modal logarithmic products proves the full stretched-exponential law with its log-power correction. The independent-of-library standalone numerical checker replays both target signs and the correct-target case.

Limitation: the overestimated-target result assumes the initial objective gap is smaller than the target error, and the result concerns deterministic stationary quadratics.

## Originality

PASS. The defining paper treats the target as a surrogate for the optimum but its linear-regression guarantee uses an accumulator that vanishes at the minimizer. AdaGrad-Norm and stochastic Polyak step-size provide relevant adaptation and optimum-value precedents with different recurrences. No directly implication-equivalent published statement was identified in the inspected sources or focused indexed queries.

Residual risk: an unindexed note may contain this exact cumulative-loss mismatch asymptotic.

## Value

PASS. The mismatch creates a sharp change from geometric convergence to a stretched-exponential rate with a precisely determined logarithmic correction, despite identical gradients under a vertical objective shift. The explicit Hessian-mode formulas and both under- and overestimated cases make this a meaningful robustness boundary for the algorithm's defining design choice.

Self-review: passed. Independent audit: not yet performed.
