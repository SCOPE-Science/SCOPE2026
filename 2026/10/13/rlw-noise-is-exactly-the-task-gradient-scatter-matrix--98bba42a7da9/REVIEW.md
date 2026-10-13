# Review

## Correctness

PASS. Exchangeability and the simplex sum force the weight covariance to be a scalar multiple of the projector orthogonal to the all-ones vector. Pushing that matrix through the fixed task-gradient matrix gives the exact centered scatter operator. The pairwise-energy identity, range and kernel, and the sharp one-hot variance maximum follow by exact linear algebra and the bound \(0\le\lambda_i\le1\). The embedded verifier reconstructs the formulas on finite exchangeable laws.

Risk: mini-batch sampling noise is deliberately excluded.

## Originality

PASS. The defining RLW source establishes unbiasedness and treats the extra weight randomness as a generic stochastic mechanism for convergence and local-minimum escape. Later primary work links RLW to stochastic regularization. The inspected sources do not state the exact task-disagreement covariance, its rank and nullspace, or the unique one-hot maximum among exchangeable simplex laws. Focused published-record searches found no implication-equivalent result.

Residual risk: the covariance calculation is elementary enough that an equivalent observation may exist in unindexed notes.

## Value

PASS. RLW's claimed benefit is tied directly to extra random-weight noise. The theorem identifies exactly where that noise acts, how its energy is determined by pairwise task disagreement, and which source weight law maximizes it. It also proves that random weighting adds no noise in task-consensus directions, making the result a structural refinement of the method's stochastic-escape interpretation rather than a generic variance exercise.

Self-review: passed. Independent audit: not yet performed.
